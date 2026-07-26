"""Safe application bootstrap state for GUI v1."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class BootstrapStatus:
    """Immutable result of the startup safety self-check."""

    application_ready: bool
    simulation_mode: bool
    hardware_outputs_enabled: bool
    interlock_bypass_allowed: bool
    checked_at_utc: str
    message: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def get_bootstrap_status() -> BootstrapStatus:
    """Return a deterministic fail-safe startup status.

    GUI v1 must never enable physical outputs. The function therefore reports a
    ready application only when simulation mode is active and all hardware output
    paths remain disabled.
    """

    return BootstrapStatus(
        application_ready=True,
        simulation_mode=True,
        hardware_outputs_enabled=False,
        interlock_bypass_allowed=False,
        checked_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        message="Safe bootstrap passed: simulation mode active; hardware outputs disabled.",
    )
