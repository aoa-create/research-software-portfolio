# AI/Developer Handover Contract

## Project objective

Develop a modular oxygen plasma monitoring and control application through small, verifiable GUI releases using a PyMoDAQ-oriented plugin architecture.

## Current task boundary

Current release is GUI v1 / 0.1.0. It implements only safe bootstrap self-check. Hardware outputs must remain disabled.

## Before editing

1. Read `CURRENT_STATE.md`.
2. Confirm the next GUI number in `docs/ROADMAP.md`.
3. Create one feature branch.
4. Do not implement later-roadmap features early.
5. Preserve testability without physical hardware.

## Never do

- Never enable RF, valves, pumps, MFC setpoints, or bypass signals in early simulation releases.
- Never assume device protocols, pinouts, voltage levels, pressure units, gas units, or safe limits.
- Never encode real limits without manufacturer documentation and project approval.
- Never weaken tests to make a release pass.
- Never store secrets in the repository.

## End-of-release record

Update `CURRENT_STATE.md` with:

- completed GUI/package version;
- implemented function;
- changed files;
- tests run and results;
- GUI launch result;
- known limitations;
- exact next task;
- commit SHA and tag after synchronization.
