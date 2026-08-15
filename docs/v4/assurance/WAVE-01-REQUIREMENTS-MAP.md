# Wave 1 requirements-to-evidence map

**Frozen against:** `WAVE-01-ASSURANCE.md`  
**Implementation commit:** `ac52ab84dead1ef5aebd74e0291c01bca0b461d5`  
**No requirement is §18.4 `closed`.** Wave 1 can only make contracts executable and internally consistent.

Disposition vocabulary:

| Disposition | Meaning |
|---|---|
| `implemented` | Executable schema/invariant + at least one positive and one negative test |
| `deferred` | In-scope as a contract name only; deeper behavior is a later wave |
| `blocked` | Cannot be completed without a named OD-* decision |
| `out_of_scope` | Not a Wave 1 exit requirement |

## Exit requirements

| ID | Requirement | Disposition | Implementation | Evidence | Residual / owner |
|---|---|---|---|---|---|
| W1-N1 | Bitemporal semantics and precision | implemented | `bitemporal-interval-v1`, `as-known-query-v1`; calendar/UTC checks in `validate.py` | `test_bitemporal_identity.py`, `test_revision_temporal.py` | Production clocks remain OD-008 |
| W1-N2 | Immutable identities | implemented | `stable-identity-v1`, `correction-identity-v1`, `dependency-edge-v1` | `test_bitemporal_identity.py`, `test_revision_identities_machines.py` | No live identity store |
| W1-N3 | Legal transitions and guards | implemented | `state-transition-v1`; nine §6.4 machines in `validate.py` | `test_bitemporal_identity.py`, `test_revision_identities_machines.py` | Which transitions need SoD is **blocked** OD-003/005 |
| W1-N4 | Authority interfaces | implemented | `authority-binding-v1`; opaque `prin_` / `org_` | `test_disclosure_authority.py` | Not an IdP; **blocked** OD-005 |
| W1-N5 | Disclosure request/decision interfaces | implemented (interface floor) | `disclosure-request-v1`, `disclosure-decision-v1`, `decide_disclosure`. r4 also added `disclosure-policy-decision-v1` and `validate_disclosure_binding` | `test_disclosure_authority.py`, `test_revision_disclosure.py`, r2–r4 regressions | Policy **content** **blocked** OD-003. The r4 extras are implementation history, not a silent expansion of the frozen floor. Full PDP / three views **deferred** to Wave 2/5 |
| W1-N6 | Source lineage / derivation | implemented | `source-lineage-v1` | `test_lineage_hypotheses.py` | Live source-family corpus is later |
| W1-N7 | Person/event hypotheses | implemented | `person-hypothesis-v1`, `event-hypothesis-v1`; polarity and reopen invariants | `test_lineage_hypotheses.py`, `test_revision_hypotheses.py` | Canonical identity **blocked** OD-006 |
| W1-N8 | Projection / artifact contracts | implemented | `projection-artifact-v1` | `test_projection_provenance.py` | Projection is not SoR |
| W1-N9 | Serialization / compatibility | implemented | `canonical_dumps`; `compatibility-v1` | `test_revision_serialization.py`, r2/r3 dumps tests | — |
| W1-N10 | Audit and AI provenance | implemented | `audit-event-v1`, `ai-execution-v1` | `test_revision_audit_ai.py`, `test_projection_provenance.py` | No model path; R-AI remains blocked for model use |
| W1-N11 | ADRs, schemas, examples | implemented | `docs/v4/adr/W1-001`…`W1-008`; `schemas/v4/`; fixtures in tests | this map; slice docs | Repair ADRs are history, not new scope |
| W1-N12 | Postgres logical model | implemented (markdown) | `architecture/POSTGRES_LOGICAL_MODEL.md` | document review; no migration tests (non-goal) | **blocked** OD-008 for any live claim |
| W1-N13 | Constraint placement | implemented (analysis) | same file, §4 | document review | — |
| W1-N14 | Invalid examples / fail-closed | implemented | unknown fields rejected; `ContractError` | every `tests/unit/v4/test_*.py` negative case | — |
| W1-N15 | Five distinctions | implemented | see assurance §7 | see assurance §7; Wave 1 evidence “Proof” table | Allegation≠guilt relies on unchanged v3 extractors |
| W1-N16 | Tests before implementation | implemented (process) | git history: failing slice/repair tests precede fixes | `5eaa3d0d`…`aaac0146` | — |
| W1-N17 | Schemas as executable surface | implemented | `schemas/v4/*.schema.json` + `validate_instance` | kernel tests | — |
| W1-N18 | Proposed ADRs under `docs/v4/adr/` | implemented | W1-001…W1-008 | files exist; `docs/adr/` untouched | — |

