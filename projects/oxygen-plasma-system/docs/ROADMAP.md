# Versioned Development Roadmap

## Release rule

Each numbered GUI release adds exactly one bounded capability. At the end of every release:

1. Run unit tests.
2. Run static checks.
3. Launch the GUI.
4. Verify the new capability through the GUI.
5. Update `CURRENT_STATE.md` and `CHANGELOG.md`.
6. Commit with `feat(gui-vN): ...`.
7. Tag with `gui-vN` and semantic package version.
8. Pull/rebase before push and verify local/remote commit equality.

## Staged roadmap

| GUI | Package | Single added capability | Hardware status | Completion evidence |
|---|---:|---|---|---|
| GUI v1 | 0.1.0 | Safe bootstrap self-check | Simulation only | GUI opens and reports outputs disabled |
| GUI v2 | 0.2.0 | Validated process parameter form | Simulation only | Invalid pressure/flow/power/time rejected |
| GUI v3 | 0.3.0 | Process state-machine simulator | Simulation only | State transitions visible in GUI |
| GUI v4 | 0.4.0 | Interlock evaluation engine | Simulation only | Unsafe simulated condition blocks transition |
| GUI v5 | 0.5.0 | Simulated live telemetry | Simulation only | Pressure/flow/power trends displayed |
| GUI v6 | 0.6.0 | Recipe save/load | Simulation only | Validated recipe round-trip succeeds |
| GUI v7 | 0.7.0 | Run logging and audit record | Simulation only | Run stored in SQLite and shown in GUI |
| GUI v8 | 0.8.0 | Device-adapter interfaces and mock drivers | Mock devices only | Connect/disconnect shown without hardware |
| GUI v9 | 0.9.0 | Pressure-gauge read-only driver | Read-only hardware | Live pressure read with timeout/fault handling |
| GUI v10 | 0.10.0 | Oxygen MFC read-only monitoring | Read-only hardware | Flow read and limits displayed |
| GUI v11 | 0.11.0 | MFC setpoint command with hard limits | Limited actuation | Setpoint constrained and physically interlocked |
| GUI v12 | 0.12.0 | Pump/valve status and command adapter | Limited actuation | Safe-state and communication-loss tests pass |
| GUI v13 | 0.13.0 | RF generator read-only monitoring | Read-only RF | Forward/reflected power displayed |
| GUI v14 | 0.14.0 | RF enable command gated by hard interlocks | Controlled actuation | Hardware interlock evidence required |
| GUI v15 | 0.15.0 | Automated recipe execution | Controlled actuation | Full simulated and supervised dry run passes |
| GUI v16 | 0.16.0 | Fault latch and deterministic safe shutdown | Controlled actuation | Injected faults force verified shutdown |
| GUI v17 | 0.17.0 | Calibration and maintenance records | Controlled actuation | Due/expired calibration visibly blocks use |
| GUI v18 | 0.18.0 | Report export | Controlled actuation | Signed PDF/CSV run report generated |
| GUI v19 | 0.19.0 | User roles and immutable audit trail | Controlled actuation | Authorization tests pass |
| GUI v20 | 1.0.0 | Validated integrated release | Deployment candidate | Acceptance protocol completed |

## Mandatory gates

### Gate A — Before any real device connection

- Simulator coverage for expected states and faults.
- Communication timeout policy.
- Configuration schema and hard operating limits.
- No command path can bypass the safety layer.

### Gate B — Before any physical actuator command

- Hardwired interlocks documented and tested independently of the PC.
- Emergency stop verified.
- Fail-safe relay/valve states documented.
- Manufacturer command protocol and limits verified.
- Supervised dry run with oxygen and RF disabled.

### Gate C — Before RF enable

- Chamber-closed, vacuum, gas-flow, cooling, pump, reflected-power and emergency-stop signals are enforced outside the application.
- Software only requests enable; it cannot defeat physical safety logic.
- Communication loss removes RF enable.
