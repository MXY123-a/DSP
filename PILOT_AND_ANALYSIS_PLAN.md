# DSP-Lab Pilot and Statistical Analysis Plan

## 1. Purpose

This document defines the minimum instrument-pilot and analysis workflow before the main undergraduate DSP teaching study. The purpose is to collect defensible evidence about the researcher-developed measures without expanding the Android application. The pilot is not the main effectiveness study and should not be used to estimate the instructional effect of DSP-Lab.

## 2. Stage A — Expert review

Recommended reviewers: approximately 3 instructors with experience teaching undergraduate DSP.

Use `EXPERT_REVIEW_PACKET.md` and the expert-review CSV template to review all 12 Form A/Form B item pairs for:

- content relevance;
- wording clarity;
- distractor quality;
- cognitive-level equivalence;
- approximate A/B difficulty equivalence;
- overall coverage of the five DSP domains.

Retain a revision log containing item ID, reviewer comment, action taken, original wording, final wording, and rationale. Analyze ratings with `analysis/analyze_expert_review.py`.

## 3. Stage B — Parallel-form student pilot

### Suggested sample

Recruit approximately 20–30 students who resemble the target population but, if feasible, will not contribute data to the main effectiveness analysis. For a small publication-oriented pilot, 24–30 participants is a practical target because it permits reasonably balanced AB/BA sequences while keeping the workload modest.

### Counterbalanced sequence

The preferred design is a same-participant counterbalanced administration:

- approximately half complete **Form A then Form B (AB)**;
- approximately half complete **Form B then Form A (BA)**.

Assign sequence before testing and record it in `analysis/templates/pilot_item_response_template.csv`.

When the objective is Form A/Form B comparability, do **not** place DSP teaching, answer feedback, app practice, or any other targeted learning intervention between the two forms. Doing so would confound form difficulty with learning. A short neutral break is acceptable.

### Administration

1. Give standardized instructions and an anonymous pilot code.
2. Administer the first assigned form without answer feedback.
3. Record completion time.
4. Provide a short neutral break of about 10–15 minutes.
5. Administer the second form without answer feedback.
6. Record completion time.
7. Ask students to identify unclear item numbers and provide short wording comments.
8. Keep the answer key hidden until both forms are completed.

Use the same room conditions, time limits, calculator policy, and instructions for both sequences.

A separate technical/usability check of the app can be conducted after the two assessment forms or with a different small subset. Do not mix app exposure into the parallel-form comparison.

## 4. Item analysis

For each binary item calculate item difficulty and corrected item–total correlation.

### Item difficulty

`p = number correct / number responding`

Values near 0 indicate difficult items and values near 1 indicate easy items. For this compact instrument, values below approximately 0.20 or above approximately 0.90 should trigger review, particularly if several items are extreme. These are pragmatic screening values, not universal validity cutoffs.

### Item discrimination

Use the corrected item–total correlation as a screening indicator. Values below approximately 0.20 should be reviewed; negative values deserve particular attention for possible ambiguity, miscoding, weak distractors, or construct mismatch. With a 20–30 student pilot, sampling uncertainty is substantial, so items should not be deleted mechanically on the basis of one coefficient.

### Internal consistency

Report KR-20 or Cronbach's alpha for each 12-item form. Because each form intentionally covers five DSP domains with only 12 items, very high internal consistency is not expected and should not be pursued at the expense of content coverage.

## 5. Parallel-form comparability

The primary pilot question is whether Form A and Form B appear sufficiently comparable for the planned pre/post use.

Report:

