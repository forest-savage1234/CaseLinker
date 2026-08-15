# Target bounded contexts (provisional)

**Kind of document:** planning skeleton.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Statement labels:** `repository fact` | `inference` | `proposal` | `human decision required`

Nothing in this file selects a vendor, policy text, or production topology. Contexts are **proposals** unless marked otherwise. They are not an implementation backlog for Wave 0.

## 1. How to read this

- **repository fact:** v3 already implements a subset of these responsibilities under `src/caselinker/` (see `CURRENT_STATE.md`).
- **proposal:** the v4 program’s logical pipeline (`docs/v4/GROK_BUILD_PROGRAM.md` §6) is a target diagram to confirm or amend after evidence, not a license to scaffold empty services.
- **human decision required:** organization, tenancy, disclosure content, and operational hosting.

## 2. Proposed contexts and v3 mapping

| Proposed context | v3 evidence | Working class | Label |
|---|---|---|---|
| Source governance and acquisition | document identity + version metadata only (`documents/`); scrapers exist outside vNext | reuse document kernel; research first for collection policy | repository fact + proposal |
| Immutable source object store | `storage_key` naming convention only; **no byte store** (`DATA_AUTHORITY.md`) | research first / later OPS-002 | repository fact of absence; proposal |
| Document and version registry | `SourceDocument` / `SourceDocumentVersion` | reuse | repository fact |
| Candidate claim extraction | platform mentions + reported legal events | reuse for fixtures; research first to broaden | repository fact |
| Authenticated review ledger | append-only `ReviewDecision`; no authn | extend | repository fact + proposal |
| Identity / event hypothesis resolution | **absent** in `src/caselinker` | research first | repository fact of absence; proposal |
| Canonical temporal evidence kernel | assertion ledger + `valid_from`/`valid_to`/`created_at`; no as-known API | extend | repository fact + proposal |
| Evidence and dependency graph projections | CAC projector + SHACL; no dependency-edge type | reuse projection; extend dependencies | repository fact + proposal |
| Study registry and research snapshots | snapshot manifests + one `legal_event` cohort unit | reuse / extend | repository fact + proposal |
| Analysis, Claim Cards, Evidence Packs, Claim CI | implemented | reuse as projections | repository fact |
| Disclosure policy decision point | explicit non-implementation (ADR 0007; Evidence Pack exclusion) | research first; policy content is human | repository fact + human decision required |
| Audience-specific views / exports / publications | not implemented | proposal; blocked on OD-003 | human decision required |

Cross-cutting (all **proposal** or **human decision required**): IAM, purpose-based authorization, tenant isolation, tamper-evident audit, correction propagation, ontology/schema governance, AI execution governance, observability, key management, backup/retention.

Conceptual flows (event/transaction, disclosure, correction, tenancy, observability/audit, failure, slice-vs-risks) are in `GATE0_PROPOSAL.md`. They are not executable contracts.

## 3. Ownership sketch (proposal only)

- Domain invariants stay in typed ports, not in FastAPI, RDF, or UI. **repository fact** that this is already the v3 rule (`ENGINEERING_CHARTER.md` §6).
- Projections remain disposable. **repository fact** (ADR 0008; CONST-016).
- Policy **content** is not owned by software. **human decision required**.

## 4. Minimum vertical slice

**proposal / human decision required:** `docs/v4/GROK_BUILD_PROGRAM.md` §12 lists a twelve-step two-source/two-reviewer path.

**human decision required (already decided for Wave 0):** that path is a **synthetic experimental hypothesis**. It is not an authorized reviewer policy, production workflow, or corpus decision. Wave 0 does not adopt it. How it would test R-ID, R-COR, and R-DIS is described in `GATE0_PROPOSAL.md` §7.

## 5. Stop-independently rule

**proposal:** later contexts must be droppable without invalidating earlier evidence integrity (aligned with `docs/vnext/ADOPTION_PLAN.md` stages 1–7, which are v3 adoption stages, not v4 releases).