## Related program IDs (partial only)

These IDs gained Wave 1 contract structure. None are `closed`.

| ID | Wave 1 effect | Still open |
|---|---|---|
| CONST-004 / TEMP-* | Interval and as-known contracts | Kernel implementation is Wave 3 |
| CONST-006 / 007 / RESOLVE-001…005 | Hypothesis and lineage contracts | OD-006; Wave 4 |
| CONST-008 / AI-001 / AI-002 | Execution provenance schema | No model; R-AI blocked |
| CONST-009 / 018 / DISCLOSE-001…004 | Request/decision interface; eligibility≠disclosure | OD-003; Wave 2/5 PDP |
| CONST-012 / CORRECT-* | Correction and dependency **identity** contracts | Impact engine is Wave 3/6 |
| CONST-016 / 017 | Projection not SoR; transition records | Authenticated audit is later |
| CONST-015 / GOV-* | Proposal identity preserved | OD-001 |
| OPS-001 | Logical Postgres analysis | OD-008 |
| REVIEW-001 | Authority interface only | OD-005 |

## Explicit later-wave items (not Wave 1 blockers)

| Item | Why not Wave 1 | Belongs |
|---|---|---|
| External policy-decision object copied field-for-field into `decide_disclosure` | §21 asks for interfaces without inventing policy, not a PDP implementation | Wave 2 item 3 / Wave 5 |
| Recompute-and-compare digest as a standalone binding API | Useful; not named in §21. Shape + recorded digest already binds the fixture path | later contract hardening or Wave 2 |
| Minimized ⇒ at least one transformation bit | Semantic tightening of a field Wave 1 added during r3; not in original §21 floor | `program_clarification_required` or later |
| Inverted disclosure `time_window` | Same family as bitemporal inversion **if** the field is kept; otherwise later | clarify whether time_window is in the W1-N5 floor |
| SoD authority-binding ids + governance-decision id | Would encode review-governance structure; OD-005/003 blocked | Wave 5 |
| Three live disclosure views on real serializers | Named as Wave 2 experiment 3 | Wave 2 |
| Fixture correction-impact engine | Wave 3 primary proof | Wave 3 |

## Baseline exceptions

Three Windows-host pytest failures exist on the pristine v3 base and are not Wave 1 regressions: path-separator rendering, symlink privilege (WinError 1314), N-Triples fail-order. Independent review should rerun on Ubuntu/CI where possible (`R-WIN`).

## Review-cycle metric (strategy §9)

| Round | Failed commit | Newly added critical/high theme |
|---|---|---|
| r1 | `b73cccc6` | missing families, calendar time, split hypotheses, request binding, AI/audit |
| r2 | `3f57afe1` | authorize only with `policy_result`; required machine/audit; AI completeness; polarity; NaN/UTC |
| r3 | `e968bdfb` | outcome consistency; opaque policy id; full §7.8 field list; replace SoD boolean |
| r4 | `f41568e2` → `ac52ab84` | external policy object; digest recompute; transformation/time_window semantics; SoD governance ids |

Four rounds restructured the same disclosure/transition contracts. Escalation rule is active. This map freezes the original §21 + D-013 boundary. r4 is present on `ac52ab84` as implementation history, not as a silent expansion of the Wave 1 exit contract.
