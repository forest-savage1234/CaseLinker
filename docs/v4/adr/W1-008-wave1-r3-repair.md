# W1-008: Wave 1 third verification repair

- **Status:** Proposed
- **Scope:** CaseLinker v4 research-network proposal only
- **Upstream:** not accepted
- **Unresolved authorities:** OD-003 owns policy **content** and which transitions require separation of duties; software only records an externally supplied SoD requirement

## Decision

1. Disclosure `outcome` must equal `policy_result` for every result. Missing policy permits only `denied`. A denied policy result cannot become `minimized`.
2. A nonempty `policy_version` must be a valid opaque identifier. Whitespace and arbitrary text are invalid.
3. Decisions bind every §7.8 field: data-subject/vulnerability context, procedural and correction state, source restrictions and collection policy, granularity/time window, transformations, expiry/revocation, decision reason, authority, and audit identity. The decision is bound to the request by `request_digest`.
4. `two_person_control` is not a governance rule. Transitions record `first_approver_id` and, when an externally supplied `separation_of_duties_required` is true, a distinct `second_approver_id`. The contract does not decide which transitions require two-person control.
5. `canonical_dumps` converts `ValueError` and `TypeError` into `ContractError`.

## Consequences

Still contracts only. No live policy content, IdP, or Wave 2 experiments.
