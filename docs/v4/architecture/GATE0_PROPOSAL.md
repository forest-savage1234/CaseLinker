# Gate 0 architecture proposal (conceptual)

**Kind of document:** planning skeleton. Not an executable contract. Not a schema.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Statement labels:** `repository fact` | `inference` | `proposal` | `human decision required`

This file completes the Gate 0 architecture proposal required by `GROK_BUILD_PROGRAM.md` §5.C. It does **not** choose vendors, finalize tables, invent disclosure/reviewer policy, or set numeric thresholds. Unresolved policy stays **blocked** on the owners and gates in `DECISION_LOG.md`.

Companion facts: `CURRENT_STATE.md`, `DATA_AUTHORITY.md`, `STATE_MACHINES.md`, `TRUST_BOUNDARIES.md`, `TARGET_CONTEXTS.md`.

---

## 1. Event flow and transaction boundaries

**repository fact:** v3 already persists document metadata, assertion batches, and review decisions in one SQLite connection with abort-on-update triggers (`migrations/sqlite/0001`–`0003`; ADR 0004). Eligibility is computed live, not stored (`resolution/publication.py`).

**inference:** the natural transaction grain today is “one atomic ledger write” (document version insert, assertion batch, or one review decision). Projections are separate, rebuildable reads.

**proposal:** keep that grain. A future production SoR (Postgres is a program suggestion only; **blocked** on OD-008) would commit, in one transaction:

1. the authoritative row change (source version metadata, assertion, review, hypothesis decision, correction, or disclosure **decision record** — not policy text invented here);
2. an outbox record naming a deterministic follow-on job (project, invalidate, rebuild), if any.

Workers would be idempotent on a stable operation id. Search, RDF, caches, and Claim Cards would **not** be written in the same transaction as the ledger (`CONST-016`).

**proposal — logical event flow (not a product):**

```text
policy-gated acquire (blocked: OD-004)
  → hash bytes in memory; persist metadata only until an object store exists (fact: no byte store)
  → extract candidates (deterministic adapters exist)
  → enqueue review (blocked: OD-005 for real principals)
  → append ReviewDecision
  → optional hypothesis accept/reject (blocked: OD-006)
  → resolve coherent bundle (resolver exists)
  → live eligibility read
  → rebuildable graph / cohort / Claim Card / pack
  → disclosure decision (blocked: OD-003) before any external serialize
  → on correction: append, invalidate dependents, enqueue rebuild
```

**human decision required:** whether any asynchronous queue is in scope before Wave 8 (OD-008). Wave 0 does not add one.

---

## 2. Access and disclosure decision flow

**repository fact:** research eligibility is a live, evidence-state gate and is explicitly **not** disclosure (`ADR 0007`; `publication.py` 37–38). Evidence Packs exclude `disclosure_authorization` (`evidence_pack.py` 38–42).

**proposal:** two sequential questions, never collapsed:

```text
1) Eligibility (software, current evidence/review/snapshot)?
      no  → no research artifact; fail closed (CONST-018)
      yes → still not visible externally
2) Disclosure (PDP using **supplied** policy version)?
      missing policy / expired / revoked → deny (CONST-009, CONST-018)
      deny / minimize → shaped or empty view + reason + audit id
      authorize → serialize only allowed fields to that audience/purpose/channel
      then enforce again at export/log/cache/admin (DISCLOSE-004)
```

**human decision required / blocked:** policy **content**, jurisdictions, audiences, and lawful basis (OD-003). Reviewer authentication (OD-005). Tenancy of the principal (OD-002, OD-007).

**proposal:** software may later implement a versioned PDP/PEP. It may not invent rules. Three views remain a **hypothesis** to test, not an adopted audience policy: internal review, approved research, aggregate-only public.

---

## 3. Correction and dependency-invalidation flow

**repository fact:** superseding a review does not delete a resolution; it makes that resolution presently ineligible (ADR 0007). There is no general `DependencyEdge` or rebuild queue (`CURRENT_STATE.md` §6).

**proposal:**

```text
append Correction / Retraction / Supersession
  → identify dependents from an authoritative dependency registry
     (not from the graph store)
  → mark dependents stale or ineligible (atomic with the append if practical)
  → block new disclosure/publication of stale artifacts
  → enqueue deterministic rebuild + re-review / re-authorization
  → preserve historical artifacts and their prior authorization state
  → emit a versioned impact report
```

**inference:** live eligibility is a necessary but incomplete instance of this flow (CORRECT-002).

**human decision required:** none to design a **fixture** impact engine (R-COR allows fixture-scope work after later waves). Production correction notices and disclosure of those notices remain blocked on OD-003.

---

## 4. Tenancy and organizational boundaries

**repository fact:** vNext has no organization, tenant, or membership type. `reviewer_id` is an opaque string.

