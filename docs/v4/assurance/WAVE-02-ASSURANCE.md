# Wave 2 assurance contract

**Status:** `proposed`. Not frozen. Not approved.  
**Wave:** 2 — risk-killing experiments.  
**Prerequisite:** Wave 1 `human_accepted` and `closed` (D-026). Accepted implementation `740862d339d8e1ea29f42d30144d51cb076045b0`. Accepted gate-ready record `c30a1d3f4175d50b5461799194ea54b960d41624`.  
**Wave 2 legal state:** `unstarted`.  
**This packet:** proposed for human review. It does not execute experiments.

This file is the **proposed** Wave 2 acceptance boundary. It becomes the frozen boundary only if the human gate owner explicitly approves it. Until then, later useful ideas are comments on a proposal, not exit requirements.

Governing sources: `GROK_BUILD_PROGRAM.md` §22; `docs/v4/STRATEGY.md`; Wave 1 closed evidence; D-2026-08-15-006 (risk ranking).

Historical Wave 1 r1–r4 disclosure and SoD refinements are **not** automatic Wave 2 requirements.

## 1. Objective

Obtain evidence about the hardest architectural assumptions **before** committing the target architecture to them.

Primary proof obligation (unchanged from §22): *obtain evidence about the hardest assumptions before committing the architecture to them*.

Experiment success, failure, or “revise architecture” does **not** select a production architecture, vendor, schema, hosting platform, disclosure policy, or official version.

## 2. Normative requirements (in scope)

Wave 2 must run the minimum isolated experiments that can succeed or fail against the five §22 assumptions. It must not implement the Wave 3 temporal kernel.

| ID | Requirement | Source |
|---|---|---|
| W2-N1 | Isolated, disposable worktrees or experiment namespaces only | §22 |
| W2-N2 | Test two layers on a disposable PostgreSQL instrument: (1) **storage enforcement** — reject a structurally collapsed representation, an invalid event interval, an explicitly declared invented-precision condition, non-UTC knowledge time, and in-place mutation of prior knowledge history; (2) **query-interface correctness** — declared `as_known` and `valid_during` interfaces address the two stored dimensions independently and return independently enumerated expected results. The experiment may test only information represented in its schema. It does **not** claim that PostgreSQL inferred whether a source invented precision, or that PostgreSQL rejects every arbitrary `SELECT` issued by a principal with unrestricted table access. Storage collapse is structural (one field or alias for both dimensions, an omitted dimension, or `time_model=collapsed`). Equal timestamps in distinct event/valid-time and knowledge/transaction-time fields remain valid. No fixed event/knowledge ordering. | §22 item 1; R-CON; W1 `reject_collapsed_clock` |
| W2-N3 | Test whether dependency invalidation can (1) find all transitives in the **registered** set, (2) prevent or detect silent unregistered dependencies against a declared fixture universe, and (3) fail closed when coverage cannot be established — without treating a graph projection as authoritative | §22 item 2; R-COR |
| W2-N4 | Test whether purpose/audience/field-level disclosure can default-deny and produce distinct internal, research, and public projections without leaking internal fields through experiment output paths P1–P8 (serializers, logs, exports, caches, search, errors, admin stubs). P9 is a separately reported observational probe of existing v3 Evidence Pack / Claim Card entry points and is outside the P1–P8 mechanism pass bar. | §22 item 3; R-DIS |
| W2-N5 | Test whether source-family modeling can distinguish independent corroboration of the **same** underlying event or claim from duplicated or syndicated reporting on frozen policy-safe examples. Unrelated-event pairs are labeled `unrelated`, not independent corroboration. | §22 item 4; RESOLVE-001/002 |
| W2-N6 | Test whether a mistaken identity-hypothesis decision can be reopened without destroying evidence or creating a canonical identity. Subject IDs remain distinct throughout. No canonical identity, merge, or split operation exists. A≈B and B≈C do not yield A=C. | §22 item 5; R-ID |
| W2-N7 | Declare falsification criteria, valid-run gates, exhaustive mutually exclusive proceed/revise/stop mappings, and negative cases **before** execution. An invalid or incomplete run is not an architecture recommendation. | §22; STRATEGY §5 |
| W2-N8 | Use synthetic or approved policy-safe fixtures only | §22; D-007 |
| W2-N9 | Measure results; do not promote spike code into production modules | §22 |
| W2-N10 | Record what must change in the target architecture | §22 |
| W2-N11 | Produce `WAVE-02-EVIDENCE.md` plus one experiment report per assumption | §22 |
| W2-N12 | Recommend proceed, revise architecture, or stop for each experiment using one shared precedence: if evidence is invalid, repeat the run; otherwise stop, then revise architecture, then proceed. Every valid non-proceed outcome maps to exactly one revise or stop branch. | §22 |
| W2-N13 | Do not begin the temporal kernel implementation | §22; Wave 3 |
| W2-N14 | Delete or quarantine disposable artifacts only after preserving evidence and with human-approved cleanup | §22 |
| W2-N15 | Experiment outcome does not select production architecture, vendor, policy content, or official version | STRATEGY §3.6; OD-003/006/008 |

