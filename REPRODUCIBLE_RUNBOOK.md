# Reproducible Runbook

Generated: 2026-05-17T21:08:07
Updated: 2026-05-18 for the PPCE v6 model-family audit route.

## Environment

Recommended Python packages:

```bash
pip install pandas matplotlib python-docx
```

## Internal full rebuild

The full local rebuild uses private workspace paths and raw Abaqus files that are not redistributed in this public package:

```bash
python scripts/build_high_probability_supplements_local.py
```

Expected internal outputs include:

- `p1_raw_solver_file_inventory.csv`
- `p1_raw_job_solver_audit.csv`
- `softwarex_shear_solver_benchmark_audit.csv`
- `deconfounded_match_probe_rows.csv`
- v8 manuscript draft and JCSR package files.

## Public verification

Public users can inspect the derived CSV files in `derived_outputs/` and verify the reported audit facts:

- `derived_outputs/ppce_numeric_traceability.csv` maps headline numbers to derived sources.
- `derived_outputs/ppce_v6_claim_boundary_table.csv` records supported and unsupported claim levels.
- `derived_outputs/ppce_v6_model_parameter_audit.csv` records model and solver information available before claim interpretation.
- `figures/Fig01_mode1_ratio.png` and `figures/Fig02_peak_abs_rf2_ratio.png` are the public figure files used for the main ratio summaries.
- raw Job-2 element type: `S4R`;
- raw Job-2 nonlinear solver status: not successfully completed;
- raw Job-2 summary: 108 increments, 20 cutbacks, 447 iterations, 8 negative-eigenvalue warnings and 2 error messages.

## Success criteria

The public package is successful if the derived audit tables reproduce the values cited in the short technical manuscript: the 11-pair elastic eigenvalue ratio, the secondary nonlinear RF-U response-index ratio, and the raw Job-2 solver-status boundary. Because raw solver files are not redistributed, this package is an audit supplement rather than a full Abaqus rerun archive.
