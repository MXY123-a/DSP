# Manuscript Methods Draft

## Study design

A quasi-experimental pre-test/post-test control-group design is proposed to evaluate DSP-Lab, an offline mobile-assisted interactive learning tool for undergraduate Digital Signal Processing education. The study compares conventional course instruction supplemented with five short mobile interactive activities against the same conventional instruction supplemented with conventional after-class review materials. DSP-Lab is intended to support self-directed after-class learning and does not replace MATLAB/Python programming laboratories or conventional laboratory teaching.

If random assignment of individual students is feasible, the design can be described as randomized. If intact classes are used, retain the term **quasi-experimental** and report baseline comparability rather than implying random allocation.

## Participants and setting

Participants should be undergraduate students enrolled in a Digital Signal Processing course at the participating institution. Inclusion criteria should be defined before recruitment, for example enrollment in the target course and completion of the pre-test. Exclusion criteria and missing-data rules should be specified before examining final outcomes.

The manuscript should report the number of students invited, consented, allocated to each learning condition, completing the pre-test, completing the intervention, completing the post-test, and included in the final analysis. Relevant course characteristics may include year of study, major, prior DSP exposure, and course format if these variables are ethically collected and analytically justified.

## Learning intervention

The experimental condition uses DSP-Lab as an after-class mobile learning tool. The intervention contains five interactive modules aligned with core undergraduate DSP concepts:

1. discrete-time signals;
2. sampling and aliasing;
3. discrete convolution;
4. the discrete Fourier transform and spectrum;
5. FIR low-pass filtering.

Each activity is designed to require approximately 15–30 minutes. Students manipulate signal-processing parameters, inspect immediate graphical or numerical feedback, compare parameter settings, and submit a short written reflection. The application records completion status, final parameter settings, activity duration, reflection text, and submission time locally on the device. After the study sequence, students export a de-identified CSV using an anonymous participant code.

The control condition receives the same regular lectures, syllabus, learning objectives, core homework, and normal course resources. Instead of DSP-Lab, control participants complete conventional after-class review material covering the same five topic areas. Where feasible, the control activities should be designed to require approximately comparable study time so that the study compares learning-support method rather than simply additional exposure.

## Study procedure

Before the intervention, both groups complete a 12-item concept pre-test (Form A). During the following instructional period, students complete the assigned after-class learning support after the corresponding DSP topic has been taught. The five modules/review activities may be distributed over approximately five weeks.

After completion of the intervention period, both groups complete a parallel 12-item concept post-test (Form B). Experimental-group students also complete a 10-item five-point Likert questionnaire about the DSP-Lab learning experience. Reflection responses generated during the five mobile activities are retained as secondary qualitative/engagement data. Research files are identified by anonymous participant codes rather than student names or university identifiers.

## Concept assessment

Two researcher-developed parallel concept tests are used. Form A serves as the pre-test and Form B as the post-test. Each form contains 12 multiple-choice items spanning five DSP domains: discrete-time signals (2 items), sampling and aliasing (3 items), convolution (2 items), DFT/spectrum (3 items), and FIR filtering (2 items). Each correct answer receives one point, giving a total score from 0 to 12.

The two forms assess the same constructs using different wording and numerical values to reduce direct test-retest recall effects. Before the main study, 2–3 DSP instructors should review the paired items for content relevance, wording clarity, distractor quality, and approximate Form A/Form B equivalence. A pilot sample of approximately 20–30 students, where feasible, should be used to inspect item difficulty, corrected item-total correlations, internal consistency, and overall parallel-form comparability. The tests should be described as researcher-developed rather than previously validated unless stronger validation evidence is obtained.

## Student-experience questionnaire

Experimental-group students complete a 10-item questionnaire using a five-point Likert response scale from 1 (strongly disagree) to 5 (strongly agree). Items address perceived learning usefulness, visualization support, parameter interactivity, content relevance, ease of use, mobile convenience, active learning, reflective learning, self-directed learning, and intention to use similar activities in the future.

Questionnaire results are treated as secondary perception outcomes and are not interpreted as objective evidence of learning effectiveness. Item-level means and standard deviations should be reported. An overall mean and Cronbach's alpha may also be reported with appropriate caution because the questionnaire samples several related constructs.

## Reflection data

Each DSP-Lab module includes one short reflection prompt. Reflection responses are scored using a four-dimension rubric covering conceptual accuracy, use of experimental evidence, causal explanation, and comparison/transfer. Each dimension is rated from 0 to 3, producing a total score from 0 to 12 per activity and an optional total from 0 to 60 across five activities.

