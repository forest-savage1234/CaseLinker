# WAVE-01 evidence packet

Wave 1 is `human_accepted` and `closed` after operator acceptance of implementation `740862d3` and gate-ready record `c30a1d3f` (D-026). Historical review, repair, and invalid-review records below are preserved. This is **not** Phase 0 / Gate 0 completion, not a deployment authorization, and not an official version. Wave 2 remains `unstarted`.

```yaml
wave: "01"
status: "closed"
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
independent_review_status: "gate_ready_recommended"
independent_review_record: "docs/v4/evidence/WAVE-01-W1N15-REVIEW.md"
prior_review_status: "review_invalid"
human_accepted: true
legal_state: "closed"
accepted_implementation_commit: "740862d339d8e1ea29f42d30144d51cb076045b0"
accepted_gate_ready_commit: "c30a1d3f4175d50b5461799194ea54b960d41624"
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

## Fourth independent re-verification (appended)

**Failed commit:** `f41568e294e9becf032af0904f1ee51483742b4a`  
**Protocol:** `GROK_BUILD_PROGRAM.md` §§31–32. Wave 0 remains closed. Wave 2 remains unstarted.

| ID | Finding | Disposition at failure |
|---|---|---|
| R4-1 | `decide_disclosure` manufactured policy reason, authority, audit identity, transformations, expiry, and revocation from a scalar result | **Confirmed; repair required** |
| R4-2 | `request_digest` was shape-checked but not recomputed against the request and copied context | **Confirmed; repair required** |
| R4-3 | `minimized` could contain no transformation; disclosure time windows could be inverted | **Confirmed; repair required** |
| R4-4 | SoD accepted distinct principal ids without authority bindings or an external governance-decision identity | **Confirmed; repair required** |

Wave 1 returned to `revision_required`. The r4 adversarial tests are committed before implementation. No Wave 2 work is authorized.

### R4 repair and self-verification (appended)

**Tests-first commit:** `08390048`  
**Contract repair:** `7521bfb8`  
**Closeout:** `ac52ab84`

| Finding | Executable correction |
|---|---|
| R4-1 | Closed `disclosure-policy-decision-v1` envelope; authorized metadata is copied verbatim; only missing-policy denial is synthesized |
| R4-2 | `validate_disclosure_binding` recomputes the digest and compares request id plus every copied §7.8 context field |
| R4-3 | `minimized` requires a transformation; disclosure time windows reject inversion |
| R4-4 | SoD records an external governance-decision id and requires distinct principal plus authority-binding ids when enabled |

Validation on `7521bfb8`: focused `tests/unit/v4` **102 passed**. Full approved pytest suite **476 passed**, with the same three Windows environment failures as the pristine base. Coverage **93.81%** (≥ 90%). Repository, traceability, ruff, format, mypy, smoke, pip-audit, and Bandit passed. Pip-audit reported no known vulnerabilities.

Wave 1 is `self_verified`, not `gate_ready`, not `human_accepted`, and not complete. Wave 0 remains closed. Wave 2 remains unstarted.

## Third independent re-verification (appended)

**Failed commit:** `e968bdfbe7602c2f1ba0dd3d010f3922e3c78c22`  
**Failing tests first:** `aaac0146`

| ID | Finding | Confirm / challenge | Correction |
|---|---|---|---|
| R3-1 | Outcome consistency only for `authorized`; missing policy could be `pending`; `denied` could become `minimized`; `policy_version` accepted whitespace/arbitrary text | **Confirmed.** `deny_without_policy` only blocked `outcome==authorized`. Version was any string. | Outcome must equal `policy_result`. Missing policy permits only `denied`. Nonempty version must be an opaque identifier |
| R3-2 | §7.8 bindings incomplete; decision not bound to the exact request | **Confirmed.** Decision lacked data-subject/vulnerability, procedural/correction state, source/collection, granularity/time window, transformations, expiry/revocation, reason, authority, audit identity, and request digest | All §7.8 fields required; `request_digest` is SHA-256 of the canonical request |
| R3-3 | `two_person_control` Boolean plus hardcoded high-risk transitions | **Confirmed.** `_check_transition` required the flag for publication/published, identity_hypothesis/confirmed_same, and disclosure_request/authorized | Flag removed. Distinct `first_approver_id` / `second_approver_id` required only when externally supplied `separation_of_duties_required` is true |
| R3-4 | `canonical_dumps` converted only `ValueError` | **Confirmed.** `object()` raised `TypeError` | `ValueError` and `TypeError` become `ContractError` |

### R3 validation

`tests/unit/v4`: 94 passed. Full suite: 468 passed, same 3 Windows environment failures. Coverage 94.19%. Smoke, ruff, mypy, pip-audit, bandit passed.

Wave 1 is again `self_verified`. Not `gate_ready`, not `human_accepted`, not complete. Wave 2 unstarted.

## Assurance-boundary freeze (appended)

**Implementation commit:** `ac52ab84dead1ef5aebd74e0291c01bca0b461d5`  
**Decision:** D-2026-08-15-019  
**Artifacts:** `docs/v4/STRATEGY.md`; `docs/v4/assurance/WAVE-01-ASSURANCE.md`; `docs/v4/assurance/WAVE-01-REQUIREMENTS-MAP.md`; Proposed ADR W1-010

The Wave 1 assurance contract is frozen to `GROK_BUILD_PROGRAM.md` §21 plus D-2026-08-15-013. Escalation under `STRATEGY.md` §6 is active after four review/repair cycles on the same contracts. r4 is already present on `ac52ab84`; no r5 implementation is authorized.

## Clean-room review (appended)

**Implementation:** `ac52ab84dead1ef5aebd74e0291c01bca0b461d5`  
**Record:** `docs/v4/evidence/WAVE-01-CLEANROOM-REVIEW.md`  
**Recommended disposition:** `gate_ready`  
**Decision:** D-2026-08-15-020

No traceable critical/high defect inside the frozen boundary. Residual items are medium/low or later-wave. r3/r4 extras are historical over-specification, not an r5 queue.

Wave 1 is `gate_ready`. Not `human_accepted`. Not complete. Wave 2 unstarted.

## Human non-acceptance (appended)

**Decision:** D-2026-08-15-021  
**Operator:** Wave 1 is **not** human-accepted.

The frozen §21 + D-013 assurance boundary and `STRATEGY.md` remain adopted. Disclosure and SoD are not reopened. Wave 2 remains unstarted. No r5. Wave 1 stays `gate_ready` only as a review disposition, not as acceptance.

## `gate_ready` withdrawn (appended)

**Decision:** D-2026-08-15-022  
**New legal state:** `revision_required`

| ID | Finding | Governing basis | Confirm |
|---|---|---|---|
| GR-1 | W1-N15 allegation≠guilt is not an executable v4 demonstration. The map marked it implemented. Clean-room M2 admitted no v4 test or contract. v3-negative-proof is insufficient. | W1-N15; CONST-005; assurance §2 required distinctions | **Confirmed.** Evidence packet “Proof” table cites only unchanged v3 extractors. |
| GR-2 | Recorded clean-room reviewer did not rerun the approved gates | Assurance §8 item 3; strategy §5 step 4, §7; disposition `review_invalid` | **Confirmed.** The review record states gates were not re-executed. |

**Decision:** D-2026-08-15-023  
The accepted critical/high set is complete. The prior `gate_ready` review is `review_invalid`. Authorized product work is one W1-N15 revision only, then a new review that reruns gates. Disclosure and SoD are not reopened. Wave 2 remains unstarted.

## W1-N15 revision self-verification (appended)

**Decision:** D-2026-08-15-024  
**Tests first:** `34930959`  
**Contract:** `740862d3`  
**Surface:** `schemas/v4/reported-claim-v1.schema.json`; `allegation_is_not_guilt`; `tests/unit/v4/test_revision_w1n15.py`; Proposed ADR W1-011

A reported claim cannot set `treat_allegation_as_guilt` or `finding: guilt`. No disclosure or SoD files were changed.

Builder gates: `tests/unit/v4` 107 passed. Full suite 481 passed, same 3 Windows baseline exceptions. Coverage 93.81%. Repository, traceability, ruff, mypy, smoke, pip-audit, bandit passed.

Wave 1 is `self_verified`. Not `gate_ready`. The prior clean-room review remains `review_invalid`. A new independent review that reruns gates is required. Wave 2 unstarted.

## W1-N15 independent review (appended)

**Record:** `docs/v4/evidence/WAVE-01-W1N15-REVIEW.md`  
**Decision:** D-2026-08-15-025  
**Gates:** rerun by the reviewer. Not `review_invalid`.  
**GR-1:** closed. **Critical/high:** none.

Wave 1 is `gate_ready` for later human acceptance. Not `human_accepted`. Wave 2 unstarted.

## Human acceptance (appended)

**Decision:** D-2026-08-15-026  
**Authority:** Forest Savage, human gate owner  
**Accepted implementation:** `740862d339d8e1ea29f42d30144d51cb076045b0`  
**Accepted gate-ready record:** `c30a1d3f4175d50b5461799194ea54b960d41624`  
**Valid review:** `docs/v4/evidence/WAVE-01-W1N15-REVIEW.md`  
**Prior review:** remains `review_invalid` (`docs/v4/evidence/WAVE-01-CLEANROOM-REVIEW.md`)  
**Boundary:** frozen Wave 1 assurance contract from `GROK_BUILD_PROGRAM.md` §21 and D-2026-08-15-013

Accepted residuals (non-blocking carry-forward): same-model independence limitation; three unchanged Windows baseline exceptions; recorded medium/low residual items.

Wave 1 is `human_accepted` and `closed`. This does not complete Phase 0 or Gate 0, establish an official version, authorize deployment or upstream adoption, resolve any blocked OD-* decision, or authorize Wave 2 implementation. Wave 2 remains `unstarted`.
