# Slice D — eligibility, disclosure, authority interfaces

**Requirements:** CONST-009, CONST-018, DISCLOSE-001…004, REVIEW-001  
**Distinctions:** research eligibility is not disclosure permission  
**Blocked:** OD-003 policy content; OD-005 real IdP/qualifications

## Acceptance contract

1. A non-denied disclosure decision copies a closed, externally supplied policy-decision envelope. `outcome` must equal its result.
2. Treating eligibility as disclosure is rejected.
3. Missing `policy_version` permits only `denied`. A denied policy result cannot become `minimized`.
4. Every §7.8 binding is required. `validate_disclosure_binding` recomputes the request digest and compares every copied context field.
5. A `minimized` result declares at least one transformation, and disclosure time windows cannot be inverted.
6. A principal and authority binding use opaque ids, not display names. No password or MFA fields exist.
7. SoD records an external governance-decision id; required approvers and authority bindings must be distinct.

## Tests

`tests/unit/v4/test_disclosure_authority.py`; `tests/unit/v4/test_revision_r4.py`
