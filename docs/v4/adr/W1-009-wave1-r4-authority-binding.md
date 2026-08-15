# W1-009: Bind disclosure and separation-of-duties authority

- **Status:** Proposed
- **Scope:** CaseLinker v4 research-network proposal only
- **Upstream:** not accepted
- **Blocked policy content:** OD-003 and OD-005 remain unresolved

## Outcome

Wave 1 can express an externally governed disclosure result and prove which
request it governs without treating locally manufactured strings as policy or
human authority.

## Invariants and threats

1. Non-denied disclosure metadata is copied from a closed external policy
   decision envelope; software does not invent its reason, transformations,
   authority binding, expiry, revocation state, or audit identity.
2. `validate_disclosure_binding` recomputes the canonical request digest and
   compares every bound context field, preventing principal or context
   substitution under a stale digest.
3. `minimized` requires at least one declared transformation. Disclosure time
   windows cannot be inverted.
4. Separation of duties records an external governance-decision identity and
   authority-binding identities. When required, approver principals and their
   bindings must both be distinct.

## Acceptance evidence

`tests/unit/v4/test_revision_r4.py` contains the adversarial fixtures. Those
tests were committed red before this implementation.

## Compatibility, migration, and rollback

This changes only the unaccepted v4 proposal contract API. Callers replace the
old scalar `policy_version` / `policy_result` arguments with a versioned
`disclosure-policy-decision-v1` mapping. There is no persisted v4 data and no
live migration. Revert this ADR and the accompanying contract commit to roll
back; Wave 0 and protected branches remain unchanged.
