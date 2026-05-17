# Reproducible Runbook

Generated: 2026-05-17T21:08:07

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

Public users can inspect the derived CSV files in `derived_outputs/` and verify the reported v8 audit facts:

- raw Job-2 element type: `S4R`;
- raw Job-2 nonlinear solver status: not successfully completed;
- raw Job-2 summary: 108 increments, 20 cutbacks, 447 iterations, 2 error messages;
- SoftwareX shear benchmark audit: 4/4 Riks records marked completed.
- SoftwareX/Scandella validation summary: 4 specimens, 0.6-7.1% absolute error, 2.85% mean absolute error.

## Success criteria

The public package is successful if the derived audit tables reproduce the exact values cited in the manuscript's v8 solver-audit section. Because raw solver files are not redistributed, this package is an audit supplement rather than a full Abaqus rerun archive.
