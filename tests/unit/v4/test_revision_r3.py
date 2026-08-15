from __future__ import annotations

import pytest

from caselinker.v4_contracts import (
    ContractError,
    canonical_dumps,
    decide_disclosure,
    validate_instance,
)
from tests.unit.v4.test_bitemporal_identity import VALID_TRANSITION
from tests.unit.v4.test_disclosure_authority import VALID_DECISION
from tests.unit.v4.test_revision_disclosure import POLICY_DECISION, REQUEST

# Accepted incomplete decision at e968bdfb: request context only, no §7.8 bindings.
INCOMPLETE_DECISION = {
    "schema_version": "1.0",
    "contract_kind": "disclosure_decision",
    "request_id": "dreq_example01",
    "decision_id": "ddec_example01",
    "principal_id": "prin_example01",
    "organization_id": "org_fixture01",
    "audience": "public_aggregate",
    "purpose": "aggregate_research",
    "requested_fields": ["legal_event_type"],
    "channel": "export",
    "jurisdiction": "unspecified_fixture",
    "outcome": "denied",
    "policy_version": "pol_fixture_unspecified",
    "policy_result": "denied",
    "research_eligible": True,
    "treat_eligible_as_disclosed": False,
}


def test_whitespace_policy_version_is_invalid() -> None:
    with pytest.raises(ContractError, match=r"policy\.version"):
        decide_disclosure(
            REQUEST,
            research_eligible=True,
            policy_decision={
                **POLICY_DECISION,
                "policy_version": "  pol_fixture_unspecified  ",
            },
        )


def test_non_opaque_policy_version_is_invalid() -> None:
    with pytest.raises(ContractError, match=r"policy\.version"):
        decide_disclosure(
            REQUEST,
            research_eligible=True,
            policy_decision={**POLICY_DECISION, "policy_version": "not a policy id"},
        )


def test_denied_policy_result_cannot_become_minimized() -> None:
    bad = {
        **VALID_DECISION,
        "policy_result": "denied",
        "outcome": "minimized",
    }
    with pytest.raises(ContractError, match="outcome"):
        validate_instance("disclosure-decision-v1", bad)


def test_missing_policy_cannot_be_pending() -> None:
    bad = {
        **VALID_DECISION,
        "policy_version": "",
        "policy_result": "pending",
        "outcome": "pending",
    }
    with pytest.raises(ContractError, match="denied"):
        validate_instance("disclosure-decision-v1", bad)


def test_decision_requires_section_78_bindings() -> None:
    with pytest.raises(ContractError, match="required"):
        validate_instance("disclosure-decision-v1", dict(INCOMPLETE_DECISION))


def test_decision_request_digest_matches_request() -> None:
    decision = decide_disclosure(REQUEST, research_eligible=False)
    assert "request_digest" in decision
    assert (
        decision["request_digest"]
        == __import__("hashlib").sha256(canonical_dumps(REQUEST)).hexdigest()
    )


def test_publication_without_external_sod_is_accepted() -> None:
    instance = {
        "schema_version": "1.0",
        "contract_kind": "state_transition",
        "machine": "publication",
        "subject_id": "pub_ex01xxxxx",
        "from_state": "authorized",
        "to_state": "published",
        "actor_kind": "reviewer",
        "reason_code": "release",
        "idempotency_key": "idem_pub_1",
        "audit_event_id": "aud_example01",
        "guard_code": "publication_ready",
        "side_effects": ["notify_subscribers"],
        "separation_of_duties_required": False,
        "separation_of_duties_decision_id": "govdec_fixture01",
        "first_approver_id": "prin_example01",
        "first_approver_authority_binding_id": "auth_fixture01",
    }
    validate_instance("state-transition-v1", instance)


def test_external_sod_requires_distinct_approvers() -> None:
    instance = {
        **VALID_TRANSITION,
        "separation_of_duties_required": True,
        "first_approver_id": "prin_example01",
        "second_approver_id": "prin_example01",
        "second_approver_authority_binding_id": "auth_fixture02",
    }
    instance.pop("two_person_control", None)
    with pytest.raises(ContractError, match="distinct"):
        validate_instance("state-transition-v1", instance)


def test_two_person_boolean_is_not_a_governance_rule() -> None:
    instance = {
        **VALID_TRANSITION,
        "two_person_control": False,
    }
    instance.pop("separation_of_duties_required", None)
    instance.pop("separation_of_duties_decision_id", None)
    instance.pop("first_approver_id", None)
    instance.pop("first_approver_authority_binding_id", None)
    instance.pop("second_approver_id", None)
    with pytest.raises(ContractError, match="unknown field"):
        validate_instance("state-transition-v1", instance)


def test_canonical_dumps_rejects_unserializable_type() -> None:
    with pytest.raises(ContractError, match="non-JSON"):
        canonical_dumps({"x": object()})
