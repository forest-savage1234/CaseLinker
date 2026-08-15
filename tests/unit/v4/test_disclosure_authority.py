from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

VALID_DECISION = {
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

VALID_PRINCIPAL = {
    "schema_version": "1.0",
    "contract_kind": "authority_binding",
    "principal_id": "prin_example01",
    "organization_id": "org_fixture01",
    "role": "reviewer",
    "authority_interface": "declared_binding",
}


def test_disclosure_decision_is_accepted() -> None:
    validate_instance("disclosure-decision-v1", VALID_DECISION)


def test_eligibility_is_not_disclosure() -> None:
    bad = {**VALID_DECISION, "treat_eligible_as_disclosed": True, "outcome": "authorized"}
    with pytest.raises(ContractError, match="eligibility is not disclosure"):
        validate_instance("disclosure-decision-v1", bad)


def test_missing_policy_version_denies() -> None:
    bad = {
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
        "outcome": "authorized",
        "policy_version": "",
        "policy_result": "authorized",
        "research_eligible": True,
        "treat_eligible_as_disclosed": False,
    }
    with pytest.raises(ContractError, match="missing policy version denies"):
        validate_instance("disclosure-decision-v1", bad)


def test_authority_binding_is_accepted() -> None:
    validate_instance("authority-binding-v1", VALID_PRINCIPAL)


def test_display_name_is_not_a_principal() -> None:
    bad = {**VALID_PRINCIPAL, "principal_id": "Reviewer Jane"}
    with pytest.raises(ContractError, match="pattern"):
        validate_instance("authority-binding-v1", bad)
