# CaseLinker v4 Strategy — Risk-Bounded, Evidence-Led Delivery

**Status:** operator-adopted process (2026-08-15).  
**Does not replace:** `GROK_BUILD_PROGRAM.md` (still governing).  
**Does not decide:** Wave 1 `gate_ready`, human acceptance, Wave 2, official version.

This file freezes the delivery method. Wave-specific assurance contracts live under `docs/v4/assurance/`.

## 1. Strategic objective

CaseLinker v4 will be developed through bounded, independently reviewable waves that reduce the highest-consequence risks before expanding implementation.

The program does not seek theoretical completeness at each wave. It seeks sufficient, demonstrated assurance for the specific decisions and risks assigned to that wave.

The governing question is not:

> Can another improvement be imagined?

It is:

> Has this wave satisfied its frozen acceptance boundary, with its remaining risk explicitly understood and accepted?

## 2. Standard of confidence

The program does not claim to use the uniquely or universally “best” development method.

It aims to use the most defensible and proportionate method presently supported by:

- the known consequences of error;
- the maturity of the product;
- available evidence;
- unresolved human-policy decisions;
- implementation cost;
- the need to preserve future design flexibility.

The process itself remains open to revision when evidence shows excessive rework, correlated review, unstable requirements, or disproportionate ceremony.

## 3. Governing principles

### 3.1 Risk before breadth

Work addresses irreversible or high-consequence risks before feature breadth, optimization, vendor selection, or production scaling.

### 3.2 Frozen wave boundaries

Before implementation begins, every wave must define:

- its objective;
- normative requirements;
- principal risks;
- non-goals;
- deferred decisions;
- required evidence;
- acceptance tests;
- review standard;
- stopping rule.

These form the wave’s assurance contract.

The boundary may be clarified during execution, but it may not be silently expanded by implementation or review.

### 3.3 Traceable findings

A finding may block a wave only when it is traceable to at least one of:

- a governing program requirement;
- an accepted architecture invariant;
- an identified material risk assigned to the wave;
- a stated wave exit criterion;
- a defect introduced by the implementation.

A useful improvement that cannot be traced to the frozen boundary is recorded for later consideration. It is not automatically converted into a current-wave requirement.

### 3.4 Tests as evidence, not proof

Tests, coverage, static analysis, and security scans provide evidence. Their counts do not independently establish correctness or completeness.

Assurance must also consider:

- semantic consistency;
- negative and adversarial behavior;
- requirements coverage;
- assumptions and omissions;
- operational feasibility;
- unresolved human authority;
- whether the design is becoming prematurely rigid.

### 3.5 Minimal implementation with coherent design

Each wave implements the smallest coherent surface capable of testing its assigned risks.

“Smallest repair” does not justify indefinite local patching. When successive repairs alter the meaning or structure of the same contract, the program pauses for a coherent design review before adding another patch.

### 3.6 Conservative state claims

States such as `self_verified`, `gate_ready`, `human_accepted`, and `closed` remain distinct.

Passing automated checks does not imply independent acceptance. Wave acceptance does not imply phase completion, production readiness, or official-version status.

## 4. Separation of roles

### Builder

The builder:

- implements the wave;
- writes tests;
- records assumptions;
- runs self-verification;
- classifies the result as no more than `self_verified`.

### Independent verifier

The independent verifier:

- must not have implemented the reviewed change;
- evaluates the frozen wave boundary and reviewed commit;
- reruns the required gates independently;
- challenges both under-implementation and over-specification;
- distinguishes defects from later-wave improvements;
- does not silently redefine the program.

A separate conversation using the same model may reduce context contamination, but it is not treated as perfect organizational independence. That limitation must remain visible.

### Human gate owner

The human gate owner:

- confirms that the wave accomplished its intended purpose;
- evaluates residual risk and proportionality;
- accepts, rejects, or requests clarification;
- does not substitute personal approval for legal, privacy, security, records, or other specialist authority where such authority is required.

### Domain decision authority

When a decision requires specialized authority, the named authority decides it. If no qualified authority is named, the dependent decision remains blocked rather than being inferred by the builder, verifier, or general gate owner.

## 5. Wave execution process

### Step 1 — Freeze the assurance contract

Before implementation, record the wave boundary, risks, requirements, non-goals, evidence, and stopping rule.

### Step 2 — Build a falsifiable slice

