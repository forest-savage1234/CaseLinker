# W1-001: Versioned JSON contracts as the Wave 1 executable surface

- **Status:** Proposed
- **Scope:** CaseLinker v4 research-network proposal only
- **Upstream:** not accepted; not an official CaseLinker ADR
- **Date:** 2026-08-15
- **Unresolved authorities:** none for this kernel; OD-008 if a later wave claims production schema registry hosting

## Context

Wave 1 must express contracts before infrastructure. Empty ports across every future subsystem would be horizontal scaffolding.

## Decision

1. Executable Wave 1 contracts are versioned JSON Schema documents under `schemas/v4/`.
2. A fail-closed validator loads those schemas and rejects unknown properties, missing required fields, and unpinned `schema_version`.
3. Python types exist only to run that validator and any invariant JSON Schema cannot state.
4. These ADRs live in `docs/v4/adr/` so they cannot be read as continuations of `docs/adr/` vNext acceptances.

## Consequences

Later slices add schemas validated by the same kernel. No database or service is required.

## Rejected alternatives

- Broad repository/adapter packages before a single coherent contract.
- Putting Proposed v4 ADRs in `docs/adr/` next to accepted vNext decisions.
