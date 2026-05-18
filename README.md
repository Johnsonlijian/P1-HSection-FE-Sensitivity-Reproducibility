# P1 H-Section FE Model-Family Audit - Public Reproducibility Package

This package contains non-sensitive reproducibility assets for a bounded short technical manuscript on Abaqus shell model-family auditing for H-section steel members.

Associated manuscript route:

> A reproducible model-family audit of Abaqus shell models for H-section steel members

## What is included

- Public derived CSV audit tables.
- Public figure files for the main reported ratios.
- Claim-boundary and model-parameter audit tables for the PPCE v6 submission package.
- Traceability metadata and public solver-status summaries.
- Local audit script used to generate internal derived outputs.
- Runbook, dataset/source registry, citation metadata and manuscript-ready reproducibility wording.

## What is excluded

- Raw Abaqus `.odb`, `.cae`, `.sim`, `.msg`, `.sta`, `.dat`, `.log`, `.prt` and other solver files.
- Active submission manuscript, cover letter, reviewer drafts and internal logs.
- Third-party raw data or files with unclear redistribution rights.

## Main reported values

- 11 valid double-positive elastic pairs.
- Separated-to-overall Mode 1 eigenvalue ratio: mean 0.961, median 0.962, 95% bootstrap CI 0.944-0.978.
- 11 primary nonlinear RF-U pairs.
- Separated-to-overall peak_abs_rf2 ratio: mean 1.236, 95% bootstrap CI 0.968-1.488.
- Raw separated-family nonlinear Job-2 audit: non-completion; 108 increments, 20 cutbacks, 447 iterations, 8 negative-eigenvalue warnings and 2 error messages.

## Evidence boundary

The package supports auditability of available derived results and solver-file traces. It does not claim experimental validation, strength prediction, design resistance or a deconfounded shell-representation effect.

## Suggested manuscript wording

See `REPRODUCIBILITY_TEXT_FOR_PAPER.md` for data availability and reproducibility text that can be adapted after the repository URL is confirmed.
