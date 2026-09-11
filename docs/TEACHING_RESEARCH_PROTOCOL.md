# DSP-Lab Android V1.0 — Teaching Research Protocol

## 1. Study positioning

DSP-Lab is positioned as a **mobile-assisted, after-class self-learning tool** for undergraduate Digital Signal Processing (DSP) education. It is not intended to replace MATLAB/Python programming laboratories or conventional hardware laboratories. Its role is to support concept exploration through rapid parameter manipulation, visualization, guided investigation, reflection, and lightweight learning analytics.

Suggested paper wording:

> DSP-Lab is an offline mobile-assisted interactive learning tool designed to support after-class self-directed learning in undergraduate DSP courses. The application complements rather than replaces conventional lectures and programming laboratories.

## 2. Instructional intervention

The intervention contains five short interactive activities. A target duration of approximately 15–30 minutes per activity is appropriate for after-class use.

| Lab | Topic | Core learning objective | Main interactive activity | Evidence collected |
|---|---|---|---|---|
| Lab 01 | Discrete-time signals | Explain how amplitude, frequency, phase, and signal type affect a discrete sequence | Change one parameter at a time and compare waveform and quantitative measures | Completion, final parameters, time on task, reflection |
| Lab 02 | Sampling and aliasing | Apply the Nyquist criterion and explain aliasing | Compare safe, boundary, and aliasing cases while changing sampling frequency | Completion, final parameters, time on task, reflection |
| Lab 03 | Discrete convolution | Explain convolution as shifted overlap and sum of products | Predict and verify selected output samples; compare basic and smoothing cases | Completion, selected step/mode, time on task, reflection |
| Lab 04 | DFT and spectrum | Explain frequency-bin spacing, resolution, bin alignment, and spectral leakage | Change N and compare bin-centered and non-bin-centered tones | Completion, N/frequency/sample rate, time on task, reflection |
| Lab 05 | FIR low-pass filter | Explain the effects of cutoff frequency and filter length | Compare short/long filters and different cutoff settings using impulse/frequency responses | Completion, taps/cutoff, time on task, reflection |

## 3. Assessment design

Two parallel 12-item concept tests are used:

- **Form A**: pre-test
- **Form B**: post-test

The forms measure the same five concept domains but use different wording and numerical values to reduce test–retest recall effects. Each item is scored 0/1, producing a total score from 0 to 12.

### 3.1 Blueprint

| Domain | Form A items | Form B items | Number per form | Construct |
|---|---|---|---:|---|
| Discrete-time signals | pre_signal_frequency; pre_signal_amplitude | post_signal_frequency; post_signal_amplitude | 2 | Frequency/amplitude effects |
| Sampling and aliasing | pre_sampling_nyquist; pre_sampling_alias_frequency; pre_sampling_below_nyquist | post_sampling_nyquist; post_sampling_alias_frequency; post_sampling_above_nyquist | 3 | Nyquist criterion and alias interpretation |
| Discrete convolution | pre_convolution_length; pre_convolution_meaning | post_convolution_length; post_convolution_meaning | 2 | Convolution length and mechanism |
| DFT and spectrum | pre_dft_bin_spacing; pre_dft_resolution; pre_dft_leakage | post_dft_bin_spacing; post_dft_resolution; post_dft_leakage | 3 | Bin spacing, resolution, leakage |
| FIR filtering | pre_fir_passband; pre_fir_length | post_fir_passband; post_fir_length | 2 | Passband behavior and tap-length trade-off |
| **Total** | 12 | 12 | **12** | Five DSP concept domains |

### 3.2 Important validation requirement

The two forms are **researcher-developed instruments** and must not be described as validated merely because they are implemented in the app. Before the main study, conduct a small validation process:

1. Ask 2–3 DSP instructors to review content relevance, clarity, and Form A/Form B equivalence.
2. Pilot the tests with approximately 20–30 students who are similar to the target population but are not included in the main analysis, if feasible.
3. Inspect item difficulty (proportion correct) and item discrimination.
4. Report internal consistency with KR-20 or Cronbach's alpha for dichotomous scoring, while recognizing that a short multidomain test may yield only moderate alpha.
5. Examine whether Form A and Form B have comparable mean difficulty in the pilot. Revise clearly mismatched items before the main study.

## 4. Recommended study design

### 4.1 Preferred design

A **quasi-experimental pre-test/post-test control-group design** is recommended.

