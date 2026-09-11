# Publication Scope Balance: App Design + Educational Effect

## Core decision

The manuscript should give **approximately equal weight to DSP-Lab itself and to its educational evaluation**.

The paper is therefore positioned as an **application-design and educational-evaluation paper**, not as a pure software paper and not as a large educational randomized trial.

## Recommended paper identity

A suitable working title is:

> **DSP-Lab: Design and Educational Evaluation of a Mobile Interactive Learning Application for Undergraduate Digital Signal Processing**

Alternative:

> **DSP-Lab: A Mobile Interactive Learning Application for Undergraduate Digital Signal Processing and Its Educational Evaluation**

These titles better reflect the intended 50/50 balance than a title centered only on quasi-experimental evaluation.

## Contribution structure

The manuscript should emphasize three contributions:

1. **Application contribution** — a lightweight Android learning application for five core undergraduate DSP topics, designed for short after-class self-directed exploration.
2. **Pedagogical interaction contribution** — a consistent predict–manipulate–observe–compare–explain learning cycle combining parameter manipulation, immediate waveform/spectrum/filter-response feedback, and short reflection.
3. **Evaluation contribution** — a compact pre-test/post-test comparison showing whether students using DSP-Lab demonstrate stronger conceptual learning than students using conventional topic-matched review.

The novelty claim should be modest and defensible. Do not claim that DSP-Lab is the first mobile DSP application. The innovation lies in the **specific integration of compact mobile delivery, five concept-focused modules, guided interactive visualization, and a directly linked educational evaluation**.

## Suggested manuscript balance

### Part A — DSP-Lab design and implementation: about 40%–50%

Include:

- instructional problem and design goals;
- why mobile after-class use is appropriate;
- application architecture at a high level;
- offline/local-data design;
- five modules and their learning objectives;
- interaction flow;
- representative screenshots;
- examples showing how parameter changes alter signals/spectra/filter responses;
- research-data export only as a supporting implementation feature.

Do not spend many pages on Android boilerplate, package structure, or routine UI code.

### Part B — Educational evaluation: about 40%–50%

Include:

- participants and course context;
- experimental vs conventional-review group;
- Form A/Form B concept test;
- five-week procedure;
- one primary baseline-adjusted comparison;
- descriptive pre/post outcomes;
- experimental-group questionnaire;
- concise limitations.

Avoid adding multiple control groups or many exploratory models.

## Minimum evaluation design

For the intended paper, the following is enough:

`Form A pre-test -> five-week DSP-Lab / conventional review -> Form B post-test`

Primary model:

`PostScore ~ Group + PreScore`

A single experimental group and a single comparison group are sufficient if implementation is described transparently.

## Figures that matter most

Keep the figure set focused. A strong paper can use roughly four main figures:

1. **Study / system overview** — where DSP-Lab sits in the undergraduate learning process.
2. **Representative DSP-Lab screenshots** — preferably a compact multi-panel figure showing 3–5 modules rather than many separate screenshots.
3. **Predict–manipulate–observe–compare–explain interaction cycle**.
4. **Learning outcome figure** — pre/post or adjusted post-test comparison after real data are collected.

The manuscript does not need several flowcharts describing research administration.

## Tables that matter most

A compact final paper can use:

- Table 1: five DSP-Lab modules, objectives, and interactive functions;
- Table 2: participant/group characteristics and pre/post scores;
- Table 3: primary adjusted effect and, if useful, questionnaire summary.

Detailed test-item diagnostics can remain in supplementary material.

## Scope limits

Do not expand the main paper into:

- a psychometric validation study;
- a multi-arm trial;
- a learning-analytics paper;
- a qualitative reflection study;
- an AI tutoring paper;
- a cloud-platform/software-engineering paper.

The current five labs are enough.

## Final publication message

The manuscript should ultimately communicate one simple story:

> DSP-Lab is a compact, mobile interactive learning application that makes key DSP relationships directly explorable through parameter manipulation and immediate visualization; a course-based evaluation provides evidence that this design can support students’ conceptual learning compared with conventional after-class review.

That claim is sufficiently focused to show innovation without requiring an oversized experimental design.