Implement the smallest coherent surface that can succeed or fail against the assurance contract. Use tests-first sequencing where the behavior can be meaningfully specified in advance.

### Step 3 — Self-verification

Run the approved gates, inspect semantic behavior, record limitations, and append evidence. The maximum resulting state is `self_verified`.

### Step 4 — Clean-room independent review

The verifier performs a two-stage review:

1. Evaluate the program boundary and commit without first adopting earlier reviewers’ conclusions.
2. Examine prior evidence and finding history for completeness, recurrence, or unresolved risk.

The verifier reports:

- traceable critical/high findings;
- medium/low residual items;
- untraceable improvements proposed for later work;
- program ambiguities requiring human clarification;
- signs of premature or excessive specification.

### Step 5 — Disposition

The permitted outcomes are:

- `revision_required` — a traceable critical/high defect exists;
- `program_clarification_required` — the alleged defect depends on an unresolved or unstable requirement;
- `gate_ready` — no critical/high defect remains within the frozen boundary;
- `review_invalid` — reviewer independence, evidence, or execution was insufficient.

### Step 6 — Human decision

The human gate owner reviews the evidence, residual risk, deferrals, and authority dependencies before accepting or rejecting the wave.

No later wave begins until the required acceptance is explicit.

## 6. Rework and escalation rule

A wave must pause for a boundary and architecture review when either condition occurs:

- two consecutive independent reviews introduce materially new critical/high requirements; or
- successive repairs repeatedly restructure the same contract or invariant.

At that point, the next action is not automatically another repair.

The program must determine whether:

- the implementation is defective;
- the assurance contract is incomplete;
- the governing program is ambiguous;
- the reviewer is expanding scope;
- the design needs coherent restructuring;
- the requirement belongs to a later wave.

Any boundary change is documented explicitly and accepted before implementation resumes.

## 7. Stopping rule

A wave may become `gate_ready` when:

- its assurance boundary is frozen;
- every in-scope normative requirement is implemented, explicitly deferred, or blocked by a named decision;
- no traceable critical/high defect remains;
- the approved verification gates pass, subject to documented baseline exceptions;
- remaining medium/low risks have owners and dispositions;
- the implementation remains proportionate to the maturity of the system;
- the independent review is valid;
- the evidence is sufficient for an informed human decision.

The possibility of additional refinement does not by itself prevent `gate_ready`.

## 8. Evidence standard

Wave evidence should prioritize:

- exact reviewed commits;
- requirements-to-evidence mapping;
- reproducible pass/fail results;
- adversarial and negative behavior;
- decisions and unresolved assumptions;
- finding disposition;
- baseline exceptions;
- reviewer identity and independence limitations;
- residual-risk ownership.

Commit counts, test counts, coverage percentages, and document volume are supporting indicators—not primary proof of readiness.

## 9. Proportionality safeguards

The program will periodically evaluate whether its governance is improving the product or merely increasing ceremony.

Track:

- number of review/repair cycles per wave;
- newly discovered critical/high findings by review round;
- requirement churn after implementation begins;
- time spent building versus documenting;
- repeated defects in the same contract family;
- untraceable reviewer findings;
- unresolved decision-authority dependencies;
- defects escaping into later waves.

Rising rework or requirement churn triggers process correction rather than automatic expansion of documentation.

## 10. Immediate application to Wave 1

Wave 1 at `ac52ab84dead1ef5aebd74e0291c01bca0b461d5` remains `self_verified`. It is neither `gate_ready` nor human-accepted.

Before another implementation revision:

1. Freeze and publish the Wave 1 assurance boundary.
2. Map every Wave 1 exit requirement to implementation, test evidence, deferral, or blocking decision.
3. Commission a fresh holistic review that did not implement the reviewed commit.
4. Require every blocking finding to identify its governing basis.
5. Classify ambiguity as `program_clarification_required`, not automatically as a code defect.
6. Consolidate any valid critical/high findings into one coherent revision.
7. If the clean-room review finds no critical/high defect within the frozen boundary, advance Wave 1 to `gate_ready`.
8. Require explicit human acceptance before Wave 2 begins.

## 11. Strategic posture

CaseLinker v4 will favor disciplined learning over claims of certainty, explicit residual risk over implied completeness, and coherent architecture over indefinite finding-by-finding patching.

The objective is not to make criticism impossible.

The objective is to make every consequential decision traceable, reviewable, proportionate, and reversible until sufficient evidence justifies moving forward.
