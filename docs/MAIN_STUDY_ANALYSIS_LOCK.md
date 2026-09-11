# DSP-Lab Main-Study Analysis Lock

## Purpose

This document freezes the minimum analysis decisions for the main quasi-experimental study **before group outcome data are inspected**. It is intended as an internal preregistration-style record for a compact SCI submission, not as an additional research component.

The paper's central question remains narrow:

> Does a five-module mobile interactive after-class DSP intervention produce better conceptual learning outcomes than topic-matched conventional after-class review?

## 1. Primary outcome

The primary outcome is the **Form B post-test concept score**, ranging from 0 to 12.

The pre-test score from Form A is used as the baseline covariate. Questionnaire scores, app time, completion, and reflections are not primary learning outcomes.

## 2. Primary exposure

`Group` has two levels:

- `Experimental`: regular DSP instruction + DSP-Lab after-class activities;
- `Control`: the same regular DSP instruction + topic-matched conventional review activities.

The exact allocation mechanism must be documented before analysis (e.g., intact class assignment or another procedure). Do not describe the design as randomized unless individual or cluster randomization was actually performed.

## 3. Primary analysis set

The primary complete-case analysis includes participants who:

1. belong to one of the two prespecified study groups;
2. have a valid anonymous participant code;
3. have a valid Form A pre-test total score;
4. have a valid Form B post-test total score;
5. meet the study's consent/ethics requirements.

Do not exclude participants merely because they have:

- a negative learning gain;
- a low pre-test or post-test score;
- an unexpectedly small intervention benefit;
- questionnaire responses that are unfavorable;
- app times that appear unusual but are technically possible.

Any exclusion for duplicate records, corrupted data, protocol ineligibility, or impossible values must be documented with counts and reasons before the primary model is reported.

## 4. Primary model

The prespecified primary model is an ANCOVA-equivalent linear regression:

`PostScore = beta0 + beta1(Group) + beta2(PreScore) + error`

The `Control` group is the reference category. Therefore, `beta1` estimates the adjusted experimental-minus-control difference in post-test score.

Report:

- adjusted group coefficient;
- 95% confidence interval;
- two-sided p value;
- group sample sizes;
- adjusted or model-based group means if useful for interpretation;
- an effect-size estimate.

Use HC3 heteroskedasticity-robust standard errors as the primary reported standard-error specification or as a clearly identified robustness specification, consistently with the final analysis script.

The main conclusion should be based on the direction, magnitude, uncertainty, and educational interpretation of the adjusted group effect, not on the p value alone.

## 5. Baseline handling

Pre-test score is included as a covariate rather than testing effectiveness by comparing gain scores alone.

Report pre-test mean and SD by group descriptively. Do not use a non-significant baseline p value as proof that the groups were equivalent.

If the groups are intact classes and only one class represents each condition, explicitly acknowledge that intervention and class membership cannot be completely separated. If feasible before recruitment, using more than one class per condition or an allocation procedure that reduces class-level confounding would strengthen inference; do not redesign the study after seeing outcomes.

## 6. Secondary analyses retained for the paper

To keep the manuscript focused, secondary analyses are limited to:

1. descriptive pre-test and post-test means/SDs by group;
2. within-group paired pre/post change;
3. raw gain (`PostScore - PreScore`);
4. normalized gain where defined, reported as supplementary rather than primary;
5. experimental-group questionnaire summaries;
6. experimental-group completion and time-on-task summaries.

Reflection scores and correlations between engagement indicators and learning outcomes are **exploratory**. They may be omitted from the main manuscript if they do not add a clear interpretation.

## 7. Questionnaire analysis

The 10-item DSP-Lab experience questionnaire is an experimental-group perception measure.

Report item means and SDs. If an overall questionnaire score is used, report its internal consistency and make clear that perceived usefulness/usability does not constitute evidence of learning effectiveness.

No control-group experience questionnaire is required for the current RQ3 because RQ3 concerns students' perceptions of DSP-Lab specifically. If a control questionnaire is later added, it must be justified and documented before outcome analysis rather than introduced post hoc to obtain additional significant results.

