# DSP-Lab Teaching Study Implementation Guide

## 1. Study purpose and positioning

DSP-Lab is used as an **after-class mobile-assisted self-learning tool** in an undergraduate Digital Signal Processing course. It complements normal lectures, textbooks, homework, MATLAB/Python activities, and conventional laboratory teaching. It should not be presented to students as a replacement for those activities.

The study compares two learning-support conditions:

- **Experimental group:** normal DSP teaching plus five DSP-Lab after-class interactive activities.
- **Control group:** the same normal DSP teaching plus conventional after-class review material of comparable topic coverage and, where feasible, approximately comparable study time.

The intended learning sequence is:

`Form A pre-test → course teaching → five after-class activities/review sessions → Form B post-test → experimental-group questionnaire → data export and analysis`

The final five-week treatment contrast, exposure rules, and pre-study freeze record are specified in `MAIN_STUDY_INTERVENTION_FREEZE_PROTOCOL.md`.

## 2. Student-facing procedure

### Before participation

Students should receive a brief study information sheet explaining:

- the purpose of the educational study;
- what participation involves;
- that participation in research is voluntary;
- whether the learning activity itself is part of normal teaching;
- how research use of their data can be declined where required by the local ethics protocol;
- that research participation or non-participation will not affect course grades or teacher treatment;
- that only anonymous participant codes should be used in the research dataset.

Do not ask students to enter names, university IDs, email addresses, phone numbers, or other direct identifiers into the DSP-Lab research export.

### Experimental-group student sequence

1. Receive the anonymous participant code assigned by the research team, for example `S023`.
2. Complete **Pre-test Form A** in DSP-Lab before using the five learning modules for the study.
3. After the corresponding classroom topic has been taught, complete the assigned DSP-Lab activity outside class.
4. During each activity, manipulate the requested parameters, observe plots/results, compare at least the required cases, and answer the reflection prompt in the student's own words.
5. Submit the activity only after completing the reflection. The app records completion, final parameters, time on task, reflection text, and submission time locally.
6. Complete all five activities in the assigned study window.
7. Complete **Post-test Form B** after the intervention period without consulting notes or discussing answers.
8. Complete the 10-item DSP-Lab student experience questionnaire once, after the post-test.
9. In the Research screen, enter the anonymous participant code and export the research CSV.
10. Submit only the exported research file through the study's approved collection channel.

### Control-group student sequence

1. Receive the same study information and an anonymous participant code.
2. Complete Pre-test Form A under the same timing and conditions as the experimental group.
3. Attend the same regular DSP teaching.
4. Complete the assigned conventional after-class review activity covering the same five topic areas.
5. Complete Post-test Form B under the same timing and conditions as the experimental group.
6. Do **not** complete the DSP-Lab-specific experience questionnaire because RQ3 concerns perceptions of the experimental tool itself.

The control group should not be disadvantaged academically. If appropriate, access to DSP-Lab may be offered after post-test data collection has ended.

## 3. Instructor implementation guide

### Keep the instructional conditions comparable

Where practical, keep these elements the same between groups:

- instructor;
- lecture content and sequence;
- syllabus and learning objectives;
- core homework;
- class time;
- test administration timing;
- assessment instructions;
- access to normal course resources.

The principal planned difference should be the **after-class learning-support method**.

### Do not coach test answers

During Pre-test Form A and Post-test Form B:

- do not explain individual test items;
- do not indicate whether an answer is correct;
- do not permit repeated attempts within the research protocol unless this is explicitly planned;
- use the same instructions and approximate completion time for both groups.

### Avoid intervention contamination

During the main study:

- do not distribute DSP-Lab to control participants before their post-test if this would undermine the group comparison;
- ask students not to share screenshots or answers from the app with the other group during the intervention period;
- avoid adding extra tutorial explanations to only one group outside the planned intervention.

Contamination cannot always be prevented in real courses, so any known cross-group exposure should be documented.

## 4. Recommended five-week schedule

