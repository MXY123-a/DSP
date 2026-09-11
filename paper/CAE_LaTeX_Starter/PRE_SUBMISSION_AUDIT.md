# CAE Manuscript Pre-Submission Audit

This checklist keeps the DSP-Lab manuscript focused on publication readiness rather than further software expansion. It separates items that can be fixed now from items that must wait for expert review, pilot testing, ethics approval, or the main study.

## A. Manuscript decisions already locked

- Journal target: *Computer Applications in Engineering Education* (CAE).
- Paper type/positioning: empirical engineering-education study, not a software-feature paper.
- Core comparison: DSP-Lab after-class mobile interactive learning versus topic-matched conventional after-class review.
- Primary outcome: Form B post-test concept score (0–12).
- Baseline covariate: Form A pre-test score.
- Primary model: `PostScore ~ Group + PreScore`.
- Control is the reference group.
- Primary report: adjusted group difference, 95% CI, two-sided p value, and effect size.
- Questionnaire: experimental-group perception outcome only; it is not evidence of learning effectiveness.
- Reflection/engagement correlations: exploratory, not additional primary research questions.
- No further Android feature expansion is required before data collection.

## B. Instrument evidence required before main study

### Expert review

Before the main study, record:

- number of DSP instructors who completed review;
- their relevant teaching expertise in non-identifying aggregate form;
- I-CVI/S-CVI or equivalent content-review summary actually obtained;
- item-pair equivalence concerns;
- all substantive revisions in the revision log.

The manuscript must continue to call the measures **researcher-developed parallel concept tests** unless stronger validation evidence is obtained.

### Student pilot

Target approximately 24–30 students if feasible. Use the counterbalanced AB/BA protocol already documented.

Before freezing the forms, inspect:

- Form A and Form B mean/SD;
- mean paired difference and 95% CI;
- Cohen's dz for the paired difference;
- item difficulty;
- corrected item-total correlation;
- paired-item difficulty differences;
- floor/ceiling behavior;
- AB/BA order sensitivity;
- repeated student clarity complaints.

Do not claim equivalence solely because a paired t test is non-significant.

## C. Main-study facts that must replace current TBD markers

The following items cannot be invented and should remain TBD until known:

1. Anonymous institution/context description.
2. Allocation mechanism and number of classes.
3. Total analyzed N and group sizes.
4. Ethics approval/exemption identifier and consent procedure.
5. Final expert-review N.
6. Final pilot N.
7. Participant-flow counts.
8. Pre/post descriptive statistics.
9. Adjusted group effect, 95% CI, p value, and effect size.
10. Questionnaire item summaries and reliability if an overall score is reported.
11. Final Data Availability Statement.
12. Final conclusion based on observed results.

## D. High-priority design risks to resolve before recruitment

### 1. Class-level confounding

If only one intact class is assigned to DSP-Lab and one intact class to control, class membership and intervention cannot be separated statistically. This is acceptable for a modest quasi-experimental paper only if the limitation is stated clearly, but more than one class per condition or a stronger allocation procedure would improve inference if feasible before the study begins.

### 2. Exposure comparability

The control condition should receive the five topic-matched conventional review activities. Record whether activities were actually delivered as planned. Avoid allowing one group substantially more instructor help or study time by design.

### 3. Test contamination

Do not expose main-study participants to answer keys or pilot feedback before their study assessment. Avoid using exact Form A/B items as routine class exercises.

### 4. Instrument changes after study start

Once the main study begins, test wording, keys, lab tasks, control activities, scoring rules, and the primary model should not be changed without a dated protocol amendment.

## E. Statistical reporting guardrails

- Do not select the primary analysis after looking at results.
- Do not exclude negative-gain students.
- Do not replace the primary ANCOVA with gain-score testing because it produces a smaller p value.
- Do not use questionnaire satisfaction as proof of learning effectiveness.
- Do not overinterpret app elapsed duration as active cognitive time.
- Do not promote exploratory engagement/reflection correlations to confirmatory findings post hoc.
- Report confidence intervals and effect magnitude, not p values alone.
- If the primary result is null, retain the prespecified analysis and report uncertainty honestly.

## F. Main-paper scope target

Keep the final paper compact:

- 3 research questions;
- 1 primary learning-effect model;
- 5 DSP modules;
- 1 matched control condition;
- 2 parallel concept forms;
- 1 short experimental-group questionnaire;
- about 3 core tables and 2 figures.

Pilot/item evidence can be summarized in Methods and moved to supplementary material if needed.

## G. Recommended next milestone

Do not add new software features. The next evidence-producing milestone should be:

**complete expert review -> conduct counterbalanced pilot -> make only evidence-justified item revisions -> freeze app/forms/control materials -> document allocation/ethics -> start main study.**
