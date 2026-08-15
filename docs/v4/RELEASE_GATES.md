# Release gates and provisional staged plan

**Kind of document:** planning skeleton.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Identity:** proposal. Not a release train. Not CaseLinker v4.0.0.

Phase material below is **provisional**. Scope, vendors, thresholds, and policy content remain `proposal` or `human decision required`. A later wave may stop independently without invalidating earlier evidence-integrity value.

Wave state machine (repository fact of the program text): only the operator may set `human_approved` or `human_accepted`. This file does not set those states.

## Gate 0 / Wave 0 — Learn from v3 and resolve authority

| Item | Content |
|---|---|
| Scope | discovery artifacts; pristine and final checks; requirement registry |
| Non-goals | product code; policy content; official version; Wave 1 |
| Entry | operator Wave 0 approval (done) |
| Deliverables | `docs/v4/*` listed in EXECUTION_STATE |
| Migration / rollback | none; delete the v4 branch if rejected (does not change v3 or main) |
| Tests | repository quality suite; no new product tests |
| Exit (self) | artifacts internally consistent; unknowns owned; `self_verified` |
| Exit (human) | independent review then `human_accepted` — **not claimed here** |
| Review burden | architecture, privacy/governance, scientific-integrity reading |
| Human gate | no implementation before that later acceptance |

## Waves 1–10 (provisional only)

| Wave | Provisional proof | Entry | Non-goals | Human gate |
|---|---|---|---|---|
| 1 Contracts | versioned domain/policy-neutral contracts; fail-closed examples | Wave 0 `human_accepted` | infrastructure build-out | contract review |
| 2 Experiments | isolated tests of R-ID, R-COR, R-DIS; optional Postgres technical experiment | Wave 1 accepted | promoting spike code | proceed / revise / stop |
| 3 Temporal kernel | correction-safe bitemporal lineage on fixtures | Wave 2 accepted | live ingest, public UI, identity merge | semantic/db/privacy/rollback |
| 4 Multi-source | agreement/derivation/contradiction without manufactured identity | Wave 3 | biometrics, auto identity | scientific + child-safety + OD-006 |
| 5 Review + disclosure | authn review + default-deny enforcement of **supplied** policy | Wave 4 + OD-003/005 | inventing legal rules; deploy | privacy/legal + security |
| 6 Correction UX | workbench + visible staleness + accessibility checks | Wave 5 | flashy network viz | UX/safety/a11y |
| 7 Scientific workbench | one preregistered shadow study, invalidated by correction | Wave 6 + OD-009 | prevalence/causation claims | methods + disclosure |
| 8 Hardening | fail/recover/isolate without deploy | Wave 7 + OD-008 | certifications; production cutover | ops/security/db |
| 9 Federation | two synthetic orgs exchange/revoke/correct | Wave 8 + explicit federation approval | real orgs or data | crypto/privacy/ontology |
| 10 Handoff | honest adoptability packet | prior included waves accepted | merge, tag, `v4.0.0` | **upstream only** |

Each wave: disabled-by-default, reversible, fixture- or policy-safe only, evidence packet required.

## Synthetic experimental hypothesis (not adopted)

The twelve-step two-source/two-reviewer path in `docs/v4/GROK_BUILD_PROGRAM.md` §12 is recorded as a **synthetic experimental hypothesis**. It is not reviewer policy, not a production workflow, and not a corpus decision. Using it later requires a new human decision.

## Scorecard rule (program fact)

Dimensions are non-compensatory (`GROK_BUILD_PROGRAM.md` §35). Excellence in tests cannot offset a privacy, identity, scientific, or child-safety fail. Wave 0 does not score later dimensions as passed.

## What would be required before any official version

**human decision required / upstream only:** maintainer authorization. This program cannot supply it.
