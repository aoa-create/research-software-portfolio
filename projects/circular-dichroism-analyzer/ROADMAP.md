# ChiroSpectra Studio — Circular Dichroism Analyzer Roadmap v2

## 1. Product definition

**Working product name:** ChiroSpectra Studio  
**Target source repository:** `aoa-create/circular-dichroism-analyzer`  
**Upstream technical skeleton:** `pcddb/DichroIDPs`  
**Desktop stack:** C++20, Qt 6, CMake, Eigen, QCustomPlot  
**Primary instrument target:** JASCO J-815/J-series exported CD data  
**Release target:** Windows x64 GUI and `.exe` package after every version

The product will be functionally comparable to a modern CD spectral-analysis workstation while retaining an independent visual design and implementation. It must support JASCO-compatible import, non-destructive preprocessing, overlays, smoothing, local and global spectral-shift analysis, secondary-structure workflows and reproducible reporting.

## 2. Non-negotiable legal and rebranding rule

The V0 series removes the old product's **visible branding**, including old application name, logo, icon, splash screen, menu wording, embedded e-mail addresses, obsolete web links, screenshots and sample project identity.

The following must **not** be removed:

- the upstream MIT license;
- copyright notices required by that license;
- third-party license notices for Eigen, ALGLIB, QCustomPlot and other dependencies;
- a factual provenance record in `THIRD_PARTY_NOTICES.md` and `UPSTREAM.md`.

The source should be imported into a new independent repository as a pinned upstream snapshot rather than presented as original work. The new GUI must not copy JASCO or BeStSel artwork, icons, layout or proprietary code.

## 3. Release gate applied to every version

A version is complete only when all items pass:

1. Exactly one primary capability or one V0 migration objective is completed.
2. Debug and Release builds complete without errors.
3. Automated tests for the new behavior pass.
4. The Release GUI opens automatically after the build.
5. The fixed smoke-test dataset loads.
6. Previous released capabilities pass regression checks.
7. A versioned Windows x64 package is produced under `dist/<version>/`.
8. `CHANGELOG.md`, `PROJECT_STATE.json` and test evidence are updated.
9. The feature branch is pushed, reviewed and merged through a pull request.
10. A signed/annotated Git tag is created only after merge.

Required artifact names:

```text
ChiroSpectra-Studio-vN.N.N-win64.zip
ChiroSpectra-Studio-vN.N.N-setup.exe
SHA256SUMS.txt
smoke-test-report.json
```

## 4. V0 series — complete identity replacement while preserving functions

### V0.0.1 — Upstream snapshot and reproducible baseline

**Objective:** import the exact upstream source snapshot and prove that the original functions still run.

- Record upstream repository and commit SHA in `UPSTREAM.md`.
- Preserve MIT and dependency notices.
- Vendor or correctly resolve Eigen, ALGLIB and QCustomPlot.
- Remove developer-specific absolute paths.
- Build the unchanged analytical behavior.
- Open the GUI and run the original sample workflow.

**Tag:** `gui-v0.0.1`

### V0.1.0 — Full visible rebrand

**Objective:** replace the complete visible identity without deleting analytical functions.

- Application name: `ChiroSpectra Studio`.
- New original icon, splash screen and Windows executable metadata.
- New main-window layout, toolbar, status bar, typography and dialogs.
- Replace old product names in window titles, menus, resources and documentation.
- Remove old logos, author signatures, e-mail addresses and obsolete external links from the visible GUI.
- Replace the About dialog with project version, build ID and legal-notice links.
- Preserve every original analysis function behind the new interface.
- Add a legacy-function regression checklist.

**Tag:** `gui-v0.1.0`

### V0.2.0 — Qt 6/CMake application architecture

**Objective:** modernize the build without changing scientific output.

- Move from qmake/Qt 5 assumptions to CMake and Qt 6.
- Separate `core`, `io`, `analysis`, `gui` and `reporting` modules.
- Add unit tests and GitHub Actions Windows build.
- Generate a portable Release EXE and dependency bundle.

**Tag:** `gui-v0.2.0`

### V0.3.0 — Stable internal spectrum model

**Objective:** create an immutable and traceable spectrum object used by all future versions.

Required fields include wavelength, CD, absorbance, HT/dynode, temperature, units, concentration, pathlength, residue count, instrument metadata, source filename and processing history.

**Tag:** `gui-v0.3.0`

## 5. Functional GUI/EXE versions

