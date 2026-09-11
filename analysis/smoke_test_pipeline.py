#!/usr/bin/env python3
"""End-to-end smoke test for the classroom data pipeline.

This script uses synthetic demonstration records only. It verifies that a
ResearchDashboard-style app export can be merged with the study metadata sheet
and processed by analyze_study.py into the manuscript result tables.
"""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
ANALYZER = ROOT / "analysis" / "analyze_study.py"


def write_app_export(path: Path, code: str, pre: int, post: int, durations: list[int]) -> None:
    max_score = 12
    gain = (post - pre) / (max_score - pre) if max_score > pre else 0.0
    header = ["ParticipantCode", "PreScore", "PostScore", "MaxScore", "NormalizedGain", "LabsCompleted"]
    row = [code, pre, post, max_score, f"{gain:.3f}", 5]
    for i, duration in enumerate(durations, start=1):
        header += [f"Lab{i}Completed", f"Lab{i}DurationSec", f"Lab{i}SubmittedAt", f"Lab{i}Reflection"]
        row += [1, duration, 1760000000000 + i, f"Synthetic reflection for lab {i}"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(row)


def main() -> None:
    participants = [
        ("S001", "Experimental", 5, 9),
        ("S002", "Experimental", 6, 9),
        ("S003", "Experimental", 6, 10),
        ("S004", "Experimental", 7, 10),
        ("S005", "Experimental", 5, 8),
        ("S006", "Control", 5, 7),
        ("S007", "Control", 6, 7),
        ("S008", "Control", 5, 7),
        ("S009", "Control", 7, 8),
        ("S010", "Control", 6, 7),
    ]

    with tempfile.TemporaryDirectory(prefix="dsplab-smoke-") as tmp:
        base = Path(tmp)
        app_dir = base / "app_exports"
        app_dir.mkdir()
        metadata_path = base / "study_metadata.csv"
        out_dir = base / "results"

        metadata_fields = ["ParticipantCode", "Group", "PreScore", "PostScore", "MaxScore"] + [f"Q{i}" for i in range(1, 11)]
        with metadata_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=metadata_fields)
            writer.writeheader()
            for idx, (code, group, pre, post) in enumerate(participants):
                row = {
                    "ParticipantCode": code,
                    "Group": group,
                    "PreScore": pre,
                    "PostScore": post,
                    "MaxScore": 12,
                }
                for q in range(1, 11):
                    row[f"Q{q}"] = 3 + ((idx + q) % 3) if group == "Experimental" else ""
                writer.writerow(row)

        for idx, (code, group, pre, post) in enumerate(participants):
            if group == "Experimental":
                write_app_export(
                    app_dir / f"DSP_Research_{code}.csv",
                    code,
                    pre,
                    post,
                    [780 + 15 * idx, 840 + 15 * idx, 900 + 15 * idx, 960 + 15 * idx, 1020 + 15 * idx],
                )

        subprocess.run(
            [
                sys.executable,
                str(ANALYZER),
                "--app-dir",
                str(app_dir),
                "--metadata",
                str(metadata_path),
                "--out",
                str(out_dir),
            ],
            check=True,
            cwd=ROOT,
        )

        required = [
            "analysis_dataset.csv",
            "table_descriptives.csv",
            "table_within_group_pre_post.csv",
            "table_between_groups.csv",
            "table_primary_ancova.csv",
            "table_questionnaire.csv",
            "analysis_summary.txt",
        ]
        missing = [name for name in required if not (out_dir / name).exists()]
        if missing:
            raise AssertionError(f"Missing expected outputs: {missing}")

        data = pd.read_csv(out_dir / "analysis_dataset.csv")
        if len(data) != 10:
            raise AssertionError(f"Expected 10 merged participants, found {len(data)}")
        counts = data["Group"].value_counts().to_dict()
        if counts.get("Experimental") != 5 or counts.get("Control") != 5:
            raise AssertionError(f"Unexpected group counts: {counts}")

        ancova = pd.read_csv(out_dir / "table_primary_ancova.csv")
        if not ancova["Term"].astype(str).str.contains("Experimental", regex=False).any():
            raise AssertionError("Experimental-group coefficient missing from ANCOVA table")

        questionnaire = pd.read_csv(out_dir / "table_questionnaire.csv")
        if set(questionnaire["Item"]) != {f"Q{i}" for i in range(1, 11)}:
            raise AssertionError("Questionnaire output does not contain Q1-Q10")

        print("DSP-Lab classroom data pipeline smoke test: PASS")
        print("Verified app-export schema -> metadata merge -> manuscript result tables.")


if __name__ == "__main__":
    main()
