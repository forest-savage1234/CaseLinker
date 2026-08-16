"""Eight experiment-only adapters that share one decision evaluator."""

from __future__ import annotations

import csv
import json
from collections.abc import Callable, Mapping
from datetime import datetime
from io import StringIO

from evaluator import SuppliedDecisionEvaluator

Rendered = str | dict[str, object] | list[dict[str, object]]


def _p1_json(view: dict[str, object]) -> Rendered:
    return json.dumps(view, ensure_ascii=True, separators=(",", ":"), sort_keys=True)


def _p2_csv(view: dict[str, object]) -> Rendered:
    if not view:
        return ""
    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=sorted(view), lineterminator="\n")
    writer.writeheader()
    writer.writerow({field: view[field] for field in sorted(view)})
    return output.getvalue()


def _p3_bundle(view: dict[str, object]) -> Rendered:
    return {
        "entries": [
            {
                "content": json.dumps(view[field], ensure_ascii=True),
                "name": f"fields/{field}.json",
            }
            for field in sorted(view)
        ]
    }


def _p4_cache(view: dict[str, object]) -> Rendered:
    return f"CacheView({view!r})"


def _p5_search(view: dict[str, object]) -> Rendered:
    return {"document": {"fields": dict(view)}, "index": "w2e3-synthetic"}


def _p6_log(view: dict[str, object]) -> Rendered:
    fields = "\t".join(
        f"{field}={json.dumps(view[field], ensure_ascii=True, separators=(',', ':'))}"
        for field in sorted(view)
    )
    return f"event=w2e3_disclosure fields={fields}"


def _p7_error(view: dict[str, object]) -> Rendered:
    return {
        "error": "synthetic_failure",
        "safe_context": dict(view),
        "status": 400,
    }


def _p8_admin(view: dict[str, object]) -> Rendered:
    return [{"field": field, "value": view[field]} for field in sorted(view)]


_RENDERERS: dict[str, Callable[[dict[str, object]], Rendered]] = {
    "P1": _p1_json,
    "P2": _p2_csv,
    "P3": _p3_bundle,
    "P4": _p4_cache,
    "P5": _p5_search,
    "P6": _p6_log,
    "P7": _p7_error,
    "P8": _p8_admin,
}


def _empty_attack_evidence(requested: object) -> dict[str, object]:
    return {
        "executed": False,
        "repr_char_length": None,
        "repr_computed": False,
        "requested": requested,
        "skip_enforcement_attempted": False,
        "source_field_count": 0,
        "source_field_names": [],
        "source_kind": None,
    }


def execute_attack(
    *,
    probe_id: str,
    record: Mapping[str, object],
    requested: object,
) -> dict[str, object]:
    """Construct the requested unsafe source. Values stay out of the evidence."""

    evidence = _empty_attack_evidence(requested)
    source = {key: record[key] for key in record}
    names = sorted(source)
    if requested == "seed_cache_from_full_record":
        cache_store: dict[str, dict[str, object]] = {}
        cache_store["w2e3-full-record"] = source
        seeded = dict(cache_store["w2e3-full-record"])
        evidence.update(
            {
                "executed": True,
                "source_field_count": len(seeded),
                "source_field_names": sorted(seeded),
                "source_kind": "full_record_cache_seed",
            }
        )
        return evidence
    if requested == "build_search_from_internal_view":
        search_document = {"document": {"fields": dict(source)}, "index": "w2e3-internal-attempt"}
        fields = dict(search_document["document"]["fields"])
        evidence.update(
            {
                "executed": True,
                "source_field_count": len(fields),
                "source_field_names": sorted(fields),
                "source_kind": "internal_view_search_document",
            }
        )
        return evidence
    if requested == "log_full_record":
        log_line = f"event=w2e3_full_record_attempt record={source!r}"
        evidence.update(
            {
                "executed": True,
                "repr_char_length": len(log_line),
                "repr_computed": True,
                "source_field_count": len(source),
                "source_field_names": names,
                "source_kind": "full_record_log",
            }
        )
        return evidence
    if requested == "include_record_repr_in_error":
        record_repr = repr(source)
        error_attempt = {
            "error": "synthetic_failure",
            "record_repr": record_repr,
            "status": 400,
        }
        evidence.update(
            {
                "executed": True,
                "repr_char_length": len(str(error_attempt["record_repr"])),
                "repr_computed": "record_repr" in error_attempt,
                "source_field_count": len(source),
                "source_field_names": names,
                "source_kind": "record_repr_error",
            }
        )
        return evidence
    if requested == "skip_enforcement_requested":
        admin_attempt = [{"field": key, "value": source[key]} for key in names]
        evidence.update(
            {
                "executed": True,
                "skip_enforcement_attempted": True,
                "source_field_count": len(admin_attempt),
                "source_field_names": [row["field"] for row in admin_attempt],
                "source_kind": "admin_skip_pep",
            }
        )
        return evidence
    if probe_id in {"P4", "P5", "P6", "P7", "P8"} and requested:
        evidence["source_kind"] = "unrecognized_attack"
    return evidence


def render_all(
    *,
    evaluator: SuppliedDecisionEvaluator,
    record: Mapping[str, object],
    decision: Mapping[str, object] | None,
    as_of: datetime,
    run_id: str,
    attack_profile: Mapping[str, object],
) -> dict[str, dict[str, object]]:
    outputs: dict[str, dict[str, object]] = {}
    for probe_id, renderer in _RENDERERS.items():
        requested = attack_profile.get(probe_id)
        attack = execute_attack(probe_id=probe_id, record=record, requested=requested)
        outcome = evaluator.evaluate(
            record=record,
            decision=decision,
            as_of=as_of,
            run_id=run_id,
            probe_id=probe_id,
        )
        outputs[probe_id] = {
            "attack": {
                **attack,
                "enforcement_applied": True,
                "evaluator_consulted": True,
            },
            "decision_reason": outcome.reason,
            "rendered": renderer(outcome.allowed_view),
        }
    return outputs
