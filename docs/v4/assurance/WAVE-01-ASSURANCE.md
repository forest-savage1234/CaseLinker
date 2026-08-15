# Wave 1 assurance contract

**Status:** frozen 2026-08-15.  
**Wave:** 1 — formal contracts before infrastructure.  
**Implementation commit under review:** `ac52ab84dead1ef5aebd74e0291c01bca0b461d5`  
**Legal state:** `revision_required`. `gate_ready` withdrawn (D-022). Not `human_accepted`.  
**Wave 2:** unstarted.

This file is the frozen Wave 1 acceptance boundary. Later useful ideas that cannot be traced here are later-wave or `program_clarification_required`. They are not automatically Wave 1 defects.

Governing sources: `GROK_BUILD_PROGRAM.md` §21; operator decision D-2026-08-15-013; `docs/v4/STRATEGY.md`.

## 1. Objective

Show that the temporal evidence network can be expressed as coherent, versioned, policy-neutral contracts **before** selecting full infrastructure.

Primary proof obligation (unchanged): *temporal evidence network expressed as versioned policy-neutral contracts before infrastructure*.

## 2. Normative requirements (in scope)

Wave 1 must produce executable contracts, not a running service, for:

| ID | Requirement | Source |
|---|---|---|
| W1-N1 | Bitemporal semantics and interval precision | §21 |
| W1-N2 | Immutable claim, event, review, correction, and dependency identities | §21 |
| W1-N3 | Legal state transitions and transition guards | §21 |
| W1-N4 | Organization / principal / reviewer **authority interfaces** (not an IdP) | §21 |
| W1-N5 | Disclosure **request and decision interfaces** that do not invent policy content | §21 |
| W1-N6 | Source lineage, source-family, and derivation contracts | §21 |
| W1-N7 | Identity and event hypothesis contracts with positive and negative evidence | §21 |
| W1-N8 | Deterministic artifact and projection contracts | §21 |
| W1-N9 | Canonical serialization, versioning, and compatibility rules | §21 |
| W1-N10 | Audit-event and AI-execution provenance contracts | §21 |
| W1-N11 | Proposed ADRs, schemas, invariants, transition tables, policy-safe examples | §21; D-013 |
| W1-N12 | PostgreSQL **logical** model and transaction-boundary analysis; no live migration | §21; D-013 |
| W1-N13 | State which constraints belong in database, domain/schema, policy engine, and UI | §21 |
| W1-N14 | Invalid examples and fail-closed behavior for every contract | §21 |
| W1-N15 | Demonstrate five distinctions (below) | §21 |
| W1-N16 | Tests committed before the contract surface that makes them pass | D-013 |
| W1-N17 | Schemas under `schemas/v4/` are the executable surface | D-013 |
| W1-N18 | Proposed ADRs live in `docs/v4/adr/`, not `docs/adr/` | D-013 |

### Required distinctions

1. Allegation is not guilt.
2. Event time is not knowledge time.
3. Similarity is not identity.
4. Research eligibility is not disclosure permission.
5. A projection is not a source of truth.

### Disclosure interface floor (W1-N5)

Enough to be internally consistent and policy-neutral:

- a request can be represented;
- a decision can be represented;
- missing or invalid policy cannot authorize;
- eligibility cannot be treated as disclosure;
- the decision records the request it answers;
- policy **content**, transformation rules, and lawful bases are not invented by software.

Deeper PDP/PEP behavior, field shaping, and three live views belong to later waves (especially Wave 2 item 3 and Wave 5 / Gate 3). OD-003 remains blocked.

### Transition / SoD floor (W1-N3, W1-N4)

Enough to reject illegal pairs and to record actor, reason, and audit identity. Which transitions require two-person control is **not** a Wave 1 software decision (OD-003, OD-005). An externally supplied SoD flag may be recorded; the contract must not hardcode a policy list of high-risk transitions.

## 3. Principal risks assigned to this wave

| Risk | Wave 1 duty | Not this wave |
|---|---|---|
| Premature infrastructure lock-in | Contracts and logical Postgres only | Live DB, object store, vendor (OD-008) |
| Collapsing event/knowledge time | Executable bitemporal contract | Production clock operations |
| Similarity becoming identity | Hypothesis contracts reject canonical merge and transitivity | Operational identity resolution (Wave 4; OD-006) |
| Eligibility becoming disclosure | Decision contract rejects that confusion; default-deny when policy is missing | Enforced PDP on every serializer (Wave 2/5; OD-003) |
| Hidden transitions | Allowlisted machines; required actor/reason/audit fields | Authenticated reviewers (OD-005) |
| AI self-approval / publish | Provenance contract; reject self-review and published disposition | Model execution |
| Official-version claim | Proposal identity only | Any tag/release |