- Form A and Form B means, SDs, medians, and score ranges;
- mean paired difference `B − A` with a 95% confidence interval;
- paired standardized difference (Cohen's dz);
- Form A/Form B score correlation when estimable;
- item-pair difficulty differences;
- floor/ceiling indicators;
- AB versus BA sequence sensitivity.

Do not interpret a non-significant paired t test as proof that the forms are equivalent. With a small pilot, emphasis should be placed on the magnitude and direction of the mean difference, the confidence interval, item-pair patterns, and expert judgment.

Pragmatic review flags used by the analysis script are:

- absolute overall Form B − Form A mean difference greater than about **1 point on the 12-point scale**;
- absolute paired standardized difference `|dz| > 0.40`;
- paired-item difficulty difference `|pB − pA| > 0.25`;
- item difficulty below 0.20 or above 0.90;
- corrected item–total correlation below 0.20, especially if negative;
- a conspicuous AB/BA sequence difference suggesting order or practice effects.

These thresholds are decision aids rather than formal psychometric standards. A flagged item should be reconsidered together with expert comments and content coverage.

## 6. Pilot decision hierarchy

### Major revision before the main study

Revise before proceeding if any of the following occurs:

- an expert identifies a substantive DSP error or incorrect key;
- one form is consistently more difficult by a practically important margin;
- several matched pairs show large difficulty mismatches in the same direction;
- one or more items show negative discrimination together with clarity/content concerns;
- severe floor or ceiling effects prevent meaningful differentiation;
- a strong sequence effect suggests the pilot administration itself is distorting the comparison.

### Minor revision

A limited wording or distractor revision is reasonable when one isolated item is unusually easy/difficult or students repeatedly identify the same ambiguity. Avoid changing multiple items merely to optimize alpha.

### Freeze

Freeze the assessment for the main study when:

1. no unresolved content/key errors remain;
2. Form A and Form B do not show a clear systematic difficulty imbalance;
3. most items function within a usable difficulty range;
4. no unresolved negative-discrimination item remains;
5. expert review supports content relevance and A/B equivalence;
6. student comments reveal no recurring major wording problem.

Once frozen, do not alter test wording during the main study.

## 7. Separate app technical pilot

The assessment pilot and the app technical pilot serve different purposes. The technical pilot can be small (for example, several representative Android devices) and should verify the complete research path:

`Form A / study setup → five labs → Form B → research dashboard → CSV export`

Check that completion, duration, reflection, pre/post scores, and participant code are exported correctly. Technical test data must not be mixed with main-study participant data.

## 8. Main-study primary analysis

### Primary outcome

Post-test concept score (0–12).

### Preferred model

Use ANCOVA or an equivalent linear regression model:

`PostScore = β0 + β1(Group) + β2(PreScore) + error`

Report the adjusted group effect with 95% confidence interval, p value, and an effect-size measure. The objective learning outcome remains primary; questionnaire perceptions remain secondary.

## 9. Secondary analyses

Keep secondary analysis limited so the paper remains focused:

- descriptive pre/post statistics;
- within-group paired change;
- raw gain;
- normalized gain as a supplementary measure;
- questionnaire item/overall summaries;
- app completion and time-on-task descriptively.

Reflection scores and engagement correlations may be treated as exploratory or supplementary rather than promoted to additional primary research questions.

## 10. Missing data and exclusions

Define rules before inspecting final group outcomes. At minimum:

- participants missing either pre-test or post-test are excluded from the primary complete-case model unless another method is prespecified;
- negative gains are retained;
- implausible app durations are flagged for sensitivity analysis rather than automatically deleted;
- participant flow from invitation to final analysis is retained transparently.

## 11. Manuscript evidence package

For a compact SCI submission, the instrument evidence can be reported briefly in Methods and, if needed, a supplementary table:

- number and expertise of reviewers;
- content-review procedure and any revisions;
- pilot sample and AB/BA administration;
- item difficulty/discrimination summary;
- Form A/Form B mean difference and 95% CI;
- reliability estimates interpreted cautiously;
- final decision to freeze the two forms before the main study.

Do not describe the tests as fully validated unless the collected evidence warrants that statement. A safer description is **researcher-developed parallel concept tests with expert content review and pilot evidence**.

## 12. Final sequence before main data collection

The intended publication-oriented sequence is:

**Expert review → targeted revision only if needed → counterbalanced 20–30 student pilot → inspect item/form evidence → final targeted revision if justified → freeze app and assessments → main two-group study.**

No further app feature expansion is recommended before the pilot and main study.
