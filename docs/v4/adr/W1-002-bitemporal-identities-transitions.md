# W1-002: Bitemporal intervals, opaque identities, legal transitions

- **Status:** Proposed
- **Scope:** CaseLinker v4 research-network proposal only
- **Upstream:** not accepted
- **Unresolved authorities:** none for fixture contracts; production clocks/timezones remain operational (OD-008)

## Decision

Express event/valid time and knowledge/transaction time as distinct fields. Reject collapsed clocks, inverted intervals, and invented precision. Identifiers are opaque prefixes, never display labels. State changes are an allowlisted pair plus actor and reason.

## Consequences

These are schemas plus invariants, not a database kernel. SQLite v3 ledgers are unchanged.
