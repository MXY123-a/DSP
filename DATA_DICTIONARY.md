# DSP-Lab Teaching Study Data Dictionary

This dictionary defines the variables used across the Android app export, study metadata file, completion tracking, questionnaire scoring, reflection coding, and final analysis dataset.

## 1. Identification and grouping

| Variable | Type | Allowed / expected values | Source | Analysis role |
|---|---|---|---|---|
| `ParticipantCode` | String | Anonymous code such as `S001`; no names or student IDs | Assigned by research team / app export | Merge key |
| `Group` | Categorical | `Experimental`, `Control` | Study metadata | Main predictor |
| `ConsentForResearch` | Categorical / logical | `Yes`, `No`, `Pending` according to approved protocol | Private study administration record | Determines research-use eligibility; do not use as outcome |

`ParticipantCode` must be unique in the analysis dataset. Any file linking a code to a real student identity must be stored separately from the research dataset and must not be committed to the public repository.

## 2. Assessment variables

| Variable | Type | Range / coding | Source | Derived? |
|---|---|---|---|---|
| `PreScore` | Integer | 0–12 | Form A | No |
| `PostScore` | Integer | 0–12 | Form B | No |
| `MaxScore` | Integer | 12 in the current protocol | App export / metadata | No |
| `RawGain` | Numeric | `PostScore - PreScore` | Analysis script | Yes |
| `NormalizedGain` | Numeric | App-exported value where available | App export | Yes |
| `NormalizedGainCalc` | Numeric | `(PostScore - PreScore)/(MaxScore - PreScore)` when denominator > 0 | Analysis script | Yes |

The primary outcome is `PostScore` adjusted for `PreScore`. Gain variables are secondary outcomes.

## 3. App completion and timing variables

For `i = 1..5`:

| Variable pattern | Type | Coding | Source | Notes |
|---|---|---|---|---|
| `LabiCompleted` | Binary | `1` completed, `0` not completed | App export | Experimental group |
| `LabiDurationSec` | Numeric | Seconds | App export | Automatically recorded time on task |
| `LabiSubmittedAt` | Integer / timestamp | Milliseconds since Unix epoch in current app export | App export | Submission-time marker |
| `LabiReflection` | Text | Free-text reflection | App export | De-identified before publication |

Additional derived fields:

| Variable | Type | Definition |
|---|---|---|
| `LabsCompleted` | Integer | Number of completed DSP-Lab activities, 0–5 |
| `TotalLabDurationSec` | Numeric | Sum of available `Lab1DurationSec` … `Lab5DurationSec` |
| `TotalLabDurationMin` | Numeric | `TotalLabDurationSec / 60` |

Recorded app time is an engagement indicator, not a direct measure of learning quality. Implausible durations should be flagged and inspected rather than automatically deleted.

## 4. Control-group activity variables

If conventional-review completion/time is recorded, recommended variables are:

| Variable | Type | Coding |
|---|---|---|
| `Review1Completed` … `Review5Completed` | Binary | `1` completed, `0` not completed |
| `Review1TimeMin` … `Review5TimeMin` | Numeric | Self-reported minutes |
| `ReviewsCompleted` | Integer | 0–5 |
| `TotalReviewTimeMin` | Numeric | Sum of self-reported review minutes |

Do not directly equate self-reported control-group review time with automatically recorded app time in inferential comparisons without clearly acknowledging the different measurement methods.

## 5. Student-experience questionnaire

| Variable | Type | Range | Meaning |
|---|---|---|---|
| `Q1` … `Q10` | Integer | 1–5 | Likert response; 1 = strongly disagree, 5 = strongly agree |
| `QuestionnaireMean` | Numeric | 1–5 | Mean of available/complete Q1–Q10 according to the prespecified scoring rule |

The questionnaire is a secondary perception measure. It must not be used as the primary evidence of learning effectiveness.

## 6. Reflection rubric variables

The current simplified metadata template stores one total per lab:

| Variable | Type | Range | Definition |
|---|---|---|---|
| `Reflection1` … `Reflection5` | Integer | 0–12 | Total rubric score for each lab |
| `ReflectionTotal` | Integer | 0–60 | Sum of the five lab reflection totals |

If dimension-level coding is retained, optional variables may be added using the pattern:

- `Lab1RefAccuracy`, `Lab1RefEvidence`, `Lab1RefCausal`, `Lab1RefTransfer`, continuing through Lab 5;
- each dimension is scored 0–3.

Use a prespecified double-coding subset for inter-rater reliability.

## 7. Participant-flow and operational variables

| Variable | Type | Suggested values | Purpose |
|---|---|---|---|
| `PreTestCompleted` | Binary / text | `1/0` or `Yes/No` | Flow tracking |
| `PostTestCompleted` | Binary / text | `1/0` or `Yes/No` | Flow tracking |
| `QuestionnaireCompleted` | Binary / text | `1/0` or `Yes/No` | Flow tracking |
| `ResearchCsvReceived` | Binary / text | `1/0` or `Yes/No` | Data-management check |
| `ReflectionCodingCompleted` | Binary / text | `1/0` or `Yes/No` | Coding workflow |
| `IncludedInPrimaryAnalysis` | Binary / text | `1/0` or `Yes/No` | Analysis flow |
| `ExclusionReason` | Text / categorical | Prespecified reason | Participant-flow reporting |

Do not use post-outcome information to invent exclusion rules after seeing the group results.

## 8. Fidelity variables

Weekly fidelity records are study-level operational data rather than participant-level outcomes.

| Variable | Type | Description |
|---|---|---|
| `Week` | Integer | Study week |
| `Date` | Date | Delivery date |
| `Topic` | Text | DSP topic |
| `Group` | Categorical | Experimental / Control |
| `PlannedActivity` | Text | Assigned activity |
| `DeliveredAsPlanned` | Logical / text | Whether delivery matched the protocol |
| `ApproxStudentsPresent` | Integer | Approximate attendance |
| `TechnicalIssue` | Text | Major technical issue |
| `ScheduleDeviation` | Text | Change in timing/order |
| `ContaminationObserved` | Text | Known cross-condition exposure |
| `ExtraInstructorSupport` | Text | Unplanned support |
| `ActionTaken` | Text | Corrective action |
| `ResearcherInitials` | String | Staff initials if allowed by local procedure |

## 9. Missing-value convention

For CSV research files, leave truly missing values blank rather than entering ambiguous placeholders such as `N/A`, `-`, or `999`. The analysis scripts convert blank numeric fields to missing values.

Use explicit zeros only when zero is the actual observed value, for example `Lab1Completed = 0` means the lab was not completed.

## 10. Dataset levels

Three data levels should be kept conceptually separate:

1. **Administrative/private key** — may link a real student to `ParticipantCode`; restricted and stored separately.
2. **Raw research data** — anonymous app exports, control scores, questionnaire responses, completion evidence; archived unchanged.
3. **Analysis dataset** — merged/derived variables used for statistical analysis.

Only levels 2 and 3 should be used for research analysis, and the filled private key should never be committed to this public repository.

## 11. Primary model mapping

The prespecified primary analysis uses:

`PostScore ~ Group + PreScore`

where:

- outcome: `PostScore`;
- main predictor: `Group`;
- baseline covariate: `PreScore`;
- reference group: `Control`.

Report the adjusted experimental-minus-control effect with confidence interval and p value, together with descriptive statistics and an appropriate effect-size measure.
