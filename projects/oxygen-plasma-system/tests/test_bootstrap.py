from pymodaq_plugins_oxygen_plasma.core.bootstrap import get_bootstrap_status


def test_gui_v1_bootstrap_is_fail_safe() -> None:
    status = get_bootstrap_status()

    assert status.application_ready is True
    assert status.simulation_mode is True
    assert status.hardware_outputs_enabled is False
    assert status.interlock_bypass_allowed is False
    assert "hardware outputs disabled" in status.message.lower()
