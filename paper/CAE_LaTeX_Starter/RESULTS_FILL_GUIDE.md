# Results Fill Guide for the CAE Manuscript

This guide is intentionally minimal. Its purpose is to make the final manuscript easy to complete after the teaching study without expanding the analysis plan.

## 1. Generate the analysis outputs

Run:

```bash
python analysis/analyze_study.py --app-dir data/app_exports --metadata data/study_metadata.csv --out results
```

Keep the raw app exports unchanged. The manuscript can be completed from the generated files below.

## 2. Fill Table 3: learning outcomes

Use `results/table_descriptives.csv`.

For the `Experimental` and `Control` rows, copy the following measures:

- `PreScore`: N, Mean, SD
- `PostScore`: N, Mean, SD
- `RawGain`: Mean, SD

Report scores on the 0--12 scale. Use one decimal place for means/SDs unless the final journal style requires otherwise.

## 3. Fill the primary adjusted group effect

Use `results/table_primary_ancova.csv`.

Locate the row whose term is the experimental-group coefficient from:

`PostScore ~ Group + PreScore`

Report only the quantities needed in the manuscript:

- adjusted Experimental-minus-Control difference = `Estimate`
- 95% CI = `CI95_Lower` to `CI95_Upper`
- p value = `p`

Suggested sentence:

> After adjustment for pre-test score, the DSP-Lab group scored [Estimate] points higher/lower than the control group on the post-test (95% CI [Lower, Upper], p = [p]).

This adjusted difference is the primary effectiveness result.

## 4. Add one standardized effect-size indicator

Use `results/table_between_groups.csv`, row `PostScore`.

Report `CohenD_ExperimentalMinusControl` as an **unadjusted descriptive standardized post-test difference**. Do not describe it as the adjusted ANCOVA effect size.

Suggested sentence:

> The corresponding unadjusted standardized post-test difference was Cohen's d = [d].

## 5. Report the DSP-Lab group's pre/post improvement

Use `results/table_within_group_pre_post.csv`, row `Experimental`.

Use:

- `PreMean`
- `PostMean`
- `MeanChange`
- `p`
- `PairedCohenD`

Suggested sentence:

> Within the DSP-Lab group, the mean score increased from [PreMean] to [PostMean], a mean change of [MeanChange] points (p = [p], paired d = [PairedCohenD]).

This is a secondary within-group result; it should not replace the adjusted between-group comparison.

## 6. Fill the student-experience summary

Use `results/table_questionnaire.csv` and `results/analysis_summary.txt`.

The item labels are:

| Item | Short label |
|---|---|
| Q1 | Perceived learning usefulness |
| Q2 | Visualization usefulness |
| Q3 | Interactivity usefulness |
| Q4 | Content relevance |
| Q5 | Ease of use |
| Q6 | Mobile convenience |
| Q7 | Active learning |
| Q8 | Reflective learning |
| Q9 | Self-directed learning |
| Q10 | Willingness to reuse |

Report:

- questionnaire N;
- overall questionnaire mean if available from `QuestionnaireMean` in `table_descriptives.csv`;
- Cronbach's alpha from `analysis_summary.txt`;
- the highest-rated item and its mean/SD;
- the lowest-rated item and its mean/SD.

The full 10-item table does not need to appear in the main paper unless requested by reviewers; it can be placed in supplementary material if necessary.

## 7. Keep the Discussion narrow

Interpret the learning result first, then use questionnaire findings only as supporting evidence about perceived usefulness and usability. Do not claim that high questionnaire ratings prove learning effectiveness. Do not treat elapsed app time as precise active-learning time.

If the adjusted group effect is not statistically significant, report the estimate and confidence interval directly rather than rewriting the study around secondary correlations or exploratory findings.

## 8. Final manuscript fields that still require manual completion

Before submission, replace all remaining `TBD` fields for:

- institution description;
- experimental/control sample sizes;
- number of expert reviewers;
- ethics approval/exemption and consent statement;
- observed learning results;
- observed questionnaire results;
- data-availability statement.

No additional primary analyses are required for the current paper design.
