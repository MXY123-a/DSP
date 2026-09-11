#!/usr/bin/env python3
"""DSP-Lab teaching-study analysis.

Combines anonymous CSV files exported by the Android app with optional study
metadata, then generates manuscript-oriented result tables.

Example:
    python analyze_study.py --app-dir data/app_exports \
        --metadata data/study_metadata.csv --out results

The metadata file may contain control-group participants who do not have an app
export. For duplicated fields, non-empty values from app exports are preferred;
metadata values are used as fallbacks.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf


QUESTIONNAIRE_COLS = [f"Q{i}" for i in range(1, 11)]
REFLECTION_SCORE_COLS = [f"Reflection{i}" for i in range(1, 6)]
DURATION_COLS = [f"Lab{i}DurationSec" for i in range(1, 6)]
COMPLETION_COLS = [f"Lab{i}Completed" for i in range(1, 6)]


def read_csv_safe(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype={"ParticipantCode": "string"})


def load_app_exports(app_dir: Path | None) -> pd.DataFrame:
    if app_dir is None or not app_dir.exists():
        return pd.DataFrame()
    frames = []
    for path in sorted(app_dir.glob("*.csv")):
        try:
            df = read_csv_safe(path)
            if "ParticipantCode" not in df.columns:
                warnings.warn(f"Skipping {path.name}: no ParticipantCode column")
                continue
            frames.append(df)
        except Exception as exc:
            warnings.warn(f"Skipping {path.name}: {exc}")
    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames, ignore_index=True)
    out["ParticipantCode"] = out["ParticipantCode"].astype("string").str.strip()
    # Keep the last exported row when the same anonymous code appears repeatedly.
    return out.drop_duplicates("ParticipantCode", keep="last")


def merge_sources(app: pd.DataFrame, metadata: pd.DataFrame | None) -> pd.DataFrame:
    if metadata is None or metadata.empty:
        return app.copy()
    meta = metadata.copy()
    meta["ParticipantCode"] = meta["ParticipantCode"].astype("string").str.strip()
    meta = meta.drop_duplicates("ParticipantCode", keep="last")
    if app.empty:
        return meta

    merged = meta.merge(app, on="ParticipantCode", how="outer", suffixes=("_meta", "_app"))
    all_base_names = set()
    for col in merged.columns:
        if col.endswith("_meta"):
            all_base_names.add(col[:-5])
        elif col.endswith("_app"):
            all_base_names.add(col[:-4])

    for base in sorted(all_base_names):
        app_col = f"{base}_app"
        meta_col = f"{base}_meta"
        if app_col in merged.columns and meta_col in merged.columns:
            merged[base] = merged[app_col].combine_first(merged[meta_col])
            merged.drop(columns=[app_col, meta_col], inplace=True)
        elif app_col in merged.columns:
            merged.rename(columns={app_col: base}, inplace=True)
        elif meta_col in merged.columns:
            merged.rename(columns={meta_col: base}, inplace=True)
    return merged


def numericize(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    numeric_cols = [
        "PreScore", "PostScore", "MaxScore", "NormalizedGain", "LabsCompleted",
        *QUESTIONNAIRE_COLS, *REFLECTION_SCORE_COLS, *DURATION_COLS,
        *COMPLETION_COLS,
    ]
    for col in numeric_cols:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")

    if "MaxScore" not in out.columns:
        out["MaxScore"] = 12.0
    out["MaxScore"] = out["MaxScore"].fillna(12.0)

    if {"PreScore", "PostScore"}.issubset(out.columns):
        out["RawGain"] = out["PostScore"] - out["PreScore"]
        denom = out["MaxScore"] - out["PreScore"]
        out["NormalizedGainCalc"] = np.where(
            denom > 0, (out["PostScore"] - out["PreScore"]) / denom, np.nan
        )

    present_durations = [c for c in DURATION_COLS if c in out.columns]
    if present_durations:
        out["TotalLabDurationSec"] = out[present_durations].sum(axis=1, min_count=1)
        out["TotalLabDurationMin"] = out["TotalLabDurationSec"] / 60.0

    present_reflections = [c for c in REFLECTION_SCORE_COLS if c in out.columns]
    if present_reflections:
        out["ReflectionTotal"] = out[present_reflections].sum(axis=1, min_count=1)

    present_q = [c for c in QUESTIONNAIRE_COLS if c in out.columns]
    if present_q:
        out["QuestionnaireMean"] = out[present_q].mean(axis=1)

    if "Group" in out.columns:
        out["Group"] = out["Group"].astype("string").str.strip().str.title()
    return out


def cronbach_alpha(items: pd.DataFrame) -> float:
    x = items.dropna(axis=0, how="any").astype(float)
    if x.shape[0] < 3 or x.shape[1] < 2:
        return np.nan
    item_vars = x.var(axis=0, ddof=1).sum()
    total_var = x.sum(axis=1).var(ddof=1)
    if total_var <= 0:
        return np.nan
    k = x.shape[1]
    return float((k / (k - 1)) * (1 - item_vars / total_var))


def cohen_d_independent(a: pd.Series, b: pd.Series) -> float:
    a = a.dropna().astype(float)
    b = b.dropna().astype(float)
    if len(a) < 2 or len(b) < 2:
        return np.nan
    va, vb = a.var(ddof=1), b.var(ddof=1)
    pooled = np.sqrt(((len(a) - 1) * va + (len(b) - 1) * vb) / (len(a) + len(b) - 2))
    return float((a.mean() - b.mean()) / pooled) if pooled > 0 else np.nan


def cohen_d_paired(pre: pd.Series, post: pd.Series) -> float:
    pair = pd.concat([pre, post], axis=1).dropna()
    if len(pair) < 2:
        return np.nan
    diff = pair.iloc[:, 1] - pair.iloc[:, 0]
    sd = diff.std(ddof=1)
    return float(diff.mean() / sd) if sd > 0 else np.nan


def descriptive_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    measures = [
        "PreScore", "PostScore", "RawGain", "NormalizedGainCalc",
        "TotalLabDurationMin", "ReflectionTotal", "QuestionnaireMean",
    ]
    groups = ["All"]
    if "Group" in df.columns:
        groups += [str(g) for g in sorted(df["Group"].dropna().unique())]

    for group in groups:
        sub = df if group == "All" else df[df["Group"] == group]
        for measure in measures:
            if measure not in sub.columns:
                continue
            s = pd.to_numeric(sub[measure], errors="coerce").dropna()
            if s.empty:
                continue
            rows.append({
                "Group": group,
                "Measure": measure,
                "N": len(s),
                "Mean": s.mean(),
                "SD": s.std(ddof=1),
                "Median": s.median(),
                "Min": s.min(),
                "Max": s.max(),
            })
    return pd.DataFrame(rows)


def paired_results(df: pd.DataFrame) -> pd.DataFrame:
    if not {"PreScore", "PostScore"}.issubset(df.columns):
        return pd.DataFrame()
    rows = []
    groups = ["All"]
    if "Group" in df.columns:
        groups += [str(g) for g in sorted(df["Group"].dropna().unique())]
    for group in groups:
        sub = df if group == "All" else df[df["Group"] == group]
        pair = sub[["PreScore", "PostScore"]].dropna()
        if len(pair) < 2:
            continue
        t, p = stats.ttest_rel(pair["PostScore"], pair["PreScore"])
        rows.append({
            "Group": group,
            "N": len(pair),
            "PreMean": pair["PreScore"].mean(),
            "PostMean": pair["PostScore"].mean(),
            "MeanChange": (pair["PostScore"] - pair["PreScore"]).mean(),
            "t": t,
            "p": p,
            "PairedCohenD": cohen_d_paired(pair["PreScore"], pair["PostScore"]),
        })
    return pd.DataFrame(rows)


def between_group_results(df: pd.DataFrame) -> pd.DataFrame:
    if "Group" not in df.columns:
        return pd.DataFrame()
    exp = df[df["Group"] == "Experimental"]
    ctl = df[df["Group"] == "Control"]
    rows = []
    for measure in ["PreScore", "PostScore", "RawGain", "NormalizedGainCalc"]:
        if measure not in df.columns:
            continue
        a = pd.to_numeric(exp[measure], errors="coerce").dropna()
        b = pd.to_numeric(ctl[measure], errors="coerce").dropna()
        if len(a) < 2 or len(b) < 2:
            continue
        t, p = stats.ttest_ind(a, b, equal_var=False)
        rows.append({
            "Measure": measure,
            "ExperimentalN": len(a),
            "ExperimentalMean": a.mean(),
            "ControlN": len(b),
            "ControlMean": b.mean(),
            "WelchT": t,
            "p": p,
            "CohenD_ExperimentalMinusControl": cohen_d_independent(a, b),
        })
    return pd.DataFrame(rows)


def ancova_table(df: pd.DataFrame) -> pd.DataFrame:
    needed = {"Group", "PreScore", "PostScore"}
    if not needed.issubset(df.columns):
        return pd.DataFrame()
    sub = df[list(needed)].dropna().copy()
    if sub["Group"].nunique() != 2 or len(sub) < 8:
        return pd.DataFrame()
    # Force Control as the reference category when present.
    formula = "PostScore ~ C(Group, Treatment(reference='Control')) + PreScore"
    try:
        model = smf.ols(formula, data=sub).fit(cov_type="HC3")
    except Exception as exc:
        warnings.warn(f"ANCOVA could not be fit: {exc}")
        return pd.DataFrame()
    ci = model.conf_int()
    rows = []
    for term in model.params.index:
        rows.append({
            "Term": term,
            "Estimate": model.params[term],
            "SE_HC3": model.bse[term],
            "CI95_Lower": ci.loc[term, 0],
            "CI95_Upper": ci.loc[term, 1],
            "t": model.tvalues[term],
            "p": model.pvalues[term],
            "N": int(model.nobs),
            "R2": model.rsquared,
            "AdjustedR2": model.rsquared_adj,
        })
    return pd.DataFrame(rows)


def engagement_correlations(df: pd.DataFrame) -> pd.DataFrame:
    sub = df[df["Group"] == "Experimental"].copy() if "Group" in df.columns else df.copy()
    outcomes = [c for c in ["PostScore", "RawGain", "NormalizedGainCalc"] if c in sub.columns]
    predictors = [c for c in ["TotalLabDurationMin", "ReflectionTotal", "LabsCompleted", "QuestionnaireMean"] if c in sub.columns]
    rows = []
    for predictor in predictors:
        for outcome in outcomes:
            pair = sub[[predictor, outcome]].dropna()
            if len(pair) < 5 or pair[predictor].nunique() < 2 or pair[outcome].nunique() < 2:
                continue
            r, p_r = stats.pearsonr(pair[predictor], pair[outcome])
            rho, p_s = stats.spearmanr(pair[predictor], pair[outcome])
            rows.append({
                "Predictor": predictor,
                "Outcome": outcome,
                "N": len(pair),
                "PearsonR": r,
                "PearsonP": p_r,
                "SpearmanRho": rho,
                "SpearmanP": p_s,
            })
    return pd.DataFrame(rows)


def questionnaire_summary(df: pd.DataFrame) -> tuple[pd.DataFrame, float]:
    cols = [c for c in QUESTIONNAIRE_COLS if c in df.columns]
    if not cols:
        return pd.DataFrame(), np.nan
    sub = df[df["Group"] == "Experimental"].copy() if "Group" in df.columns else df.copy()
    rows = []
    for col in cols:
        s = pd.to_numeric(sub[col], errors="coerce").dropna()
        if not s.empty:
            rows.append({"Item": col, "N": len(s), "Mean": s.mean(), "SD": s.std(ddof=1), "Median": s.median()})
    alpha = cronbach_alpha(sub[cols].apply(pd.to_numeric, errors="coerce"))
    return pd.DataFrame(rows), alpha


def write_table(df: pd.DataFrame, path: Path) -> None:
    if df.empty:
        return
    df.to_csv(path, index=False, float_format="%.4f")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze DSP-Lab teaching-study data")
    parser.add_argument("--app-dir", type=Path, default=None, help="Directory containing app-exported CSV files")
    parser.add_argument("--metadata", type=Path, default=None, help="Optional study_metadata.csv")
    parser.add_argument("--out", type=Path, default=Path("results"), help="Output directory")
    args = parser.parse_args()

    app = load_app_exports(args.app_dir)
    metadata = read_csv_safe(args.metadata) if args.metadata and args.metadata.exists() else None
    data = numericize(merge_sources(app, metadata))
    if data.empty:
        raise SystemExit("No analyzable data found. Provide --app-dir and/or --metadata.")
    if "ParticipantCode" not in data.columns:
        raise SystemExit("ParticipantCode is required.")

    args.out.mkdir(parents=True, exist_ok=True)
    data.to_csv(args.out / "analysis_dataset.csv", index=False)

    write_table(descriptive_table(data), args.out / "table_descriptives.csv")
    write_table(paired_results(data), args.out / "table_within_group_pre_post.csv")
    write_table(between_group_results(data), args.out / "table_between_groups.csv")
    write_table(ancova_table(data), args.out / "table_primary_ancova.csv")
    write_table(engagement_correlations(data), args.out / "table_engagement_correlations.csv")

    q_table, alpha = questionnaire_summary(data)
    write_table(q_table, args.out / "table_questionnaire.csv")

    summary_lines = [
        "DSP-Lab teaching-study analysis summary",
        f"Participants in merged dataset: {len(data)}",
    ]
    if "Group" in data.columns:
        for group, n in data["Group"].value_counts(dropna=False).items():
            summary_lines.append(f"Group {group}: {n}")
    if not np.isnan(alpha):
        summary_lines.append(f"Questionnaire Cronbach alpha: {alpha:.3f}")
    summary_lines.append("Primary inferential result: see table_primary_ancova.csv")
    summary_lines.append("Interpret p-values together with confidence intervals and effect sizes; do not treat statistical significance alone as educational importance.")
    (args.out / "analysis_summary.txt").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    print(f"Analysis complete. Results written to: {args.out.resolve()}")


if __name__ == "__main__":
    main()
