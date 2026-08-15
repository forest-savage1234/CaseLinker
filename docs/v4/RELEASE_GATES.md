# Release gates and provisional staged plan

**Kind of document:** planning skeleton.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Identity:** proposal. Not a release train. Not CaseLinker v4.0.0.

Phase material below is **provisional**. Scope, vendors, thresholds, and policy content remain `proposal` or `human decision required`. A later wave may stop independently without invalidating earlier evidence-integrity value.

Wave state machine (repository fact of the program text): only the operator may set `human_approved` or `human_accepted`. This file does not set those states.

## Wave 0 artifact acceptance is not Phase 0 completion

| Item | Wave 0 (this program control plane) | Phase 0 (`GROK_BUILD_PROGRAM.md` §10) |
|---|---|---|
| Scope | discovery artifacts, requirement registry, risk/decision logs, non-mutating checks | maintainer feedback, controlled shadow mode, error taxonomy, reviewer disagreement, domain/privacy/scientific consultation, v4 vision and threat model |
| What “accept” would mean | independent reviewer + operator accept **these documents** as `human_accepted` for Wave 0 | approved baseline, approved pilot, measured v3 limitations, **named** decision owners, Gate 0 architecture disposition |
| Current state | Wave 0 may return to `self_verified` after revision; **not** `gate_ready`; **not** `human_accepted` | **incomplete**. OD-001, OD-002, OD-003, OD-009 remain blocked. No approved pilot. |
| Implementation | none | HUMAN GATE 0 still forbids product implementation until Phase 0 / Gate 0 is actually complete |

Independent acceptance of Wave 0 documents, if it later occurs, authorizes **only** Wave 1 contract design if the operator also explicitly accepts Wave 0. It does **not** complete Phase 0 and does **not** authorize product implementation, live data, or an official version.

---

## Gate 0 / Wave 0 — Learn from v3 (document discovery only)

| Field | Content |
|---|---|
| Scope | discovery artifacts; pristine and final checks; requirement registry |
| Non-goals | product code; policy content; official version; Wave 1; claiming Phase 0 complete |
| Dependencies | approved v4 base `4a17a9e5`; isolated branch |
| Entry criteria | operator Wave 0 approval (done) |
| Deliverables | `docs/v4/*` listed in EXECUTION_STATE |
| Migration | none |
| Rollback | abandon `proposal/v4-research-network`; does not change v3 or main |
| Tests | repository quality suite; no new product tests |
| Measurable exit (self) | artifacts internally consistent; every requirement in one bucket; findings appended; `self_verified` |
| Measurable exit (human) | named independent reviewer records pass; operator sets `human_accepted` — **not claimed** |
| Estimated review burden | one architecture/privacy/governance reading of `docs/v4/` |
| Human gate | no implementation before Gate 0 / Phase 0 completion |
| Can stop independently | yes; documents only |

---

## Provisional phases 1–8 (skeletons)

Each row is **proposal**. Blocked items inherit OD-* from `DECISION_LOG.md`.

### Phase 1 — Temporal evidence kernel (maps to Wave 3 after Wave 1–2)

| Field | Content |
|---|---|
| Scope | bitemporal claims/events, immutable transitions, correction/retraction/supersession, dependency identity, PostgreSQL **design** and compatibility adapter |
| Non-goals | live ingestion; public UI; identity merge; production deploy |
| Dependencies | Wave 0 `human_accepted`; Wave 1 contracts; Wave 2 experiments (R-COR at fixture scope) |
| Entry criteria | prior waves `human_accepted`; no unnamed policy required for fixture kernel |
| Deliverables | typed kernel, forward migrations, fixture proof of as-known/valid-time |
| Migration | expand/migrate/contract on fixtures only |
| Rollback | disable new writes; keep additive tables |
| Tests | concurrency, as-known queries, invalidation on a policy-safe fixture |
| Measurable exit | January/February scenario passes; dependents stale; history queryable |
| Estimated review burden | semantic + database + privacy + rollback review |
| Human gate | Gate 1 |
| Can stop independently | yes; fixture kernel without UI |

### Phase 2 — Multi-source resolution (Wave 4)

| Field | Content |
|---|---|
| Scope | source families, derivation, corroboration/contradiction, identity and event hypotheses, reversible adjudication |
| Non-goals | biometrics; automatic canonical identity |
| Dependencies | Phase 1; **OD-006** |
| Entry criteria | OD-006 decided; Wave 3 accepted |
| Deliverables | hypothesis types; false-merge evaluation on fixtures |
| Migration | additive relations |
| Rollback | stop hypothesis writes; retain records |
| Tests | false-merge-first; no transitivity; syndication ≠ corroboration |
| Measurable exit | no automatic identity; reversible states demonstrated |
| Estimated review burden | scientific + child-safety + ontology + reviewer-workflow |
| Human gate | Gate 2 |
| Can stop independently | yes, if kernel remains useful without multi-source |
| Blocked until | OD-006 |

### Phase 3 — Governance platform (Wave 5)

