# Oxygen Plasma System

A versioned, safety-first software skeleton for an oxygen plasma process-control and monitoring application.

The project follows the PyMoDAQ plugin-template architecture while keeping the first releases hardware-independent. Every development increment must add exactly one bounded function, update the GUI, run automated tests, open the GUI successfully, and create a Git commit/tag.

## Published location

GUI v1 is published in `aoa-create/research-software-portfolio` under `projects/oxygen-plasma-system`. A dedicated repository may be created later without changing the versioned development protocol.

## Current release

**GUI v1 / package v0.1.0**

Implemented function: safe bootstrap self-check.

- Starts in simulation mode.
- Hardware output is disabled.
- Displays package version and safety state.
- Runs a deterministic bootstrap self-check.
- Does not communicate with pumps, valves, MFCs, gauges, or RF generators.

## Run GUI v1 on Windows

```powershell
Set-Location "C:\Users\aoa02\Documents\oxygen-plasma-system"
.\scripts\setup.ps1
.\scripts\run_gui.ps1
```

## Development invariant

A version is not complete unless all of the following are true:

1. One bounded function is implemented.
2. Unit tests pass.
3. GUI starts without traceback.
4. The new function is visible or testable in the GUI.
5. `CURRENT_STATE.md` and `CHANGELOG.md` are updated.
6. The change is committed and tagged.
7. Remote synchronization is verified.

## Safety boundary

This software is not a substitute for hardwired interlocks, safety relays, emergency-stop circuits, certified pressure protection, or manufacturer safety controls. Hardware actuation remains prohibited until the roadmap reaches the explicitly gated hardware-control stages.
