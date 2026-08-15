from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

PERSON = {
    "schema_version": "1.0",
    "contract_kind": "person_hypothesis",
    "hypothesis_id": "phyp_example01",
    "left_subject_id": "per_alpha01xxx",
    "right_subject_id": "per_beta01xxxx",
    "state": "possibly_same",
    "positive_evidence": [{"kind": "shared_name_token", "polarity": "supports"}],
    "negative_evidence": [{"kind": "distinct_date_of_birth", "polarity": "contradicts"}],
    "creates_canonical_identity": False,
    "inference_method": "reviewer_comparison",
}

EVENT = {
    "schema_version": "1.0",
    "contract_kind": "event_hypothesis",
    "hypothesis_id": "ehyp_example01",
    "left_event_id": "evt_alpha01xxx",
    "right_event_id": "evt_beta01xxxx",
    "state": "possibly_same",
    "positive_evidence": [{"kind": "shared_date", "polarity": "supports"}],
    "negative_evidence": [{"kind": "distinct_forum", "polarity": "contradicts"}],
    "creates_canonical_identity": False,
    "inference_method": "reviewer_comparison",
}


def test_person_hypothesis_is_accepted() -> None:
    validate_instance("person-hypothesis-v1", PERSON)


def test_event_hypothesis_is_accepted() -> None:
    validate_instance("event-hypothesis-v1", EVENT)


def test_person_hypothesis_rejects_identical_subjects() -> None:
    bad = {**PERSON, "right_subject_id": PERSON["left_subject_id"]}
    with pytest.raises(ContractError, match="distinct subjects"):
        validate_instance("person-hypothesis-v1", bad)


def test_event_hypothesis_rejects_identical_events() -> None:
    bad = {**EVENT, "right_event_id": EVENT["left_event_id"]}
    with pytest.raises(ContractError, match="distinct subjects"):
        validate_instance("event-hypothesis-v1", bad)


def test_reopened_person_hypothesis_is_accepted() -> None:
    reopened = {**PERSON, "state": "reopened", "prior_state": "possibly_same"}
    validate_instance("person-hypothesis-v1", reopened)


def test_person_cannot_use_event_identifiers() -> None:
    bad = {**PERSON, "left_subject_id": "evt_notaperson"}
    with pytest.raises(ContractError, match="pattern"):
        validate_instance("person-hypothesis-v1", bad)


def test_untyped_evidence_string_is_rejected() -> None:
    bad = {**EVENT, "positive_evidence": ["shared_date"]}
    with pytest.raises(ContractError, match="object"):
        validate_instance("event-hypothesis-v1", bad)