### Experiment identifiers

| ID | Family | Ranked risk |
|---|---|---|
| W2-E1 | PostgreSQL transaction invariants | R-CON (not top three) |
| W2-E2 | Transitive dependency invalidation | R-COR (rank 2) |
| W2-E3 | Default-deny disclosure and leakage | R-DIS (rank 3) |
| W2-E4 | Source-family corroboration vs syndication | scientific / RESOLVE |
| W2-E5 | Reversible identity hypotheses | R-ID (rank 1) |

Detailed procedures live in `docs/v4/experiments/WAVE-02-PLAN.md`.

Default execution is **sequential**: W2-E5 → W2-E2 → W2-E3 → W2-E4 → W2-E1. The experiments are logically independent; sequence is not a result dependency. Parallel execution requires an explicit human amendment (builders or namespaces, capacity, evidence isolation, reviewer availability, contamination controls).

## 3. Principal risks assigned to this wave

| Risk | Wave 2 duty | Not this wave |
|---|---|---|
| R-ID silent false merge | Falsify blind transitivity and irreversible hypothesis decisions on fixtures. Do not create or split a canonical identity. | Operational identity resolution and canonical split (Wave 4; OD-006) |
| R-COR incomplete invalidation | Falsify closure errors, silent non-registration, incomplete-state claims, and projection-authoritative impact | Wave 3 temporal kernel; unknowable external dependents |
| R-DIS alternate-path leakage | Falsify default-deny and three synthetic views on experiment output paths | Real policy content (OD-003); Wave 5 PDP |
| R-CON lost concurrent review | Falsify append-only / bitemporal / review conflicts on disposable Postgres | Production vendor, schema, hosting (OD-008) |
| Syndicated “corroboration” | Falsify family-vs-independent classification without a single score | Live corpus (OD-004) |
| Premature architecture lock-in | Keep spikes disposable; record implications only | Selecting the SoR or PDP |

R-ID, R-COR, and R-DIS remain the program’s top product-safety risks. Wave 2 **tests assumptions about them**. It does not close them.

## 4. Non-goals

- Wave 3 temporal kernel, live rebuild queue, or production correction notices
- Production PostgreSQL selection, migrations, object store, cloud, or RPO/RTO
- Real lawful bases, jurisdictions, audience policy, minimization rules, or disclosure governance
- Authenticated reviewers, IdP, or which transitions require two-person control
- Canonical person or event identities
- Service scaffolding, HTTP APIs, UI, or deployment
- Promoting spike modules into `src/caselinker` production paths
- Completing Phase 0 / Gate 0
- Official version, merge, tag, release, or upstream adoption
- Closing CONST-* / DISCLOSE-* / CORRECT-* / RESOLVE-* / OPS-* as §18.4 `closed`
- Treating Wave 1 r3/r4 disclosure or SoD extras as silent Wave 2 exit criteria

## 5. Deferred and blocked decisions

| ID | Question | Effect on Wave 2 |
|---|---|---|
| OD-003 | Privacy/disclosure authority and policy content | Policy **content** blocked. W2-E3 may use **synthetic** decision fixtures only. |
| OD-005 | Reviewer qualifications and IdP | Out of scope. Experiments use unauthenticated fixture actors. |
| OD-006 | Identity-resolution scope | Operational resolution blocked. W2-E5 tests reversibility only; no canonical identity. |
| OD-008 | Infrastructure | Production claim blocked. W2-E1 may use a **disposable** Postgres instrument only. |
| OD-004 | Source classes / live corpus | Live sources blocked. W2-E4 uses frozen synthetic examples. |
| OD-001 | Upstream disposition | Proposal identity only. |

Synthetic fixtures do **not** resolve these decisions. If an experiment cannot proceed without inventing a blocked decision, the disposition is `program_clarification_required` or `blocked`, not a software default.

## 6. Required evidence

- This proposed contract, once human-approved and frozen
- `WAVE-02-REQUIREMENTS-MAP.md`
- `docs/v4/experiments/WAVE-02-PLAN.md` with pre-declared falsification
- Per-experiment report: hypothesis, fixtures, measurements, valid-run determination, proceed/revise/stop, architecture implications
- `docs/v4/evidence/WAVE-02-EVIDENCE.md` (created only during execution)
- Isolation record (worktree or namespace identity) and cleanup approval
- Approved repository gates, subject to the three documented Windows baseline exceptions
- Explicit statement that no spike was promoted

