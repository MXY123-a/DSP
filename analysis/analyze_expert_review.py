#!/usr/bin/env python3
"""Summarize expert review ratings for the DSP-Lab parallel concept tests.

Usage example:
    python analysis/analyze_expert_review.py \
        data/expert_reviews/reviewer1.csv \
        data/expert_reviews/reviewer2.csv \
        data/expert_reviews/reviewer3.csv \
        --out results/expert_review

Each input file should follow analysis/templates/expert_review_template.csv.
Ratings must be integers from 1 to 4. Ratings of 3 or 4 are treated as
endorsements for content-validity summaries.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd

RATING_COLS = [
    "RelevanceA",
    "ClarityA",
    "DistractorA",
    "RelevanceB",
    "ClarityB",
    "DistractorB",
    "Equivalence",
]

PAIR_DOMAINS = {
    1: "Signals",
    2: "Signals",
    3: "Sampling",
    4: "Sampling",
    5: "Sampling",
    6: "Convolution",
    7: "Convolution",
    8: "DFT",
    9: "DFT",
    10: "DFT",
    11: "FIR",
    12: "FIR",
}


def read_review(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    required = ["ReviewerCode", "Pair", "Domain"] + RATING_COLS
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise SystemExit(f"{path}: missing columns: {', '.join(missing)}")

    if len(df) != 12:
        raise SystemExit(f"{path}: expected 12 item-pair rows, found {len(df)}")

    df = df.copy()
    df["Pair"] = pd.to_numeric(df["Pair"], errors="coerce")
    if set(df["Pair"].dropna().astype(int)) != set(range(1, 13)):
        raise SystemExit(f"{path}: Pair must contain each integer 1..12 exactly once")

    for col in RATING_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        invalid = df[col].notna() & ~df[col].isin([1, 2, 3, 4])
        if invalid.any():
            raise SystemExit(f"{path}: {col} contains values outside 1..4")

    reviewer_codes = [
        str(x).strip()
        for x in df["ReviewerCode"].dropna().unique()
        if str(x).strip()
    ]
    if len(reviewer_codes) != 1:
        raise SystemExit(
            f"{path}: enter exactly one nonblank ReviewerCode for this reviewer; "
            "it may be entered once or repeated on all rows"
        )

    reviewer = reviewer_codes[0]
    df["ReviewerCode"] = reviewer
    df["SourceFile"] = path.name
    return df


def endorsement_rate(series: pd.Series) -> float:
    s = series.dropna()
    if len(s) == 0:
        return np.nan
    return float((s >= 3).mean())


def mean_rating(series: pd.Series) -> float:
    s = series.dropna()
    return float(s.mean()) if len(s) else np.nan


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze DSP-Lab expert review ratings and content-validity summaries"
    )
    parser.add_argument("inputs", nargs="+", type=Path, help="Expert-review CSV files")
    parser.add_argument("--out", type=Path, default=Path("expert_review_results"))
    args = parser.parse_args()

    reviews = pd.concat([read_review(p) for p in args.inputs], ignore_index=True)
    reviewers = sorted(reviews["ReviewerCode"].unique())
    if len(reviewers) < 2:
        raise SystemExit("At least two completed expert-review files are required")

    args.out.mkdir(parents=True, exist_ok=True)
    reviews.to_csv(args.out / "expert_review_long.csv", index=False)

    pair_rows = []
    for pair in range(1, 13):
        d = reviews[reviews["Pair"] == pair]
        pair_rows.append({
            "Pair": pair,
            "Domain": PAIR_DOMAINS[pair],
            "N_Experts": int(d["ReviewerCode"].nunique()),
            "I_CVI_RelevanceA": endorsement_rate(d["RelevanceA"]),
            "Mean_RelevanceA": mean_rating(d["RelevanceA"]),
            "ClarityEndorsementA": endorsement_rate(d["ClarityA"]),
            "DistractorEndorsementA": endorsement_rate(d["DistractorA"]),
            "I_CVI_RelevanceB": endorsement_rate(d["RelevanceB"]),
            "Mean_RelevanceB": mean_rating(d["RelevanceB"]),
            "ClarityEndorsementB": endorsement_rate(d["ClarityB"]),
            "DistractorEndorsementB": endorsement_rate(d["DistractorB"]),
            "EquivalenceEndorsement": endorsement_rate(d["Equivalence"]),
            "Mean_Equivalence": mean_rating(d["Equivalence"]),
        })

    pair_stats = pd.DataFrame(pair_rows)
    pair_stats.to_csv(
        args.out / "expert_review_pair_statistics.csv", index=False, float_format="%.4f"
    )

    relevance_values = pd.concat([
        pair_stats["I_CVI_RelevanceA"], pair_stats["I_CVI_RelevanceB"]
    ]).dropna()
    s_cvi_ave = float(relevance_values.mean()) if len(relevance_values) else np.nan

    item_flags = []
    flagged_pairs: set[int] = set()
    for _, row in pair_stats.iterrows():
        pair = int(row["Pair"])
        for form in ["A", "B"]:
            cvi = row[f"I_CVI_Relevance{form}"]
            if pd.notna(cvi) and cvi < 0.78:
                item_flags.append(
                    f"Pair {pair} Form {form}: relevance I-CVI={cvi:.3f} (<0.78)"
                )
                flagged_pairs.add(pair)
        equiv = row["EquivalenceEndorsement"]
        if pd.notna(equiv) and equiv < 0.78:
            item_flags.append(
                f"Pair {pair}: equivalence endorsement={equiv:.3f} (<0.78)"
            )
            flagged_pairs.add(pair)

    summary = pd.DataFrame([{
        "N_Experts": len(reviewers),
        "ReviewerCodes": ";".join(reviewers),
        "S_CVI_Ave_Relevance_24_Items": s_cvi_ave,
        "Mean_Equivalence_Rating_12_Pairs": pair_stats["Mean_Equivalence"].mean(),
        "Pairs_With_Relevance_or_Equivalence_Flag": len(flagged_pairs),
    }])
    summary.to_csv(args.out / "expert_review_summary.csv", index=False, float_format="%.4f")

    notes = [
        "DSP-Lab expert review summary",
        f"Experts included: {len(reviewers)} ({', '.join(reviewers)})",
        "Ratings of 3 or 4 are treated as endorsements.",
        "I-CVI is calculated for item relevance separately for Form A and Form B.",
        "S-CVI/Ave is the mean of the 24 relevance I-CVI values.",
        "Clarity, distractor quality, and A/B equivalence are summarized as endorsement proportions and mean ratings rather than mislabeled as relevance CVIs.",
        "Polit, Beck, and Owen (2007) suggested I-CVI >= 0.78 as evidence of good content validity for three or more experts. With exactly three experts, the possible endorsement proportions mean that this threshold requires unanimous 3/4 ratings.",
        "Do not mechanically delete an item because of one statistic; review the written expert comments and preserve coverage of the five planned DSP domains.",
        "",
        f"S-CVI/Ave (relevance): {s_cvi_ave:.3f}" if pd.notna(s_cvi_ave) else "S-CVI/Ave (relevance): NA",
        "",
        "Items/pairs requiring review:" if item_flags else "No relevance/equivalence flags under the 0.78 screening rule.",
    ]
    notes.extend([f"- {x}" for x in item_flags])
    (args.out / "expert_review_notes.txt").write_text("\n".join(notes) + "\n", encoding="utf-8")

    print(f"Expert-review analysis complete. Results written to: {args.out.resolve()}")


if __name__ == "__main__":
    main()
