"""Fail-closed validator for versioned v4 proposal JSON contracts."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, Sequence
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Final

SCHEMA_ROOT: Final = Path(__file__).resolve().parents[3] / "schemas" / "v4"
SCHEMA_NAME_PATTERN: Final = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
UTC_TIMESTAMP: Final = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")
OPAQUE_ID: Final = re.compile(r"^[a-z]+_[a-z0-9][a-z0-9._-]{2,127}$")

MACHINE_TRANSITIONS: Final[dict[str, list[list[str]]]] = {
    "source_version": [
        ["observed", "acquired"],
        ["acquired", "verified"],
        ["verified", "changed"],
        ["verified", "removed"],
        ["verified", "superseded"],
        ["verified", "authenticity_uncertain"],
    ],
    "candidate_claim": [
        ["proposed", "queued"],
        ["queued", "under_review"],
        ["under_review", "accepted"],
        ["under_review", "rejected"],
        ["under_review", "corrected"],
        ["under_review", "escalated"],
        ["under_review", "contested"],
    ],
    "accepted_claim": [
        ["active", "qualified"],
        ["active", "superseded"],
        ["active", "retracted"],
        ["active", "disputed"],
        ["active", "ineligible"],
    ],
    "identity_hypothesis": [
        ["candidate", "needs_review"],
        ["needs_review", "possibly_same"],
        ["needs_review", "confirmed_same"],
        ["needs_review", "confirmed_different"],
        ["needs_review", "unresolved"],
        ["possibly_same", "reopened"],
        ["confirmed_same", "reopened"],
        ["confirmed_different", "reopened"],
        ["unresolved", "reopened"],
        ["reopened", "needs_review"],
    ],
    "review_task": [
        ["open", "assigned"],
        ["assigned", "submitted"],
        ["submitted", "second_review"],
        ["submitted", "adjudication"],
        ["second_review", "closed"],
        ["adjudication", "closed"],
        ["closed", "reopened"],
    ],
    "research_artifact": [
        ["building", "verified"],
        ["verified", "eligible"],
        ["eligible", "stale"],
        ["eligible", "invalid"],
        ["eligible", "superseded"],
    ],
    "disclosure_request": [
        ["requested", "evaluating"],
        ["evaluating", "authorized"],
        ["evaluating", "minimized"],
        ["evaluating", "denied"],
        ["authorized", "expired"],
        ["authorized", "revoked"],
        ["minimized", "expired"],
        ["minimized", "revoked"],
    ],
    "publication": [
        ["draft", "authorized"],
        ["authorized", "published"],
        ["published", "corrected"],
        ["published", "withdrawn"],
        ["published", "superseded"],
    ],
    "federation_package": [
        ["received", "verified"],
        ["verified", "quarantined"],
        ["verified", "accepted"],
        ["accepted", "revoked"],
        ["accepted", "superseded"],
    ],
    "legacy_assertion": [
        ["extracted", "resolved"],
        ["extracted", "contested"],
        ["resolved", "retracted"],
        ["resolved", "superseded"],
    ],
}


class ContractError(ValueError):
    """Raised when a v4 proposal contract instance is not acceptable."""


def canonical_dumps(instance: object) -> bytes:
    """Return sorted, compact UTF-8 JSON for governed comparison."""
    return json.dumps(instance, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )


def decide_disclosure(
    request: Mapping[str, object],
    *,
    policy_version: str | None,
    research_eligible: bool,
    policy_result: str | None = None,
) -> dict[str, object]:
    """Return a policy-neutral decision bound to *request*. Missing policy denies."""
    validate_instance("disclosure-request-v1", dict(request))
    request_id = request["request_id"]
    audience = request["audience"]
    purpose = request["purpose"]
    if not isinstance(request_id, str):
        raise ContractError("disclosure request context is malformed")
    if not isinstance(audience, str) or not isinstance(purpose, str):
        raise ContractError("disclosure request context is malformed")
    missing = policy_version is None or policy_version == ""
    decision: dict[str, object] = {
        "schema_version": "1.0",
        "contract_kind": "disclosure_decision",
        "request_id": request_id,
        "decision_id": "ddec_" + request_id.removeprefix("dreq_"),
        "audience": audience,
        "purpose": purpose,
        "outcome": "denied" if missing else "authorized",
        "policy_version": "" if missing else policy_version,
        "research_eligible": research_eligible,
        "treat_eligible_as_disclosed": False,
    }
    if missing:
        validate_instance("disclosure-decision-v1", decision)
        return decision
    validate_instance("disclosure-decision-v1", decision)
    return decision


def validate_instance(schema_name: str, instance: object) -> None:
    """Validate *instance* against ``schemas/v4/{schema_name}.schema.json``."""
    if SCHEMA_NAME_PATTERN.fullmatch(schema_name) is None:
        raise ContractError("schema_name must be a lowercase hyphenated token")
    path = SCHEMA_ROOT / f"{schema_name}.schema.json"
    if not path.is_file():
        raise ContractError(f"unknown contract schema: {schema_name}")
    schema = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(schema, dict):
        raise ContractError(f"schema {schema_name} must be a JSON object")
    _validate(instance, schema, path="$")
    if isinstance(instance, dict):
        _apply_invariants(instance, schema)


def _types_of(schema: Mapping[str, object]) -> set[str]:
    raw = schema.get("type")
    if isinstance(raw, str):
        return {raw}
    if isinstance(raw, list) and all(isinstance(item, str) for item in raw):
        return set(raw)
    return set()


def _validate(instance: object, schema: Mapping[str, object], *, path: str) -> None:
    allowed_types = _types_of(schema)
    if instance is None:
        if "null" in allowed_types:
            return
        raise ContractError(f"{path} must not be null")
    if "object" in allowed_types:
        if not isinstance(instance, dict):
            raise ContractError(f"{path} must be an object")
        if not all(isinstance(key, str) for key in instance):
            raise ContractError(f"{path} keys must be strings")
        properties = schema.get("properties", {})
        declared = properties if isinstance(properties, dict) else {}
        if schema.get("additionalProperties") is False:
            unknown = sorted(set(instance) - set(declared))
            if unknown:
                raise ContractError(f"{path} has unknown field: {unknown[0]}")
        required = schema.get("required", [])
        if isinstance(required, list):
            for field in required:
                if not isinstance(field, str) or field not in instance:
                    raise ContractError(f"{path} is missing required field {field}")
        for field, value in instance.items():
            child = declared.get(field)
            if isinstance(child, dict):
                _validate(value, child, path=f"{path}.{field}")
        return
    if "string" in allowed_types:
        if not isinstance(instance, str):
            raise ContractError(f"{path} must be a string")
        const = schema.get("const")
        if const is not None and instance != const:
            raise ContractError(f"{path} must equal the declared const")
        enum = schema.get("enum")
        if isinstance(enum, list) and instance not in enum:
            raise ContractError(f"{path} must be one of the declared enum values")
        minimum_length = schema.get("minLength")
        if isinstance(minimum_length, int) and len(instance) < minimum_length:
            raise ContractError(f"{path} is shorter than minLength")
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.fullmatch(pattern, instance) is None:
            raise ContractError(f"{path} does not match required pattern")
        fmt = schema.get("format")
        if fmt == "utc-date-time":
            _require_utc(instance, path=path)
        if fmt == "calendar-date":
            _parse_calendar(instance, precision="day", path=path)
        return
    if "integer" in allowed_types:
        if isinstance(instance, bool) or not isinstance(instance, int):
            raise ContractError(f"{path} must be an integer")
        minimum = schema.get("minimum")
        if isinstance(minimum, int) and instance < minimum:
            raise ContractError(f"{path} is below minimum")
        maximum = schema.get("maximum")
        if isinstance(maximum, int) and instance > maximum:
            raise ContractError(f"{path} is above maximum")
        return
    if "boolean" in allowed_types:
        if not isinstance(instance, bool):
            raise ContractError(f"{path} must be a boolean")
        return
    if "array" in allowed_types:
        if not isinstance(instance, list):
            raise ContractError(f"{path} must be an array")
        items = schema.get("items")
        if isinstance(items, dict):
            for index, item in enumerate(instance):
                _validate(item, items, path=f"{path}[{index}]")
        unique = schema.get("uniqueItems")
        if unique is True:
            serialized = [
                json.dumps(item, sort_keys=True, separators=(",", ":")) for item in instance
            ]
            if len(set(serialized)) != len(serialized):
                raise ContractError(f"{path} items must be unique")
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(instance) < min_items:
            raise ContractError(f"{path} has fewer than minItems")
        return
    raise ContractError(f"{path} schema is missing a supported type")


def _require_utc(value: str, *, path: str) -> datetime:
    if UTC_TIMESTAMP.fullmatch(value) is None:
        raise ContractError(f"{path} must be a UTC timestamp ending with Z")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() != UTC.utcoffset(parsed):
        raise ContractError(f"{path} must be UTC")
    return parsed


def _parse_calendar(value: str, *, precision: str, path: str) -> date | None:
    try:
        if precision == "year":
            if re.fullmatch(r"[0-9]{4}", value) is None:
                raise ValueError
            return date(int(value), 1, 1)
        if precision == "month":
            if re.fullmatch(r"[0-9]{4}-[0-9]{2}", value) is None:
                raise ContractError(f"{path} month precision requires YYYY-MM")
            year, month = value.split("-")
            return date(int(year), int(month), 1)
        if precision == "day":
            if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value) is None:
                raise ContractError(f"{path} day precision requires a full date")
            return date.fromisoformat(value)
        if precision == "unknown":
            return None
    except ContractError:
        raise
    except ValueError as error:
        raise ContractError(f"{path} is an invalid calendar value") from error
    raise ContractError(f"{path} has unknown precision")


def _apply_invariants(instance: dict[str, object], schema: Mapping[str, object]) -> None:
    raw = schema.get("x-caselinker-invariants")
    if not isinstance(raw, list):
        return
    for name in raw:
        _run_invariant(str(name), instance, schema)


def _run_invariant(name: str, instance: Mapping[str, object], schema: Mapping[str, object]) -> None:
    if name == "reject_collapsed_clock" and instance.get("time_model") != "bitemporal":
        raise ContractError("event time is not knowledge time")
    if name == "precision_aware_interval":
        _check_interval(instance)
    if name == "legal_transition":
        _check_transition(instance, schema)
    if name == "no_self_correction" and instance.get("target_id") == instance.get("successor_id"):
        raise ContractError("cannot correct itself")
    if name == "no_reflexive_dependency" and instance.get("from_id") == instance.get("to_id"):
        raise ContractError("reflexive dependency")
    if name == "distinct_subjects":
        left = instance.get("left_subject_id", instance.get("left_event_id"))
        right = instance.get("right_subject_id", instance.get("right_event_id"))
        if left == right:
            raise ContractError("distinct subjects required")
    if name == "compatibility_versions":
        if instance.get("writer_schema_version") != instance.get("reader_schema_version"):
            raise ContractError("incompatible schema versions")
        if instance.get("unknown_fields_policy") != "reject":
            raise ContractError("unknown_fields_policy must reject")
    if name == "ai_no_self_review" and instance.get("reviewer_disposition") == "self_approved":
        raise ContractError("AI cannot self-review")
    if name == "similarity_is_not_identity" and instance.get("creates_canonical_identity") is True:
        raise ContractError("similarity is not identity")
    if name == "no_blind_transitivity" and instance.get("inference_method") == "transitive_closure":
        raise ContractError("blind transitivity is not identity evidence")
    if name == "derivation_is_not_corroboration":
        same_family = instance.get("same_source_family") is True
        if instance.get("relation") == "corroboration" and same_family:
            raise ContractError("derivation is not corroboration")
    if (
        name == "eligibility_is_not_disclosure"
        and instance.get("treat_eligible_as_disclosed") is True
    ):
        raise ContractError("eligibility is not disclosure permission")
    if name == "deny_without_policy":
        missing_policy = not instance.get("policy_version")
        if missing_policy and instance.get("outcome") != "denied":
            raise ContractError("missing policy version denies disclosure")
    if name == "projection_not_authoritative" and instance.get("authoritative") is True:
        raise ContractError("a projection is not a source of truth")
    if name == "ai_cannot_publish" and instance.get("disposition") == "published":
        raise ContractError("AI execution cannot publish")


def _check_interval(instance: Mapping[str, object]) -> None:
    event = instance.get("event_time")
    if not isinstance(event, dict):
        raise ContractError("event_time is required")
    precision = event.get("precision")
    start = event.get("start")
    end = event.get("end")
    if not isinstance(precision, str) or not isinstance(start, str):
        raise ContractError("event_time is malformed")
    if instance.get("precision_source") == "invented":
        raise ContractError("precision must not be invented")
    start_date = _parse_calendar(start, precision=precision, path="$.event_time.start")
    if end is None:
        if event.get("open_end") is not True:
            raise ContractError("open interval requires open_end")
        return
    if not isinstance(end, str):
        raise ContractError("event_time.end must be a date or null")
    end_date = _parse_calendar(end, precision=precision, path="$.event_time.end")
    if start_date is not None and end_date is not None and start_date > end_date:
        raise ContractError("inverted interval")
    knowledge = instance.get("knowledge_time")
    if isinstance(knowledge, str):
        _require_utc(knowledge, path="$.knowledge_time")


def _check_transition(instance: Mapping[str, object], schema: Mapping[str, object]) -> None:
    machine = instance.get("machine", "legacy_assertion")
    if not isinstance(machine, str):
        raise ContractError("machine must be a string")
    allowed: Sequence[object]
    machines = schema.get("x-caselinker-machines")
    if isinstance(machines, dict) and machine in machines:
        raw_allowed = machines[machine]
    elif machine in MACHINE_TRANSITIONS:
        raw_allowed = MACHINE_TRANSITIONS[machine]
    else:
        raw_allowed = schema.get("x-caselinker-allowed-transitions")
    if not isinstance(raw_allowed, list):
        raise ContractError("illegal transition")
    allowed = raw_allowed
    pair = [instance.get("from_state"), instance.get("to_state")]
    if pair not in allowed:
        raise ContractError("illegal transition")
