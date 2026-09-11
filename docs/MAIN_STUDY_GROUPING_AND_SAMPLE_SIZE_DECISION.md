# Main-Study Grouping and Sample-Size Decision

## Purpose

This document defines a **compact, publication-oriented evaluation design** for the DSP-Lab paper. The paper is not intended to be a large educational trial. Its contribution is deliberately balanced between:

1. **the design and implementation of DSP-Lab as a mobile interactive DSP learning application**, and
2. **an empirical evaluation showing whether the application is educationally useful**.

The evaluation should therefore be credible but proportionate. The project does **not** need a large multi-class trial, multiple control conditions, or an extensive psychometric study in order to support the intended paper.

## 1. Recommended study design for this paper

The preferred practical design is a **two-group pre-test/post-test quasi-experimental study**:

- **Experimental group:** regular DSP teaching + five DSP-Lab after-class activities.
- **Control group:** the same regular DSP teaching + conventional topic-matched review.
- **Pre-test:** Form A.
- **Post-test:** Form B.
- **Primary analysis:** post-test score adjusted for pre-test score.

A very practical implementation is **one intact experimental class and one intact control class**, provided the same instructor, syllabus, teaching sequence, and main course resources are used whenever possible.

This design is sufficient for the present paper because the empirical study is intended to support the educational value of the application, not to establish a definitive causal effect across institutions.

## 2. What is not required

For the present publication scope, the following are **not required** unless they are naturally available:

- individual randomization within each class;
- four or more course sections;
- multiple control conditions;
- crossover designs;
- repeated post-tests;
- long-term retention testing;
- structural equation modelling;
- extensive subgroup analysis;
- large-scale psychometric validation of the 12-item tests;
- complex multilevel modelling with many classes.

Adding these elements would increase workload and could shift the paper away from its intended contribution as an **application-design plus educational-evaluation** paper.

## 3. Minimum controls that should be retained

Even with a compact design, several controls are worth keeping because they directly improve credibility:

- both groups receive the same regular DSP teaching where feasible;
- both groups use the same Form A pre-test and Form B post-test;
- both groups cover the same five DSP topic domains;
- the control group receives conventional review rather than no activity at all;
- pre-test score is included as a baseline covariate in the primary analysis;
- known major implementation deviations are recorded briefly;
- the paper explicitly describes the design as quasi-experimental if intact classes are used.

These are sufficient safeguards for the intended scope. Fidelity documentation should remain lightweight.

## 4. Sample-size target

The sample-size target should be realistic for a course-based engineering-education paper.

### Preferred practical target

**60–100 analyzable students in total** is a reasonable target for this project, ideally with approximately balanced experimental and control groups.

Examples:

- 30 + 30 = 60 analyzable students;
- 35 + 35 = 70;
- 40 + 40 = 80;
- 50 + 50 = 100.

If approximately 10%–15% attrition or incomplete post-test data are expected, recruit somewhat more than the desired analyzable total.

### Stronger but not necessary

If 100–120 or more analyzable students are naturally available, use them. The additional sample improves precision, but the study should not be made operationally more complex merely to reach a large target.

### Smaller samples

A total of roughly 40–60 analyzable students can still support a preliminary educational evaluation, especially when the software contribution is substantial, but confidence intervals will be wider and effect estimates should be interpreted cautiously.

The manuscript should not claim that a non-significant result proves the absence of an educational effect.

## 5. Primary statistical analysis

The main effectiveness analysis remains deliberately simple:

`PostScore ~ Group + PreScore`

with the control group as the reference category.

Report:

- group sample sizes;
- pre-test and post-test mean ± SD;
- adjusted experimental-minus-control post-test difference;
- 95% confidence interval;
- p value;
- one effect-size measure.

This single analysis is sufficient as the main inferential result.

Secondary analyses may include:

- within-group pre/post change;
- raw gain;
- normalized gain;
- experimental-group questionnaire descriptives.

Do not add many secondary hypothesis tests merely to increase the amount of statistical output.

## 6. Recommended manuscript wording

If two intact classes are used, a suitable Methods statement is:

> A quasi-experimental pre-test/post-test design was implemented in two undergraduate DSP course sections. One section used DSP-Lab as the after-class interactive learning support, whereas the comparison section completed topic-matched conventional review activities. Both sections followed the same core instructional sequence. Form A was administered before the intervention and Form B after the five-week intervention period. Post-test performance was compared between groups while adjusting for pre-test score.

A suitable limitation statement is:

> Because intervention condition was implemented at the intact-class level, class membership and treatment condition could not be fully separated. The results should therefore be interpreted as baseline-adjusted comparative evidence rather than as a definitive causal estimate.

This limitation is acceptable for the intended CAE-style application-and-evaluation paper as long as it is stated clearly.

## 7. Publication balance

The final paper should allocate attention approximately as follows:

- **40%–50%:** DSP-Lab motivation, pedagogical design, implementation, five learning modules, interaction design, and representative screenshots/figures;
- **40%–50%:** study design, learning-effect analysis, questionnaire, and interpretation;
- **remaining space:** Introduction, related work, limitations, and conclusion.

The paper should therefore not read like either:

- a software manual with a very small satisfaction survey, or
- a large educational trial in which the application itself is barely described.

The intended contribution is the combination of a technically implemented mobile DSP learning application and credible evidence that it can support conceptual learning.

## 8. Final decision record

Complete before main-study data collection:

| Decision item | Final value |
|---|---|
| Experimental classes | TBD |
| Control classes | TBD |
| Approximate students per group | TBD |
| Target analyzable total | TBD: preferably 60–100 |
| Same instructor across groups? | TBD |
| Same course content/sequence? | TBD |
| Form A / Form B frozen? | TBD |
| APK frozen? | TBD |
| Main-study start date | TBD |

## Publication priority

For this project, **a well-designed application plus one clean, understandable two-group evaluation is more valuable than a complicated experimental design**. The goal is to demonstrate technical/pedagogical innovation and provide credible evidence of educational usefulness without turning the project into a large-scale education-science trial.