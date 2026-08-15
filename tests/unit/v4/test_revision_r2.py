from __future__ import annotations

import math

import pytest

from caselinker.v4_contracts import (
    ContractError,
    canonical_dumps,
    decide_disclosure,
    validate_instance,
)
from tests.unit.v4.test_bitemporal_identity import VALID_TRANSITION
from tests.unit.v4.test_disclosure_authority import VALID_DECISION
from tests.unit.v4.test_revision_audit_ai import VALID_AI
from tests.unit.v4.test_revision_disclosure import REQUEST
from tests.unit.v4.test_revision_hypotheses import EVENT, PERSON

# --- 1. nonempty policy_version must not authorize ---


def test_arbitrary_policy_version_does_not_authorize() -> None:
    decision = decide_disclosure(
        REQUEST, policy_version="pol_arbitrary_string", research_eligible=True
    )
    assert decision["outcome"] != "authorized"
    assert decision["outcome"] in {"denied", "pending"}


def test_explicit_external_policy_result_is_required_to_authorize() -> None:
    decision = decide_disclosure(
        REQUEST,
        policy_version="pol_fixture_unspecified",
        research_eligible=True,
        policy_result="authorized",
    )
    assert decision["outcome"] == "authorized"
    assert decision["policy_result"] == "authorized"


# --- 2. purpose and request context on the decision ---


def test_disclosure_decision_requires_purpose() -> None:
    bad = dict(VALID_DECISION)
    bad.pop("purpose")
    with pytest.raises(ContractError, match="purpose"):
        validate_instance("disclosure-decision-v1", bad)


def test_decision_preserves_request_fields() -> None:
    decision = decide_disclosure(
        REQUEST, policy_version=None, research_eligible=False, policy_result=None
    )
    for field in (
        "principal_id",
        "organization_id",
        "audience",
        "purpose",
        "requested_fields",
        "channel",
        "jurisdiction",
    ):
        assert field in decision


# --- 3. machine, idempotency, audit required; no silent legacy default ---


def test_state_transition_requires_selected_machine() -> None:
    bad = dict(VALID_TRANSITION)
    bad.pop("machine")
    with pytest.raises(ContractError, match="machine"):
        validate_instance("state-transition-v1", bad)


def test_state_transition_requires_idempotency_and_audit() -> None:
    incomplete = dict(VALID_TRANSITION)
    incomplete.pop("idempotency_key")
    incomplete.pop("audit_event_id")
    with pytest.raises(ContractError, match="required"):
        validate_instance("state-transition-v1", incomplete)


def test_publication_does_not_hardcode_two_person_control() -> None:
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
        "separation_of_duties_required": False,
        "first_approver_id": "prin_example01",
        "side_effects": ["notify_subscribers"],
    }
    validate_instance("state-transition-v1", instance)


# --- 4. complete AI provenance ---


def test_ai_execution_requires_retrieved_artifacts_cost_and_timing() -> None:
    incomplete = dict(VALID_AI)
    incomplete.pop("retrieved_artifact_ids")
    incomplete.pop("cost")
    incomplete.pop("timing_ms")
    with pytest.raises(ContractError, match="required"):
        validate_instance("ai-execution-v1", incomplete)


def test_ai_tool_call_rejects_source_passage() -> None:
    complete = {
        **VALID_AI,
        "retrieved_artifact_ids": ["proj_example01"],
        "structured_output": {"kind": "candidate_span"},
        "validation_result": "schema_valid",
        "cost": {"currency": "USD", "amount_millionths": 0},
        "timing_ms": 1,
        "resulting_canonical_ids": [],
        "tool_calls": [{"name": "read_fixture", "args_digest": "d" * 64, "source_passage": "no"}],
    }
    with pytest.raises(ContractError, match="unknown field"):
        validate_instance("ai-execution-v1", complete)


# --- 5. coherent reopening and evidence polarity ---


def test_reopened_without_prior_state_is_rejected() -> None:
    bad = {**PERSON, "state": "reopened"}
    bad.pop("prior_state", None)
    with pytest.raises(ContractError, match="prior_state"):
        validate_instance("person-hypothesis-v1", bad)


def test_event_reopened_without_prior_state_is_rejected() -> None:
    bad = {**EVENT, "state": "reopened"}
    with pytest.raises(ContractError, match="prior_state"):
        validate_instance("event-hypothesis-v1", bad)


def test_positive_evidence_cannot_contradict() -> None:
    bad = {
        **PERSON,
        "positive_evidence": [{"kind": "shared_name_token", "polarity": "contradicts"}],
    }
    with pytest.raises(ContractError, match="polarity"):
        validate_instance("person-hypothesis-v1", bad)


def test_negative_evidence_cannot_support() -> None:
    bad = {
        **EVENT,
        "negative_evidence": [{"kind": "distinct_forum", "polarity": "supports"}],
    }
    with pytest.raises(ContractError, match="polarity"):
        validate_instance("event-hypothesis-v1", bad)


# --- 6-7. canonical JSON and parse errors ---


def test_canonical_dumps_rejects_nan() -> None:
    with pytest.raises(ContractError, match="non-JSON"):
        canonical_dumps({"n": math.nan})


def test_canonical_dumps_rejects_infinity() -> None:
    with pytest.raises(ContractError, match="non-JSON"):
        canonical_dumps({"n": math.inf})


def test_impossible_utc_timestamp_is_contract_error() -> None:
    query = {
        "schema_version": "1.0",
        "contract_kind": "as_known_query",
        "as_of_knowledge_time": "2026-01-32T00:00:00Z",
        "valid_on": "2026-01-05",
    }
    with pytest.raises(ContractError):
        validate_instance("as-known-query-v1", query)
