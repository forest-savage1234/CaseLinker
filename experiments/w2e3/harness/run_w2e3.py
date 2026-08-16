"""Freeze, execute, and independently score the disposable W2-E3 r2 experiment."""

from __future__ import annotations

import ast
import csv
import inspect
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from collections.abc import Mapping
from datetime import UTC, datetime
from hashlib import sha256
from io import StringIO
from pathlib import Path

EXPERIMENT_ID = "W2-E3"
APPROVED_PARENT = "64dc010feaf8fc79a61bea8b70e2386fa39ce546"
FROZEN_PACKET = "5fb8913e78d0e54ed25021bb34fcade43d2aff3c"
PACKET_FILES = (
    "docs/v4/assurance/WAVE-02-ASSURANCE.md",
    "docs/v4/assurance/WAVE-02-REQUIREMENTS-MAP.md",
    "docs/v4/experiments/WAVE-02-PLAN.md",
)
PROBE_IDS = tuple(f"P{index}" for index in range(1, 9))
ATTACK_PROBE_IDS = ("P4", "P5", "P6", "P7", "P8")
FORBIDDEN_FIXTURE_KEY_PARTS = ("expected", "gold", "oracle")

HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3]
EXPERIMENT_ROOT = REPO_ROOT / "experiments" / "w2e3"
FIXTURE_PATH = EXPERIMENT_ROOT / "fixtures" / "input_fixture.json"
ORACLE_PATH = EXPERIMENT_ROOT / "oracle" / "expected_results.json"
SUT_DIR = EXPERIMENT_ROOT / "sut"
OUTPUT_DIR = EXPERIMENT_ROOT / "outputs"
REPRO_DIR = EXPERIMENT_ROOT / "repro"


class SequenceRecorder:
    def __init__(self) -> None:
        self._sequence = 0
        self._last_monotonic_ns = 0
        self.events: list[dict[str, object]] = []

    def add(self, event: str, **details: object) -> None:
        now = time.monotonic_ns()
        if now <= self._last_monotonic_ns:
            now = self._last_monotonic_ns + 1
        self._last_monotonic_ns = now
        self._sequence += 1
        self.events.append(
            {
                "details": details,
                "event": event,
                "monotonic_ns": now,
                "seq": self._sequence,
                "timestamp_utc": datetime.now(UTC)
                .isoformat(timespec="microseconds")
                .replace("+00:00", "Z"),
            }
        )


def digest_bytes(value: bytes) -> str:
    return sha256(value).hexdigest()


def digest_file(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=True, indent=2, sort_keys=True)
        stream.write("\n")


def git(*args: str) -> str:
    command = [
        "git",
        "-c",
        f"safe.directory={REPO_ROOT.as_posix()}",
        "-C",
        str(REPO_ROOT),
        *args,
    ]
    return subprocess.check_output(command, text=True).strip()


def forbidden_fixture_keys(value: object, prefix: str = "$") -> list[str]:
    findings: list[str] = []
    if isinstance(value, Mapping):
        for key, nested in value.items():
            key_text = str(key)
            lowered = key_text.lower()
            if any(part in lowered for part in FORBIDDEN_FIXTURE_KEY_PARTS):
                findings.append(f"{prefix}.{key_text}")
            findings.extend(forbidden_fixture_keys(nested, f"{prefix}.{key_text}"))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            findings.extend(forbidden_fixture_keys(nested, f"{prefix}[{index}]"))
    return findings


def is_scalar(value: object) -> bool:
    return value is None or isinstance(value, (str, int, float, bool))


def collect_scalars(value: object, into: set[object]) -> None:
    if isinstance(value, Mapping):
        for nested in value.values():
            collect_scalars(nested, into)
        return
    if isinstance(value, list):
        for nested in value:
            collect_scalars(nested, into)
        return
    if is_scalar(value):
        into.add(value)


def walk_keys_and_scalars(value: object) -> tuple[set[str], set[object]]:
    keys: set[str] = set()
    scalars: set[object] = set()

    def walk(node: object) -> None:
        if isinstance(node, Mapping):
            for key, nested in node.items():
                keys.add(str(key))
                walk(nested)
            return
        if isinstance(node, list):
            for nested in node:
                walk(nested)
            return
        if is_scalar(node):
            scalars.add(node)

    walk(value)
    return keys, scalars


