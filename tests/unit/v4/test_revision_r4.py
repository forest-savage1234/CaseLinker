from __future__ import annotations

import pytest

import caselinker.v4_contracts as contracts
from caselinker.v4_contracts import ContractError, decide_disclosure, validate_instance
from tests.unit.v4.test_bitemporal_identity import VALID_TRANSITION
from tests.unit.v4.test_disclosure_authority import VALID_DECISION
from tests.unit.v4.test_revision_disclosure import REQUEST

EXTERNAL_POLICY_DECISION = {
    "schema_version": "1.0",
    "contract_kind": "disclosure_policy_decision",
    "policy_decision_id": "pdec_fixture01",
    "request_id": "dreq_example01",
    "request_digest": VALID_DECISION["request_digest"],
    "policy_version": "pol_fixture_unspecified",
    "policy_result": "authorized",
    "transformations": {
        "minimization": False,
        "pseudonymization": True,
        "aggregation": False,
        "redaction": True,
        "watermarking": False,
    },
    "expiry": "2026-02-01T00:00:00Z",
    "revocation_state": "not_revoked",
    "decision_reason": "authorized_fixture_policy",
    "authority_binding_id": "auth_fixture01",
    "audit_event_id": "aud_policy01",
}


def test_authorized_metadata_is_copied_from_external_policy_decision() -> None:
    decision = decide_disclosure(
        REQUEST,
        research_eligible=True,
        policy_decision=EXTERNAL_POLICY_DECISION,
    )
    for field in (
        "policy_decision_id",
        "policy_version",
        "policy_result",
        "transformations",
        "expiry",
        "revocation_state",
        "decision_reason",
        "authority_binding_id",
        "audit_event_id",
    ):
        assert decision[field] == EXTERNAL_POLICY_DECISION[field]


def test_request_digest_binding_rejects_substituted_context() -> None:
    tampered = {**VALID_DECISION, "principal_id": "prin_attacker01"}
    with pytest.raises(ContractError, match="request binding"):
        contracts.validate_disclosure_binding(REQUEST, tampered)


def test_minimized_decision_requires_a_real_transformation() -> None:
    bad = {
        **VALID_DECISION,
        "outcome": "minimized",
        "policy_result": "minimized",
        "transformations": {
            "minimization": False,
            "pseudonymization": False,
            "aggregation": False,
            "redaction": False,
            "watermarking": False,
        },
    }
    with pytest.raises(ContractError, match="transformation"):
        validate_instance("disclosure-decision-v1", bad)


def test_disclosure_time_window_cannot_be_inverted() -> None:
    bad = {
        **VALID_DECISION,
        "time_window": {"start": "2026-02-01", "end": "2026-01-01"},
    }
    with pytest.raises(ContractError, match="time_window"):
        validate_instance("disclosure-decision-v1", bad)


def test_sod_requires_approver_authority_bindings() -> None:
    bad = {
        **VALID_TRANSITION,
        "separation_of_duties_required": True,
        "second_approver_id": "prin_example02",
    }
    bad.pop("first_approver_authority_binding_id", None)
    bad.pop("second_approver_authority_binding_id", None)
    with pytest.raises(ContractError, match="authority"):
        validate_instance("state-transition-v1", bad)


def test_sod_requirement_must_reference_external_governance_decision() -> None:
    bad = {
        **VALID_TRANSITION,
        "separation_of_duties_required": True,
        "second_approver_id": "prin_example02",
    }
    bad.pop("separation_of_duties_decision_id", None)
    with pytest.raises(ContractError, match="governance"):
        validate_instance("state-transition-v1", bad)


def test_sod_accepts_distinct_authorized_approvers() -> None:
    governed = {
        **VALID_TRANSITION,
        "separation_of_duties_required": True,
        "second_approver_id": "prin_example02",
        "second_approver_authority_binding_id": "auth_fixture02",
    }
    validate_instance("state-transition-v1", governed)