| Field | Content |
|---|---|
| Scope | authenticated orgs/principals, reviewer authority, adjudication, disclosure **framework**, audience projections |
| Non-goals | inventing legal rules; deploy |
| Dependencies | **OD-002, OD-003, OD-005, OD-007** |
| Entry criteria | named privacy/legal and review authorities; policy **content** supplied by them |
| Deliverables | default-deny PDP/PEP against supplied rules |
| Migration | additive authz tables |
| Rollback | disable new disclosure paths |
| Tests | SoD, field shaping, cross-tenant denial, revocation |
| Measurable exit | scientifically eligible claim can still be denied |
| Estimated review burden | domain-expert privacy/legal + independent security |
| Human gate | Gate 3 |
| Can stop independently | kernel can remain internal-only |
| Blocked until | OD-002, OD-003, OD-005 |

### Phase 4 — Correction operations and evidence-first UX (Wave 6)

| Field | Content |
|---|---|
| Scope | dependency impact, stale/rebuild, reviewer workbench, claim-to-evidence navigation |
| Non-goals | flashy network visualization; conversational assistants |
| Dependencies | Phases 1–3 for disclosure-aware UX; Phase 1 alone for internal impact reports |
| Entry criteria | prior accepted waves in the chosen slice |
| Deliverables | impact report; visible stale states; a11y checks |
| Migration | none beyond prior |
| Rollback | disable workbench |
| Tests | complete impact; WCAG 2.2 AA checks; comprehension study |
| Measurable exit | one correction marks all declared dependents stale |
| Estimated review burden | operational + UX + scientific + safety |
| Human gate | Gate 4 |
| Can stop independently | yes at impact-engine-only |

### Phase 5 — Scientific workbench (Wave 7)

| Field | Content |
|---|---|
| Scope | preregistered study specs, coverage/missingness/denominator audits, signed research-release manifest |
| Non-goals | prevalence, causation, individual-risk, platform-danger claims |
| Dependencies | **OD-009**; Phase 1 snapshots |
| Entry criteria | named methods reviewer; approved fixture/shadow protocol |
| Deliverables | one reproducible shadow study + correction rebuild |
| Migration | none |
| Rollback | disable study publication path |
| Tests | independent reproduction; stale-after-correction |
| Measurable exit | prior result stale; successor reauthorized |
| Estimated review burden | methodological + disclosure |
| Human gate | Gate 5 |
| Can stop independently | yes |
| Blocked until | OD-009 |

### Phase 6 — Production hardening (Wave 8)

| Field | Content |
|---|---|
| Scope | transactional infra, object store **if OD-008 accepts**, queues, IAM, backups, restore, fault tests |
| Non-goals | certifications; production cutover; this program deploying |
| Dependencies | **OD-008**; chosen vertical slice |
| Entry criteria | named operations owner; environment described |
| Deliverables | rehearsed restore; tenant tests if tenancy exists |
| Migration | forward-only with rehearsal |
| Rollback | documented recovery; no live data in this program |
| Tests | load, backpressure, restore, isolation |
| Measurable exit | restore rehearsal recorded; no unresolved high-severity in scope |
| Estimated review burden | security + privacy + database + operations |
| Human gate | Gate 6 (not a deploy authorization) |
| Can stop independently | yes; remain fixture/shadow |
| Blocked until | OD-008 |

### Phase 7 — Federation (Wave 9)

| Field | Content |
|---|---|
| Scope | signed packages, org identities, revoke/quarantine, local policy remains authoritative |
| Non-goals | real organizations or data |
| Dependencies | explicit federation approval (not yet an OD; create one if this phase is attempted) |
| Entry criteria | named federation governance |
| Deliverables | two synthetic orgs exchange/revoke/correct |
| Migration | none |
| Rollback | disable federation endpoints |
| Tests | poisoned package, revoked key, conflicting corrections |
| Measurable exit | signature ≠ truth or disclosure permission |
| Estimated review burden | crypto + interoperability + ontology + privacy + security |
| Human gate | Gate 7 |
| Can stop independently | yes |
| Blocked until | federation authority named |

### Phase 8 — Release-candidate evaluation (Wave 10)

| Field | Content |
|---|---|
| Scope | clean-room audit, selective adoption packet, honest non-claims |
| Non-goals | merge, tag, `v4.0.0`, deploy, publish |
| Dependencies | all included prior waves `human_accepted` |
| Entry criteria | operator requests audit only |
| Deliverables | scorecard, residual-risk owners, draft PR language saying “proposal, not release” |
| Migration | report only |
| Rollback | n/a |
| Tests | rerun required gates |
| Measurable exit | maintainer decision packet exists; no official version claimed |
| Estimated review burden | multi-role independent review |
| Human gate | Gate 8 — **upstream only** |
| Can stop independently | yes; reject or defer is success |

---

## Synthetic experimental hypothesis (not adopted)

The twelve-step two-source/two-reviewer path in `docs/v4/GROK_BUILD_PROGRAM.md` §12 is a **synthetic experimental hypothesis**. It is not reviewer policy, not a production workflow, and not a corpus decision.

## Scorecard rule (program fact)

Dimensions are non-compensatory (`GROK_BUILD_PROGRAM.md` §35). Wave 0 does not score later dimensions as passed.

## What would be required before any official version

**human decision required / upstream only:** maintainer authorization. This program cannot supply it.