def subject_for_run(base: Mapping[str, object], run: Mapping[str, object]) -> dict[str, object]:
    subject = dict(base)
    changes = run.get("subject_changes", {})
    if isinstance(changes, Mapping):
        subject.update(changes)
    return subject


def denied_surface(
    subject: Mapping[str, object],
    authorized_names: set[str],
) -> tuple[set[str], set[object]]:
    denied_keys: set[str] = set()
    denied_values: set[object] = set()

    def walk(node: object) -> None:
        if isinstance(node, Mapping):
            for key, nested in node.items():
                if key not in authorized_names:
                    denied_keys.add(str(key))
                    collect_scalars(nested, denied_values)
                else:
                    walk(nested)
            return
        if isinstance(node, list):
            for nested in node:
                walk(nested)

    walk(subject)
    return denied_keys, denied_values


def extract_fields(probe_id: str, rendered: object) -> list[str]:
    parsed = parse_rendered(probe_id, rendered)
    if isinstance(parsed, Mapping):
        return sorted(str(key) for key in parsed)
    raise TypeError(f"{probe_id} parsed payload must be an object")


def parse_rendered(probe_id: str, rendered: object) -> dict[str, object]:
    if probe_id == "P1":
        if not isinstance(rendered, str):
            raise TypeError("P1 output must be a JSON string")
        value = json.loads(rendered)
        if not isinstance(value, dict):
            raise TypeError("P1 JSON root must be an object")
        return value
    if probe_id == "P2":
        if not isinstance(rendered, str):
            raise TypeError("P2 output must be CSV text")
        if rendered == "":
            return {}
        reader = csv.DictReader(StringIO(rendered))
        rows = list(reader)
        if reader.fieldnames is None:
            raise ValueError("P2 CSV has no header")
        parsed: dict[str, object] = {str(name): [] for name in reader.fieldnames}
        for row in rows:
            for name, cell in row.items():
                if name is None:
                    continue
                try:
                    parsed[str(name)].append(json.loads(cell))  # type: ignore[union-attr]
                except (TypeError, json.JSONDecodeError):
                    parsed[str(name)].append(cell)  # type: ignore[union-attr]
        return parsed
    if probe_id == "P3":
        if not isinstance(rendered, Mapping) or not isinstance(rendered.get("entries"), list):
            raise TypeError("P3 output must contain an entries list")
        fields: dict[str, object] = {}
        for entry in rendered["entries"]:
            if not isinstance(entry, Mapping) or not isinstance(entry.get("name"), str):
                raise TypeError("P3 entry lacks a name")
            name = entry["name"]
            if not name.startswith("fields/") or not name.endswith(".json"):
                raise ValueError("P3 entry name is outside the field namespace")
            field = name.removeprefix("fields/").removesuffix(".json")
            fields[field] = json.loads(str(entry.get("content")))
        return fields
    if probe_id == "P4":
        if not isinstance(rendered, str) or not rendered.startswith("CacheView("):
            raise TypeError("P4 output must be a CacheView representation")
        if not rendered.endswith(")"):
            raise ValueError("P4 CacheView representation is unterminated")
        value = ast.literal_eval(rendered[len("CacheView(") : -1])
        if not isinstance(value, dict):
            raise TypeError("P4 CacheView payload must be an object")
        return value
    if probe_id == "P5":
        if not isinstance(rendered, Mapping):
            raise TypeError("P5 output must be an object")
        document = rendered.get("document")
        if not isinstance(document, Mapping) or not isinstance(document.get("fields"), Mapping):
            raise TypeError("P5 document must contain a fields object")
        return dict(document["fields"])
    if probe_id == "P6":
        if not isinstance(rendered, str) or not rendered.startswith(
            "event=w2e3_disclosure fields="
        ):
            raise TypeError("P6 output must be the synthetic log line")
        body = rendered.removeprefix("event=w2e3_disclosure fields=")
        if not body:
            return {}
        fields = {}
        for item in body.split("\t"):
            field, separator, raw_value = item.partition("=")
            if not separator or not field:
                raise ValueError("P6 log field is malformed")
            fields[field] = json.loads(raw_value)
        return fields
    if probe_id == "P7":
        if not isinstance(rendered, Mapping) or not isinstance(
            rendered.get("safe_context"), Mapping
        ):
            raise TypeError("P7 output must contain safe_context")
        return dict(rendered["safe_context"])
    if probe_id == "P8":
        if not isinstance(rendered, list):
            raise TypeError("P8 output must be a row list")
        fields = {}
        for row in rendered:
            if not isinstance(row, Mapping) or not isinstance(row.get("field"), str):
                raise TypeError("P8 row lacks a field")
            fields[row["field"]] = row.get("value")
        return fields
    raise ValueError(f"unknown probe: {probe_id}")


