from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DERIVED = ROOT / "derived_outputs"


EXPECTED_TRACEABILITY = {
    "Mode 1 eigenvalue paired valid cases": "11",
    "Separated-to-overall Mode 1 eigenvalue ratio mean": "0.961",
    "Mode 1 eigenvalue ratio bootstrap CI": "0.944-0.978",
    "Primary nonlinear RF-U paired valid cases": "11",
    "Separated-to-overall peak_abs_rf2 ratio mean": "1.236",
    "peak_abs_rf2 ratio bootstrap CI": "0.968-1.488",
    "Raw separated-family Job-2 ODB size": "393673564",
    "Raw separated-family Job-2 increments/cutbacks/iterations/errors": "108/20/447/2",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    trace_rows = read_csv(DERIVED / "ppce_numeric_traceability.csv")
    values = {row["numeric_statement"]: row["reported_value"] for row in trace_rows}

    missing: list[str] = []
    mismatched: list[tuple[str, str, str | None]] = []
    for key, expected in EXPECTED_TRACEABILITY.items():
        actual = values.get(key)
        if actual is None:
            missing.append(key)
        elif actual != expected:
            mismatched.append((key, expected, actual))

    solver_rows = read_csv(DERIVED / "p1_raw_job_solver_audit_public.csv")
    job2 = next((row for row in solver_rows if row.get("job") == "Job-2"), None)
    if job2 is None:
        missing.append("Job-2 raw solver audit row")
    else:
        checks = {
            "Job-2 element type": (job2.get("element_types"), "S4R"),
            "Job-2 Static Riks": (job2.get("has_static_riks"), "True"),
            "Job-2 contact": (job2.get("has_contact"), "True"),
            "Job-2 friction": (job2.get("has_friction"), "True"),
            "Job-2 completion status": (job2.get("sta_completed_successfully"), "False"),
            "Job-2 increments": (job2.get("total_increments"), "108"),
            "Job-2 cutbacks": (job2.get("cutbacks"), "20"),
            "Job-2 iterations": (job2.get("iterations"), "447"),
            "Job-2 negative eigenvalue warnings": (job2.get("negative_eigenvalue_warnings"), "8"),
            "Job-2 error messages": (job2.get("error_messages"), "2"),
        }
        for label, (actual, expected) in checks.items():
            if actual != expected:
                mismatched.append((label, expected, actual))

    if missing or mismatched:
        print("PUBLIC PACKAGE CHECK: FAIL")
        for key in missing:
            print(f"missing: {key}")
        for key, expected, actual in mismatched:
            print(f"mismatch: {key}: expected {expected!r}, got {actual!r}")
        return 1

    print("PUBLIC PACKAGE CHECK: PASS")
    print("Verified headline ratios and Job-2 solver-status boundary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
