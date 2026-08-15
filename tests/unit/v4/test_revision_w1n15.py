from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

VALID_REPORTED_CLAIM = {
    "schema_version": "1.0",
    "contract_kind": "reported_claim",
    "assertion_id": "asrt_example01",
    "speech_status": "reported",
    "procedural_status": "charge",
    "finding": "none",
    "treat_allegation_as_guilt": False,
}


def test_reported_charge_is_accepted() -> None:
    validate_instance("reported-claim-v1", VALID_REPORTED_CLAIM)


def test_treat_allegation_as_guilt_is_rejected() -> None:
    bad = {**VALID_REPORTED_CLAIM, "treat_allegation_as_guilt": True}
    with pytest.raises(ContractError, match="allegation is not guilt"):
        validate_instance("reported-claim-v1", bad)


def test_charge_cannot_be_recorded_as_guilt() -> None:
    bad = {**VALID_REPORTED_CLAIM, "finding": "guilt"}
    with pytest.raises(ContractError, match="allegation is not guilt"):
        validate_instance("reported-claim-v1", bad)


def test_acquittal_cannot_be_recorded_as_guilt() -> None:
    bad = {**VALID_REPORTED_CLAIM, "procedural_status": "acquittal", "finding": "guilt"}
    with pytest.raises(ContractError, match="allegation is not guilt"):
        validate_instance("reported-claim-v1", bad)


def test_dismissal_cannot_be_recorded_as_guilt() -> None:
    bad = {**VALID_REPORTED_CLAIM, "procedural_status": "dismissal", "finding": "guilt"}
    with pytest.raises(ContractError, match="allegation is not guilt"):
        validate_instance("reported-claim-v1", bad)
