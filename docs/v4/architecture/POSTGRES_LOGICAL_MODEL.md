# PostgreSQL logical constraint and transaction analysis

**Kind:** proposal / analysis.  
**Not:** an executable migration, a running service, a driver dependency, or a vendor selection.  
**Blocked:** OD-008.

## 1. Why mention PostgreSQL

`GROK_BUILD_PROGRAM.md` §6.1 and §21 ask for a logical model and transaction-boundary analysis. SQLite is the implemented v3 adapter (`migrations/sqlite/0001`–`0003`). This file does not replace it.

## 2. Proposed authoritative tables (logical names only)

- source_documents / source_document_versions (metadata; **not** source bytes)
- assertions, assertion_evidence, assertion_inputs, review_decisions, assertion_review_inputs
- source_families, source_lineage_edges
- identity_hypotheses, hypothesis_evidence
- dependency_edges, invalidation_events
- disclosure_requests, disclosure_decisions (policy **version id** only)
- organizations, principals, role_bindings (interface records)
- audit_events, ai_executions

Bytes, RDF, search, and Claim Cards stay off this ledger.

## 3. Transaction grains

| Grain | Commits together | Must not include |
|---|---|---|
| Version insert | document + version metadata | object bytes, graph triples |
| Assertion batch | assertions + evidence + inputs | reviews, projections |
| Review | one decision + linear successor check | eligibility cache |
| Hypothesis decision | hypothesis row + evidence rows | canonical person row (forbidden) |
| Correction | supersession + dependency stale marks + outbox rebuild id | projection rewrite in-place |
| Disclosure decision | request + decision + policy version id | policy rule text invention |

Isolation note (**analysis only**): review linearization and correction-vs-publish need serializable or equivalent predicate locks. SQLite tests do not prove that (`THREAT_MODEL.md`). Wave 2 may experiment; Wave 1 does not.

## 4. Constraint placement

| Invariant | Logical DB | Domain/schema | Policy engine | UI |
|---|---|---|---|---|
| Opaque ids, append-only | CHECK + abort triggers | yes | no | no |
| Event vs knowledge time | columns, not one timestamp | yes | no | display both |
| Illegal transitions | optional CHECK | yes (Wave 1) | no | no |
| Similarity ≠ identity | no person merge table | yes | no | no |
| Eligibility ≠ disclosure | no single accepted flag | yes | **content blocked OD-003** | no |
| Projection authority | projections not in ledger | yes | no | no |

## 5. Explicitly not authorized

`CREATE TABLE`, Alembic/Flyway, `psycopg` usage, Docker Postgres, cloud selection, live migrate.
