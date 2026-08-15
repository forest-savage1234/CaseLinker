# W1-011: Allegation is not guilt

- **Status:** Proposed
- **Scope:** CaseLinker v4 research-network proposal only
- **Upstream:** not accepted
- **Closes:** W1-N15 / CONST-005 executable gap (D-022, D-024)

## Decision

A reported claim is a versioned contract. `treat_allegation_as_guilt` is rejected. A `finding` of `guilt` is rejected. Procedural statuses (charge, indictment, acquittal, dismissal, and the rest of the recorded set) are not findings of guilt. This invents no legal rule about when a court finding exists.

## Consequences

Wave 1 still has no live extractor change. Disclosure and SoD contracts are unchanged.
