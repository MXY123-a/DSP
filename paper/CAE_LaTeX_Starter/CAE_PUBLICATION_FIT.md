# CAE publication-fit note for DSP-Lab

Last checked: 2026-09-11

Target journal: **Computer Applications in Engineering Education (CAE), Wiley**

This is an internal submission-strategy note. It should not be included in the manuscript.

## 1. Scope fit

CAE's current author guidance explicitly welcomes work on educational software, technology-based modules in engineering curricula, virtual/real laboratory tools, distance learning, visualization, and assessment of technology-supported implementation. DSP-Lab therefore fits the journal scope well **provided the paper is framed as an evaluated engineering-education intervention rather than an Android software-development report**.

The journal's recent content also shows continued interest in virtual experiments, interactive learning systems, visualization, and technology-enhanced engineering pedagogy. This increases topical fit but also raises the novelty bar: simply implementing an Android application is not sufficient as the main contribution.

## 2. Defensible manuscript contribution

The paper should consistently foreground this contribution:

> A compact, after-class mobile interactive intervention for five core DSP concepts is evaluated against topic-matched conventional review using parallel concept tests and a prespecified baseline-adjusted group comparison.

The contribution is **not**:

- the first interactive DSP teaching tool;
- the first mobile/Android DSP environment;
- the first use of visualization in DSP education;
- the first comparison of DSP instructional software with conventional teaching.

Those precedents already exist and are cited in the manuscript.

## 3. Why the present study can still be publishable

The publication value comes from the combination of four design choices:

1. **Narrow instructional positioning:** short after-class conceptual exploration rather than a claim to replace laboratories or programming.
2. **Matched active control:** the control group receives topic-matched conventional review rather than no extra study.
3. **Parallel concept assessment:** Form A and Form B target the same DSP domains while reducing direct test-retest recall.
4. **Baseline-adjusted primary analysis:** post-test performance is compared between groups while controlling pre-test score; effect estimates and confidence intervals are prioritized over significance alone.

Together, these choices make the work an empirical engineering-education study rather than a feature demonstration.

## 4. Editorial-risk check

### Main risk A: “This is only another educational app.”

**Mitigation:** minimize Android implementation detail; emphasize the learning cycle, matched comparison, parallel assessment, and objective learning outcome.

### Main risk B: “Prior mobile DSP tools already exist.”

**Mitigation:** explicitly cite AJDSP and avoid first-of-kind language. Differentiate DSP-Lab by its after-class self-directed positioning and evaluation design.

### Main risk C: “The observed effect could simply reflect extra study time.”

**Mitigation:** retain the structured topic-matched control activities and report intended/observed study exposure as transparently as possible.

### Main risk D: “The concept test is researcher-developed.”

**Mitigation:** complete expert review and a small pilot before the main study; report item difficulty, discrimination/internal consistency, and Form A/B comparability without calling the instrument validated beyond the obtained evidence.

### Main risk E: “Questionnaire satisfaction is being treated as effectiveness.”

**Mitigation:** keep questionnaire results secondary. The primary effectiveness evidence must come from the baseline-adjusted concept-test comparison.

### Main risk F: “Quasi-experimental design cannot support strong causal claims.”

**Mitigation:** state the allocation mechanism accurately, report baseline balance, use pre-test adjustment, and use cautious language such as “associated with” or “produced higher adjusted post-test scores” rather than universal causal claims when random assignment is absent.

## 5. Manuscript emphasis by section

- **Title:** intervention + DSP + quasi-experimental evaluation; avoid “novel Android system.”
- **Abstract:** problem, intervention, matched control, parallel assessment, primary adjusted result, concise implication.
- **Introduction:** establish direct DSP predecessors first; then define the remaining evaluation gap precisely.
- **Related Work:** keep compact and claim-accurate; do not turn the paper into a broad mobile-learning review.
- **System section:** explain only features needed to understand the instructional mechanism and reproducibility.
- **Methods:** strongest section before data collection; give enough detail for replication.
- **Results:** objective learning outcome first, perceptions second.
- **Discussion:** interpret the adjusted group effect and avoid attributing any effect to a single mechanism unless directly measured.

## 6. Evidence threshold before submission

Minimum evidence package recommended for a competitive CAE submission:

- expert review of Form A/Form B;
- pilot evidence that the two forms are usable and approximately comparable;
- two-group pre/post implementation with documented participant flow;
- primary ANCOVA-equivalent/baseline-adjusted model;
- adjusted group estimate, 95% CI, p value, and effect size;
- transparent attrition/missing-data reporting;
- questionnaire reliability if an overall questionnaire score is reported;
- concise fidelity/completion information;
- ethics/consent statement appropriate to the institution.

## 7. Current decision

**Keep CAE as the primary target.** The project has a good scope match, but publication probability will depend far more on the quality of the student-study evidence than on additional software development. No further APP feature expansion is recommended before pilot and main data collection.
