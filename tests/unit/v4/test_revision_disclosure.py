from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, decide_disclosure, validate_instance

REQUEST = {
    "schema_version": "1.0",
    "contract_kind": "disclosure_request",
    "request_id": "dreq_example01",
    "principal_id": "prin_example01",
    "organization_id": "org_fixture01",
    "jurisdiction": "unspecified_fixture",
    "audience": "public_aggregate",
    "purpose": "aggregate_research",
    "requested_fields": ["legal_event_type"],
    "channel": "export",
    "data_subject_role": "unspecified_fixture",
    "vulnerability_classification": "unspecified_fixture",
    "procedural_status": "unspecified_fixture",
    "correction_state": "none",
    "source_restrictions": ["unspecified_fixture"],
    "collection_policy": "unspecified_fixture",
    "granularity": "field",
    "time_window": {"start": "2026-01-01", "end": "2026-01-31"},
}


def test_disclosure_request_is_accepted() -> None:
    validate_instance("disclosure-request-v1", REQUEST)


def test_decision_must_bind_request() -> None:
    decision = decide_disclosure(
        REQUEST, policy_version="pol_fixture_unspecified", research_eligible=True
    )
    validate_instance("disclosure-decision-v1", decision)
    assert decision["request_id"] == REQUEST["request_id"]
    assert decision["audience"] == REQUEST["audience"]
    assert decision["purpose"] == REQUEST["purpose"]


def test_missing_policy_returns_denied_decision() -> None:
    decision = decide_disclosure(REQUEST, policy_version=None, research_eligible=True)
    validate_instance("disclosure-decision-v1", decision)
    assert decision["outcome"] == "denied"
    assert decision["research_eligible"] is True
    assert decision["treat_eligible_as_disclosed"] is False


def test_eligible_without_policy_is_not_authorized() -> None:
    decision = decide_disclosure(REQUEST, policy_version="", research_eligible=True)
    assert decision["outcome"] != "authorized"
    with pytest.raises(ContractError, match="eligibility is not disclosure"):
        validate_instance(
            "disclosure-decision-v1",
            {**decision, "treat_eligible_as_disclosed": True, "outcome": "authorized"},
        )
