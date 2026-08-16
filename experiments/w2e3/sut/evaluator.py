"""Shared supplied-decision evaluator for the disposable W2-E3 r2 mechanism."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Final

EVALUATOR_IDENTITY: Final = "shared-supplied-decision-evaluator-v2"


@dataclass(frozen=True, slots=True)
class DecisionOutcome:
    allowed_view: dict[str, object]
    reason: str


def parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() != UTC.utcoffset(parsed):
        return None
    return parsed.astimezone(UTC)


def _is_scalar(value: object) -> bool:
    return value is None or isinstance(value, (str, int, float, bool))


def _collect_scalars(value: object, into: set[object]) -> None:
    if isinstance(value, Mapping):
        for nested in value.values():
            _collect_scalars(nested, into)
        return
    if isinstance(value, list):
        for nested in value:
            _collect_scalars(nested, into)
        return
    if _is_scalar(value):
        into.add(value)


def _has_unauthorized_structure(
    value: object,
    *,
    authorized_names: set[str],
    unauthorized_values: set[object],
) -> bool:
    """Default-deny nested names and unauthorized source values at every depth."""

    if isinstance(value, Mapping):
        for key, nested in value.items():
            if not isinstance(key, str) or key not in authorized_names:
                return True
            if _has_unauthorized_structure(
                nested,
                authorized_names=authorized_names,
                unauthorized_values=unauthorized_values,
            ):
                return True
        return False
    if isinstance(value, list):
        return any(
            _has_unauthorized_structure(
                item,
                authorized_names=authorized_names,
                unauthorized_values=unauthorized_values,
            )
            for item in value
        )
    if _is_scalar(value):
        return value in unauthorized_values
    return True


class SuppliedDecisionEvaluator:
    """Apply only the supplied decision; never infer policy or consult eligibility."""

    identity: Final = EVALUATOR_IDENTITY

    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    def evaluate(
        self,
        *,
        record: Mapping[str, object],
        decision: Mapping[str, object] | None,
        as_of: datetime,
        run_id: str,
        probe_id: str,
    ) -> DecisionOutcome:
        outcome = self._evaluate(record=record, decision=decision, as_of=as_of)
        self.calls.append(
            {
                "evaluator_identity": self.identity,
                "run_id": run_id,
                "probe_id": probe_id,
                "decision_id": decision.get("decision_id") if decision else None,
                "authorized_fields": sorted(outcome.allowed_view),
                "reason": outcome.reason,
                "eligibility_consulted": False,
            }
        )
        return outcome

    @staticmethod
    def _evaluate(
        *,
        record: Mapping[str, object],
        decision: Mapping[str, object] | None,
        as_of: datetime,
    ) -> DecisionOutcome:
        if decision is None:
            return DecisionOutcome({}, "missing_decision")
        if decision.get("effect") != "allow":
            return DecisionOutcome({}, "explicit_or_invalid_deny")
        if decision.get("revocation_state") != "active":
            return DecisionOutcome({}, "revoked_or_invalid")
        if not isinstance(decision.get("audience"), str) or not decision["audience"]:
            return DecisionOutcome({}, "invalid_audience")
        if not isinstance(decision.get("purpose"), str) or not decision["purpose"]:
            return DecisionOutcome({}, "invalid_purpose")
        expiry = parse_utc(decision.get("expiry"))
        if expiry is None or expiry <= as_of:
            return DecisionOutcome({}, "expired_or_invalid_expiry")
        allowed = decision.get("allowed_fields")
        if (
            not isinstance(allowed, list)
            or any(not isinstance(field, str) for field in allowed)
            or len(set(allowed)) != len(allowed)
            or any(field not in record for field in allowed)
        ):
            return DecisionOutcome({}, "invalid_allowed_fields")

        authorized_names = set(allowed)
        unauthorized_values: set[object] = set()
        for name, value in record.items():
            if name not in authorized_names:
                _collect_scalars(value, unauthorized_values)
        for field in allowed:
            if _has_unauthorized_structure(
                record[field],
                authorized_names=authorized_names,
                unauthorized_values=unauthorized_values,
            ):
                return DecisionOutcome({}, "nested_unauthorized_structure")

        view = {field: record[field] for field in sorted(allowed)}
        return DecisionOutcome(view, "supplied_allow")