def packet_identity_errors() -> list[str]:
    errors: list[str] = []
    for path in PACKET_FILES:
        frozen_blob = git("rev-parse", f"{FROZEN_PACKET}:{path}")
        current_blob = git("hash-object", str(REPO_ROOT / path))
        if current_blob != frozen_blob:
            errors.append(f"frozen packet mismatch: {path}")
    return errors


def isolation_errors() -> list[str]:
    errors: list[str] = []
    allowed = ("experiments/w2e3/", "docs/v4/evidence/experiments/W2-E3-REPORT.md")
    for line in git("status", "--porcelain", "--untracked-files=all").splitlines():
        path = line[3:].replace("\\", "/")
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if not path.startswith(allowed):
            errors.append(f"change outside W2-E3 isolation allowlist: {path}")
    return errors


def run_p9_observation(fixture: Mapping[str, object]) -> dict[str, object]:
    carry_forward = (
        "Wave 5 must add an authorized supplied-decision enforcement hook before "
        "Claim Card or Evidence Pack entry points can support a disclosure-safety claim."
    )
    try:
        subject = fixture["subject"]
        if not isinstance(subject, Mapping):
            raise TypeError("fixture subject is not an object")
        public_count = subject["public_aggregate_count"]
        if not isinstance(public_count, int) or isinstance(public_count, bool):
            raise TypeError("public_aggregate_count is not an integer")

        sys.path.insert(0, str(REPO_ROOT / "src"))
        from caselinker.analysis.claims import ClaimCardBuilder
        from caselinker.analysis.cohorts import (
            CohortQuery,
            CohortResult,
            SnapshotReference,
        )
        from caselinker.analysis.evidence_pack import EvidencePackAssembler

        snapshot = SnapshotReference(
            snapshot_id="snap_w2e3_fixture_001",
            manifest_sha256="a" * 64,
            output_sha256s=("c" * 64,),
        )
        query = CohortQuery(
            query_id="qry_w2e3_public_aggregate",
            event_type="legal_event_charge",
        )
        result = CohortResult(
            snapshot=snapshot,
            query=query,
            numerator=public_count,
            denominator=2,
            numerator_event_ids=("event_w2e3_001",),
            denominator_event_ids=("event_w2e3_001", "event_w2e3_002"),
            projection_sha256s=("c" * 64,),
            shapes_sha256="d" * 64,
        )
        builder = ClaimCardBuilder()
        card = builder.build(result)
        card_payload = card.to_dict()
        assembler = EvidencePackAssembler()
        pack = assembler.assemble(card)
        pack_payload = json.loads(pack.canonical_json)

        denied_canaries = {
            "display_name": subject["display_name"],
            "internal_note": subject["internal_note"],
            "research_status": subject["research_status"],
        }
        card_bytes = json.dumps(card_payload, ensure_ascii=True, sort_keys=True).encode()
        pack_bytes = pack.canonical_json
        denied_presence = {
            field: {
                "claim_card": str(value).encode() in card_bytes,
                "evidence_pack": str(value).encode() in pack_bytes,
            }
            for field, value in denied_canaries.items()
        }
        confirmed_leak = any(
            location for presence in denied_presence.values() for location in presence.values()
        )
        signatures = {
            "ClaimCardBuilder.build": str(inspect.signature(builder.build)),
            "ClaimCard.to_dict": str(inspect.signature(card.to_dict)),
            "EvidencePackAssembler.assemble": str(inspect.signature(assembler.assemble)),
            "EvidencePack.canonical_json": "bytes attribute read",
        }
        classification = "confirmed_leak" if confirmed_leak else "path_lacks_enforcement"
        return {
            "carry_forward": carry_forward,
            "classification": classification,
            "confirmed_leak": confirmed_leak,
            "decision": "D-public",
            "decision_supplied_to_product_entrypoints": False,
            "denied_canary_presence": denied_presence,
            "entrypoints": signatures,
            "mapping": {
                "display_name": "unmappable",
                "internal_note": "unmappable",
                "public_aggregate_count": "CohortResult.numerator",
                "research_status": "unmappable; builder owns fixed limitations",
            },
            "observed_output_keys": {
                "claim_card": sorted(card_payload),
                "evidence_pack": sorted(pack_payload),
            },
            "policy_hook_observed": False,
            "product_code_modified": False,
            "requires_unapproved_repair_to_continue": False,
        }
    except Exception as error:  # observational incompleteness must remain explicit
        return {
            "carry_forward": carry_forward,
            "classification": "not_evaluable",
            "confirmed_leak": False,
            "error": f"{type(error).__name__}: {error}",
            "product_code_modified": False,
            "requires_unapproved_repair_to_continue": False,
        }


