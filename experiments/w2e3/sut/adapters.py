"""Eight experiment-only adapters that share one decision evaluator."""

from __future__ import annotations

import csv
import json
from collections.abc import Callable, Mapping
from datetime import datetime
from io import StringIO

from evaluator import SuppliedDecisionEvaluator

Rendered = str | dict[str, object] | list[dict[str, object]]


def _p1_json(view: dict[str, object]) -> Rendered:
    return json.dumps(view, ensure_ascii=True, separators=(",", ":"), sort_keys=True)


def _p2_csv(view: dict[str, object]) -> Rendered:
    if not view:
        return ""
    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=sorted(view), lineterminator="\n")
    writer.writeheader()
    writer.writerow({field: view[field] for field in sorted(view)})
    return output.getvalue()


def _p3_bundle(view: dict[str, object]) -> Rendered:
    return {
        "entries": [
            {
                "content": json.dumps(view[field], ensure_ascii=True),
                "name": f"fields/{field}.json",
            }
            for field in sorted(view)
        ]
    }


def _p4_cache(view: dict[str, object]) -> Rendered:
    return f"CacheView({view!r})"


def _p5_search(view: dict[str, object]) -> Rendered:
    return {"document": {"fields": dict(view)}, "index": "w2e3-synthetic"}


def _p6_log(view: dict[str, object]) -> Rendered:
    fields = "\t".join(
        f"{field}={json.dumps(view[field], ensure_ascii=True, separators=(',', ':'))}"
        for field in sorted(view)
    )
    return f"event=w2e3_disclosure fields={fields}"


def _p7_error(view: dict[str, object]) -> Rendered:
    return {
        "error": "synthetic_failure",
        "safe_context": dict(view),
        "status": 400,
    }


def _p8_admin(view: dict[str, object]) -> Rendered:
    return [{"field": field, "value": view[field]} for field in sorted(view)]


_RENDERERS: dict[str, Callable[[dict[str, object]], Rendered]] = {
    "P1": _p1_json,
    "P2": _p2_csv,
    "P3": _p3_bundle,
    "P4": _p4_cache,
    "P5": _p5_search,
    "P6": _p6_log,
    "P7": _p7_error,
    "P8": _p8_admin,
}


def render_all(
    *,
    evaluator: SuppliedDecisionEvaluator,
    record: Mapping[str, object],
    decision: Mapping[str, object] | None,
    as_of: datetime,
    run_id: str,
    attack_profile: Mapping[str, object],
) -> dict[str, dict[str, object]]:
    outputs: dict[str, dict[str, object]] = {}
    for probe_id, renderer in _RENDERERS.items():
        outcome = evaluator.evaluate(
            record=record,
            decision=decision,
            as_of=as_of,
            run_id=run_id,
            probe_id=probe_id,
        )
        outputs[probe_id] = {
            "attack_requested": attack_profile.get(probe_id),
            "decision_reason": outcome.reason,
            "rendered": renderer(outcome.allowed_view),
        }
    return outputs