A prespecified subset, such as 20–30% of reflections, should be scored independently by two raters. Inter-rater reliability may be reported using weighted Cohen's kappa for ordinal dimension scores or an intraclass correlation coefficient for total scores when appropriate. Disagreements should be used to refine coding rules before one trained rater completes the remaining dataset.

## Learning analytics

For the experimental group, the application records completion status and time on task for each lab. Total time on task is calculated as the sum of available lab durations. These variables are used as secondary indicators of engagement rather than as measures of learning by themselves.

The application also stores the latest submitted reflection for each lab and exports assessment scores, completion status, timing information, and reflection text in a de-identified CSV file. Raw export files should be archived unchanged, with cleaning and coding performed on working copies.

## Outcomes

The **primary outcome** is post-test score adjusted for baseline pre-test score.

Secondary outcomes include:

- raw gain, defined as PostScore − PreScore;
- normalized gain, defined as `(PostScore − PreScore) / (12 − PreScore)` when the denominator is positive;
- within-group pre/post change;
- lab completion rate;
- total and per-lab time on task;
- reflection rubric scores;
- questionnaire item and overall scores;
- correlations between engagement indicators and learning outcomes within the experimental group.

Normalized gain should not be the sole effectiveness endpoint because it can behave poorly for participants with very high pre-test scores.

## Statistical analysis

Descriptive statistics should summarize participant counts and all principal outcome variables. Baseline pre-test scores should be compared descriptively between groups. Within-group pre/post changes may be evaluated using paired-sample tests, while unadjusted between-group comparisons may use Welch's t test when appropriate.

The primary inferential analysis is an ANCOVA-equivalent linear regression model:

`PostScore = β0 + β1(Group) + β2(PreScore) + ε`

with the control group as the reference category. The adjusted group coefficient estimates the experimental-minus-control difference in post-test performance after accounting for baseline score. Report the coefficient, 95% confidence interval, p value, and an appropriate effect-size measure. Robust HC3 standard errors may be used as a sensitivity to heteroskedasticity.

For within-experimental-group exploratory analyses, Pearson and/or Spearman correlations may be used to examine associations of total time on task, reflection score, completion, and questionnaire score with post-test or gain measures. These analyses should be interpreted as associations rather than causal effects.

Assumptions, missingness, floor/ceiling effects, implausible timing values, and influential observations should be inspected before final reporting. If assumptions are seriously violated, a robust or nonparametric sensitivity analysis should be reported rather than silently replacing the prespecified primary model.

## Missing data and analysis population

The primary complete-case analysis should include participants with both pre-test and post-test scores unless another missing-data method is prespecified. Participants should not be excluded because they show negative learning gain. Extremely short or long recorded lab durations should be flagged for sensitivity analysis and investigated before exclusion. A participant-flow summary should report all exclusions and reasons.

## Ethics and data protection

Before recruitment, the research team should obtain the institutional ethics/IRB determination required by the participating university. Because students are a potentially dependent population relative to their instructor, the protocol should explicitly state that research participation or non-participation will not affect grades, access to instruction, or teacher treatment.

The application export should use only anonymous participant codes. Direct identifiers such as names, student numbers, email addresses, and phone numbers should not be included in the research CSV. Any participant-code key should be stored separately with access restricted to authorized research personnel. Published results should use aggregate statistics and de-identified qualitative excerpts.

Insert the final ethics committee name, approval/exemption identifier, approval date, consent procedure, retention period, and data-storage location only after these details are formally established.

## Reproducibility

The Android application version, Git commit SHA, test forms, reflection prompts, analysis scripts, exclusion rules, and statistical plan should be frozen before main-study data collection begins. Analysis should be conducted using the version-controlled scripts in the repository's `analysis/` directory. Any post-start protocol amendment should be documented with its date, reason, and affected participants.

## Suggested manuscript description of the platform

A concise version suitable for the Introduction or Methods is:

> DSP-Lab is an offline Android-based mobile learning tool developed to support after-class self-directed learning in undergraduate Digital Signal Processing courses. The platform provides five interactive concept modules covering discrete-time signals, sampling and aliasing, convolution, the DFT, and FIR filtering. Each module combines rapid parameter manipulation, immediate visualization, guided comparison, and a short written reflection. The platform complements rather than replaces conventional lectures and programming laboratories.