| Version | Single primary capability | Required visible result | Branch | Tag |
|---|---|---|---|---|
| V1 | JASCO exported-file import | Import wizard and metadata/channel preview | `feature/gui-v01-jasco-import` | `gui-v1.0.0` |
| V2 | Direct `.jws` intake decision implementation | Native parser if validated; otherwise controlled conversion workflow | `feature/gui-v02-jws-intake` | `gui-v2.0.0` |
| V3 | Multi-spectrum overlay | Selectable overlaid spectra with legend and synchronized axes | `feature/gui-v03-overlay` | `gui-v3.0.0` |
| V4 | Buffer/blank subtraction | Raw, blank and corrected curves shown together | `feature/gui-v04-blank-subtraction` | `gui-v4.0.0` |
| V5 | Replicate averaging | Mean curve with pointwise SD/SEM band | `feature/gui-v05-replicate-average` | `gui-v5.0.0` |
| V6 | CD unit conversion | mdeg, ΔA, Δε, molar ellipticity and MRE | `feature/gui-v06-unit-conversion` | `gui-v6.0.0` |
| V7 | Baseline correction | User-defined or fitted baseline with preview | `feature/gui-v07-baseline-correction` | `gui-v7.0.0` |
| V8 | Savitzky–Golay smoothing | Live raw/smoothed preview and parameter validation | `feature/gui-v08-savgol-smoothing` | `gui-v8.0.0` |
| V9 | Extrema detection | Positive maxima, negative minima and zero crossings | `feature/gui-v09-extrema-detection` | `gui-v9.0.0` |
| V10 | Local red/blue shift analysis | Matched-feature Δλ table and annotated overlay | `feature/gui-v10-local-shift` | `gui-v10.0.0` |
| V11 | Global spectral-shift analysis | Cross-correlation shift, similarity and confidence | `feature/gui-v11-global-shift` | `gui-v11.0.0` |
| V12 | Difference/ratio analysis | Difference spectrum, ratio and selected-range area | `feature/gui-v12-difference-ratio` | `gui-v12.0.0` |
| V13 | JASCO-style quality control | HT/absorbance cutoff and usable wavelength range | `feature/gui-v13-quality-control` | `gui-v13.0.0` |
| V14 | Publication export | CSV/TXT/JCAMP-DX plus PNG/SVG/PDF | `feature/gui-v14-export` | `gui-v14.0.0` |
| V15 | BeStSel-compatible handoff | Validated BeStSel input file and browser launch | `feature/gui-v15-bestsel-export` | `gui-v15.0.0` |
| V16 | BeStSel result comparison | Imported result table versus internal result | `feature/gui-v16-bestsel-results` | `gui-v16.0.0` |
| V17 | Internal SELCON analysis | Secondary-structure fractions, refit and error metrics | `feature/gui-v17-selcon` | `gui-v17.0.0` |
| V18 | SVD/PCA series exploration | Components, scores and explained variance | `feature/gui-v18-svd-pca` | `gui-v18.0.0` |
| V19 | Thermal unfolding analysis | Tm fit, residuals and parameter uncertainty | `feature/gui-v19-thermal-unfolding` | `gui-v19.0.0` |
| V20 | Batch/project workflow | Save, reopen and batch-process experiment sets | `feature/gui-v20-project-batch` | `gui-v20.0.0` |
| V21 | Reproducible report | PDF/HTML report with provenance and processing history | `feature/gui-v21-report` | `gui-v21.0.0` |
| V22 | Production installer | Signed-ready installer, portable ZIP and update manifest | `feature/gui-v22-installer` | `gui-v22.0.0` |

## 6. V1 JASCO import specification

V1 must read JASCO Spectra Manager **readable exports**:

- `.txt` and ASCII XY/multichannel exports;
- `.csv` exports;
- `.dx` / JCAMP-DX exports;
- generic delimited files with explicit column mapping.

The import wizard must detect or request:

- wavelength column and direction;
- CD, absorbance, HT/dynode and temperature channels;
- delimiter and decimal symbol;
- units and pathlength;
- concentration and number of residues;
- scan/replicate identifiers;
- acquisition metadata retained in headers.

Import must never silently guess scientifically critical units. Ambiguous fields require user confirmation.

## 7. V2 `.jws` rule

`.jws` is treated as a separate engineering gate because it is a binary JASCO experiment format.

V2 proceeds in this order:

1. Acquire representative `.jws` files from J-815/J-series instruments and matching TXT/CSV exports.
2. Verify whether a stable, legally usable parser or documented conversion interface exists.
3. Validate imported numerical channels point-by-point against Spectra Manager exports.
4. Release native parsing only if wavelength, CD, absorbance, HT and metadata match within defined tolerances.
5. Otherwise release a guided Spectra Manager export/conversion workflow and do not claim native `.jws` support.

