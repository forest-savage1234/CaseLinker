from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

VALID_LINEAGE = {
    "schema_version": "1.0",
    "contract_kind": "source_lineage",
    "source_family_id": "sfam_presswire01",
    "left_version_id": "docv_example01",
    "right_version_id": "docv_example02",
    "relation": "derivation",
    "same_source_family": True,
}

VALID_HYPOTHESIS = {
    "schema_version": "1.0",
    "contract_kind": "identity_hypothesis",
    "hypothesis_id": "hyp_example01",
    "left_id": "evt_example01",
    "right_id": "evt_example02",
    "state": "possibly_same",
    "positive_evidence": ["shared_date"],
    "negative_evidence": ["different_jurisdiction"],
    "creates_canonical_identity": False,
    "inference_method": "reviewer_comparison",
}


def test_derivation_record_is_accepted() -> None:
    validate_instance("source-lineage-v1", VALID_LINEAGE)


def test_same_family_corroboration_is_rejected() -> None:
    bad = {**VALID_LINEAGE, "relation": "corroboration"}
    with pytest.raises(ContractError, match="derivation is not corroboration"):
        validate_instance("source-lineage-v1", bad)


def test_hypothesis_is_accepted() -> None:
    validate_instance("identity-hypothesis-v1", VALID_HYPOTHESIS)


def test_similarity_does_not_create_identity() -> None:
    bad = {**VALID_HYPOTHESIS, "creates_canonical_identity": True}
    with pytest.raises(ContractError, match="similarity is not identity"):
        validate_instance("identity-hypothesis-v1", bad)


def test_transitive_closure_is_rejected() -> None:
    bad = {**VALID_HYPOTHESIS, "inference_method": "transitive_closure"}
    with pytest.raises(ContractError, match="blind transitivity"):
        validate_instance("identity-hypothesis-v1", bad)