**proposal:** treat an Organization as a policy and audit boundary, not as a shared fact store. Authoritative records would carry an organization (or “fixture/single-tenant”) scope. Isolation would be tested at database, job, cache, search, graph, export, log, and backup channels (`OPS-004`) **if** multi-tenancy is chosen.

**human decision required / blocked:** whether there is more than one organization, who the sponsor is, and what isolation is required (OD-002, OD-007). Until then the conceptual default is **single logical tenant / fixture namespace**. That default is **not** a tenancy policy.

**proposal:** federation (FED-001) is a late, optional boundary. A valid foreign signature would prove integrity and issuer only. Local disclosure policy would still apply (blocked on OD-003). Wave 0 does not design key ceremony.

---

## 5. Observability and audit boundaries

**repository fact:** v3 logs and CI do not define product SLIs. Charter says logs should use stable ids, not source text (`ENGINEERING_CHARTER.md` §5).

**proposal (OPS-006):** instrument only after journeys exist. Candidate **privacy-safe** signals (no source passages, no display names):

- source acquire failures and freshness (when collection exists)
- review backlog age
- stale-dependent count
- policy deny counts (not denied content)
- rebuild/projection-drift failures
- snapshot verify failures
- restore-rehearsal success/fail

Alerts would need an owner, severity, and runbook. **No SLO numbers are set here.**

**proposal (audit):** every canonical transition records actor, authority, reason, time, prior/new state, governing inputs, and audit id (`CONST-017`). Audit stores must not copy source spans or unnecessary personal data (`OPS-007`).

**human decision required / blocked:** operational ownership and hosting (OD-008); what personal data an audit may retain (OD-003).

---

## 6. Failure containment and recovery

**repository fact:** v3 fail-closed constructors and CLI exit codes exist; there is no vNext backup/restore drill; exact source bytes are **not** in the ledger (`DATA_AUTHORITY.md`).

**proposal:**

| Failure | Containment | Recovery |
|---|---|---|
| Missing evidence, review, policy, or snapshot | produce no publication (CONST-018) | supply the missing governed input |
| Partial assertion batch | roll back the transaction (exists in v3) | retry identical batch |
| Projection / SHACL fail | do not enter analysis | rebuild from ledger |
| Stale review or policy | eligibility or PDP deny | new review / new policy version |
| Worker poison message | quarantine; do not retry blindly | human inspect fixture; replay by id |
| Lost object bytes | **cannot restore today** (fact) | prevent live ingest until OPS-002 exists (OD-008, OD-004) |
| Dual-write drift | projections are disposable | rebuild; never “fix” the graph in place |

**human decision required / blocked:** RPO/RTO, backup ownership, production DR (OD-008). This program does not authorize deployment (PROHIB-012).

---

## 7. Synthetic vertical slice vs the three riskiest assumptions

**human decision required (already decided):** the §12 twelve-step path is a **synthetic experimental hypothesis** (D-2026-08-15-007). It is not reviewer policy, a production workflow, or a corpus decision.

**proposal:** if later authorized on **policy-safe fixtures only**, the slice would exercise the three human-ranked product-safety risks as follows. It would **not** close them.

| Step (program §12) | R-ID silent false merge | R-COR incomplete invalidation | R-DIS disclosure bypass |
|---|---|---|---|
| 1–2 two families, extract | supplies two sources; must **not** auto-merge people | — | fixture text never exported as source |
| 3 two independent reviews | humans accept candidates; no model self-accept | review lineage becomes a dependency | reviewers see internal view only (if OD-003 later supplies rules) |
| 4 same-event hypothesis, reopen | **primary R-ID test:** `possibly_same` ≠ canonical identity; reopen after new evidence; no A≈B≈C | hypothesis decision is a dependent | hypothesis not disclosed by default |
| 5 resolve with contradiction + derivation | contradiction must survive; derivation ≠ corroboration | resolved bundle registered as parent | — |
| 6–8 projection, snapshot, Claim Card, pack | — | dependents registered at creation | pack still excludes disclosure authorization |
| 9 two disclosure decisions | — | — | **primary R-DIS test:** internal vs public-aggregate; default deny if policy missing |
| 10–11 source correction, stale dependents, blocked publish, rebuild | reopened identity must stay reversible | **primary R-COR test:** complete impact; no eligible stale pack | stale artifacts cannot pass PDP |
| 12 clean-room reproduce | — | successor digest differs; history queryable | reproduction must not leak internal fields |

**inference:** steps 3, 4, and 9 require OD-005, OD-006, and OD-003 respectively before they are more than paper. Until those authorities exist, the slice may be specified and later implemented only as **unauthenticated fixture actors** and **explicit deny-without-policy**, not as real review or disclosure.

**proposal:** that limitation is acceptable for killing architectural assumptions; it is not a substitute for named policy.

---

## 8. What this proposal deliberately is not

- not a PostgreSQL schema or vendor bill of materials
- not approved disclosure, identity-scope, or tenancy policy
- not Phase 0 completion or Gate 0 `human_accepted`
- not permission to implement Wave 1+