def score(
    *,
    output: Mapping[str, object],
    oracle: Mapping[str, object],
    fixture: Mapping[str, object],
    p9: Mapping[str, object],
    validity_errors: list[str],
) -> dict[str, object]:
    findings: list[dict[str, object]] = []
    matrix: dict[str, dict[str, list[str]]] = {}
    attack_proof: dict[str, dict[str, dict[str, object]]] = {}

    expected_revision = oracle.get("expected_sut_revision")
    evaluator_identity = oracle.get("expected_evaluator_identity")
    required_probes = oracle.get("required_probe_ids")
    expected_fields = oracle.get("expected_fields")
    required_attacks = oracle.get("required_attacks")
    if not isinstance(expected_revision, str):
        validity_errors.append("oracle lacks expected_sut_revision")
    if not isinstance(evaluator_identity, str):
        validity_errors.append("oracle lacks expected_evaluator_identity")
    if required_probes != list(PROBE_IDS):
        validity_errors.append("oracle required probe set is incomplete or reordered")
    if not isinstance(expected_fields, Mapping):
        validity_errors.append("oracle expected_fields is missing")
        expected_fields = {}
    if not isinstance(required_attacks, Mapping):
        validity_errors.append("oracle required_attacks is missing")
        required_attacks = {}

    if output.get("sut_revision") != expected_revision:
        validity_errors.append("SUT revision does not match the frozen oracle")
    if output.get("oracle_received") is not False:
        validity_errors.append("SUT reports oracle exposure")
    if output.get("eligibility_received_by_evaluator") is not False:
        findings.append({"kind": "eligibility_confusion", "path": "evaluator"})
    if output.get("evaluator_identity") != evaluator_identity:
        findings.append({"kind": "wrong_evaluator_identity", "path": "SUT"})

    raw_results = output.get("results")
    if not isinstance(raw_results, list):
        validity_errors.append("SUT output lacks result list")
        raw_results = []
    results: dict[str, Mapping[str, object]] = {}
    for result in raw_results:
        if not isinstance(result, Mapping) or not isinstance(result.get("run_id"), str):
            validity_errors.append("SUT output contains an invalid result record")
            continue
        run_id = result["run_id"]
        if run_id in results:
            validity_errors.append(f"duplicate SUT result: {run_id}")
        results[run_id] = result

    if set(results) != set(expected_fields):
        validity_errors.append("SUT run ids do not exactly match the oracle")

    fixture_runs = fixture.get("runs")
    fixture_subject = fixture.get("subject")
    fixture_attack_profile = fixture.get("attack_profile")
    runs_by_id: dict[str, Mapping[str, object]] = {}
    if isinstance(fixture_runs, list):
        for run in fixture_runs:
            if isinstance(run, Mapping) and isinstance(run.get("run_id"), str):
                runs_by_id[run["run_id"]] = run
    if not isinstance(fixture_subject, Mapping):
        validity_errors.append("fixture subject is missing")
        fixture_subject = {}
    if not isinstance(fixture_attack_profile, Mapping):
        validity_errors.append("fixture attack_profile is missing")
        fixture_attack_profile = {}

    for run_id, expected in expected_fields.items():
        if not isinstance(run_id, str) or not isinstance(expected, list):
            validity_errors.append("oracle contains malformed expected fields")
            continue
        result = results.get(run_id)
        if result is None:
            continue
        outputs = result.get("outputs")
        if not isinstance(outputs, Mapping) or set(outputs) != set(PROBE_IDS):
            validity_errors.append(f"{run_id} lacks an exact P1-P8 output set")
            continue
        matrix[run_id] = {}
        attack_proof[run_id] = {}
        run_spec = runs_by_id.get(run_id, {})
        subject = subject_for_run(fixture_subject, run_spec)
        authorized = {str(field) for field in expected}
        denied_keys, denied_values = denied_surface(subject, authorized)
        expected_source_names = sorted(subject)
        for probe_id in PROBE_IDS:
            probe = outputs[probe_id]
            if not isinstance(probe, Mapping) or "rendered" not in probe:
                validity_errors.append(f"{run_id}/{probe_id} lacks rendered output")
                continue
            try:
                parsed = parse_rendered(probe_id, probe["rendered"])
                actual = sorted(parsed)
            except (ValueError, TypeError, SyntaxError, json.JSONDecodeError) as error:
                findings.append(
                    {
                        "detail": f"{type(error).__name__}: {error}",
                        "kind": "unparseable_output",
                        "path": f"{run_id}/{probe_id}",
                    }
                )
                continue
            matrix[run_id][probe_id] = actual
            if actual != expected:
                findings.append(
                    {
                        "actual": actual,
                        "expected": expected,
                        "kind": "field_set_mismatch",
                        "path": f"{run_id}/{probe_id}",
                    }
                )
            observed_keys, observed_scalars = walk_keys_and_scalars(parsed)
            leaked_keys = sorted(denied_keys.intersection(observed_keys))
            leaked_values = [
                value for value in sorted(observed_scalars, key=repr) if value in denied_values
            ]
            if leaked_keys or leaked_values:
                findings.append(
                    {
                        "kind": "nested_denied_structure",
                        "leaked_keys": leaked_keys,
                        "leaked_values": leaked_values,
                        "path": f"{run_id}/{probe_id}",
                    }
                )
            if probe_id in ATTACK_PROBE_IDS:
                attack = probe.get("attack")
                requested = fixture_attack_profile.get(probe_id)
                if required_attacks.get(probe_id) != requested:
                    validity_errors.append(
                        f"{probe_id} fixture attack does not match the oracle required attack"
                    )
                if not isinstance(attack, Mapping):
                    validity_errors.append(f"{run_id}/{probe_id} attack evidence missing")
                    continue
                executed = attack.get("executed") is True
                source_names = attack.get("source_field_names")
                source_ok = source_names == expected_source_names
                skip_ok = probe_id != "P8" or attack.get("skip_enforcement_attempted") is True
                repr_ok = probe_id not in {"P6", "P7"} or (
                    attack.get("repr_computed") is True
                    and isinstance(attack.get("repr_char_length"), int)
                    and int(attack["repr_char_length"]) > 0
                )
                evaluator_after_attack = (
                    attack.get("evaluator_consulted") is True
                    and attack.get("enforcement_applied") is True
                )
                attack_proof[run_id][probe_id] = {
                    "executed": executed,
                    "requested": attack.get("requested"),
                    "source_field_names": source_names,
                    "source_kind": attack.get("source_kind"),
                    "used_full_subject": source_ok,
                }
                if attack.get("requested") != requested or not executed:
                    validity_errors.append(f"{run_id}/{probe_id} required attack was not executed")
                if not source_ok:
                    validity_errors.append(
                        f"{run_id}/{probe_id} attack source was not the full subject"
                    )
                if not skip_ok:
                    validity_errors.append(f"{run_id}/{probe_id} did not attempt PEP skip")
                if not repr_ok:
                    validity_errors.append(
                        f"{run_id}/{probe_id} did not compute the full-record representation"
                    )
                if not evaluator_after_attack:
                    findings.append(
                        {
                            "kind": "attack_bypassed_evaluator",
                            "path": f"{run_id}/{probe_id}",
                        }
                    )

    calls = output.get("evaluator_calls")
    expected_call_pairs = {
        (run_id, probe_id) for run_id in expected_fields for probe_id in PROBE_IDS
    }
    actual_call_pairs: set[tuple[object, object]] = set()
    if not isinstance(calls, list):
        validity_errors.append("SUT output lacks evaluator call trace")
    else:
        for call in calls:
            if not isinstance(call, Mapping):
                validity_errors.append("evaluator call trace contains a non-object")
                continue
            actual_call_pairs.add((call.get("run_id"), call.get("probe_id")))
            if call.get("evaluator_identity") != evaluator_identity:
                findings.append({"kind": "adapter_evaluator_bypass", "path": call})
            if call.get("eligibility_consulted") is not False:
                findings.append({"kind": "eligibility_confusion", "path": call})
        if actual_call_pairs != expected_call_pairs or len(calls) != len(expected_call_pairs):
            findings.append(
                {
                    "actual_call_count": len(calls),
                    "expected_call_count": len(expected_call_pairs),
                    "kind": "adapter_evaluator_bypass",
                    "path": "call_trace",
                }
            )

    m3 = oracle.get("m3")
    if isinstance(m3, Mapping):
        before = results.get(str(m3.get("before_run_id")), {})
        after = results.get(str(m3.get("after_run_id")), {})
        before_id = before.get("decision_identity") if isinstance(before, Mapping) else None
        after_id = after.get("decision_identity") if isinstance(after, Mapping) else None
        if not isinstance(before_id, Mapping) or not isinstance(after_id, Mapping):
            validity_errors.append("M3 decision identity was not reported")
        else:
            preserved = m3.get("preserved_fields", [])
            changed = m3.get("changed_fields", [])
            if not isinstance(preserved, list) or not isinstance(changed, list):
                validity_errors.append("oracle M3 identity contract is malformed")
            else:
                for field in preserved:
                    if before_id.get(field) != after_id.get(field):
                        validity_errors.append(f"M3 did not preserve decision field {field}")
                if all(before_id.get(field) == after_id.get(field) for field in changed):
                    validity_errors.append("M3 did not revoke or expire the same decision")
                if before_id.get("decision_id") != after_id.get("decision_id"):
                    validity_errors.append("M3 changed decision identity")

    deny_all_runs = oracle.get("deny_all_runs", [])
    deny_on_missing_count = 0
    for run_id in deny_all_runs if isinstance(deny_all_runs, list) else []:
        probes = matrix.get(str(run_id), {})
        if probes and all(fields == [] for fields in probes.values()):
            deny_on_missing_count += 1

    internal_fields = set(oracle.get("internal_fields", []))
    internal_leaks = []
    non_internal_runs = oracle.get("non_internal_runs", [])
    for run_id in non_internal_runs if isinstance(non_internal_runs, list) else []:
        for probe_id, fields in matrix.get(str(run_id), {}).items():
            leaked = sorted(internal_fields.intersection(fields))
            if leaked:
                internal_leaks.append({"fields": leaked, "path": f"{run_id}/{probe_id}"})
    findings.extend({"kind": "internal_field_leak", **leak} for leak in internal_leaks)

    distinct_runs = oracle.get("distinct_view_runs", [])
    view_sets = []
    for run_id in distinct_runs if isinstance(distinct_runs, list) else []:
        view_sets.append(tuple(matrix.get(str(run_id), {}).get("P1", [])))
    three_views_distinct = len(view_sets) == 3 and len(set(view_sets)) == 3
    if not three_views_distinct:
        findings.append({"kind": "views_not_distinct", "path": "D-internal/research/public"})

    metamorphic_runs = oracle.get("metamorphic_runs", [])
    metamorphic_pass = (
        all(
            matrix.get(str(run_id), {}).get(probe_id) == expected_fields.get(run_id)
            for run_id in metamorphic_runs
            for probe_id in PROBE_IDS
        )
        if isinstance(metamorphic_runs, list)
        else False
    )
    if not metamorphic_pass:
        findings.append({"kind": "metamorphic_failure", "path": "M1-M5"})

    structural_runs = oracle.get("structural_runs", [])
    structural_pass = (
        all(
            matrix.get(str(run_id), {}).get(probe_id) == expected_fields.get(run_id)
            for run_id in structural_runs
            for probe_id in PROBE_IDS
        )
        if isinstance(structural_runs, list)
        else False
    )
    if not structural_pass:
        findings.append({"kind": "structural_fail_closed_failure", "path": "N-nested"})

    mechanism_pass = not validity_errors and not findings
    p9_classification = p9.get("classification")
    stop_reasons: list[str] = []
    if (
        p9.get("confirmed_leak") is True
        and p9.get("requires_unapproved_repair_to_continue") is True
    ):
        stop_reasons.append("confirmed P9 leak requires unapproved repair to continue")
    revise_reasons: list[str] = []
    if not mechanism_pass and not validity_errors:
        revise_reasons.append("bounded P1-P8 mechanism failure")
    if p9_classification == "confirmed_leak" and not stop_reasons:
        revise_reasons.append("confirmed P9 leak carried forward without in-run repair")

    if validity_errors:
        recommendation = "invalid/incomplete"
        decision_rule = "invalid -> repeat"
    elif stop_reasons:
        recommendation = "stop"
        decision_rule = "valid stop condition -> stop"
    elif revise_reasons:
        recommendation = "revise architecture"
        decision_rule = "valid revise condition and no stop condition -> revise architecture"
    elif p9_classification in {"path_lacks_enforcement", "not_evaluable"}:
        recommendation = "proceed"
        decision_rule = "P1-P8 pass and P9 not confirmed leak -> proceed with carry-forward"
    else:
        recommendation = "invalid/incomplete"
        decision_rule = "unknown P9 classification -> repeat"
        validity_errors.append("P9 classification is missing or unknown")

    return {
        "attack_proof": attack_proof,
        "decision_rule": decision_rule,
        "decision_mapping": {
            "invalid_or_incomplete": bool(validity_errors),
            "precedence": "invalid -> repeat; otherwise stop > revise architecture > proceed",
            "proceed_conditions_met": mechanism_pass
            and p9_classification in {"path_lacks_enforcement", "not_evaluable"},
            "revise_reasons": revise_reasons,
            "stop_reasons": stop_reasons,
        },
        "deny_on_missing_count": deny_on_missing_count,
        "eligibility_disclosure_confusion_count": sum(
            finding["kind"] == "eligibility_confusion" for finding in findings
        ),
        "field_presence_matrix": matrix,
        "findings": findings,
        "internal_leak_count": len(internal_leaks),
        "mechanism_pass": mechanism_pass,
        "metamorphic_pass": metamorphic_pass,
        "p9_classification": p9_classification,
        "recommendation": recommendation,
        "shared_evaluator_call_count": len(calls) if isinstance(calls, list) else 0,
        "structural_pass": structural_pass,
        "three_views_distinct": three_views_distinct,
        "valid_run": not validity_errors,
        "validity_errors": validity_errors,
    }


