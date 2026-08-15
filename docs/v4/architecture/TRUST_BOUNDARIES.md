# Trust boundaries

**Kind of document:** discovery + provisional target notes.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`

## 1. v3 trust boundaries (repository fact)

Copied in substance from `docs/vnext/THREAT_MODEL.md` lines 22–39:

1. External source → immutable document. Public availability is not truth or disclosure permission.
2. Document → extracted candidate. Deterministic rules are fallible.
3. Candidate → human review. Reviewer identity, competence, and currentness are outside the extractor.
4. Reviewed candidates → resolution. Only coherent current bundles become canonical internal relations.
5. Resolution → graph. Mapping may be broader than the exact procedural term.
6. Graph → claim. Validation, snapshot, unit, and membership must be pinned.
7. Research artifact → audience. Eligibility is never sufficient disclosure authorization.
8. Repository and CI. Paths, dependencies, runners, and expectations are supply-chain inputs.

## 2. Residual risks already named (repository fact)

From the same threat-model table and “Required deployment controls”:

- source authenticity and retention policy require governance
- reviewer authentication and authorization are not implemented
- database concurrency beyond SQLite needs deployment analysis
- de-identification, audience policy, and legal/privacy review remain mandatory
- Claim CI expectation approval is a human process
- hostile runner or repository write access is a broader control

## 3. Additional boundaries the v4 program would introduce (proposal)

These are **not** implemented and are **not** policy:

| Boundary | Why it is not yet a fact | Depends on |
|---|---|---|
| Collection policy → acquisition worker | scrapers exist; no vNext allowlist/retention engine | OD-004 |
| Authenticated principal → review write | `reviewer_id` is an opaque string | OD-005 |
| Hypothesis generator → canonical identity | no hypothesis type exists; generator must not write identity | OD-006 |
| Eligibility result → disclosure PDP | separate on purpose today | OD-003 |
| Serializer / export / log / cache / admin | no second enforcement point | OD-003, OD-007 |
| Organization A package → organization B | federation is a late proposal | OD-002, OD-007 |
| Model prompt → source text | no governed AI execution record in `src/caselinker` | later AI wave |

## 4. Highest-risk boundary failures (human-ranked)

Operator binding decision 6. These are the failures Wave 0 treats as product-safety critical:

1. Silent false merge of people or events (identity/same-event boundary collapse).
2. Correction that leaves a still-eligible dependent (dependency boundary incomplete).
3. Internal field leaving through an alternate path (disclosure boundary bypass).

PostgreSQL isolation is a later technical experiment, not one of these three.

## 5. What Wave 0 will not infer

**human decision required:** live privacy policy, lawful basis, reviewer qualifications, production topology, and data classifications are not inferred from source code (`docs/v4/GROK_BUILD_PROGRAM.md` §4.1.7).
