# DSP-Lab Teaching-Research Analysis

This folder contains a small reproducible analysis workflow for the DSP-Lab educational study. It is intentionally separate from the Android application so the app can remain frozen during participant data collection.

## Files

- `analyze_study.py` — main effectiveness and engagement analysis.
- `smoke_test_pipeline.py` — synthetic end-to-end check of app export, metadata merge, and manuscript result tables.
- `analyze_pilot.py` — counterbalanced Form A/Form B pilot item analysis.
- `analyze_expert_review.py` — expert content-review summary.
- `sample_size_scenarios.py` — transparent planning scenarios for main-study sample size.
- `requirements.txt` — Python dependencies.
- `templates/study_metadata_template.csv` — group assignment, control-group scores, questionnaire responses, and reflection rubric scores.
- `templates/pilot_item_response_template.csv` — counterbalanced AB/BA item-level response matrix for the pilot.
- `templates/expert_review_template.csv` — one expert's 12-pair rating sheet.
- `templates/main_study_fidelity_log.csv` — weekly implementation/fidelity record.

## 1. Environment

Use Python 3.10 or newer.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r analysis/requirements.txt
```

## 2. Main-study folder structure

A convenient structure is:

```text
data/
  app_exports/
    DSP_Research_S001.csv
    DSP_Research_S002.csv
    ...
  study_metadata.csv
```

Copy each coded research CSV exported by the Android app into `data/app_exports/`.

Create `study_metadata.csv` from `templates/study_metadata_template.csv`.

### Metadata columns

- `ParticipantCode` — must match the study code in the app export.
- `Group` — use exactly `Experimental` or `Control`.
- `PreScore`, `PostScore`, `MaxScore` — optional fallback/manual fields. These are especially useful for control participants who do not have app-export files.
- `Q1`–`Q10` — five-point questionnaire items, normally used for the experimental group.
- `Reflection1`–`Reflection5` — rubric totals (0–12) for the five lab reflections.

Do not put student names, university IDs, email addresses, or other direct identifiers into these files. If a code-to-name key is needed for course administration, store it separately from the research dataset.

## 3. Run the main analysis

```bash
python analysis/analyze_study.py \
  --app-dir data/app_exports \
  --metadata data/study_metadata.csv \
  --out results
```

The script creates:

- `analysis_dataset.csv` — merged analysis dataset;
- `table_descriptives.csv` — descriptive statistics by group;
- `table_within_group_pre_post.csv` — paired pre/post results;
- `table_between_groups.csv` — Welch group comparisons and Cohen's d;
- `table_primary_ancova.csv` — primary ANCOVA/linear regression with HC3 robust standard errors;
- `table_engagement_correlations.csv` — exploratory time/reflection/completion associations;
- `table_questionnaire.csv` — questionnaire item summaries;
- `analysis_summary.txt` — compact analysis status and questionnaire alpha when available.

### Quick pipeline check

Before using real classroom data, run:

```bash
python analysis/smoke_test_pipeline.py
```

This uses synthetic demonstration records only. It verifies the same field layout produced by the app, merges it with a two-group metadata sheet, runs `analyze_study.py`, and checks that the manuscript-oriented result files are produced. It does not create or alter research data.

### Primary manuscript model

The main effectiveness result is based on:

```text
PostScore ~ Group + PreScore
```

`Control` is used as the reference group. The group coefficient therefore estimates the adjusted experimental-minus-control post-test difference.

Treat raw gain and normalized gain as secondary outcomes. The objective concept-test outcome should remain primary in the manuscript.

## 4. Sample-size planning

Use `docs/MAIN_STUDY_GROUPING_AND_SAMPLE_SIZE_DECISION.md` for the publication-oriented allocation hierarchy and practical recruitment target.

The planning helper can be run before recruitment:

```bash
python analysis/sample_size_scenarios.py
```

or with explicit assumptions:

```bash
python analysis/sample_size_scenarios.py \
  --alpha 0.05 \
  --power 0.80 \
  --r2 0.25 \
  --attrition 0.15
