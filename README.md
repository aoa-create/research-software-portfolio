# Ali Onur Aşap — Research Software Portfolio

Independent scientific software and laboratory-automation portfolio focused on analytical instrumentation, cleanroom and microfabrication workflows, laboratory safety, traceability, and reproducible data analysis.

My professional background combines laboratory operations, analytical instrumentation, cleanroom practice, HSE/quality systems, scientific research support, and Python-based workflow development. The projects below are independent portfolio work. Unless explicitly stated otherwise, they use synthetic or demonstration data and are not institutionally deployed, formally validated, or approved for production, fabrication, diagnostic, regulatory, or safety-critical decisions.

## Selected applications

### 1. MEMS Photomask Designer
**Status:** Functional early-stage prototype — current release `v0.4.0`

Parametric MEMS pattern generation, element-level editing, multi-layer management, advisory geometric DRC, real GDSII export, SVG preview, and traceable ZIP handoff packages with SHA-256 checksums.

**Technical focus:** Python, Streamlit, gdstk, geometric checks, test automation, GitHub Actions CI.

**Repository access:** Private source; technical summary available in this portfolio.

### 2. Mask Process Traveler
**Status:** Functional early-stage prototype — current stable release `v0.2.0`

SQLite-based traceability for lithography travelers, samples or wafers, masks, layout-file integrity, photoresists, operators, deviations, timestamps, UUIDs, and audit events through a PySide6 desktop GUI.

**Technical focus:** Python, PySide6, SQLite, SHA-256 integrity, audit trails, automated tests, Windows CI.

**Repository access:** Private source; technical summary available in this portfolio.

### 3. LithoProcess Window
**Repository:** `lithopattern-studio`

**Status:** GUI V1 baseline released; GUI V2 scientific engine in development

Local-first desktop software for importing, validating, analysing, visualising, and reporting photolithography dose/focus process-window data. Current work includes replicate-aware aggregation, pass-rate calculation, connected-region detection, and deterministic nominal-point selection.

**Technical focus:** Python, PySide6, deterministic scientific services, test/coverage gates, recoverable micro-increment releases.

**Repository access:** Private source; technical summary available in this portfolio.

### 4. SEM Metrology Suite
**Status:** Phase 1 active — GUI v1 stages 1–3 implemented (`0.1.0-dev3`)

Offline-capable SEM image metrology platform for traceable calibration, image provenance, critical-dimension workflows, particle and morphology analysis, roughness analysis, defect review, and controlled human approval.

**Technical focus:** Python, napari/PyQt6, scikit-image, OpenCV, calibration manifests, review states, reproducible measurement workflows.

**Repository access:** Private source; technical summary available in this portfolio.

### 5. DLS Zeta Analysis Suite
**Status:** Working GUI V1 foundation — `v0.1.0-foundation`

Scientific desktop application for DLS autocorrelation analysis, cumulants-derived hydrodynamic diameter and PDI estimation, electrophoretic-mobility-to-zeta-potential conversion, and traceable JSON/CSV reporting.

**Technical focus:** Python, PySide6, Stokes–Einstein calculations, Smoluchowski/Hückel/Henry models, unit tests, CI, handoff documentation.

**Scientific boundary:** The application does not control vendor instruments and does not claim equivalence to proprietary vendor algorithms.

**Repository access:** Private source; technical summary available in this portfolio.

### 6. General Data Tool
**Status:** Working prototype; current Windows acceptance test pending

Desktop utility for laboratory and scientific data files, including CSV/Excel import, header repair, column matching, cleaning, filtering, merging, comparison, basic statistics, visualisation, and multi-format export.

**Technical focus:** Python, pandas, Tkinter, structured import workflows, smoke tests and focused tests.

**Repository access:** Private source; technical summary available in this portfolio.

### 7. Chemical Storage Planner
**Status:** Functional prototype — `v0.3.0`; portable Windows EXE validated locally

Decision-support tool for chemical inventory review and practical laboratory storage planning. It supports inventory import, laboratory and cabinet definition, conservative placement planning, traceability fields, missing-data warnings, manual-review items, and Excel reporting.

**Technical focus:** Python, Tkinter, Excel workflows, guided planning, traceability and safety-boundary controls.

**Safety boundary:** Outputs are advisory. Final decisions require current SDS/GBF records, institutional rules, legal requirements, expert risk assessment, and OHS verification.

**Repository access:** Private source; technical summary available in this portfolio.

### 8. MS-Pipeline
**Status:** Developing desktop application framework

A staged mass-spectrometry workflow project for open-format data processing, GUI verification, release builds, testing, and future modular analysis functions. The source-based configuration supports ABF, CDF, and mzML workflows.

**Technical focus:** Windows desktop development, mass-spectrometry workflow integration, incremental releases, GUI verification and test gates.

**Attribution:** This project is based on MS-DIAL source code. LGPL and third-party license notices are preserved; it is not presented as an original replacement for MS-DIAL.

**Public repository:** https://github.com/aoa-create/ms-pipeline

## Professional context

- Laboratory operations, analytical instrumentation, user training, maintenance/calibration follow-up, quality and HSE.
- Cleanroom and microfabrication experience including photolithography, spin coating, mask alignment, UV exposure, thin-film deposition, oxygen-plasma activation, microfluidic fabrication, and microscopy-based characterisation.
- Scientific data analysis and research support across mass spectrometry, spectroscopy, polymer/particle characterisation, microscopy, molecular biology, and biostatistics.
- International industrial laboratory experience in the Chevron Gorgon LNG project through Monadelphous Engineering Associates.

## Publication

Çelik, M.; Kanbeş-Dindar, C.; Khan, R.; Rehman, F.; Meraki, G. E.; Mohamad, S. B.; Aşap, A. O.; İnci, F.; Uslu, B. **Multianalytical and Theoretical Tendency for the Clarification of the Binding of Lansoprazole and Albumin Protein.** *ACS Omega* 2026, 11(14), 21657–21670. DOI: `10.1021/acsomega.5c09146`.

## Access and collaboration

Most project source repositories remain private while documentation, testing, licensing, and release boundaries are being reviewed. Demonstrations or source access may be provided selectively for technical evaluation.

## Public portfolio link

https://github.com/aoa-create/research-software-portfolio
