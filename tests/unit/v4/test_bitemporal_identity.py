from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

VALID_INTERVAL = {
    "schema_version": "1.0",
    "contract_kind": "bitemporal_interval",
    "event_time": {"start": "2026-01-05", "end": "2026-01-05", "precision": "day"},
    "knowledge_time": "2026-01-08T00:00:00Z",
    "precision_source": "source_text",
    "time_model": "bitemporal",
}

VALID_TRANSITION = {
    "schema_version": "1.0",
    "contract_kind": "state_transition",
    "subject_id": "asrt_example01",
    "from_state": "extracted",
    "to_state": "resolved",
    "actor_kind": "reviewer",
    "reason_code": "accepted_bundle",
}

VALID_IDENTITY = {
    "schema_version": "1.0",
    "contract_kind": "stable_identity",
    "assertion_id": "asrt_example01",
    "document_version_id": "docv_example01",
    "review_id": "rvw_example01",
    "event_id": "evt_example01",
    "dependency_id": "dep_example01",
}


def test_valid_bitemporal_interval_is_accepted() -> None:
    validate_instance("bitemporal-interval-v1", VALID_INTERVAL)


def test_knowledge_time_is_not_event_time() -> None:
    bad = {**VALID_INTERVAL, "time_model": "collapsed"}
    with pytest.raises(ContractError, match="event time is not knowledge time"):
        validate_instance("bitemporal-interval-v1", bad)


def test_inverted_event_interval_is_rejected() -> None:
    bad = {
        **VALID_INTERVAL,
        "event_time": {"start": "2026-01-09", "end": "2026-01-05", "precision": "day"},
    }
    with pytest.raises(ContractError, match="interval"):
        validate_instance("bitemporal-interval-v1", bad)


def test_invented_day_precision_is_rejected() -> None:
    bad = {
        **VALID_INTERVAL,
        "event_time": {"start": "2026-01", "end": "2026-01", "precision": "day"},
        "precision_source": "invented",
    }
    with pytest.raises(ContractError, match="precision"):
        validate_instance("bitemporal-interval-v1", bad)


def test_valid_identity_bundle_is_accepted() -> None:
    validate_instance("stable-identity-v1", VALID_IDENTITY)


def test_display_label_is_not_an_identity() -> None:
    bad = {**VALID_IDENTITY, "assertion_id": "Jane Doe"}
    with pytest.raises(ContractError, match="pattern"):
        validate_instance("stable-identity-v1", bad)


def test_legal_transition_is_accepted() -> None:
    validate_instance("state-transition-v1", VALID_TRANSITION)


def test_illegal_transition_is_rejected() -> None:
    bad = {**VALID_TRANSITION, "from_state": "retracted", "to_state": "extracted"}
    with pytest.raises(ContractError, match="illegal transition"):
        validate_instance("state-transition-v1", bad)