```

The script reports a conventional two-independent-groups benchmark and an ANCOVA planning sensitivity. The latter assumes that the pre-test explains the specified fraction of post-test variance; this is a planning assumption, not a guarantee. Do not choose `r2` after inspecting main-study outcomes. If assignment is by intact class, clustering can increase the required sample beyond these student-level calculations.

## 5. Expert-review analysis

Each reviewer completes a separate copy of `templates/expert_review_template.csv`.

Example:

```bash
python analysis/analyze_expert_review.py \
  data/expert_reviews/reviewer1.csv \
  data/expert_reviews/reviewer2.csv \
  data/expert_reviews/reviewer3.csv \
  --out results/expert_review
```

The script summarizes relevance I-CVI, clarity, distractor quality, A/B equivalence, and overall S-CVI/Ave relevance evidence. Written reviewer comments and the revision log remain essential; numerical content-validity indices should not be treated as the sole basis for item decisions.

## 6. Parallel-form pilot analysis

Follow `docs/PILOT_IMPLEMENTATION_PROTOCOL.md`.

The preferred pilot uses the same participants for both forms with approximately half assigned to `AB` and half to `BA`. When assessing Form A/Form B comparability, do not place targeted DSP teaching, answer feedback, or DSP-Lab practice between the two forms.

The pilot CSV must contain:

- `ParticipantCode`;
- `Sequence` — exactly `AB` or `BA`;
- `A1`–`A12` and `B1`–`B12`, coded `1=correct`, `0=incorrect`;
- optional `A_DurationSec`, `B_DurationSec`, unclear-item fields, and notes.

Use one row per pilot participant.

```bash
python analysis/analyze_pilot.py \
  data/pilot_item_responses.csv \
  --out pilot_results
```

The pilot script produces:

- `pilot_participant_scores.csv` — A/B scores and paired differences;
- `pilot_item_statistics.csv` — difficulty and corrected item–total correlation;
- `pilot_form_summary.csv` — form-level descriptives, reliability, paired difference, 95% CI, Cohen's dz, and correlation;
- `pilot_parallel_item_pairs.csv` — paired-item difficulty comparison;
- `pilot_order_sensitivity.csv` — AB/BA sequence sensitivity;
- `pilot_review_flags.txt` — pragmatic screening flags and interpretation notes.

The automated flags are review prompts, not universal psychometric pass/fail standards. In particular, a non-significant paired t test does **not** demonstrate equivalence. Evaluate effect magnitude, confidence intervals, item patterns, expert review, and student wording comments together.

## 7. Reflection scoring

Use `docs/REFLECTION_RUBRIC.md`. Each lab reflection receives four 0–3 dimension scores and a 0–12 total. In the main paper, reflection analysis can remain exploratory or supplementary so that the publication stays focused on the objective learning outcome.

## 8. Questionnaire

Use `docs/STUDENT_QUESTIONNAIRE.md`. Enter responses 1–5 in `Q1`–`Q10`. The script reports item descriptives and Cronbach's alpha when enough complete questionnaire responses are present.

Questionnaire scores are secondary perception outcomes and should not be presented as evidence of learning effectiveness by themselves.

## 9. Before final manuscript analysis

Freeze the app, assessment wording, scoring keys, exclusion rules, and primary statistical plan before examining the final group outcomes. Keep untouched original CSV exports in a read-only archive and perform analysis on copies. Document any data cleaning or protocol deviations.

The publication-oriented sequence is:

```text
Expert review
  -> targeted revision if needed
  -> counterbalanced Form A/Form B pilot
  -> final targeted revision if justified
  -> freeze instruments and app
  -> main two-group study
  -> prespecified primary analysis
```

The analysis scripts improve reproducibility but do not replace statistical judgment.
