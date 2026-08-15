from __future__ import annotations

import pytest

from caselinker.v4_contracts import ContractError, validate_instance

DAY = {
    "schema_version": "1.0",
    "contract_kind": "bitemporal_interval",
    "event_time": {"start": "2026-01-05", "end": "2026-01-05", "precision": "day"},
    "knowledge_time": "2026-01-08T00:00:00Z",
    "precision_source": "source_text",
    "time_model": "bitemporal",
}


def test_invalid_calendar_day_is_rejected() -> None:
    bad = {
        **DAY,
        "event_time": {"start": "2026-02-30", "end": "2026-02-30", "precision": "day"},
    }
    with pytest.raises(ContractError, match="invalid calendar"):
        validate_instance("bitemporal-interval-v1", bad)


def test_open_interval_is_accepted() -> None:
    open_interval = {
        **DAY,
        "event_time": {"start": "2026-01-05", "end": None, "precision": "day", "open_end": True},
    }
    validate_instance("bitemporal-interval-v1", open_interval)


def test_month_precision_rejects_day_component() -> None:
    bad = {
        **DAY,
        "event_time": {"start": "2026-01-05", "end": "2026-01-05", "precision": "month"},
    }
    with pytest.raises(ContractError, match="month precision"):
        validate_instance("bitemporal-interval-v1", bad)


def test_year_precision_accepts_year_only() -> None:
    year_only = {
        **DAY,
        "event_time": {"start": "2026", "end": "2026", "precision": "year"},
    }
    validate_instance("bitemporal-interval-v1", year_only)


def test_non_utc_knowledge_time_is_rejected() -> None:
    bad = {**DAY, "knowledge_time": "2026-01-08T00:00:00+00:00"}
    with pytest.raises(ContractError, match="UTC"):
        validate_instance("bitemporal-interval-v1", bad)


def test_as_known_query_is_accepted() -> None:
    query = {
        "schema_version": "1.0",
        "contract_kind": "as_known_query",
        "as_of_knowledge_time": "2026-01-20T00:00:00Z",
        "valid_on": "2026-01-05",
    }
    validate_instance("as-known-query-v1", query)


def test_january_as_known_does_not_use_february_knowledge() -> None:
    january = {
        **DAY,
        "knowledge_time": "2026-01-08T00:00:00Z",
    }
    february_correction = {
        **DAY,
        "event_time": {"start": "2026-01-05", "end": "2026-01-05", "precision": "day"},
        "knowledge_time": "2026-02-03T00:00:00Z",
    }
    validate_instance("bitemporal-interval-v1", january)
    validate_instance("bitemporal-interval-v1", february_correction)
    query = {
        "schema_version": "1.0",
        "contract_kind": "as_known_query",
        "as_of_knowledge_time": "2026-01-20T00:00:00Z",
        "valid_on": "2026-01-05",
        "exclude_knowledge_after": "2026-01-20T00:00:00Z",
    }
    validate_instance("as-known-query-v1", query)
    assert january["knowledge_time"] <= query["exclude_knowledge_after"]
    assert february_correction["knowledge_time"] > query["exclude_knowledge_after"]
