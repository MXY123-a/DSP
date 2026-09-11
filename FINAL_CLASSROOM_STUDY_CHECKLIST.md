# DSP-Lab Final Classroom Study Checklist

This checklist is intentionally short. The target is a simple engineering-education paper in which the DSP-Lab application and the classroom evaluation have roughly equal weight. Do not add extra treatment groups, extra outcomes, or complex analyses unless they become necessary in the actual course.

## 1. Freeze before the first student participates

Record the final versions used in the study:

- DSP-Lab APK / source commit;
- Form A pre-test and Form B post-test;
- five DSP-Lab learning modules and reflection prompts;
- five topic-matched control review sheets;
- 10-item DSP-Lab student-experience questionnaire;
- analysis script and metadata template;
- ethics approval/exemption and consent wording required by the institution.

Once classroom data collection starts, do not change test questions or the learning tasks unless a technical failure makes a correction unavoidable. Any such correction should be documented.

## 2. Participant codes

Use one study code per student, for example `S001`, `S002`, ... . Use the same code on:

- the app research export;
- the group/metadata sheet;
- the questionnaire record;
- any completion tracking sheet.

Do not use student names or institutional student numbers in the analysis dataset. If a code-to-name mapping is needed for course administration, keep it separately from the research dataset.

## 3. Experimental group workflow

1. Form A pre-test.
2. Five DSP-Lab activities over the planned teaching period.
3. Form B post-test after all five activities are submitted.
4. 10-item DSP-Lab experience questionnaire.
5. Export the DSP-Lab research CSV using the participant code.

The app study flow should be used consistently. The post-test is intended to become available only after Labs 01--05 have been completed.

## 4. Control group workflow

1. Form A pre-test.
2. Five conventional topic-matched review activities covering the same DSP topics.
3. Form B post-test at approximately the same point in the course.

The control condition does not need the DSP-Lab experience questionnaire because the questionnaire asks specifically about DSP-Lab.

## 5. What must be recorded

For the main paper, the essential variables are only:

- `ParticipantCode`;
- `Group` (`Experimental` or `Control`);
- `PreScore`;
- `PostScore`;
- `MaxScore` (= 12);
- Q1--Q10 for experimental-group students.

The app also records completion, elapsed duration and reflections. These may be retained as supporting information, but they are not required as main outcomes for the current paper.

## 6. Data check immediately after collection

Before analysis, verify:

- every participant code is unique;
- group labels are correct;
- Form A and Form B scores are within 0--12;
- experimental students have the expected app export;
- missing post-tests are identified rather than silently removed;
- questionnaire values, where present, are within 1--5.

Keep the original app exports unchanged and work on copies or the merged analysis dataset.

## 7. Analysis kept deliberately simple

Run:

```bash
python analysis/analyze_study.py \
  --app-dir data/app_exports \
  --metadata data/study_metadata.csv \
  --out results
```

The main paper needs only:

1. pre-test and post-test mean (SD) for both groups;
2. raw gain as a supporting descriptive result;
3. the baseline-adjusted group comparison

   `PostScore ~ Group + PreScore`;

4. one descriptive standardized difference (Cohen's d);
5. experimental-group pre/post improvement;
6. concise questionnaire results: overall mean, alpha, highest-rated item and lowest-rated item.

Do not add multiple exploratory models merely to obtain a significant result.

## 8. Minimum manuscript completion fields

Before submission, replace the remaining manuscript placeholders with:

- institution description;
- experimental and control sample sizes;
- number of DSP instructors who reviewed the concept test;
- ethics/consent statement;
- observed learning results;
- observed questionnaire results;
- final data-availability statement.

## 9. Final study story

The paper should remain easy to follow:

> DSP concepts can be difficult to connect with observable signal behavior. DSP-Lab provides short mobile activities based on parameter manipulation and immediate visualization. A straightforward classroom comparison is then used to examine whether the application is educationally useful and acceptable to students.

This is sufficient for the current paper. The study does not need to become a large educational trial.