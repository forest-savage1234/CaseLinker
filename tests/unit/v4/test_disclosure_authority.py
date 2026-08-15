from __future__ import annotations

import hashlib

import pytest

from caselinker.v4_contracts import ContractError, canonical_dumps, validate_instance
from tests.unit.v4.test_revision_disclosure import POLICY_DECISION, REQUEST

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
    "data_subject_role": "unspecified_fixture",
    "vulnerability_classification": "unspecified_fixture",
    "procedural_status": "unspecified_fixture",
    "correction_state": "none",
    "source_restrictions": ["unspecified_fixture"],
    "collection_policy": "unspecified_fixture",
    "granularity": "field",
    "time_window": {"start": "2026-01-01", "end": "2026-01-31"},
    "outcome": "denied",
    "policy_version": "pol_fixture_unspecified",
    "policy_result": "denied",
    "policy_decision_id": "pdec_fixture01",
    "research_eligible": True,
    "treat_eligible_as_disclosed": False,
    "transformations": {
        "minimization": False,
        "pseudonymization": False,
        "aggregation": False,
        "redaction": False,
        "watermarking": False,
    },
    "expiry": None,
    "revocation_state": "not_applicable",
    "decision_reason": "denied_fixture_policy",
    "authority_binding_id": "auth_fixture01",
    "audit_event_id": "aud_example01",
    "request_digest": hashlib.sha256(canonical_dumps(REQUEST)).hexdigest(),
}

VALID_PRINCIPAL = {
    "schema_version": "1.0",
    "contract_kind": "authority_binding",
    "authority_binding_id": "auth_fixture01",
    "principal_id": "prin_example01",
    "organization_id": "org_fixture01",
    "role": "reviewer",
    "authority_interface": "declared_binding",
}


def test_disclosure_decision_is_accepted() -> None:
    validate_instance("disclosure-decision-v1", VALID_DECISION)


def test_external_policy_decision_is_accepted() -> None:
    validate_instance("disclosure-policy-decision-v1", POLICY_DECISION)


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
        "data_subject_role": "unspecified_fixture",
        "vulnerability_classification": "unspecified_fixture",
        "procedural_status": "unspecified_fixture",
        "correction_state": "none",
        "source_restrictions": ["unspecified_fixture"],
        "collection_policy": "unspecified_fixture",
        "granularity": "field",
        "time_window": {"start": "2026-01-01", "end": "2026-01-31"},
        "outcome": "authorized",
        "policy_version": "",
        "policy_result": "authorized",
        "policy_decision_id": None,
        "research_eligible": True,
        "treat_eligible_as_disclosed": False,
        "transformations": {
            "minimization": False,
            "pseudonymization": False,
            "aggregation": False,
            "redaction": False,
            "watermarking": False,
        },
        "expiry": None,
        "revocation_state": "not_applicable",
        "decision_reason": "missing_policy",
        "authority_binding_id": None,
        "audit_event_id": "aud_example01",
        "request_digest": hashlib.sha256(canonical_dumps(REQUEST)).hexdigest(),
    }
    with pytest.raises(ContractError, match="missing policy version denies"):
        validate_instance("disclosure-decision-v1", bad)


def test_authority_binding_is_accepted() -> None:
    validate_instance("authority-binding-v1", VALID_PRINCIPAL)


def test_display_name_is_not_a_principal() -> None:
    bad = {**VALID_PRINCIPAL, "principal_id": "Reviewer Jane"}
    with pytest.raises(ContractError, match="pattern"):
        validate_instance("authority-binding-v1", bad)
