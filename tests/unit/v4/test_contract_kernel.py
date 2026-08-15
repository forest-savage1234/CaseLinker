from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

VALID_ENVELOPE = {
    "schema_version": "1.0",
    "contract_kind": "envelope",
    "payload": {"note": "policy-safe fixture"},
}


def test_valid_envelope_is_accepted() -> None:
    validate_instance("envelope-v1", VALID_ENVELOPE)


def test_unknown_property_is_rejected() -> None:
    bad = {**VALID_ENVELOPE, "internal_note": "must not pass"}
    with pytest.raises(ContractError, match="unknown field"):
        validate_instance("envelope-v1", bad)


def test_missing_contract_kind_is_rejected() -> None:
    bad = {"schema_version": "1.0", "payload": {}}
    with pytest.raises(ContractError, match="required"):
        validate_instance("envelope-v1", bad)


def test_unsupported_schema_version_is_rejected() -> None:
    bad = {**VALID_ENVELOPE, "schema_version": "2.0"}
    with pytest.raises(ContractError, match="schema_version"):
        validate_instance("envelope-v1", bad)


def test_non_object_instance_is_rejected() -> None:
    with pytest.raises(ContractError, match="object"):
        validate_instance("envelope-v1", ["not", "an", "object"])
