# DSP-Lab Parallel-Form Pilot — Administrator Run Sheet

This sheet is the short operational version of `PILOT_IMPLEMENTATION_PROTOCOL.md`. It is intended to be printed or kept open during the pilot session.

## Before students arrive

- Prepare the final candidate Form A and Form B.
- Prepare participant codes such as `P01`, `P02`, ...
- Assign approximately half of participants to `AB` and half to `BA` before testing.
- Prepare the response-entry template used by `analysis/analyze_pilot.py`.
- Confirm the same calculator and time policy will be used for both forms.
- Do not prepare answer feedback for use between the forms.

## Recommended size

For a simple teaching-research paper, aim for approximately **20–30 pilot participants** if practical. A balanced AB/BA split is more important than forcing an exact target when access is limited.

This pilot is a quality check, not a second effectiveness experiment.

## Opening script

Read or paraphrase:

> We are checking the clarity and approximate comparability of two short DSP concept tests. You will complete both forms in an assigned order. Please work independently. We will not discuss answers or provide DSP teaching between the two forms. After both forms, you may tell us which questions were unclear.

## Session sequence

### 1. First form — 10–15 min

- AB participants complete Form A.
- BA participants complete Form B.
- No discussion, hints, app use, or answer checking.
- Record duration if practical.

### 2. Neutral break — about 10 min

Allowed:

- rest;
- unrelated conversation/activity.

Not allowed:

- DSP teaching;
- answer discussion;
- showing solutions;
- DSP-Lab use;
- targeted explanation of difficult items.

### 3. Second form — 10–15 min

- AB participants complete Form B.
- BA participants complete Form A.
- Use the same conditions as the first form.

### 4. Clarity comments — 3–5 min

Ask participants to identify only genuinely unclear items or wording problems. Do not turn this into a teaching discussion until all responses have been collected.

## Data-entry minimum

For each participant enter:

- `ParticipantCode`
- `Sequence` = `AB` or `BA`
- `A1`–`A12` as 1/0
- `B1`–`B12` as 1/0

Optional:

- `A_DurationSec`
- `B_DurationSec`
- unclear-item notes

Do not enter names or university IDs into the analysis file.

## Analysis command

```bash
python analysis/analyze_pilot.py data/pilot_item_responses.csv --out pilot_results
```

## Simple decision rule

For this paper, do not turn the pilot into a large psychometric study. Review the instrument only when there is a clear practical problem, especially:

- incorrect/debatable key;
- repeated student ambiguity reports;
- negative or clearly poor item discrimination;
- a large A/B item-pair difficulty gap;
- a clear overall Form A/Form B difficulty imbalance;
- obvious AB/BA order sensitivity.

A non-significant difference between A and B does **not** prove equivalence. Use the mean difference, confidence interval, item behavior, student comments, and expert judgment together.

## After the pilot

Record only the revisions that are actually justified. Prefer small wording/distractor corrections over redesigning the instrument.

Once the final revisions are made:

1. record the final Form A/Form B version;
2. freeze the scoring keys;
3. update the instrument evidence record;
4. do not alter the tests after the main-study pre-test begins unless a genuine error requires a dated amendment.
