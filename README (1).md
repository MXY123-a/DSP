# DSP-Lab Study Operations Package

This folder contains the operational templates used to run the teaching study consistently after the Android app and research instruments have been frozen.

## Files

- `PARTICIPANT_CODE_ALLOCATION_TEMPLATE.csv` — anonymous code assignment and high-level administration status.
- `WEEKLY_FIDELITY_LOG_TEMPLATE.csv` — weekly delivery/fidelity record for both groups.
- `COMPLETION_TRACKER_TEMPLATE.csv` — participant flow and completion tracker.
- `DATA_DICTIONARY.md` — definitions, coding rules, source, and analysis role for the study variables.

## Privacy rule

These repository files are **templates only**. Do not commit a filled table containing names, student IDs, email addresses, phone numbers, or any other direct identifier.

If the study requires a mapping between a real student and an anonymous `ParticipantCode`, keep that mapping in an institution-approved restricted location separate from the research dataset and separate from this public GitHub repository.

## Recommended participant-code convention

Use a simple anonymous sequence such as `S001`, `S002`, … . The code itself should not encode the student's name, class number, gender, grade, or other personal characteristic.

For group allocation, keep `Group` as a separate field using exactly:

- `Experimental`
- `Control`

Do not encode the group into the code unless the protocol has a specific reason to do so, because visible group information in the code can make blinding and data handling less clean.

## Operational workflow

Before recruitment, duplicate the templates into a private working directory. During the study, update the allocation/completion and weekly fidelity records without modifying the frozen app or test wording. After data collection, retain untouched raw app exports and merge only anonymous research data into the analysis workflow in `analysis/`.

The filled operational records should follow the university's approved storage, access, retention, and deletion rules.

## Recommended status coding

For administrative tracker fields, use a consistent convention throughout the study, for example `Yes`, `No`, `Pending`, and blank only when the value has not yet been determined. For the statistical analysis CSVs, follow the numeric/missing-value conventions in `DATA_DICTIONARY.md` and `analysis/README.md`.

## Freeze point

Once the first main-study participant begins the protocol, record the frozen APK/commit SHA, Form A/Form B versions, control-group worksheets, reflection prompts, analysis plan, and ethics approval/version. Avoid changing any of these during data collection unless an amendment is documented.
