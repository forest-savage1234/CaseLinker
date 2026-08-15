from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

VALID_CORRECTION = {
    "schema_version": "1.0",
    "contract_kind": "correction_identity",
    "correction_id": "corr_example01",
    "target_id": "asrt_example01",
    "kind": "supersession",
    "successor_id": "asrt_example02",
}

VALID_DEPENDENCY = {
    "schema_version": "1.0",
    "contract_kind": "dependency_edge",
    "dependency_id": "dep_example01",
    "from_id": "asrt_example01",
    "to_id": "proj_example01",
    "edge_kind": "projected_as",
}

VALID_SOURCE_TRANSITION = {
    "schema_version": "1.0",
    "contract_kind": "state_transition",
    "machine": "source_version",
    "subject_id": "docv_example01",
    "from_state": "observed",
    "to_state": "acquired",
    "actor_kind": "system",
    "reason_code": "bytes_hashed",
    "idempotency_key": "idem_source_1",
    "audit_event_id": "aud_example01",
    "guard_code": "hash_present",
    "separation_of_duties_required": False,
    "separation_of_duties_decision_id": "govdec_fixture01",
    "first_approver_id": "prin_example01",
    "first_approver_authority_binding_id": "auth_fixture01",
    "side_effects": [],
}


def test_correction_identity_is_accepted() -> None:
    validate_instance("correction-identity-v1", VALID_CORRECTION)


def test_correction_cannot_target_itself() -> None:
    bad = {**VALID_CORRECTION, "successor_id": "asrt_example01", "target_id": "asrt_example01"}
    with pytest.raises(ContractError, match="cannot correct itself"):
        validate_instance("correction-identity-v1", bad)


def test_dependency_edge_is_accepted() -> None:
    validate_instance("dependency-edge-v1", VALID_DEPENDENCY)


def test_dependency_cannot_be_reflexive() -> None:
    bad = {**VALID_DEPENDENCY, "to_id": "asrt_example01", "from_id": "asrt_example01"}
    with pytest.raises(ContractError, match="reflexive dependency"):
        validate_instance("dependency-edge-v1", bad)


def test_source_version_transition_is_accepted() -> None:
    validate_instance("state-transition-v1", VALID_SOURCE_TRANSITION)


def test_source_version_illegal_transition_is_rejected() -> None:
    bad = {**VALID_SOURCE_TRANSITION, "from_state": "removed", "to_state": "observed"}
    with pytest.raises(ContractError, match="illegal transition"):
        validate_instance("state-transition-v1", bad)


@pytest.mark.parametrize(
    ("machine", "subject_id", "from_state", "to_state"),
    [
        ("candidate_claim", "asrt_cand01", "proposed", "queued"),
        ("accepted_claim", "asrt_actv01", "active", "retracted"),
        ("identity_hypothesis", "hyp_id01xxxx", "needs_review", "possibly_same"),
        ("review_task", "tsk_rev01xxxx", "open", "assigned"),
        ("research_artifact", "proj_art01xxx", "building", "verified"),
        ("disclosure_request", "dreq_ex01xxx", "requested", "evaluating"),
        ("publication", "pub_ex01xxxxx", "draft", "authorized"),
        ("federation_package", "fed_ex01xxxxx", "received", "verified"),
    ],
)
def test_required_machines_accept_a_legal_step(
    machine: str, subject_id: str, from_state: str, to_state: str
) -> None:
    instance = {
        **VALID_SOURCE_TRANSITION,
        "machine": machine,
        "subject_id": subject_id,
        "from_state": from_state,
        "to_state": to_state,
    }
    validate_instance("state-transition-v1", instance)