| Element | Experimental group | Control group |
|---|---|---|
| Regular DSP lectures | Same course/teacher/content | Same course/teacher/content |
| Conventional homework/materials | Same required course materials | Same required course materials |
| Additional after-class activity | DSP-Lab five interactive modules | Conventional review material of comparable content/time |
| Pre-test | Form A | Form A |
| Post-test | Form B | Form B |
| App learning analytics | Completion, time on task, reflections | Not applicable unless a comparable log is collected |
| Perception questionnaire | Recommended | Optional, or use parallel questions about conventional review |

To reduce confounding, the groups should receive the same lectures, syllabus, instructor, assessment schedule, and core homework wherever possible. The main difference should be the after-class learning support condition.

### 4.2 Group assignment

If individual randomization is feasible, use randomized assignment. If intact classes must be used, describe the study explicitly as quasi-experimental and report baseline comparability rather than implying random allocation.

## 5. Research questions and hypotheses

### RQ1 — Learning effectiveness

**RQ1:** Does mobile-assisted after-class DSP learning improve students' conceptual understanding?

- H1a: The experimental group will show a statistically significant increase from pre-test to post-test.
- H1b: After controlling for pre-test score, the experimental group will have a higher post-test score than the control group.

### RQ2 — Learning gain

**RQ2:** Does the DSP-Lab group achieve greater learning gain than the control group?

Normalized gain can be calculated as:

`g = (Post - Pre) / (Max - Pre)`

Use normalized gain as a supplementary outcome rather than the sole primary outcome because it can behave poorly for students with very high pre-test scores.

### RQ3 — Learning behavior

**RQ3:** Within the DSP-Lab group, are learning behaviors associated with learning outcomes?

Candidate variables:

- total time on task;
- number of completed labs;
- per-lab time on task;
- reflection quality score (if coded with a rubric).

Possible hypothesis:

- H3: Greater meaningful engagement with the five learning activities is positively associated with post-test performance or learning gain.

## 6. Primary and secondary outcomes

### Primary outcome

**Post-test score (0–12), adjusted for pre-test score.**

This should be the main effectiveness outcome.

### Secondary outcomes

- raw gain: Post − Pre;
- normalized gain;
- completion rate;
- total and per-lab time on task;
- student perceptions/usability;
- reflection quality or themes.

Avoid defining many primary outcomes after seeing the data.

## 7. Statistical analysis plan

### 7.1 Descriptive statistics

Report for each group:

- N;
- pre-test mean ± SD;
- post-test mean ± SD;
- raw gain mean ± SD;
- normalized gain mean ± SD or median/IQR if strongly skewed;
- completion rate.

### 7.2 Baseline comparability

Compare pre-test distributions descriptively. If intact classes are used, also report relevant baseline variables that are ethically and practically available, such as prior DSP-related course performance, but do not over-collect personal data.

### 7.3 Main group comparison

Preferred primary model:

`PostScore = β0 + β1(Group) + β2(PreScore) + ε`

Use ANCOVA or an equivalent linear regression model with post-test score as the dependent variable, group as the main predictor, and pre-test score as a covariate.

Report:

- adjusted group difference;
- 95% confidence interval;
- p-value;
- effect size where appropriate.

If assumptions are seriously violated, use an appropriate robust/nonparametric sensitivity analysis rather than relying only on a t-test.

### 7.4 Within-group improvement

Use a paired t-test when assumptions are reasonable; otherwise use the Wilcoxon signed-rank test. Treat this as supplementary evidence, not a substitute for the between-group comparison.

### 7.5 Learning gain comparison

Compare raw or normalized gains between groups using an independent-samples t-test when appropriate, with a nonparametric alternative as a sensitivity analysis.

### 7.6 Learning behavior analysis

Within the experimental group, examine associations between time on task and learning outcomes using Pearson correlation if approximately linear/normal or Spearman correlation otherwise.

Do not interpret correlation as causation. Longer time may reflect either engagement or difficulty.

### 7.7 Reflection analysis

A simple rubric is preferable to unrestricted qualitative claims. For example, rate each reflection from 0–2:

- 0: absent/irrelevant;
- 1: describes an observed result but gives limited conceptual explanation;
- 2: correctly links observed behavior to the relevant DSP concept.

For stronger qualitative analysis, two raters can independently code a subset and report inter-rater agreement.

## 8. Suggested perception questionnaire

