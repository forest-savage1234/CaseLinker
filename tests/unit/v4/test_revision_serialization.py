from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, canonical_dumps, validate_instance

DOC = {
    "schema_version": "1.0",
    "contract_kind": "envelope",
    "payload": {"b": 2, "a": 1},
}


def test_canonical_dumps_is_byte_stable_and_key_sorted() -> None:
    first = canonical_dumps(DOC)
    second = canonical_dumps({"payload": {"a": 1, "b": 2}, "contract_kind": "envelope", "schema_version": "1.0"})
    assert first == second
    assert first.startswith(b"{")
    assert b'"a":1' in first


def test_compatibility_record_is_accepted() -> None:
    record = {
        "schema_version": "1.0",
        "contract_kind": "compatibility",
        "writer_schema_version": "1.0",
        "reader_schema_version": "1.0",
        "unknown_fields_policy": "reject",
    }
    validate_instance("compatibility-v1", record)


def test_incompatible_reader_is_rejected() -> None:
    record = {
        "schema_version": "1.0",
        "contract_kind": "compatibility",
        "writer_schema_version": "1.0",
        "reader_schema_version": "0.9",
        "unknown_fields_policy": "reject",
    }
    with pytest.raises(ContractError, match="incompatible"):
        validate_instance("compatibility-v1", record)


def test_unknown_fields_policy_must_reject() -> None:
    record = {
        "schema_version": "1.0",
        "contract_kind": "compatibility",
        "writer_schema_version": "1.0",
        "reader_schema_version": "1.0",
        "unknown_fields_policy": "ignore",
    }
    with pytest.raises(ContractError, match="unknown_fields_policy"):
        validate_instance("compatibility-v1", record)
