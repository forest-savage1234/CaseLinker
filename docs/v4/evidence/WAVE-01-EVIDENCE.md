# WAVE-01 evidence packet

```yaml
wave: "01"
status: "self_verified"
prior_independent_review_status: "fail"
failed_verification_commit: "b73cccc6f96b2b5d343df8b3cbbdb484ffc1ad45"
approved_base_commit: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
wave_00_accepted_closeout: "a370cfbc6ee419746cf925a682b85da1efd1193e"
result_commit: "uncommitted"
primary_proof_obligation: "temporal evidence network expressed as versioned policy-neutral contracts before infrastructure"
requirements_closed: []
requirements_partially_met_added_this_wave:
  - RESOLVE-001
  - RESOLVE-002
  - RESOLVE-003
  - RESOLVE-004
  - RESOLVE-005
  - AI-001
  - AI-002
  - OPS-001
adrs:
  - docs/v4/adr/W1-001-versioned-json-contracts.md
  - docs/v4/adr/W1-002-bitemporal-identities-transitions.md
  - docs/v4/adr/W1-003-lineage-and-hypotheses.md
  - docs/v4/adr/W1-004-eligibility-disclosure-authority.md
  - docs/v4/adr/W1-005-projections-ai-logical-postgres.md
migrations: []
implementation:
  - src/caselinker/v4_contracts/validate.py
  - schemas/v4/
tests:
  - tests/unit/v4/
independent_review_status: "not_started"
human_accepted: false
wave_02: "unstarted"
```

## Proof

Five distinctions are executable on policy-safe fixtures:

| Distinction | Test |
|---|---|
| Allegation is not guilt | unchanged v3 extractors; Wave 1 does not add a guilt type |
| Event time is not knowledge time | `test_knowledge_time_is_not_event_time` |
| Similarity is not identity | `test_similarity_does_not_create_identity` |
| Eligibility is not disclosure | `test_eligibility_is_not_disclosure` |
| Projection is not source of truth | `test_authoritative_projection_is_rejected` |

## Slice order (tests before implementation)

Recorded in git: failing test commits precede the schema/ADR commits for slices A–E.

## What Wave 1 did not do

No live migration, no Postgres service, no object store, no IdP, no policy content, no Wave 2 experiments, no official version.

## Rollback

Revert Wave 1 commits on `proposal/v4-research-network`. `main` and `proposal/v3-foundation` unchanged.

## Independent verification findings and disposition (appended)

**Failed commit:** `b73cccc6f96b2b5d343df8b3cbbdb484ffc1ad45`  
**Protocol:** §32. Wave 0 remains closed. Wave 2 remains unstarted.

| ID | Finding | Confirm / challenge | Correction |
|---|---|---|---|
| F1 | Correction/dependency identities, required machines, serialization/compatibility, disclosure requests, audit events missing or narrative-only | **Confirmed.** At `b73cccc6`, `schemas/v4/` had no correction, dependency, request, audit, compatibility, or as-known schemas; `state-transition-v1` listed four assertion pairs only. | New schemas + nine-machine table; `canonical_dumps`; `compatibility-v1` |
| F2 | Temporal checks were raw string compare / length | **Confirmed.** `validate.py` at that commit compared `start > end` as strings and treated day precision as `len(start) < 10`. | Calendar `date.fromisoformat`, UTC `Z` timestamps, open/partial intervals, as-known query |
| F3 | Person and event hypotheses were fused; evidence untyped | **Confirmed.** `identity-hypothesis-v1` used `evt_` for both sides and string evidence. | `person-hypothesis-v1` / `event-hypothesis-v1`; distinct subjects; `reopened`; `{kind, polarity}` |
| F4 | Disclosure decisions not bound to request; missing-policy only raised | **Confirmed.** No request schema; empty `policy_version` raised instead of producing a denied decision. | `disclosure-request-v1`; `decide_disclosure` copies request context and returns `denied` when policy is missing |
| F5 | AI provenance incomplete; no audit-event contract | **Confirmed.** AI schema lacked provider/tools/egress; no `audit-event-v1`. | Complete AI fields; reject `self_approved`; `audit-event-v1` rejects `source_passage` |
| F6 | Tests-before-fix | **Confirmed as process.** | Failing revision tests committed in `b9344156` before this repair |

### Revision validation

Focused `tests/unit/v4`: 68 passed. Full approved suite: repository/traceability/ruff/mypy/bandit/pip-audit/smoke passed. Fast pytest 442 passed, **same 3 Windows environment failures** as the pristine v3 base. Coverage 93.89% (≥ 90%).

Wave 1 is `self_verified`, not `gate_ready`, not `human_accepted`.

## Second independent re-verification (appended)

**Failed commit:** `3f57afe1a11b97e608bae4b184396240262a65c4`  
**Failing tests first:** `57f961fb`

| ID | Finding | Confirm / challenge | Correction |
|---|---|---|---|
| R2-1 | Nonempty `policy_version` authorized | **Confirmed.** `decide_disclosure` set `outcome` to `authorized` whenever a version string was present. | Authorize only with explicit `policy_result="authorized"` plus a version; otherwise `denied` |
| R2-2 | Decision omitted purpose and request context | **Confirmed.** Purpose was optional; request fields were not required on the decision. | Purpose and request context required and copied |
| R2-3 | Missing machine defaulted to `legacy_assertion`; guards unmodeled | **Confirmed.** `_check_transition` used `instance.get("machine", "legacy_assertion")`. | Machine, idempotency key, audit id, guard, two-person flag, and side effects required; no default machine |
| R2-4 | Incomplete AI provenance; open `tool_calls` | **Confirmed.** No retrieved artifacts/cost/timing/output; tool items were open objects. | Closed tool-call schema; required provenance fields; reject `source_passage` |
| R2-5 | `reopened` optional prior; polarity unconstrained | **Confirmed.** | Prior state required for `reopened`; polarity placement enforced |
| R2-6 | `canonical_dumps` allowed NaN | **Confirmed.** `json.dumps` default `allow_nan=True`. | `allow_nan=False` → `ContractError` |
| R2-7 | Impossible UTC could raise `ValueError` | **Confirmed.** `fromisoformat` was unwrapped after a digit regex that accepts `01-32`. | Wrap parse failures as `ContractError` |

### R2 validation

`tests/unit/v4`: 84 passed. Full suite: 458 passed, same 3 Windows environment failures. Coverage 94.19%. Smoke, ruff, mypy, pip-audit, bandit passed.

Wave 1 is again `self_verified`. Not `gate_ready`, not `human_accepted`, not complete. Wave 2 unstarted.