## 7. Review protocol

The independent verifier:

1. Reads this contract (once approved) and §22 **before** prior evidence conclusions.
2. Reviews the approved planning commit plus the experiment-execution commits.
3. Reruns the approved repository gates **and** the recorded experiment procedures.
4. Must not have built the experiment being reviewed.
5. May block only on findings traceable to §2, §3, a pre-declared falsification, or a defect introduced by the experiment.
6. Records untraceable improvements as later work.
7. Records unstable or missing requirements as `program_clarification_required`.
8. Does not implement repairs, mark `human_accepted`, start Wave 3, or select vendors/policy.

Independence limitation: a separate conversation using the same model is not organizational independence. That limitation must remain visible. A review that does not rerun gates and experiment procedures is `review_invalid`.

## 8. State definitions for Wave 2

| State | Meaning for this wave |
|---|---|
| `unstarted` | No experiment executed. Planning may exist as a proposal. **Current legal state.** |
| `proposed` | Planning packet exists; human has not approved execution. Not claimed here as `legal_state`. |
| `human_approved` | Human gate owner approved this boundary and authorized execution. Not claimed. |
| `self_verified` | Builder executed the in-scope experiments or recorded a named block/deferral; evidence appended; each experiment has proceed/revise/stop; spikes not promoted; Wave 3 not started. Maximum builder state. |
| `gate_ready` | A valid independent review reran gates and experiment procedures and found no in-boundary critical/high defect. Not human acceptance. |
| `human_accepted` / `closed` | Human accepts residual risk and recorded architecture implications. Does **not** select production architecture or complete Phase 0. |

Passing an experiment is not `gate_ready`. `gate_ready` is not human acceptance. Human acceptance is not an official version.

## 9. Stopping and escalation rules

Wave 2 may become `gate_ready` when:

- this boundary is frozen by explicit human approval, or an explicit accepted amendment exists;
- every W2-N* row is executed, explicitly deferred, or blocked on a named OD-*;
- each executed experiment has a valid-run determination and a pre-declared proceed / revise / stop recommendation; an invalid run is repeated and is not an architecture recommendation;
- no traceable critical/high defect remains inside this boundary;
- approved gates pass, subject to the three Windows baseline exceptions;
- remaining medium/low items have owners;
- spikes remain disposable;
- a valid independent review has been recorded;
- the human gate owner has enough evidence to accept, reject, or require architecture revision.

Further refinement of disclosure or SoD **contracts** does not, by itself, prevent `gate_ready`. Wave 1 already closed that contract layer.

`STRATEGY.md` §6 is already active from Wave 1. Wave 2 must pause for boundary review when:

- two consecutive independent reviews introduce materially new critical/high requirements; or
- successive experiment patches repeatedly restructure the same assumption or contract family.

At that point the next action is not automatically another spike.

## 10. Carry-forward from Wave 1 (not automatic scope)

Accepted Wave 1 residuals remain non-blocking carry-forward unless a later human decision traces them into this boundary:

| Residual | Wave 2 treatment |
|---|---|
| Same-model independence limitation | Standing process risk; keep visible |
| Three Windows baseline exceptions | Unchanged; do not “fix” by weakening tests |
| Clean-room M1 SoD governance ids | **out of scope**; OD-005 / Wave 5 |
| W1-N15 extractor wiring | **out of scope**; later wave |
| Leftover `identity-hypothesis-v1` | **out of scope**; Wave 4 / OD-006 |
| r3/r4 disclosure field extras | **not** Wave 2 exit requirements unless a human amendment says so |
| Three live views on **real** product serializers | W2-E3 tests the **mechanism** on P1–P8. That P1–P8 result is governed by the shared valid-run / stop / revise / proceed algorithm. P9 is a separately reported observational probe of the existing `ClaimCardBuilder.build` / `ClaimCard.to_dict` and `EvidencePackAssembler.assemble` entry points: it cannot improve or invalidate the P1–P8 mechanism result, but a confirmed leak still requires a predeclared `revise architecture` or `stop` disposition with a named carry-forward. `Not evaluable` is an incomplete observational result, not a mechanism pass or failure. No P9 outcome authorizes unplanned product repair. |

## 11. What human approval of this packet would authorize

If later accepted, this packet would authorize **Wave 2 experiment execution only**, inside the frozen boundary, on synthetic fixtures, in disposable namespaces.

It would **not** authorize Wave 3, deployment, vendor selection, policy content, Phase 0 completion, or an official version.
