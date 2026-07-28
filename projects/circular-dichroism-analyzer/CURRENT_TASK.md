# Current Task — ChiroSpectra Studio V0.0.1

## Objective

Create a reproducible Windows x64 build of the pinned `pcddb/DichroIDPs` upstream snapshot before any scientific behavior is modified.

## Required work

- Create `aoa-create/circular-dichroism-analyzer` as an independent repository.
- Import a pinned upstream snapshot.
- Add `LICENSE`, `UPSTREAM.md` and `THIRD_PARTY_NOTICES.md`.
- Repair Eigen, ALGLIB and QCustomPlot dependency paths.
- Remove developer-specific absolute paths.
- Build Release mode.
- Open the original GUI.
- Execute and record the legacy smoke workflow.
- Produce `ChiroSpectra-Studio-v0.0.1-win64.zip`.
- Record SHA-256 and smoke-test evidence.

## Prohibited in V0.0.1

- No algorithm changes.
- No removal of legally required attribution.
- No JASCO import implementation.
- No smoothing or shift-analysis implementation.
- No claims of validated instrument equivalence.

## Completion evidence

```text
build/Release/ executable
smoke-test-report.json
SHA256SUMS.txt
screenshots/v0.0.1-main-window.png
CHANGELOG.md entry
Git tag gui-v0.0.1
```