## 8. Smoothing specification

V8 uses a non-destructive Savitzky–Golay implementation.

- Raw data remain immutable.
- Window must be odd and larger than polynomial order.
- Wavelength spacing must be checked; irregular grids require controlled resampling.
- Raw and smoothed curves are always displayed together.
- The software reports window in both points and nanometers.
- A BeStSel-oriented preset must target a moderate approximately 2 nm smoothing window, not aggressive smoothing.
- Shift analysis records whether raw or smoothed data were used.

## 9. Red-shift and blue-shift specification

For a reference spectrum and comparison spectrum:

```text
Δλ = λcomparison − λreference
Δλ > 0  → red shift / longer wavelength
Δλ < 0  → blue shift / shorter wavelength
```

V10 local-shift analysis must:

- detect positive maxima and negative minima separately;
- match features by sign, wavelength neighborhood, prominence and shape;
- calculate Δλ, amplitude change and local confidence;
- reject unmatched or low-prominence features;
- annotate matched features on the overlay;
- report replicate-based uncertainty when replicates exist.

V11 global-shift analysis must:

- interpolate both spectra only over their common wavelength range;
- avoid extrapolation by default;
- estimate whole-spectrum displacement by normalized cross-correlation;
- report best shift, correlation/similarity and confidence interval;
- flag spectra whose shape changed too much for a single shift value to be meaningful.

## 10. BeStSel integration policy

The supported integration is initially a controlled data handoff, not undocumented web automation.

V15 must:

- export two-column wavelength/CD data for one spectrum;
- export wavelength plus multiple spectral columns for series analysis;
- use dot decimals and accepted delimiters;
- preserve/validate input units;
- include concentration, residue count and pathlength in a companion metadata file;
- open the official BeStSel page after export;
- record the exact exported spectrum checksum.

V16 may import saved BeStSel result tables or manually entered results for comparison. Automatic form submission or result scraping is prohibited until an official API or explicit permission is available.

## 11. JASCO-like functional scope without visual copying

The target scope includes the same general classes of laboratory workflow expected from modern spectral software:

- overlay and synchronized display;
- add/subtract/divide operations;
- baseline correction;
- smoothing;
- peak/minimum detection;
- derivatives in a later optional module;
- axis/unit conversion;
- CD/absorbance/HT inspection;
- quality flags;
- publication-ready export;
- audit-style processing history.

The interface must remain original and must not reproduce JASCO trademarks, screenshots, icons or proprietary layout.

## 12. Repository structure

```text
circular-dichroism-analyzer/
├── app/
│   ├── gui/
│   └── resources/
├── src/
│   ├── core/
│   ├── io/jasco/
│   ├── preprocessing/
│   ├── shift_analysis/
│   ├── secondary_structure/
│   ├── unfolding/
│   └── reporting/
├── include/
├── tests/
│   ├── unit/
│   ├── regression/
│   ├── golden/
│   └── smoke/
├── test_data/
│   ├── synthetic/
│   ├── jasco_exports/
│   └── expected_results/
├── third_party/
├── docs/
├── scripts/
├── CMakeLists.txt
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── UPSTREAM.md
├── CHANGELOG.md
└── PROJECT_STATE.json
```

## 13. Git and EXE workflow for every version

```powershell
Set-Location "C:\Users\aoa02\Documents\CD_Analyzer_Open"
git fetch --all --prune
git switch main
git pull --ff-only origin main
git switch -c feature/gui-vNN-feature-name

cmake -S . -B build -G "Ninja" -DCMAKE_BUILD_TYPE=Release
cmake --build build
ctest --test-dir build --output-on-failure

# Open the built GUI for the mandatory manual smoke test.
Start-Process ".\build\bin\ChiroSpectraStudio.exe"

git status --short
git add --all
git commit -m "feat(gui-vNN): add feature name"
git push -u origin feature/gui-vNN-feature-name
```

After pull-request merge:

```powershell
git switch main
git pull --ff-only origin main
git tag -a gui-vN.0.0 -m "ChiroSpectra Studio GUI vN"
git push origin gui-vN.0.0
```

## 14. Immediate next task

Start with **V0.0.1** only:

- establish the independent source repository;
- import the pinned upstream snapshot;
- preserve required licenses and provenance;
- repair dependencies and paths;
- build the original functions;
- open the GUI;
- create the first reproducible Windows package.

No JASCO parser, smoothing or shift-analysis code is added before the V0 baseline passes.