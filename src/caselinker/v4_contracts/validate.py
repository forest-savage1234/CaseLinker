"""Placeholder: Slice A tests must fail until the kernel is implemented."""


class ContractError(ValueError):
    """Raised when a v4 proposal contract instance is not acceptable."""


def validate_instance(schema_name: str, instance: object) -> None:
    """Reject every instance until the versioned validator exists."""
    raise ContractError(f"v4 contract validator is not implemented ({schema_name})")
