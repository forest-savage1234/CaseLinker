from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

VALID_PROJECTION = {
    "schema_version": "1.0",
    "contract_kind": "projection_artifact",
    "artifact_id": "proj_example01",
    "kind": "cac_ntriples",
    "digest_sha256": "a" * 64,
    "authoritative": False,
}

VALID_AI = {
    "schema_version": "1.0",
    "contract_kind": "ai_execution",
    "execution_id": "aiex_example01",
    "provider": "fixture",
    "model_identity": "fixture-unspecified",
    "model_version": "0",
    "parameters_digest": "c" * 64,
    "execution_environment": "test",
    "prompt_identity": "prm_example01",
    "allowed_input_digest": "b" * 64,
    "tool_calls": [],
    "structured_output_valid": True,
    "policy_decision": "bounded_proposal",
    "egress_class": "none",
    "reproducibility_limitation": "fixture_only",
    "reviewer_disposition": "pending",
    "disposition": "proposed",
}


def test_non_authoritative_projection_is_accepted() -> None:
    validate_instance("projection-artifact-v1", VALID_PROJECTION)


def test_authoritative_projection_is_rejected() -> None:
    bad = {**VALID_PROJECTION, "authoritative": True}
    with pytest.raises(ContractError, match="projection is not a source of truth"):
        validate_instance("projection-artifact-v1", bad)


def test_ai_proposal_is_accepted() -> None:
    validate_instance("ai-execution-v1", VALID_AI)


def test_ai_cannot_publish() -> None:
    bad = {**VALID_AI, "disposition": "published"}
    with pytest.raises(ContractError, match="AI execution cannot publish"):
        validate_instance("ai-execution-v1", bad)