def main() -> None:
    recorder = SequenceRecorder()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPRO_DIR.mkdir(parents=True, exist_ok=True)

    validity_errors: list[str] = []
    if git("rev-parse", "HEAD") != APPROVED_PARENT:
        validity_errors.append("experiment base is not the published D-036 commit")
    validity_errors.extend(packet_identity_errors())
    validity_errors.extend(isolation_errors())

    fixture_bytes = FIXTURE_PATH.read_bytes()
    oracle_bytes = ORACLE_PATH.read_bytes()
    fixture = json.loads(fixture_bytes)
    if not isinstance(fixture, Mapping):
        validity_errors.append("fixture root is not an object")
        fixture = {}
    exposed_keys = forbidden_fixture_keys(fixture)
    if exposed_keys:
        validity_errors.append(f"oracle-like fixture keys exposed to SUT: {exposed_keys}")

    frozen_hashes = {
        "fixture": digest_bytes(fixture_bytes),
        "harness": digest_file(HERE),
        "oracle": digest_bytes(oracle_bytes),
        "sut_adapters": digest_file(SUT_DIR / "adapters.py"),
        "sut_driver": digest_file(SUT_DIR / "driver.py"),
        "sut_evaluator": digest_file(SUT_DIR / "evaluator.py"),
    }
    if validity_errors:
        raise SystemExit("preflight failed: " + "; ".join(validity_errors))

    recorder.add(
        "freeze_completed",
        oracle_bytes_hashed=True,
        oracle_content_deserialized=False,
        hashes=frozen_hashes,
    )

    with tempfile.TemporaryDirectory(prefix="w2e3-sut-") as temporary:
        stage = Path(temporary)
        stage_sut = stage / "sut"
        shutil.copytree(SUT_DIR, stage_sut)
        stage_fixture = stage / "input_fixture.json"
        stage_output = stage / "sut_output.json"
        stage_fixture.write_bytes(fixture_bytes)
        command = [
            sys.executable,
            "-B",
            str(stage_sut / "driver.py"),
            "--fixture",
            str(stage_fixture),
            "--output",
            str(stage_output),
        ]
        environment = {
            key: os.environ[key]
            for key in ("PATH", "SYSTEMROOT", "TEMP", "TMP")
            if key in os.environ
        }
        environment.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
        recorder.add(
            "sut_started",
            argv=[
                "<python>",
                "-B",
                "<isolated>/sut/driver.py",
                "--fixture",
                "<isolated>/input_fixture.json",
                "--output",
                "<isolated>/sut_output.json",
            ],
            cwd="<isolated>",
            oracle_available_to_sut=False,
            staged_files=sorted(
                str(path.relative_to(stage)).replace("\\", "/")
                for path in stage.rglob("*")
                if path.is_file()
            ),
        )
        completed = subprocess.run(
            command,
            cwd=stage,
            env=environment,
            capture_output=True,
            check=False,
            text=True,
        )
        recorder.add(
            "sut_completed",
            returncode=completed.returncode,
            stderr=completed.stderr,
            stdout=completed.stdout,
        )
        if completed.returncode != 0 or not stage_output.is_file():
            raise SystemExit("SUT failed before output capture")
        output_bytes = stage_output.read_bytes()
        shutil.copyfile(stage_output, OUTPUT_DIR / "sut_output.json")
        recorder.add(
            "sut_output_captured",
            output_sha256=digest_bytes(output_bytes),
            oracle_content_deserialized=False,
        )

    output = json.loads(output_bytes)
    if not isinstance(output, Mapping):
        validity_errors.append("SUT output root is not an object")
        output = {}
    oracle = json.loads(oracle_bytes)
    recorder.add(
        "oracle_loaded",
        after_sut_output_capture=True,
        oracle_sha256=frozen_hashes["oracle"],
    )
    if not isinstance(oracle, Mapping):
        validity_errors.append("oracle root is not an object")
        oracle = {}
    recorder.add("oracle_validated", validity_error_count=len(validity_errors))

    p9 = run_p9_observation(fixture)
    write_json(OUTPUT_DIR / "p9_observation.json", p9)
    recorder.add(
        "p9_observed",
        classification=p9.get("classification"),
        confirmed_leak=p9.get("confirmed_leak"),
    )

    comparison = score(
        output=output,
        oracle=oracle,
        fixture=fixture,
        p9=p9,
        validity_errors=validity_errors,
    )
    comparison["artifact_hashes_at_score"] = {
        **frozen_hashes,
        "p9_observation": digest_file(OUTPUT_DIR / "p9_observation.json"),
        "sut_output": digest_file(OUTPUT_DIR / "sut_output.json"),
    }
    recorder.add(
        "comparison_written",
        recommendation=comparison["recommendation"],
        valid_run=comparison["valid_run"],
    )
    write_json(OUTPUT_DIR / "comparison.json", comparison)

    recorder.add("evidence_finalized")
    write_json(OUTPUT_DIR / "run_sequence.json", {"events": recorder.events})
    sequence_hash = digest_file(OUTPUT_DIR / "run_sequence.json")
    freeze_record = {
        "approved_parent": APPROVED_PARENT,
        "commands": {
            "harness": "python -B experiments/w2e3/harness/run_w2e3.py",
            "sut_interface": (
                "python -B experiments/w2e3/sut/driver.py --fixture "
                "experiments/w2e3/fixtures/input_fixture.json --output "
                "experiments/w2e3/outputs/sut_output.json"
            ),
        },
        "experiment_id": EXPERIMENT_ID,
        "frozen_hashes": frozen_hashes,
        "frozen_planning_packet": FROZEN_PACKET,
        "isolation": {
            "namespace": "experiments/w2e3",
            "oracle_available_to_sut": False,
            "product_code_modified": False,
            "temporary_sut_stage_destroyed": True,
        },
        "oracle_bytes_hashed_before_sut": True,
        "oracle_content_deserialized_before_sut": False,
        "oracle_loaded_after_sut_output_capture": True,
        "output_hashes": {
            "comparison": digest_file(OUTPUT_DIR / "comparison.json"),
            "p9_observation": digest_file(OUTPUT_DIR / "p9_observation.json"),
            "run_sequence": sequence_hash,
            "sut_output": digest_file(OUTPUT_DIR / "sut_output.json"),
        },
        "preserved_ineligible_r1": "4e620ab45e2dd771e6ed04eca243259bafb610a8",
        "python": sys.version,
        "run_sequence": recorder.events,
        "sut_revision": output.get("sut_revision"),
    }
    write_json(REPRO_DIR / "freeze_record.json", freeze_record)
    print(json.dumps(comparison, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