## 8. Missing data

The primary analysis is complete-case unless another missing-data method is specified **before** final group outcomes are inspected.

Always report participant flow:

`invited -> consented/eligible -> pre-test -> intervention/review -> post-test -> primary analysis`

Report the number and percentage of missing post-tests by group. If missingness is appreciable or clearly imbalanced, add a sensitivity analysis and discuss attrition as a limitation.

## 9. App duration and completion

App duration is elapsed screen/activity time rather than a validated measure of active cognitive engagement. It should therefore be described as **time-on-task proxy / recorded elapsed activity duration**, not as precise active-learning time.

Primary group-effect conclusions must not depend on removing participants solely because their app duration is short or long. Implausible values can be flagged and examined in sensitivity analysis.

Completion should be reported transparently (e.g., number completing all five modules). A per-protocol analysis, if shown, is supplementary; the paper should not replace the primary analysis with a post hoc high-compliance subgroup because it produces a larger effect.

## 10. Sensitivity checks

Keep sensitivity analyses limited and interpretable. Recommended checks are:

- conventional standard errors versus HC3 robust standard errors;
- primary complete-case analysis versus a justified alternative only if missingness warrants it;
- optional analysis excluding clearly corrupted/impossible duration records without changing pre/post eligibility;
- optional model diagnostic checks for residual behavior and influential observations.

Do not run a large collection of alternative models and selectively report the most favorable result.

## 11. Multiple outcomes and multiplicity

Only one primary learning outcome and one primary group-effect model are prespecified. Secondary and exploratory analyses should be labeled as such.

Because the manuscript is deliberately narrow, formal multiplicity adjustment is not required for the single primary test. Avoid presenting multiple secondary p values as independent confirmatory evidence.

## 12. Effect reporting

For the primary result, report at minimum:

`adjusted group difference + 95% CI + p value + effect size`

For paired within-group change, report mean change, 95% CI, and an appropriate paired effect size if included.

Interpret effect size in the course context. Avoid converting a statistically significant result into a claim of large educational importance without considering the 0–12 score scale and confidence interval.

## 13. Main manuscript tables and figures

The target paper should remain compact:

- **Table 1:** participant flow/baseline and group sizes;
- **Table 2:** learning outcomes and adjusted group effect;
- **Table 3:** DSP-Lab questionnaire/perception summary (experimental group);
- **Figure 1:** study/intervention flow;
- **Figure 2:** DSP-Lab learning cycle or final pre/post visualization.

Pilot/item evidence can be summarized briefly in Methods and moved to supplementary material if space is tight.

## 14. Interpretation boundaries

If the adjusted experimental-group post-test score is higher, the safest interpretation is that DSP-Lab **was associated with / produced higher adjusted post-test performance under the implemented quasi-experimental design**, depending on the actual allocation procedure.

Do not claim that:

- mobile learning is universally superior;
- each individual DSP-Lab feature caused the effect;
- the study proves long-term retention unless retention is measured;
- the intervention replaces conventional DSP laboratories or programming;
- the results generalize beyond comparable undergraduate DSP contexts without qualification.

If the primary result is null, retain the same analysis and report the confidence interval. Do not redefine the primary outcome around whichever secondary metric becomes significant.

## 15. Freeze point

Before main-study outcome data are examined, record and preserve:

- final app version / commit;
- final Form A and Form B wording and keys;
- expert-review and pilot revision history;
- allocation mechanism;
- eligibility/exclusion rules;
- primary model;
- planned secondary analyses;
- questionnaire scoring rule;
- data-cleaning rules.

After this point, any substantive change should be documented as a protocol deviation or amendment with a date and rationale.

## 16. Publication-oriented decision

The main study should remain centered on **one objective learning-effect comparison**. The app, reflection data, engagement variables, and questionnaire exist to support interpretation and reproducibility; they should not turn the paper into several loosely connected studies.
