#!/usr/bin/env python3
"""Pilot analysis for DSP-Lab Form A / Form B.

Recommended pilot design:
- Same participants complete both forms.
- Counterbalance order with Sequence = AB or BA.
- Do not provide teaching, answer feedback, or DSP-Lab practice between forms
  when the purpose is to inspect parallel-form comparability.
- A1..A12 and B1..B12 are coded 1=correct, 0=incorrect.

The script reports item difficulty, corrected item-total correlations,
internal consistency, paired form differences with 95% confidence intervals,
parallel-form correlation, floor/ceiling indicators, and a simple order/sequence
sensitivity check. Screening flags are prompts for content review rather than
automatic item-deletion rules.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

A_COLS = [f"A{i}" for i in range(1, 13)]
B_COLS = [f"B{i}" for i in range(1, 13)]
REQUIRED_META = ["ParticipantCode", "Sequence"]


def cronbach_alpha(x: pd.DataFrame) -> float:
    x = x.dropna(axis=0, how="any").astype(float)
    if len(x) < 3 or x.shape[1] < 2:
        return np.nan
    total_var = x.sum(axis=1).var(ddof=1)
    if total_var <= 0:
        return np.nan
    k = x.shape[1]
    return float((k / (k - 1)) * (1 - x.var(axis=0, ddof=1).sum() / total_var))


def ci_mean(values: pd.Series, confidence: float = 0.95) -> tuple[float, float]:
    values = values.dropna().astype(float)
    if len(values) < 2:
        return np.nan, np.nan
    mean = values.mean()
    sem = stats.sem(values)
    if not np.isfinite(sem):
        return np.nan, np.nan
    crit = stats.t.ppf((1 + confidence) / 2, df=len(values) - 1)
    return float(mean - crit * sem), float(mean + crit * sem)


def item_table(x: pd.DataFrame, cols: list[str], form: str) -> pd.DataFrame:
    rows = []
    for col in cols:
        item = x[col]
        total_without = x.drop(columns=[col]).sum(axis=1, min_count=len(cols) - 1)
        pair = pd.concat([item, total_without], axis=1).dropna()
        corr = np.nan
        if (
            len(pair) >= 5
            and pair.iloc[:, 0].nunique() > 1
            and pair.iloc[:, 1].nunique() > 1
        ):
            corr = stats.pearsonr(pair.iloc[:, 0], pair.iloc[:, 1]).statistic

        difficulty = item.mean()
        flags: list[str] = []
        if pd.notna(difficulty) and (difficulty < 0.20 or difficulty > 0.90):
            flags.append("extreme_difficulty")
        if pd.notna(corr) and corr < 0:
            flags.append("negative_discrimination")
        elif pd.notna(corr) and corr < 0.20:
            flags.append("weak_discrimination")

        rows.append(
            {
                "Form": form,
                "Item": col,
                "N": int(item.notna().sum()),
                "Difficulty_p": difficulty,
                "CorrectedItemTotalR": corr,
                "ScreeningFlag": ";".join(flags),
            }
        )
    return pd.DataFrame(rows)


def safe_ttest_rel(a: pd.Series, b: pd.Series) -> tuple[float, float]:
    pair = pd.concat([a, b], axis=1).dropna()
    if len(pair) < 3:
        return np.nan, np.nan
    result = stats.ttest_rel(pair.iloc[:, 0], pair.iloc[:, 1])
    return float(result.statistic), float(result.pvalue)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze counterbalanced DSP-Lab Form A/Form B pilot responses"
    )
    parser.add_argument(
        "input",
        type=Path,
        help="CSV with ParticipantCode, Sequence (AB/BA), A1..A12, B1..B12",
    )
    parser.add_argument("--out", type=Path, default=Path("pilot_results"))
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    required = REQUIRED_META + A_COLS + B_COLS
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing required columns: {', '.join(missing)}")

    if df["ParticipantCode"].isna().any() or (
        df["ParticipantCode"].astype(str).str.strip() == ""
    ).any():
        raise SystemExit("ParticipantCode must be nonblank for every pilot participant")
    if df["ParticipantCode"].astype(str).duplicated().any():
        raise SystemExit("ParticipantCode values must be unique")

    sequence = df["Sequence"].astype(str).str.upper().str.strip()
    invalid_sequence = ~sequence.isin(["AB", "BA"])
    if invalid_sequence.any():
        bad_values = sorted(sequence[invalid_sequence].unique())
        raise SystemExit(
            "Sequence must be AB or BA. Invalid values: " + ", ".join(bad_values)
        )
    df["Sequence"] = sequence

    x = df[A_COLS + B_COLS].apply(pd.to_numeric, errors="coerce")
    invalid = ~x.isin([0, 1]) & x.notna()
    if invalid.any().any():
        bad = list(x.columns[invalid.any(axis=0)])
        raise SystemExit(
            f"Pilot responses must be coded 0/1. Invalid values found in: {', '.join(bad)}"
        )

    args.out.mkdir(parents=True, exist_ok=True)

    A = x[A_COLS]
    B = x[B_COLS]
    score_a = A.sum(axis=1, min_count=12)
    score_b = B.sum(axis=1, min_count=12)

    participant = pd.DataFrame(
        {
            "ParticipantCode": df["ParticipantCode"].astype(str),
            "Sequence": df["Sequence"],
            "FormA": score_a,
            "FormB": score_b,
        }
    )
    participant["BminusA"] = participant["FormB"] - participant["FormA"]
    participant.to_csv(
        args.out / "pilot_participant_scores.csv", index=False, float_format="%.4f"
    )

    items = pd.concat(
        [
            item_table(A, A_COLS, "A"),
            item_table(B, B_COLS, "B"),
        ],
        ignore_index=True,
    )
    items.to_csv(
        args.out / "pilot_item_statistics.csv", index=False, float_format="%.4f"
    )

    complete = participant.dropna(subset=["FormA", "FormB"]).copy()
    alpha_a = cronbach_alpha(A)
    alpha_b = cronbach_alpha(B)

    summary: dict[str, float | int] = {
        "N_Total": int(len(df)),
        "N_Sequence_AB": int((df["Sequence"] == "AB").sum()),
        "N_Sequence_BA": int((df["Sequence"] == "BA").sum()),
        "N_FormA_complete": int(score_a.notna().sum()),
        "N_FormB_complete": int(score_b.notna().sum()),
        "FormA_mean": score_a.mean(),
        "FormA_SD": score_a.std(ddof=1),
        "FormA_median": score_a.median(),
        "FormA_floor_0to2_rate": (score_a <= 2).mean(),
        "FormA_ceiling_10to12_rate": (score_a >= 10).mean(),
        "FormB_mean": score_b.mean(),
        "FormB_SD": score_b.std(ddof=1),
        "FormB_median": score_b.median(),
        "FormB_floor_0to2_rate": (score_b <= 2).mean(),
        "FormB_ceiling_10to12_rate": (score_b >= 10).mean(),
        "Alpha_FormA": alpha_a,
        "Alpha_FormB": alpha_b,
    }

    if len(complete) >= 3:
        diff = complete["BminusA"]
        t, p = safe_ttest_rel(complete["FormB"], complete["FormA"])
        ci_low, ci_high = ci_mean(diff)
        diff_sd = diff.std(ddof=1)
        dz = diff.mean() / diff_sd if pd.notna(diff_sd) and diff_sd > 0 else np.nan

        summary.update(
            {
                "MeanDifference_BminusA": diff.mean(),
                "Difference_SD": diff_sd,
                "Difference_95CI_Low": ci_low,
                "Difference_95CI_High": ci_high,
                "Paired_t": t,
                "Paired_p": p,
                "Cohen_dz_BminusA": dz,
            }
        )

        if complete["FormA"].nunique() > 1 and complete["FormB"].nunique() > 1:
            r, rp = stats.pearsonr(complete["FormA"], complete["FormB"])
            summary["ParallelForm_PearsonR"] = float(r)
            summary["ParallelForm_PearsonP"] = float(rp)

    # Counterbalancing/order sensitivity. The B-A score difference is compared
    # between AB and BA sequences. This is a screening diagnostic, not a formal
    # equivalence test.
    order_rows = []
    for seq in ["AB", "BA"]:
        d = complete.loc[complete["Sequence"] == seq, "BminusA"]
        low, high = ci_mean(d)
        order_rows.append(
            {
                "Sequence": seq,
                "N": int(d.notna().sum()),
                "Mean_BminusA": d.mean(),
                "SD_BminusA": d.std(ddof=1),
                "CI95_Low": low,
                "CI95_High": high,
            }
        )
    order_table = pd.DataFrame(order_rows)
    order_table.to_csv(
        args.out / "pilot_order_sensitivity.csv", index=False, float_format="%.4f"
    )

    ab = complete.loc[complete["Sequence"] == "AB", "BminusA"].dropna()
    ba = complete.loc[complete["Sequence"] == "BA", "BminusA"].dropna()
    if len(ab) >= 3 and len(ba) >= 3:
        order_test = stats.ttest_ind(ab, ba, equal_var=False)
        summary["SequenceDifference_ABminusBA"] = float(ab.mean() - ba.mean())
        summary["Sequence_Welch_t"] = float(order_test.statistic)
        summary["Sequence_Welch_p"] = float(order_test.pvalue)

    # Optional completion-time columns are summarized when present.
    for col in ["A_DurationSec", "B_DurationSec"]:
        if col in df.columns:
            values = pd.to_numeric(df[col], errors="coerce")
            summary[f"{col}_Mean"] = values.mean()
            summary[f"{col}_Median"] = values.median()

    pd.DataFrame([summary]).to_csv(
        args.out / "pilot_form_summary.csv", index=False, float_format="%.4f"
    )

    pair_rows = []
    for i in range(12):
        a = A[A_COLS[i]].mean()
        b = B[B_COLS[i]].mean()
        difference = b - a if pd.notna(a) and pd.notna(b) else np.nan
        pair_rows.append(
            {
                "Pair": i + 1,
                "FormA_Item": A_COLS[i],
                "FormB_Item": B_COLS[i],
                "Difficulty_A": a,
                "Difficulty_B": b,
                "DifficultyDifference_BminusA": difference,
                "AbsoluteDifficultyDifference": abs(difference)
                if pd.notna(difference)
                else np.nan,
                "ScreeningFlag": "pair_difference_gt_0.25"
                if pd.notna(difference) and abs(difference) > 0.25
                else "",
            }
        )
    pair_table = pd.DataFrame(pair_rows)
    pair_table.to_csv(
        args.out / "pilot_parallel_item_pairs.csv", index=False, float_format="%.4f"
    )

    flags: list[str] = []
    item_flags = items.loc[items["ScreeningFlag"].astype(str) != ""]
    for _, row in item_flags.iterrows():
        corr_text = (
            f"{row['CorrectedItemTotalR']:.3f}"
            if pd.notna(row["CorrectedItemTotalR"])
            else "NA"
        )
        flags.append(
            f"{row['Item']}: {row['ScreeningFlag']} "
            f"(p={row['Difficulty_p']:.3f}, r_it={corr_text})"
        )

    pair_flags = pair_table.loc[pair_table["ScreeningFlag"] != ""]
    for _, row in pair_flags.iterrows():
        flags.append(
            f"Pair {int(row['Pair'])}: |pB-pA|={row['AbsoluteDifficultyDifference']:.3f} > 0.25"
        )

    if len(complete) >= 3:
        mean_diff = complete["BminusA"].mean()
        if abs(mean_diff) > 1.0:
            flags.append(
                f"Form-level mean difference is {mean_diff:.3f} points (B-A), "
                "which exceeds the 1-point pragmatic review threshold."
            )
        diff_sd = complete["BminusA"].std(ddof=1)
        if pd.notna(diff_sd) and diff_sd > 0:
            dz = mean_diff / diff_sd
            if abs(dz) > 0.40:
                flags.append(
                    f"Paired standardized form difference |dz|={abs(dz):.3f} > 0.40."
                )

    if len(ab) >= 3 and len(ba) >= 3:
        sequence_gap = ab.mean() - ba.mean()
        if abs(sequence_gap) > 1.0:
            flags.append(
                f"AB versus BA sequence difference in B-A scores is {sequence_gap:.3f} points; "
                "inspect possible order/practice effects."
            )

    notes = [
        "DSP-Lab pilot interpretation notes",
        "",
        "Design:",
        "- Use a counterbalanced AB/BA design when the purpose is to inspect Form A/Form B comparability.",
        "- Do not place DSP teaching, answer feedback, or DSP-Lab practice between the two forms.",
        "- A neutral break is acceptable. Record Sequence for every participant.",
        "",
        "Interpretation:",
        "- Difficulty_p is the proportion answering correctly (0=difficult, 1=easy).",
        "- Items with p < 0.20 or p > 0.90 are flagged for review, not automatic deletion.",
        "- CorrectedItemTotalR < 0.20 is a screening flag; negative values deserve particular review.",
        "- Paired-item |pB-pA| > 0.25 is a pragmatic mismatch flag.",
        "- A form-level absolute mean difference > 1 point (out of 12) or |Cohen dz| > 0.40 triggers review.",
        "- The paired t-test p value is descriptive here. A non-significant p value does NOT prove form equivalence.",
        "- Because each form contains only 12 items across five DSP domains, alpha may be moderate. Do not tune items solely to maximize alpha.",
        "- Use expert-review evidence, pilot statistics, and student clarity comments together.",
        "",
        "Screening flags:",
    ]
    if flags:
        notes.extend([f"- {flag}" for flag in flags])
    else:
        notes.append("- No automatic screening flags under the current pragmatic rules.")

    (args.out / "pilot_review_flags.txt").write_text(
        "\n".join(notes) + "\n", encoding="utf-8"
    )

    print(f"Pilot analysis complete. Results written to: {args.out.resolve()}")


if __name__ == "__main__":
    main()
