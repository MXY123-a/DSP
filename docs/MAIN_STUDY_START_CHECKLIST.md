# DSP-Lab Main-Study Start Checklist

Use this checklist immediately before the first main-study pre-test. It is the final operational gate between preparation and real data collection.

## Study design locked

- [ ] Experimental and control conditions are defined.
- [ ] Allocation method is recorded as individual or intact-class assignment.
- [ ] If only one intact class is used per condition, the class/intervention confounding limitation is acknowledged in the protocol and manuscript plan.
- [ ] Primary outcome remains Form B post-test score.
- [ ] Primary analysis remains baseline-adjusted `PostScore ~ Group + PreScore` with HC3 robust standard errors.

## Instruments locked

- [ ] Form A pre-test wording and scoring key are final.
- [ ] Form B post-test wording and scoring key are final.
- [ ] Expert-review evidence has been collected or scheduled before the main study.
- [ ] Counterbalanced AB/BA pilot has been completed or explicitly documented as not feasible before the main study.
- [ ] No assessment item will be changed after outcome collection begins without a dated amendment.

## Intervention locked

- [ ] Frozen APK file is available.
- [ ] APK SHA-256 verified as `0955208b496a002cff738639651347f8d5fdc605917efbce2ce8aa133987b495`.
- [ ] Week 1 Signals activity ready for both groups.
- [ ] Week 2 Sampling activity ready for both groups.
- [ ] Week 3 Convolution activity ready for both groups.
- [ ] Week 4 DFT activity ready for both groups.
- [ ] Week 5 FIR activity ready for both groups.
- [ ] Release/deadline/reminder policy is the same for both conditions.

## Participant coding and privacy ready

- [ ] Participant codes prepared using `S001`, `S002`, ... or an equivalent non-identifying scheme.
- [ ] The same participant code will be used across pre-test, post-test, app export, questionnaire, and analysis data.
- [ ] No names/student IDs will be entered in app exports or analysis files.
- [ ] Any code-to-name administrative key is stored separately and access is restricted.

## Fidelity and data collection ready

- [ ] Weekly fidelity log template is ready.
- [ ] Participant flow template is ready.
- [ ] Technical/support contact procedure is defined for app problems.
- [ ] Experimental participants know how to export the coded research CSV.
- [ ] Raw app exports will be archived unchanged.
- [ ] Control-group pre/post scores will be entered into the study metadata file.

## Ethics ready

- [ ] Required institutional ethics approval/exemption has been obtained or confirmed as applicable.
- [ ] Participant information/consent procedure is ready.
- [ ] Participation in research data use does not create inappropriate grade pressure.
- [ ] Students understand that course participation and permission to use their data for research are treated according to the approved procedure.

## Analysis pipeline ready

- [ ] Python environment installed from `analysis/requirements.txt`.
- [ ] Synthetic smoke test passes with `python analysis/smoke_test_pipeline.py`.
- [ ] Raw data and analysis copies will be stored separately.
- [ ] Main analysis command and Results Fill Guide are available.

## Start rule

Begin the main study only after all applicable boxes above are checked or any unavoidable exception has been dated and documented. After the first participant completes the main-study pre-test, treat the app, instruments, control materials, scoring, exclusion rules, and primary analysis as frozen unless a genuine protocol/safety correction is necessary.