| Time | Experimental group | Control group | Research data |
|---|---|---|---|
| Before Week 1 | Form A pre-test | Form A pre-test | PreScore |
| Week 1 | Lab 01: Discrete-time signals | Conventional review: signals | Experimental completion/time/reflection; weekly fidelity |
| Week 2 | Lab 02: Sampling and aliasing | Conventional review: sampling | Experimental completion/time/reflection; weekly fidelity |
| Week 3 | Lab 03: Convolution | Conventional review: convolution | Experimental completion/time/reflection; weekly fidelity |
| Week 4 | Lab 04: DFT and spectrum | Conventional review: DFT | Experimental completion/time/reflection; weekly fidelity |
| Week 5 | Lab 05: FIR filtering | Conventional review: FIR | Experimental completion/time/reflection; weekly fidelity |
| End of Week 5 or Week 6 | Form B post-test + questionnaire + CSV export | Form B post-test | PostScore, questionnaire, app export |

Each mobile activity is intended to require approximately **15–30 minutes**, although actual time-on-task is recorded and should be reported rather than forced into a narrow range. The control worksheets use the corresponding target ranges in `control_group/ALIGNMENT_MATRIX.md` and `MAIN_STUDY_INTERVENTION_FREEZE_PROTOCOL.md`.

## 5. Operational checklist before the first main-study participant

- Complete expert review and pilot analysis.
- Make only evidence-justified assessment revisions.
- Freeze the APK version and record its commit SHA.
- Freeze Form A and Form B wording and answer keys.
- Freeze the reflection prompts.
- Freeze the control-group review materials and instructor key.
- Complete the version/date record in `MAIN_STUDY_INTERVENTION_FREEZE_PROTOCOL.md`.
- Confirm the local ethics/IRB or institutional approval requirement.
- Prepare anonymous participant-code list separately from research data.
- Test CSV export on several Android devices.
- Test the complete sequence: pre-test → Labs 01–05 → post-test → export.
- Confirm who will collect files and where they will be stored.
- Define exclusion and missing-data rules before examining final outcomes.
- Prepare `analysis/templates/main_study_fidelity_log.csv` for weekly completion.

## 6. Data-handling workflow

Keep any participant-code key, if one exists, separate from the analysis dataset. The analysis dataset should contain only anonymous codes.

Recommended folders:

```text
study_data/
  raw_app_exports/       # untouched student exports
  raw_control_scores/    # original control-group data
  working/               # cleaned/merged copies
  fidelity/              # completed weekly fidelity log
  analysis_results/      # generated tables
```

The untouched raw files should be archived and not edited. Perform cleaning and coding on copies.

## 7. Fidelity log

Use `analysis/templates/main_study_fidelity_log.csv` during the main study. Complete one row for each study week and use the pre-test/post-test rows if a meaningful administration deviation occurs.

The fidelity record should capture:

- session date and topic;
- whether both groups received the same regular instruction and core homework;
- whether the planned experimental/control activity was actually assigned;
- major experimental technical problems or control-material delivery problems;
- differential instructor support;
- known cross-group contamination;
- schedule or protocol deviations;
- corrective action;
- whether the event is meaningful for interpretation of the final results.

Do not include names or student IDs. The fidelity log is intended to support transparent Methods/Limitations reporting, not to become a new outcome dataset.

## 8. Stop rule for software and intervention changes

Once main-study data collection begins, do not change the APK, test items, lab prompts, scoring rules, control worksheets, instructor key, or export structure unless a protocol amendment is necessary. Any unavoidable change should be documented with date, reason, affected groups/weeks, corrective action, and version/commit identifier.

## 9. Publication-focused implementation rule

The study should remain compact. Fidelity documentation exists to strengthen the credibility of the main comparison, not to create additional research questions. The final paper should summarize whether the planned five-week intervention was delivered as intended and briefly report meaningful deviations, while retaining the baseline-adjusted post-test comparison as the primary evidence.