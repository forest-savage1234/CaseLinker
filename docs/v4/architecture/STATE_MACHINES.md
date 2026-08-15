# State machines

**Kind of document:** inventory of current machines + provisional target names.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`

Legal transitions, guards, and two-person control for unimplemented machines are **proposal** or **human decision required**. Wave 0 does not adopt transition tables as executable contracts (that is Wave 1).

## 1. Implemented today (repository fact)

### 1.1 Assertion epistemic state

`AssertionState` (`src/caselinker/assertions/models.py` lines 24–32):  
`observed | extracted | resolved | derived | inferred | authored | contested | retracted`.

Guards (same file, lines 289–307): source states require evidence; lineage states require input assertion IDs; retraction must identify and include its target.

There is no stored “active/qualified/superseded” machine beyond `supersedes_assertion_id` and live eligibility.

### 1.2 Review outcome

`ReviewOutcome` (lines 73–76): `accepted | rejected | needs_changes`.  
Linear chain: one root, at most one successor, strictly advancing time (ADR 0004).

`ReviewerRole` (lines 79–82) is a label, not an authorization check.

### 1.3 Research eligibility (live, not persisted)

`EligibilityReason` (`resolution/publication.py` lines 12–18). Eligible iff resolved, complete current accepted review lineage.

Superseding a review does not delete the resolution; it makes it presently ineligible (ADR 0007).

### 1.4 Document versions

Insert-only. Update/delete aborted by triggers (`0001_source_documents.sql` lines 62–79). No `observed → acquired → verified → changed` machine.

### 1.5 Extraction / resolution process identity

`ExtractionRun` and `ResolutionRun` are immutable process identities, not user-visible workflows.

## 2. Program-named machines not implemented (proposal)

From `docs/v4/GROK_BUILD_PROGRAM.md` §6.4. Names only; no Wave 0 schema:

1. Source version: `observed → acquired → verified → changed | removed | superseded | authenticity_uncertain`
2. Candidate claim: `proposed → queued → under_review → accepted | rejected | corrected | escalated | contested`
3. Accepted claim: `active → qualified | superseded | retracted | disputed | ineligible`
4. Identity hypothesis: `candidate → needs_review → possibly_same | confirmed_same | confirmed_different | unresolved → reopened`
5. Review task: `open → assigned → submitted → second_review | adjudication → closed | reopened`
6. Research artifact: `building → verified → eligible → stale | invalid | superseded`
7. Disclosure request: `requested → evaluating → authorized | minimized | denied | expired | revoked`
8. Publication: `draft → authorized → published → corrected | withdrawn | superseded`
9. Federation package: `received → verified → quarantined | accepted → revoked | superseded`

**human decision required:** who may fire high-risk transitions; whether two-person control is required (OD-005, OD-003).

## 3. Safety notes (not implementations)

- **repository fact:** v3 already separates review, resolution, eligibility, disclosure (unimplemented), and access control (unimplemented) (ADR 0007 table).
- **proposal:** identity hypotheses must not have a transition that writes a canonical person from similarity.
- **proposal:** disclosure must default deny; missing policy ⇒ no publication (CONST-018).
- **inference:** mapping program machine (2) onto v3 `extracted` + `ReviewDecision` is possible later; doing it in Wave 0 would be premature concretization.