Use approximately 8–10 five-point Likert items after the intervention. Example constructs:

1. The app helped me understand DSP concepts.
2. Interactive parameter adjustment helped me connect equations with signal behavior.
3. The plots were clear and useful.
4. The activities encouraged me to test predictions rather than only read explanations.
5. The app was easy to use without instructor assistance.
6. The app was convenient for after-class study.
7. The reflection questions helped me think about why the observed results occurred.
8. I would use this type of mobile tool for reviewing other engineering topics.
9. The activity workload was reasonable.
10. Overall, I was satisfied with the learning experience.

If a validated usability scale such as SUS is used, preserve its official item wording and scoring rules instead of mixing or rewriting items while still calling the result SUS.

## 9. Sample-size planning

Do not justify sample size only by a fixed rule such as "50 students is enough." Perform an a priori power analysis based on the primary group effect and the feasible design.

As a rough planning reference, a conventional two-group comparison targeting a medium standardized effect (d ≈ 0.50), α = .05, and power = .80 often requires roughly 64 participants per group. ANCOVA can improve power when pre-test and post-test are correlated, but the final target should be determined with the actual planned analysis and expected attrition.

If only one or two intact classes are available, present the work as a pilot or quasi-experimental study and acknowledge the resulting limitations.

## 10. Suggested study timeline

| Week | Experimental group | Control group | Data |
|---|---|---|---|
| 0 | Consent/information + Form A | Consent/information + Form A | Baseline |
| 1 | Lab 01 after class | Conventional review | Lab 01 log/reflection |
| 2 | Lab 02 after class | Conventional review | Lab 02 log/reflection |
| 3 | Lab 03 after class | Conventional review | Lab 03 log/reflection |
| 4 | Lab 04 after class | Conventional review | Lab 04 log/reflection |
| 5 | Lab 05 after class | Conventional review | Lab 05 log/reflection |
| 5–6 | Form B + questionnaire | Form B | Primary outcome |

This schedule can be shortened or lengthened to match the actual course sequence.

## 11. Data exported by the current app

The V1.0 research workflow is designed to export de-identified records using a participant code rather than a name/student number. The research CSV includes assessment results and the latest lab-level records, including completion, time on task, timestamps, and reflections.

Recommended participant code format: `S001`, `S002`, ...

Maintain the code-to-identity key, if one is needed, separately from exported research data and restrict access according to institutional requirements.

## 12. Ethics and research integrity

Before collecting data for publication:

- follow the institution's ethics/IRB/educational-research review requirements;
- provide appropriate participant information/consent or obtain an approved waiver where applicable;
- ensure course grades are not unfairly affected by research participation;
- avoid collecting names or student IDs in the app export;
- predefine the primary outcome and main analysis before inspecting final group results;
- report exclusions, attrition, missing data, and deviations from the planned protocol transparently.

## 13. Minimal V1.0 freeze criterion

The application can be frozen for the main teaching study once the following have been verified on physical devices:

- Form A contains 12 items and saves the pre-test correctly;
- all five labs can be completed and reflections are saved;
- time-on-task is recorded for each lab;
- Lab 04 plots display completely;
- Form B contains 12 parallel items and saves the post-test correctly;
- Research Dashboard shows 5/5 completion and correct pre/post scores;
- normalized gain is calculated correctly;
- anonymous CSV export opens correctly and preserves quoted reflection text;
- no personally identifying information is required by the app.

After these checks, avoid substantive UI/logic changes during the main study so that all participants receive the same intervention version.

## 14. Methods-section skeleton for the paper

A concise Methods structure can be:

1. **Participants and study design** — course context, groups, inclusion, ethics.
2. **Mobile-assisted learning intervention** — DSP-Lab positioning and five modules.
3. **Learning procedure** — pre-test, five after-class activities, post-test, questionnaire.
4. **Instruments** — Form A/Form B blueprint, expert review/pilot, reflection rubric, perception scale.
5. **Learning analytics** — completion and time-on-task variables exported by the app.
6. **Statistical analysis** — primary ANCOVA/regression, secondary gains, correlations, effect sizes, confidence intervals.

## 15. Recommended main paper claim

The defensible research claim is not that a mobile app replaces a DSP laboratory. The study should test whether a lightweight mobile interactive tool can **support after-class self-directed concept learning** and improve conceptual outcomes when used as a complement to normal DSP teaching.
