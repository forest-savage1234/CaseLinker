# Current state (vNext / v3 proposal)

**Kind of document:** discovery.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Statement labels:** `repository fact` | `inference` | `proposal` | `human decision required`

This file describes what exists. It does not authorize a future architecture.

## 1. Product identity

- **repository fact:** `AGENTS.md` lines 3–5 and README lines 3–8 state this branch is a proposal, not an official CaseLinker release, and does not claim upstream `v3.0.0`.
- **repository fact:** workspace metadata version is `0.0.0` (`pyproject.toml` lines 1–4; ADR 0000).
- **repository fact:** recorded upstream product baseline is `9da0a4ff8b45df03fed073a9af5c00d22aab0d9d` (`docs/vnext/BASELINE.md` lines 5–7; `docs/vnext/traceability.v1.json` field `upstream_baseline`).
- **repository fact:** historical v3 implementation checkpoint is `802fb7d244e3751b42dbb20cc8d258e1b71adbc7` (`traceability.v1.json` field `implementation_checkpoint`; M07).
- **human decision required (decided for Wave 0):** the v4 proposal base is `4a17a9e5`, which includes four later CI/handoff commits after `802fb7d2`.

## 2. Two stacks in one repository

### 2.1 Additive vNext path (`src/caselinker/`)

**repository fact** (`docs/vnext/UPSTREAM_HANDOFF.md` lines 10–22; package tree):

```text
immutable SourceDocument / SourceDocumentVersion
  → evidence-bound extracted assertions
  → append-only ReviewDecision lineage
  → LegalEventResolver
  → live ResearchPublicationEligibilityPolicy
  → deterministic CAC N-Triples + pinned local SHACL
  → snapshot-scoped legal_event cohort / Claim Card / Evidence Pack
  → content-addressed Claim CI
  → repository-bound claim pipeline CLI
```

Ports and adapters:

- **repository fact:** `src/caselinker/documents/ports.py` defines `DocumentRepository`.
- **repository fact:** `src/caselinker/assertions/ports.py` defines `AssertionRepository`.
- **repository fact:** first adapters are SQLite (`documents/sqlite_repository.py`, `assertions/sqlite_repository.py`).
- **repository fact:** domain modules do not import FastAPI (charter §6; package layout).

### 2.2 Legacy application

**repository fact:** layered tree under `src/Ingestion Layer`, `src/Processing Layer`, `src/Storage Layer`, `src/Clustering & Analysis Layer`, `src/Visualization Layer`, plus `run/`, `caselinker_mcp/`, `scripts/scraper/`, `ontology/`.

**repository fact:** `src/Storage Layer/storage_postgres.py` lines 1–14 describe a mutable PostgreSQL case store.

**inference:** the two stacks are not a single source of truth. vNext ADRs 0002 and 0004 say they do not modify the legacy `cases` table.

## 3. Authoritative vNext records

**repository fact:** SQLite migrations:

- `migrations/sqlite/0001_source_documents.sql` — `source_documents`, `source_document_versions`; update/delete abort triggers (lines 62–79).
- `migrations/sqlite/0002_assertion_ledger.sql` — `assertions` including `valid_from`, `valid_to`, `created_at`, `supersedes_assertion_id`.
- `migrations/sqlite/0003_assertion_review_lineage.sql` — `assertion_review_inputs` with a trigger requiring the review to govern an input assertion (lines 17–27).

**repository fact:** `Assertion` (`assertions/models.py` lines 244–258) is immutable (frozen dataclass) with states `observed|extracted|resolved|derived|inferred|authored|contested|retracted` (lines 24–32).

**repository fact:** `ReviewDecision` (lines 317–325) is a separate append-only record. Outcomes: `accepted|rejected|needs_changes` (lines 73–76). Roles: `domain_reviewer|corpus_curator|policy_reviewer` (lines 79–82). There is no authentication implementation behind `reviewer_id`.

**repository fact:** `ResearchPublicationEligibilityPolicy` (`resolution/publication.py` lines 37–69) is a live read: resolved + current accepted reviews. Docstring: “not disclosure authorization or access control.”

## 4. Rebuildable projections

**repository fact:**

- Snapshot manifests: `src/caselinker/snapshots/manifest.py`; ADR 0001.
- Graph: `src/caselinker/graph/cac_legal_events.py`; profile `cac-legal-event-projection-v1`; SHACL `schemas/rdf/cac-legal-event-projection-v1.shacl.ttl`.
- Cohorts: unit is exactly `legal_event` (`analysis/cohorts.py` line 32).
- Claim Cards: generated text + mandatory `LIMITATIONS` (`analysis/claims.py` lines 12–21).
- Evidence Packs: digest index excluding `source_text`, `personal_display_labels`, `disclosure_authorization` (`analysis/evidence_pack.py` lines 38–42).
- Claim CI: content-addressed expectations; CLI never auto-approves (ADR 0010–0011).

## 5. Extraction and resolution limits

**repository fact:** legal-event extractor emits reported predicates only (`extraction/legal_events.py` lines 28–30) for six procedural types (arrest, charge, indictment, guilty plea, conviction, sentencing). Caller must supply `AttributedSubject` aliases. Negation, prediction, and pronoun resolution are out of scope (`docs/vnext/LEGAL_EVENT_METHOD.md`).

**repository fact:** platform extractor emits `caselinker:platformMentioned` only (ADR 0005). It does not infer use, harm, or prevalence.

**repository fact:** resolver requires one coherent current-review bundle (ADR 0007; `resolution/legal_events.py`). It does not merge identities or events across sources.

## 6. What is explicitly absent

**repository fact** (threat model “Required deployment controls”; search of `src/caselinker`):

- authenticated principals, MFA, organization membership
- disclosure policy decision/enforcement point
- tenant isolation
- vNext PostgreSQL ledger
- source mutation monitoring beyond content-addressed versions
- source-family / derivation / corroboration / contradiction types
- identity or same-event hypothesis types with reversible adjudication
- dependency-impact engine beyond live eligibility of one resolution
- collaborative review workspace
- federation packages
- production object store, outbox, backup/restore drills

## 7. Quality surface

**repository fact:** `AGENTS.md` lines 39–40 and `docs/vnext/UPSTREAM_HANDOFF.md` lines 89–102 define the locked quality commands. CI mirrors them in `.github/workflows/quality.yml`.

**repository fact:** smoke tests prove application construction with `CASELINKER_DISABLE_MCP=1`, not PostgreSQL, Redis, or model-provider correctness (`docs/vnext/BASELINE.md` “Honest limitations”).

## 8. Data-flow (current, not target)

```text
[policy-safe fixture or caller-supplied bytes]
        → SourceDocumentVersion (digest + metadata; bytes not in SQL)
        → deterministic extractor → extracted Assertion batch (atomic)
        → human ReviewDecision (unauthenticated id string)
        → LegalEventResolver → resolved Assertion bundle
        → live eligibility check
        → CAC N-Triples + SHACL
        → snapshot-bound cohort / Claim Card / Evidence Pack / Claim CI
```

**inference:** a case in the legacy UI is not this path. A vNext “case” does not exist as a mutable container; the charter and ADR 0006 treat events as independently sourced reports.

## 9. Known current limits that v4 must not paper over

These are **repository facts**, not design choices:

- eligibility ≠ disclosure (ADR 0007)
- SQLite ≠ PostgreSQL isolation (ADR 0004; threat model)
- snapshot integrity ≠ scientific validity (ADR 0001 consequences)
- Claim CI ≠ approval (ADR 0010)
- public source ≠ republication permission (threat model trust boundary 1)
- no official version without upstream (ADR 0000)
