# Slice D — eligibility, disclosure, authority interfaces

**Requirements:** CONST-009, CONST-018, DISCLOSE-001…004, REVIEW-001  
**Distinctions:** research eligibility is not disclosure permission  
**Blocked:** OD-003 policy content; OD-005 real IdP/qualifications

## Acceptance contract

1. A disclosure decision naming a policy version may be `denied` or `authorized`.
2. Treating eligibility as disclosure is rejected.
3. Missing `policy_version` denies.
4. A principal binding uses an opaque id, not a display name. No password or MFA fields exist.

## Tests

`tests/unit/v4/test_disclosure_authority.py`
