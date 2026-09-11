# Main-Study Intervention Freeze Protocol

## Purpose

This document defines the **final five-week intervention structure that should be frozen before main-study recruitment**. Its purpose is publication quality control: the experimental and control conditions should remain aligned in topic coverage and expected study exposure while preserving the intended treatment contrast of mobile parameter manipulation and immediate dynamic visualization.

This is not a new intervention and does not expand the Android app. It operationalizes the study design already described in `STUDY_IMPLEMENTATION_GUIDE.md` and `control_group/ALIGNMENT_MATRIX.md`.

## 1. Core contrast to preserve

Both groups receive the same regular DSP teaching. The intended difference is only the after-class learning-support method.

**Experimental condition**

`structured concept task + direct parameter manipulation + immediate dynamic visualization + guided comparison + app-based reflection`

**Control condition**

`structured conventional review + worked example + written practice + compare/explain task + short written summary`

The control group must not receive another interactive simulator, MATLAB/Python parameter-sweep task, interactive website, or prerecorded dynamic parameter demonstration during the intervention window, because these would reproduce the defining affordances of DSP-Lab.

## 2. Five-week frozen intervention map

| Week | Shared topic / learning objective | Experimental activity | Control activity | Intended time | Defining treatment contrast |
|---|---|---|---|---|---|
| 1 | Discrete-time signals: explain effects of amplitude, frequency, phase, and signal type | `LAB01_SIGNALS` in DSP-Lab | `docs/control_group/LAB01_SIGNALS_REVIEW.md` | 15–25 min | direct signal-parameter manipulation and immediate waveform feedback |
| 2 | Sampling and aliasing: apply Nyquist criterion and explain aliasing | `LAB02_SAMPLING` in DSP-Lab | `docs/control_group/LAB02_SAMPLING_REVIEW.md` | 20–30 min | interactive safe/boundary/alias cases with immediate feedback |
| 3 | Convolution: explain shifted overlap, multiplication, summation, and output length | `LAB03_CONVOLUTION` in DSP-Lab | `docs/control_group/LAB03_CONVOLUTION_REVIEW.md` | 20–30 min | interactive stepwise exploration versus written calculation |
| 4 | DFT and spectrum: explain bin spacing, DFT length, alignment, and leakage | `LAB04_DFT` in DSP-Lab | `docs/control_group/LAB04_DFT_REVIEW.md` | 20–30 min | immediate spectrum response to parameter changes |
| 5 | FIR low-pass filtering: explain cutoff and tap-count trade-offs | `LAB05_FIR` in DSP-Lab | `docs/control_group/LAB05_FIR_REVIEW.md` | 20–30 min | interactive impulse/frequency-response visualization |

The instructor key for the control materials is `docs/control_group/INSTRUCTOR_KEY.md`. It should remain instructor-only during the relevant activity and should not be used to provide immediate answer-by-answer feedback while students are completing the worksheet.

## 3. Elements that must be held constant across groups

Where feasible, use the same:

- instructor and scheduled course;
- lecture content and sequence;
- learning objectives;
- core textbook/slide resources;
- core homework and normal laboratory requirements;
- week in which each topic is studied;
- pre-test and post-test administration instructions;
- test environment and approximate test duration;
- access to ordinary course help outside the intervention;
- deadlines for the topic-matched after-class activity.

If any of these differ materially between groups, record the difference in the fidelity log rather than silently treating the conditions as equivalent.

## 4. Instructor delivery script

For each week, use a short neutral assignment statement. Do not describe one condition as superior, innovative, easier, or expected to improve grades.

Suggested common wording:

> This week's after-class activity reviews the DSP concept introduced in class. Complete the assigned activity independently within the stated study window. Work through all required comparisons and explanations. The activity is intended for conceptual review and does not replace the regular course homework or laboratory work.

Experimental-group addition:

> Use the assigned DSP-Lab module and submit the required reflection in the app.

Control-group addition:

> Use the assigned conventional review worksheet and complete the written comparison/explanation tasks.

Do not provide extra hints to only one group. If clarification is necessary, provide equivalent clarification to both groups whenever the issue concerns shared DSP content rather than the treatment-specific interface.

## 5. Exposure and timing rules

