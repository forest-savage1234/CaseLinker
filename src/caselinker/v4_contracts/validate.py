"""Fail-closed validator for versioned v4 proposal JSON contracts."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from pathlib import Path
from typing import Final

SCHEMA_ROOT: Final = Path(__file__).resolve().parents[3] / "schemas" / "v4"
SCHEMA_NAME_PATTERN: Final = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class ContractError(ValueError):
    """Raised when a v4 proposal contract instance is not acceptable."""


def canonical_dumps(instance: object) -> bytes:
    """Placeholder until canonical serialization is implemented."""
    raise ContractError("canonical serialization is not implemented")


def decide_disclosure(
    request: Mapping[str, object],
    *,
    policy_version: str | None,
    research_eligible: bool,
) -> dict[str, object]:
    """Placeholder until missing-policy denial is implemented."""
    raise ContractError("disclosure decision procedure is not implemented")


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


def _validate(instance: object, schema: Mapping[str, object], *, path: str) -> None:
    expected_type = schema.get("type")
    if expected_type == "object":
        if not isinstance(instance, dict) or not all(isinstance(key, str) for key in instance):
            raise ContractError(f"{path} must be an object")
        properties = schema.get("properties", {})
        if properties is not None and not isinstance(properties, dict):
            raise ContractError(f"{path} schema properties must be an object")
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
    if expected_type == "string":
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
        return
    if expected_type == "integer":
        if isinstance(instance, bool) or not isinstance(instance, int):
            raise ContractError(f"{path} must be an integer")
        minimum = schema.get("minimum")
        if isinstance(minimum, int) and instance < minimum:
            raise ContractError(f"{path} is below minimum")
        maximum = schema.get("maximum")
        if isinstance(maximum, int) and instance > maximum:
            raise ContractError(f"{path} is above maximum")
        return
    if expected_type == "boolean":
        if not isinstance(instance, bool):
            raise ContractError(f"{path} must be a boolean")
        return
    if expected_type == "array":
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


def _apply_invariants(instance: dict[str, object], schema: Mapping[str, object]) -> None:
    raw = schema.get("x-caselinker-invariants")
    if not isinstance(raw, list):
        return
    for name in raw:
        if name == "reject_collapsed_clock" and instance.get("time_model") != "bitemporal":
            raise ContractError("event time is not knowledge time")
        if name == "reject_inverted_interval":
            event = instance.get("event_time")
            if isinstance(event, dict):
                start = event.get("start")
                end = event.get("end")
                if isinstance(start, str) and isinstance(end, str) and start > end:
                    raise ContractError("inverted interval")
        if name == "reject_invented_precision":
            if instance.get("precision_source") == "invented":
                raise ContractError("precision must not be invented")
            event = instance.get("event_time")
            if isinstance(event, dict) and event.get("precision") == "day":
                start = event.get("start")
                if isinstance(start, str) and len(start) < 10:
                    raise ContractError("day precision requires a full date")
        if name == "legal_transition":
            allowed = schema.get("x-caselinker-allowed-transitions")
            pair = [instance.get("from_state"), instance.get("to_state")]
            if not isinstance(allowed, list) or pair not in allowed:
                raise ContractError("illegal transition")
        _apply_named_safety_invariant(str(name), instance)


def _apply_named_safety_invariant(name: str, instance: Mapping[str, object]) -> None:
    if name == "similarity_is_not_identity" and instance.get(
        "creates_canonical_identity"
    ) is True:
        raise ContractError("similarity is not identity")
    if name == "no_blind_transitivity" and instance.get("inference_method") == (
        "transitive_closure"
    ):
        raise ContractError("blind transitivity is not identity evidence")
    if name == "derivation_is_not_corroboration":
        same_family = instance.get("same_source_family") is True
        if instance.get("relation") == "corroboration" and same_family:
            raise ContractError("derivation is not corroboration")
    if name == "eligibility_is_not_disclosure" and instance.get(
        "treat_eligible_as_disclosed"
    ) is True:
        raise ContractError("eligibility is not disclosure permission")
    if name == "deny_without_policy" and not instance.get("policy_version"):
        raise ContractError("missing policy version denies disclosure")
    if name == "projection_not_authoritative" and instance.get("authoritative") is True:
        raise ContractError("a projection is not a source of truth")
    if name == "ai_cannot_publish" and instance.get("disposition") == "published":
        raise ContractError("AI execution cannot publish")
