# Circular Dichroism Analyzer — Incremental GUI Roadmap

## Project basis

- Upstream source: `pcddb/DichroIDPs`
- Upstream license: MIT
- Target source repository: `aoa-create/circular-dichroism-analyzer`
- Intended local path: `C:\Users\aoa02\Documents\CD_Analyzer_Open`
- Direction: one codebase, Qt desktop GUI, C++ analysis core
- Release rule: do not create copied folders such as `gui_v1_final`. Preserve runnable states with Git tags.

## Mandatory release gate

Every version must:

1. Add exactly one primary user-visible function.
2. Build without compile errors.
3. Pass tests for the new function.
4. Open the desktop GUI after the build.
5. Load the fixed smoke-test dataset.
6. Confirm that prior functions still work.
7. Update changelog and handoff state.
8. Merge through a pull request and create the corresponding `gui-vN.0.0` tag.

## Phase 0 — baseline recovery

### GUI v0.1 — reproducible upstream build

- Preserve MIT license and attribution.
- Record the exact upstream commit.
- Repair Eigen, ALGLIB and QCustomPlot paths.
- Build and open the unchanged original GUI.
- No analytical behavior changes.

Tag: `gui-v0.1.0`

## Functional versions

| GUI version | Single added function | Branch | Tag |
|---|---|---|---|
| v1 | Generic two-column TXT/CSV spectrum import | `feature/gui-v01-generic-import` | `gui-v1.0.0` |
| v2 | Raw spectrum plotting | `feature/gui-v02-spectrum-plot` | `gui-v2.0.0` |
| v3 | Buffer/blank subtraction | `feature/gui-v03-blank-subtraction` | `gui-v3.0.0` |
| v4 | Replicate averaging and pointwise SD | `feature/gui-v04-replicate-average` | `gui-v4.0.0` |
| v5 | Millidegree-to-MRE conversion | `feature/gui-v05-mre-conversion` | `gui-v5.0.0` |
| v6 | Savitzky–Golay smoothing | `feature/gui-v06-savgol-smoothing` | `gui-v6.0.0` |
| v7 | Wavelength-range selection | `feature/gui-v07-wavelength-range` | `gui-v7.0.0` |
| v8 | HT/absorbance quality flags | `feature/gui-v08-quality-flags` | `gui-v8.0.0` |
| v9 | Processed spectrum CSV export | `feature/gui-v09-csv-export` | `gui-v9.0.0` |
| v10 | Project save/load | `feature/gui-v10-project-session` | `gui-v10.0.0` |
| v11 | SELCON secondary-structure analysis | `feature/gui-v11-selcon-analysis` | `gui-v11.0.0` |
| v12 | SVD decomposition | `feature/gui-v12-svd` | `gui-v12.0.0` |
| v13 | Thermal unfolding fit | `feature/gui-v13-thermal-unfolding` | `gui-v13.0.0` |
| v14 | Chemical unfolding fit | `feature/gui-v14-chemical-unfolding` | `gui-v14.0.0` |
| v15 | Batch processing | `feature/gui-v15-batch-processing` | `gui-v15.0.0` |
| v16 | Reproducible analysis report | `feature/gui-v16-report` | `gui-v16.0.0` |
| v17 | Reproducible Windows package | `feature/gui-v17-windows-package` | `gui-v17.0.0` |

## Core acceptance rules

- Raw imported data are immutable.
- Every processed spectrum is a derived object with provenance.
- Units are explicit and validated.
- Invalid numerical inputs are blocked rather than silently corrected.
- Scientific fits report convergence, residuals and uncertainty.
- GUI and analysis logic are separated.
- No version may depend on developer-specific absolute paths.
- No release may claim clinical, regulatory or instrument validation.

## Git workflow for every version

```powershell
Set-Location "C:\Users\aoa02\Documents\CD_Analyzer_Open"
git fetch --all --prune
git switch main
git pull --ff-only origin main
git switch -c feature/gui-vNN-feature-name

# Implement one function, build, test and open GUI.

git status --short
git add --all
git commit -m "feat(gui-vNN): add feature name"
git push -u origin feature/gui-vNN-feature-name
```

After pull-request merge:

```powershell
git switch main
git pull --ff-only origin main
git tag -a gui-vN.0.0 -m "GUI vN - feature name"
git push origin gui-vN.0.0
```

## Remote configuration

The source repository will use two remotes:

```powershell
git remote rename origin upstream
git remote add origin https://github.com/aoa-create/circular-dichroism-analyzer.git
git fetch --all --prune
```

- `upstream`: `pcddb/DichroIDPs`
- `origin`: `aoa-create/circular-dichroism-analyzer`

Upstream changes must be integrated through a dedicated synchronization branch, never directly inside an active GUI feature branch.
