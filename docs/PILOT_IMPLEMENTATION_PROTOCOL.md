# DSP-Lab Parallel-Form Pilot Implementation Protocol

## Purpose

This protocol is the operational version of the assessment pilot. Its primary purpose is to determine whether Form A and Form B are usable and approximately comparable before they are used as pre- and post-tests in the main quasi-experimental study.

The pilot is **not** designed to estimate the learning effectiveness of DSP-Lab.

## Recommended sample

Target: **24–30 undergraduate students** with prior exposure to introductory DSP concepts comparable to the future study population.

If possible, pilot participants should not be reused in the main effectiveness analysis. If institutional constraints require overlap, document it explicitly and avoid exposing pilot participants to answer feedback before the main study.

## Sequence allocation

Use a counterbalanced two-sequence design:

- `AB`: Form A first, then Form B;
- `BA`: Form B first, then Form A.

Aim for approximately equal numbers in the two sequences. For example:

- 24 participants: 12 AB / 12 BA;
- 26 participants: 13 AB / 13 BA;
- 30 participants: 15 AB / 15 BA.

Assign sequence before testing. A simple randomized allocation list is sufficient. Do not change sequence because of the student's perceived ability.

## Required materials

1. Current frozen Form A and Form B item sets.
2. `analysis/templates/pilot_item_response_template.csv`.
3. A timer or recorded start/end time for each form.
4. A short sheet or online field for unclear-item comments.
5. No answer key visible to students during the session.

## Standardized session

### Step 1 — Introduction (about 2 minutes)

Tell participants that the purpose is to improve the clarity and comparability of two DSP concept tests. Do not describe one form as the pre-test or the other as the post-test, and do not imply that one form should be easier.

Use anonymous participant codes only.

### Step 2 — First form (about 10–15 minutes)

Administer the form specified by `Sequence`.

Conditions should be identical for both sequences:

- same calculator policy;
- same time allowance;
- no discussion;
- no answer checking;
- no teaching hints;
- no app use.

Record the completion time in seconds if practical.

### Step 3 — Neutral break (about 10–15 minutes)

Use a break or unrelated neutral activity. Do not provide DSP instruction, show solutions, discuss difficult items, or let participants use DSP-Lab.

This restriction is important because targeted learning between forms would make a Form A/Form B score difference impossible to distinguish from a learning effect.

### Step 4 — Second form (about 10–15 minutes)

Administer the second form under the same conditions.

Again, do not provide answer feedback until the second form is complete.

### Step 5 — Clarity comments (about 3–5 minutes)

Ask students to list item numbers that were unclear or awkwardly worded. Encourage concise comments such as:

- “Term X was unclear.”
- “Two options seemed possible.”
- “The numerical information was confusing.”

Enter item numbers in `A_UnclearItems` / `B_UnclearItems` and any useful comments in `Notes`.

## Data entry

For every participant record:

- `ParticipantCode`;
- `Sequence` = `AB` or `BA`;
- `A1`–`A12` coded `1` for correct and `0` for incorrect;
- `B1`–`B12` coded `1` for correct and `0` for incorrect;
- optional `A_DurationSec` and `B_DurationSec`;
- optional unclear-item fields and notes.

Do not enter names, student numbers, emails, or other direct identifiers into the pilot analysis file.

## Analysis

Run:

```bash
python analysis/analyze_pilot.py data/pilot_item_responses.csv --out pilot_results
```

The script produces:

- `pilot_participant_scores.csv`;
- `pilot_item_statistics.csv`;
- `pilot_form_summary.csv`;
- `pilot_parallel_item_pairs.csv`;
- `pilot_order_sensitivity.csv`;
- `pilot_review_flags.txt`.

The most important outputs for publication preparation are the Form A/Form B mean difference and 95% CI, the direction of the difference, item-pair difficulty patterns, corrected item–total correlations, and the AB/BA order sensitivity.

## Screening rules

The following rules are deliberately pragmatic and should not be presented as universal psychometric standards.

### Review an individual item if

- `p < 0.20` or `p > 0.90`;
- corrected item–total correlation is below approximately `0.20`;
- corrected item–total correlation is negative;
- multiple students independently identify the same ambiguity.

### Review an A/B item pair if

- `|pB − pA| > 0.25`;
- experts previously questioned equivalence;
- the two items appear to require different cognitive operations after seeing pilot performance.

### Review the forms as a whole if

- the absolute mean Form B − Form A difference exceeds about `1 point` on the 12-point scale;
- `|Cohen's dz| > 0.40` for the paired form difference;
- many item-pair differences point in the same direction;
- floor/ceiling patterns are substantial;
- the AB and BA sequences show a conspicuous difference suggestive of order/practice effects.

A non-significant paired t test is **not** evidence that the forms are equivalent. With a small pilot, effect magnitude, confidence intervals, item behavior, student comments, and expert review should be considered together.

## Revision rule

Prefer the smallest defensible revision.

- Correct any factual or keying error immediately.
- Revise an isolated ambiguous distractor or wording problem rather than replacing the entire pair.
- If one form is systematically easier, revise the few pairs contributing most clearly to the imbalance.
- Do not expand beyond 12 items per form unless the pilot reveals a specific content-coverage problem.
- Do not optimize the instrument only to raise Cronbach's alpha; the test intentionally samples five DSP domains.

After any substantive item change, record the change in a revision log and, if the change materially affects difficulty, consider a small confirmation check before the main study.

## App technical check

Keep the app technical pilot separate from the parallel-form comparison. After the assessment pilot, or with a separate small set of users/devices, verify:

`study setup → Form A → Labs 01–05 → Form B → Research Dashboard → CSV export`

Confirm that scores, lab completion, duration, reflection text, timestamps, and participant code are exported correctly.

## Main-study freeze decision

The instrument is ready to freeze when:

1. expert review has no unresolved major content problem;
2. no scoring-key problem remains;
3. A/B performance does not show a clear systematic difficulty imbalance;
4. no unresolved negative-discrimination item remains;
5. repeated student wording complaints have been addressed;
6. the technical data-export path has been verified.

Once main-study data collection begins, do not alter test items, answer keys, lab tasks, or scoring rules without documenting a protocol amendment.

## Suggested manuscript wording after the pilot

Use only after the described work has actually been completed:

> Two researcher-developed parallel 12-item DSP concept tests underwent expert content review and student pilot testing before the main study. During the pilot, the order of Form A and Form B was counterbalanced to reduce systematic order effects, and no targeted instruction or answer feedback was provided between forms. Item difficulty, corrected item–total correlations, internal consistency, paired form-score differences, and item-pair difficulty patterns were inspected before the instruments were frozen for the main study.

Do not replace this wording with “validated instrument” unless substantially stronger validation evidence is obtained.
