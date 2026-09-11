# DSP-Lab Main-Study Execution Timeline

This is the practical schedule for the simple two-group teaching study used in the CAE manuscript. It is intentionally compact: one experimental group, one control group, one pre-test, five topic-matched after-class activities, one post-test, and one short questionnaire for the experimental group.

## Before Week 0

Complete only the necessary preparation:

- confirm ethics/consent requirements;
- complete expert review and the small Form A/Form B pilot if feasible;
- freeze Form A, Form B, scoring keys, control materials, and the classroom APK;
- prepare participant codes such as `S001`, `S002`, ...;
- record the group assignment for each coded participant;
- verify the frozen APK SHA-256 and run the synthetic analysis smoke test once.

Do not add new study arms, new outcomes, or new app functions after the main study begins unless a genuine correction is required.

## Study schedule

| Time | Topic / activity | Experimental group | Control group | Data to retain |
|---|---|---|---|---|
| Week 0 | Baseline | Form A pre-test | Form A pre-test | ParticipantCode, Group, PreScore |
| Week 1 | Discrete signals | DSP-Lab Lab 1 | Matched signals review | Completion + brief weekly fidelity record |
| Week 2 | Sampling and aliasing | DSP-Lab Lab 2 | Matched sampling review | Completion + brief weekly fidelity record |
| Week 3 | Convolution | DSP-Lab Lab 3 | Matched convolution review | Completion + brief weekly fidelity record |
| Week 4 | DFT and spectrum | DSP-Lab Lab 4 | Matched DFT review | Completion + brief weekly fidelity record |
| Week 5 | FIR filtering | DSP-Lab Lab 5 | Matched FIR review | Completion + brief weekly fidelity record |
| End of Week 5 / next scheduled session | Outcome assessment | Form B post-test | Form B post-test | PostScore |
| Immediately after Form B | Student experience | 10-item DSP-Lab questionnaire | Not required | Q1-Q10 for experimental group |
| After assessment is complete | Research export | Export coded DSP-Lab CSV | Enter scores in metadata | Raw app exports + study metadata |
| After data are frozen | Analysis | Merge and analyze | Merge and analyze | Results tables for manuscript |

## Weekly operating rule

For Weeks 1-5, keep normal classroom teaching the same for both groups. Release the experimental and control activities in the same general time window, use the same deadline and reminder policy, and target approximately 15-30 minutes of after-class work. Record only meaningful deviations or technical problems; do not turn fidelity monitoring into a second research project.

## Minimum data required for the paper

The main manuscript needs only:

- group membership;
- Form A pre-test score;
- Form B post-test score;
- experimental-group questionnaire responses;
- basic participant counts and any important implementation deviation.

DSP-Lab completion, elapsed time, and reflection data may be retained as supporting information, but they do not need to become additional main outcomes.

## Analysis after the study

Preserve the original app CSV exports unchanged. Prepare `study_metadata.csv`, then run:

```bash
python analysis/smoke_test_pipeline.py
python analysis/analyze_study.py --app-dir data/app_exports --metadata data/study_metadata.csv --out results
```

The primary manuscript comparison remains:

```text
PostScore ~ Group + PreScore
```

Use the generated Results Fill Guide to complete the manuscript. Do not add extra models simply because a secondary analysis looks more favorable.

## Practical completion rule

The study is complete when both groups have finished Form B, the experimental group questionnaire has been collected, coded app exports and metadata have been archived, and all important protocol deviations have been noted. At that point the dataset should be frozen for analysis.
