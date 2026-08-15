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
            raise ContractError(f"{path} schema_version mismatch: expected {const}")
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
