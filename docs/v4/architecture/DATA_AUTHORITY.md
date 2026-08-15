# Data authority

**Kind of document:** discovery + provisional notes.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`

## 1. Current authority (repository fact)

| Data | Authoritative store today | Rebuildable? | Citation |
|---|---|---|---|
| Source document identity and version **metadata** | SQLite `source_documents` / `source_document_versions` | no (this is the metadata record) | `migrations/sqlite/0001_source_documents.sql` |
| Exact source **bytes** | **None implemented.** Only `content_sha256`, `byte_length`, and a derived `storage_key` string are stored. ADR 0002 forbids storing source text in these tables. `SourceDocumentVersion.capture` hashes caller-supplied bytes in memory and discards them (`documents/models.py` 180–204). There is no object-store port, put/get adapter, or restore path. | **No.** A digest cannot reconstruct bytes. Tests and fixtures retain bytes outside the ledger. | ADR 0002 lines 41–45; `0001` `storage_key` check (naming convention only) |
| Assertions, evidence, inputs, supersession | SQLite `assertions` and related tables | no | `0002_assertion_ledger.sql`; ADR 0004 |
| Review decisions and review-input edges | SQLite `review_decisions`, `assertion_review_inputs` | no | `0002`, `0003`; ADR 0003–0004, 0007 |
| Research eligibility | **not stored**; computed live | yes | `resolution/publication.py`; ADR 0007 |
| Snapshot membership and component digests | snapshot manifest JSON | yes, from pinned **repository files** named by the spec, not from a byte store | ADR 0001 |
| CAC graph bytes | generated N-Triples | yes, from eligible assertions + projector | ADR 0008 |
| Claim Card / Evidence Pack / Claim CI | generated canonical JSON | yes | ADR 0009–0011 |
| Legacy `cases` rows | legacy SQLite/Postgres application tables | n/a to vNext | ADR 0002: no automatic backfill |

**repository fact:** dual-write between the legacy case store and the vNext ledger is not implemented. Treating them as equivalent would create a competing source of truth (program CONST-016).

**repository fact:** a `storage_key` value such as `sha256/<prefix>/<digest>` is a **content-addressed name**, not proof that an object exists at that name. No vNext code writes or reads that path.

## 2. Time

**repository fact:** `Assertion.valid_from` / `valid_to` are optional `date` fields (`assertions/models.py` lines 251–252). `created_at` is timezone-aware UTC (line 258, validated at 313).

**inference:** `valid_*` is the closest existing event/valid-time slot; `created_at` is the closest knowledge-time slot. Neither is a documented bitemporal query API.

**proposal:** a later temporal kernel would distinguish event/valid time from knowledge/transaction time without collapsing them. That is not implemented and is not a Wave 0 schema.

## 3. Proposed future authority (proposal only)

Subject to ADR and environment review, **not** a Wave 0 product decision:

- transactional system of record for governed records: likely PostgreSQL (`GROK_BUILD_PROGRAM.md` §6.1) — **proposal**
- immutable object store that actually persists and restores exact source bytes addressed by `storage_key` — **proposal**; **not present today**
- search, RDF, analytics, cache, vectors: disposable projections — **proposal**, consistent with CONST-016
- SQLite retained for fixtures/tests — **proposal**, consistent with ADR 0004

**human decision required:** actual hosting, encryption, backup ownership, RPO/RTO (OD-008). **Status:** blocked until a named infrastructure authority exists.

## 4. Dual-write rule

**proposal:** a future transaction must commit authoritative state and any outbox record atomically. Workers must be idempotent. This is not designed in Wave 0 beyond naming the risk.

**repository fact:** v3 already uses atomic assertion-batch writes and exact-retry idempotency (ADR 0004).

## 5. Disclosure and export

**repository fact:** no audience-shaped serializer exists in `src/caselinker`. Evidence Packs explicitly exclude disclosure authorization (`evidence_pack.py` lines 38–42).

**human decision required:** what may be shown to whom (OD-003). Software may later enforce a supplied policy; it may not invent one. **Status:** blocked until a named privacy/legal authority exists.
