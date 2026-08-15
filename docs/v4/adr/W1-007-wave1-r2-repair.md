# W1-007: Wave 1 second verification repair

- **Status:** Proposed
- **Scope:** CaseLinker v4 research-network proposal only
- **Upstream:** not accepted
- **Unresolved authorities:** OD-003 still owns policy **content**; software only records an externally supplied `policy_result`

## Decision

1. `decide_disclosure` authorizes only when a nonempty policy version **and** an explicit `policy_result="authorized"` are supplied. A version string alone denies.
2. Decisions require purpose and copy request context (principal, organization, audience, fields, channel, jurisdiction).
3. State transitions require machine, idempotency key, audit id, guard, two-person flag, and side effects. Missing machine is an error, not `legacy_assertion`.
4. AI executions record retrieved artifacts, structured output, validation, cost, timing, and resulting ids. Tool calls are closed objects and cannot embed source passages.
5. `reopened` requires a legal prior state. Positive evidence must `supports`; negative must `contradicts`.
6. Canonical JSON rejects NaN/Infinity. Timestamp parse failures are `ContractError`.
