# DSP-Lab Main-Study Teacher Runbook

This is the one-page operational sequence for running the DSP-Lab main teaching study. It is intentionally short so that the study can be implemented consistently without adding new research procedures.

## Before the study begins

1. Confirm ethics/consent requirements are satisfied before research data collection.
2. Finalize group allocation and record whether allocation is individual or by intact class.
3. Create coded participant IDs such as `S001`, `S002`, etc. Keep any code-to-name mapping separate from research data.
4. Confirm all experimental devices use the frozen APK:
   - file: `DSP-Lab-V1.0-final-classroom.apk`
   - SHA-256: `0955208b496a002cff738639651347f8d5fdc605917efbce2ce8aa133987b495`
5. Confirm Form A, Form B, control-group materials, questionnaire, analysis lock, and intervention freeze record are final.
6. Do not inspect or optimize the main-study group outcomes while data collection is ongoing.

## Baseline session

- Both groups receive the same instructions for the concept assessment.
- Administer **Form A** as the pre-test.
- Record each participant using the assigned study code, not a name or student ID.
- Do not provide item-by-item answer feedback before the intervention period.

## Five-week intervention

Use the same weekly rhythm for both groups:

| Week | Topic | Experimental | Control |
|---|---|---|---|
| 1 | Signals | DSP-Lab Lab 1 | Signals review |
| 2 | Sampling | DSP-Lab Lab 2 | Sampling review |
| 3 | Convolution | DSP-Lab Lab 3 | Convolution review |
| 4 | DFT | DSP-Lab Lab 4 | DFT review |
| 5 | FIR | DSP-Lab Lab 5 | FIR review |

Each week:

1. Release both groups' activity in the same general time window.
2. Use the same deadline rule.
3. Use the same reminder rule.
4. Keep normal classroom instruction the same.
5. Record group-level completion and any deviations in the weekly fidelity log.
6. Do not give one group extra worked solutions or condition-specific coaching.
7. Record technical problems, schedule disruptions, or cross-group material sharing.

The intended after-class activity duration is approximately 15–30 minutes per week. Do not force the two recorded time measures to be numerically identical: experimental app time is elapsed-device time, while control time may be self-reported or administratively recorded.

## Post-test session

- Administer **Form B** to both groups after the five-week intervention.
- Use comparable testing conditions for both groups.
- Do not reveal scores or solutions until the required research assessment is complete.
- Experimental participants complete the planned student-experience questionnaire after the learning assessment.

## Experimental-group data export

For each experimental participant:

1. Open **Research** in DSP-Lab.
2. Enter the coded participant ID, e.g. `S023`.
3. Confirm the code contains no name or student number.
4. Tap **Export Research CSV**.
5. Save the CSV using the generated filename `DSP_Research_<code>.csv`.
6. Copy the untouched original export into the protected raw-data archive.

The app export contains the coded ID, pre/post scores, completion status, elapsed lab duration, and latest reflection for each lab.

## Control-group and study metadata

Create the study metadata file using the existing analysis template. Use exactly:

- `Experimental`
- `Control`

for group labels. Enter control-group pre/post scores there. Enter experimental questionnaire responses in Q1–Q10 when collected. Do not enter direct identifiers.

## Before analysis

1. Check participant codes for duplicates or transcription errors.
2. Preserve the raw exports unchanged.
3. Run the synthetic pipeline check first:

```bash
python analysis/smoke_test_pipeline.py
```

4. Then run the real-data analysis:

```bash
python analysis/analyze_study.py --app-dir data/app_exports --metadata data/study_metadata.csv --out results
```

5. Fill the manuscript using `paper/CAE_LaTeX_Starter/RESULTS_FILL_GUIDE.md`.

## What not to change after main data collection starts

Do not silently change the APK, Form A/Form B items or keys, control activities, scoring rules, exclusion rules, primary model, group labels, or weekly intervention structure. If an unavoidable change occurs, document it with date, reason, affected participants/groups, and potential consequence.

## Primary result to report

The main effectiveness result is the adjusted experimental-versus-control post-test difference from:

`PostScore ~ Group + PreScore`

Secondary results may support interpretation, but they should not replace this primary comparison because another analysis happens to be more favorable.
