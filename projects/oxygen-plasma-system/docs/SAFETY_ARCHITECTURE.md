# Safety Architecture Boundary

## Principle

The application is a supervisory interface, not the primary safety system.

## Required independent controls

- Hardwired emergency stop.
- Chamber-door/cover interlock.
- Vacuum permissive for RF.
- Gas-flow permissive and upper limit.
- Cooling permissive where required.
- Pump-running feedback.
- Reflected-power trip or generator-native protection.
- Maximum process duration independent of the GUI.
- Safe de-energized valve and relay states.

## Software requirements

- Default-deny commands.
- Explicit connection state.
- Bounded setpoints.
- Command acknowledgement and timeout.
- Fault latch.
- Append-only audit events.
- Deterministic safe-shutdown sequence.
- Simulation mode clearly separated from hardware mode.
- No interlock bypass control in the GUI.
