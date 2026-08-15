# Slice D — eligibility, disclosure, authority interfaces

**Requirements:** CONST-009, CONST-018, DISCLOSE-001…004, REVIEW-001  
**Distinctions:** research eligibility is not disclosure permission  
**Blocked:** OD-003 policy content; OD-005 real IdP/qualifications

## Acceptance contract

1. A disclosure decision naming a valid opaque policy version may record the supplied `policy_result`. `outcome` must equal that result.
2. Treating eligibility as disclosure is rejected.
3. Missing `policy_version` permits only `denied`. A denied policy result cannot become `minimized`.
4. Every §7.8 binding is required, and the decision carries a `request_digest` of the request.
5. A principal binding uses an opaque id, not a display name. No password or MFA fields exist.

## Tests

`tests/unit/v4/test_disclosure_authority.py`
