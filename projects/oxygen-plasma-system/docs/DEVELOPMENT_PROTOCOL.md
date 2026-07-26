# Development and Handover Protocol

## One-function release rule

No release may combine unrelated features. A release request must be expressible as:

> Add one function, expose it in the GUI, test it, open the GUI, document it, commit it, tag it, and synchronize it.

## Required branch flow

```text
main
└── feature/gui-vNN-short-function-name
```

Recommended sequence:

```powershell
git switch main
git pull --rebase origin main
git switch -c feature/gui-v02-parameter-validation
# implement one function
git add --all
git commit -m "feat(gui-v2): add validated process parameter form"
git switch main
git pull --rebase origin main
git merge --ff-only feature/gui-v02-parameter-validation
git tag -a gui-v2 -m "GUI v2"
git push origin main
git push origin gui-v2
```

## Handover files

Every AI agent or developer must read these files before changing code:

1. `AGENTS.md`
2. `CURRENT_STATE.md`
3. `docs/ROADMAP.md`
4. `docs/SAFETY_ARCHITECTURE.md`
5. `CHANGELOG.md`

## Definition of done

- New behavior has a focused unit test.
- Existing tests remain green.
- GUI launch command exits only when the user closes the window.
- No new hardware command is introduced without an explicit safety gate.
- No credentials, serial numbers, calibration certificates, patient data, or sensitive laboratory data are committed.
- Working tree is clean after synchronization.