R-ID, R-COR, and R-DIS remain the program’s top product-safety risks. Wave 1 **names and contracts** them. It does not close them.

## 4. Non-goals

- Live migration, object store, IdP, passwords, MFA
- Policy rule text, jurisdictions as law, lawful-basis invention
- Deciding which transitions require two-person control
- Wave 2 experiments or disposable worktrees
- Service scaffolding, HTTP APIs, UI
- Official version, deploy, publication, upstream adoption
- Completing Phase 0 / Gate 0
- Closing CONST-* / DISCLOSE-* / AI-* as §18.4 `closed`

## 5. Deferred and blocked decisions

| ID | Question | Effect on Wave 1 |
|---|---|---|
| OD-003 | Privacy/disclosure authority and policy content | Policy **content** blocked; interfaces only |
| OD-005 | Reviewer qualifications and IdP | Authority is a declared binding, not authentication |
| OD-006 | Identity-resolution scope | Hypotheses stay reversible; no canonical person |
| OD-008 | Infrastructure | Postgres remains logical markdown |
| OD-001 | Upstream disposition | Proposal identity only |

## 6. Required evidence

- Versioned schemas in `schemas/v4/`
- Fail-closed validator `caselinker.v4_contracts`
- Proposed ADRs W1-001…W1-005 (slice decisions) plus later repair ADRs as history
- Logical Postgres analysis
- Policy-safe fixtures and negative tests
- `WAVE-01-EVIDENCE.md` with appended, not erased, review history
- This frozen contract plus `WAVE-01-REQUIREMENTS-MAP.md`
- Approved quality gates, with the three documented Windows baseline exceptions

## 7. Acceptance tests (falsifiable)

A Wave 1 review may treat these as the executable exit tests. Additional tests exist as regression history; they do not silently enlarge the boundary.

| Distinction / rule | Primary tests |
|---|---|
| Envelope fail-closed | `test_contract_kernel.py` |
| Event time ≠ knowledge time; inverted interval; invented precision | `test_bitemporal_identity.py`, `test_revision_temporal.py` |
| Opaque identities; illegal transition | `test_bitemporal_identity.py`, `test_revision_identities_machines.py` |
| Derivation ≠ corroboration; similarity ≠ identity; no transitivity | `test_lineage_hypotheses.py`, `test_revision_hypotheses.py` |
| Eligibility ≠ disclosure; missing policy does not authorize | `test_disclosure_authority.py`, `test_revision_disclosure.py` |
| Projection ≠ source of truth; AI cannot publish | `test_projection_provenance.py`, `test_revision_audit_ai.py` |
| Canonical JSON / compatibility | `test_revision_serialization.py` |

Repair-round tests (`test_revision_r2.py`, `test_revision_r3.py`) are historical evidence that specific defects were closed. They are not a license to keep growing the same contracts.

## 8. Review standard

The independent verifier:

1. Reads this contract and §21 **before** prior evidence conclusions.
2. Reviews `ac52ab84` (implementation, including r4) plus any later **documentation-only** freeze commits.
3. Reruns approved gates independently.
4. May block only on findings traceable to §2, §3, §7, or a defect introduced by the implementation.
5. Records untraceable improvements as later work.
6. Records unstable or missing requirements as `program_clarification_required`.
7. Does not implement, mark `human_accepted`, or start Wave 2.

Independence limitation: builders of r3/r4 must not be the independent verifier. A same-model conversation is not perfect organizational independence.

## 9. Stopping rule

Wave 1 may become `gate_ready` when:

- this boundary remains frozen (or an explicit, accepted amendment exists);
- every W1-N* row is implemented, explicitly deferred, or blocked on a named OD-*;
- no traceable critical/high defect remains inside this boundary;
- approved gates pass, subject to the three Windows baseline exceptions;
- remaining medium/low items have owners;
- the implementation is still a contract layer, not a service or policy engine;
- a valid independent review has been recorded;
- the human gate owner has enough evidence to accept or reject.

Further refinement of disclosure or SoD records does not, by itself, prevent `gate_ready`.

## 10. Escalation already triggered

As of 2026-08-15, Wave 1 had four consecutive review/repair cycles (r1–r4, closeout `ac52ab84`) that repeatedly restructured disclosure and transition contracts. `STRATEGY.md` §6 is therefore active.

**Next implementation is not authorized** until a clean-room review of `ac52ab84` against this frozen boundary reports, and the human gate owner disposes:

- `revision_required` — then one coherent revision of only the accepted critical/high items;
- `program_clarification_required` — then a boundary amendment, explicitly accepted;
- `gate_ready` — then human acceptance is still required before Wave 2;
- `review_invalid` — then another independent review.

r4 is already on `ac52ab84`. It is historical implementation, not an expansion of this frozen boundary. No r5 queue is authorized.
