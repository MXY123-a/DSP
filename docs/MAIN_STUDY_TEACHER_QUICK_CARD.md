# DSP-Lab Teacher Quick Card

**Before Week 0**: verify ethics/consent, group allocation, participant codes, frozen APK hash, Form A/Form B, control materials, and the start checklist.

**Week 0**: both groups complete Form A pre-test under comparable conditions. No item-level answer feedback.

**Weeks 1–5**: release the topic-matched experimental/control activity in the same general window, use the same deadline and reminder rule, and complete the weekly fidelity log.

**Week 6**: both groups complete Form B post-test. Experimental group then completes Q1–Q10 questionnaire.

**Data export**: experimental group exports `DSP_Research_<code>.csv`; keep raw exports unchanged. Control scores and group labels go into the study metadata file.

**Analysis**: run `python analysis/smoke_test_pipeline.py` first, then run the prespecified real-data analysis.

**Do not change after launch**: APK, assessment wording/keys, control activities, primary outcome/model, scoring/exclusion rules, or group labels without a dated protocol deviation.
