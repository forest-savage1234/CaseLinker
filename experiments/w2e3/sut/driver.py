"""CLI driver for the isolated W2-E3 supplied-decision SUT."""

from __future__ import annotations

import argparse
import copy
import json
from collections.abc import Mapping
from pathlib import Path

from adapters import render_all
from evaluator import EVALUATOR_IDENTITY, SuppliedDecisionEvaluator, parse_utc

SUT_REVISION = "w2e3-disclosure-v1"


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=True, indent=2, sort_keys=True)
        stream.write("\n")


def _subject_for_run(base: Mapping[str, object], run: Mapping[str, object]) -> dict[str, object]:
    subject = dict(base)
    changes = run.get("subject_changes", {})
    if not isinstance(changes, Mapping):
        raise ValueError("subject_changes must be an object")
    subject.update(changes)
    order = run.get("subject_order")
    if order is None:
        return subject
    if not isinstance(order, list) or any(not isinstance(key, str) for key in order):
        raise ValueError("subject_order must be a list of field names")
    if set(order) != set(subject):
        raise ValueError("subject_order must name every subject field exactly once")
    return {key: subject[key] for key in order}


def _decision_for_run(
    decisions: Mapping[str, object], run: Mapping[str, object]
) -> Mapping[str, object] | None:
    decision_id = run.get("decision_id")
    if decision_id is None:
        return None
    if not isinstance(decision_id, str) or not isinstance(decisions.get(decision_id), Mapping):
        raise ValueError(f"unknown decision: {decision_id!r}")
    decision = copy.deepcopy(dict(decisions[decision_id]))
    changes = run.get("decision_changes", {})
    if not isinstance(changes, Mapping):
        raise ValueError("decision_changes must be an object")
    decision.update(changes)
    return decision


def execute(fixture: Mapping[str, object]) -> dict[str, object]:
    subject = fixture.get("subject")
    decisions = fixture.get("decisions")
    runs = fixture.get("runs")
    attack_profile = fixture.get("attack_profile")
    as_of = parse_utc(fixture.get("as_of"))
    if (
        not isinstance(subject, Mapping)
        or not isinstance(decisions, Mapping)
        or not isinstance(runs, list)
        or not isinstance(attack_profile, Mapping)
        or as_of is None
    ):
        raise ValueError("fixture is missing a required input surface")

    evaluator = SuppliedDecisionEvaluator()
    results: list[dict[str, object]] = []
    for run in runs:
        if not isinstance(run, Mapping) or not isinstance(run.get("run_id"), str):
            raise ValueError("each run must have a string run_id")
        run_id = run["run_id"]
        outputs = render_all(
            evaluator=evaluator,
            record=_subject_for_run(subject, run),
            decision=_decision_for_run(decisions, run),
            as_of=as_of,
            run_id=run_id,
            attack_profile=attack_profile,
        )
        results.append(
            {
                "group": run.get("group"),
                "outputs": outputs,
                "run_id": run_id,
            }
        )

    return {
        "schema_version": "w2e3-sut-output-v1",
        "sut_revision": SUT_REVISION,
        "evaluator_identity": EVALUATOR_IDENTITY,
        "eligibility_received_by_evaluator": False,
        "oracle_received": False,
        "results": results,
        "evaluator_calls": evaluator.calls,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    if not isinstance(fixture, Mapping):
        raise ValueError("fixture root must be an object")
    _write_json(args.output, execute(fixture))


if __name__ == "__main__":
    main()
