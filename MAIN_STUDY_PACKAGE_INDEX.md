# DSP-Lab Main-Study Package Index

This index identifies the minimum set of files needed to run the publication-oriented main teaching study without expanding the project scope.

## Operational documents

- `MAIN_STUDY_INTERVENTION_FREEZE.md` — frozen intervention/build/instrument record.
- `MAIN_STUDY_FIDELITY_PROTOCOL.md` — five-week implementation-fidelity rules.
- `TEACHER_CLASSROOM_RUNBOOK.md` — concise classroom execution sequence.
- `MAIN_STUDY_START_CHECKLIST.md` — final pre-study gate.
- `MAIN_STUDY_ANALYSIS_LOCK.md` — prespecified primary outcome, model, exclusions, and interpretation rules.

## Working templates

- `templates/PARTICIPANT_CODE_ROSTER_TEMPLATE.md` — research-facing coded roster.
- `templates/WEEKLY_FIDELITY_LOG_TEMPLATE.md` — aggregate group/week fidelity record.
- `templates/PARTICIPANT_FLOW_TEMPLATE.md` — aggregate study flow counts.

## Existing study materials

- `control_group/` — five matched conventional after-class review activities and instructor materials.
- `PILOT_IMPLEMENTATION_PROTOCOL.md` — AB/BA parallel-form pilot procedure.
- `EXPERT_REVIEW_FORM.md` — assessment expert-review form.
- `STUDENT_QUESTIONNAIRE.md` — experimental-group perception questionnaire.
- `CONSENT_AND_ETHICS_TEMPLATE.md` — planning template for ethics/consent documentation.

## Analysis and manuscript

- `../analysis/analyze_study.py` — main analysis pipeline.
- `../analysis/smoke_test_pipeline.py` — synthetic end-to-end pipeline check.
- `../analysis/templates/study_metadata_template.csv` — analysis metadata template.
- `../paper/CAE_LaTeX_Starter/RESULTS_FILL_GUIDE.md` — direct mapping from analysis outputs to the CAE manuscript.

## Main-study sequence

```text
Expert review / pilot evidence finalized
        ↓
Check MAIN_STUDY_START_CHECKLIST.md
        ↓
Form A pre-test
        ↓
5 weeks: Experimental DSP-Lab vs matched conventional control
        ↓
Weekly fidelity documentation
        ↓
Form B post-test
        ↓
Experimental questionnaire
        ↓
Coded CSV export + metadata merge
        ↓
Prespecified ANCOVA-style analysis
        ↓
Fill CAE manuscript results
```

The package is deliberately narrow: no additional app features, extra outcomes, or exploratory models are required for the current paper unless a genuine methodological problem appears before the main study starts.