The target activity duration is approximate, not a forced minimum or maximum. Do not instruct students to remain in an activity artificially to satisfy a target time.

For the experimental group, the app's recorded duration is a **recorded elapsed-duration / time-on-task proxy**, not proof of continuous cognitive engagement.

For the control group, if study time is collected, it should be explicitly labelled **self-reported duration** unless an independently verified timing procedure is used. App-recorded and self-reported time should not be treated as directly equivalent measures in the main analysis.

The primary paper should not use time-on-task as a confirmatory outcome. It may be reported descriptively to show approximate exposure.

## 6. Assessment separation

Form A and Form B are research assessments, not practice worksheets.

During the intervention:

- do not use exact Form A/Form B items as worked examples;
- do not distribute answer keys before the post-test;
- do not explain test answers after the pre-test while the intervention is ongoing;
- do not allow repeated research-test attempts unless explicitly approved in the protocol;
- keep test administration instructions the same across conditions.

## 7. Contamination control

Ask students not to share DSP-Lab screenshots, control worksheets with completed answers, or assessment answers across groups before post-test completion.

Known cross-group exposure should be logged, including:

- a control participant using DSP-Lab before the post-test;
- an experimental participant receiving control answer materials;
- sharing of assessment answers;
- one group receiving an unplanned interactive demonstration;
- substantially different instructor help between groups.

Do not automatically exclude students because contamination is suspected. Record the event first; any exclusion must follow the prespecified analysis rules.

## 8. Weekly fidelity record

Use `analysis/templates/main_study_fidelity_log.csv`. Complete one row for each study week, plus additional rows for pre-test/post-test sessions if a meaningful deviation occurs.

A useful fidelity record answers four questions:

1. Was the same regular DSP instruction delivered to both groups?
2. Was the planned after-class activity actually assigned to each group?
3. Did either group receive an unplanned advantage, additional support, or treatment contamination?
4. Did any technical, scheduling, or procedural problem materially change exposure?

The fidelity log is a study-management record, not a student-level outcome dataset. Do not enter names or student IDs.

## 9. Freeze record before the first main-study participant

Complete and retain the following record after expert review and pilot-driven revisions are finished.

| Item to freeze | Final identifier / date |
|---|---|
| Android APK version | TBD |
| Android source commit SHA | TBD |
| Form A version | TBD |
| Form B version | TBD |
| Assessment source commit SHA | TBD |
| Experimental reflection prompts | TBD |
| Control review materials commit SHA | TBD |
| Instructor key version | TBD |
| Analysis plan commit SHA | TBD |
| Ethics/approval identifier | TBD |
| Freeze date | TBD |
| Main-study recruitment start date | TBD |

Once this record is completed and main-study data collection begins, do not change the APK, assessment wording, answer keys, activity prompts, control worksheets, scoring rules, or primary statistical model unless a dated protocol amendment is necessary.

## 10. Protocol deviations after freeze

For any unavoidable change after freeze, record:

- date;
- reason;
- exact change;
- affected group(s) and week(s);
- affected participant codes if necessary and ethically permitted;
- whether the change occurred before or after outcome data were inspected;
- corrective action;
- relevant version/commit identifier.

Do not quietly update the app or worksheet mid-study. Transparency is more defensible than attempting to make the implementation appear perfectly uniform after the fact.

## 11. Minimal manuscript reporting

The final CAE Methods section should summarize fidelity without turning the paper into an implementation report. A suitable structure after data collection is:

> Both conditions followed the same five-week topic sequence and regular course instruction. The experimental group completed the five DSP-Lab modules, whereas the control group completed five topic-matched conventional review activities with comparable intended study time. Intervention delivery was documented weekly using a prespecified fidelity log that recorded activity delivery, scheduling or technical deviations, differential instructor support, and known cross-group contamination. [Insert concise observed fidelity result, e.g., number/nature of meaningful deviations.]

If no meaningful deviations occur, report that fact briefly. If meaningful deviations do occur, describe them and consider them in the limitations rather than omitting them.

## Publication priority

The purpose of this protocol is not to make the intervention larger. It is to make the eventual learning-effect claim more credible by showing that content, timing, and ordinary instruction were controlled as far as feasible while the defining interactive affordances were intentionally different.