# DSP-Lab Main-Study Intervention Freeze Record

This file records the version of the intervention package intended for the main teaching study. Its purpose is to prevent unnoticed mid-study changes and to make the intervention reproducible in the manuscript.

## 1. Freeze status

- Target study: two-group undergraduate DSP teaching study.
- Experimental condition: DSP-Lab mobile-assisted after-class self-directed learning.
- Control condition: matched conventional after-class review.
- Planned intervention duration: five instructional weeks.
- Main outcome: Form B post-test score, with Form A pre-test score as the baseline covariate.
- Primary analysis: `PostScore ~ Group + PreScore`, with Control as the reference group and HC3 robust standard errors.

This record freezes the intended intervention materials before the main group outcomes are inspected.

## 2. Frozen experimental intervention

The experimental group receives the same normal classroom instruction as the control group and completes one DSP-Lab module after class each week:

1. Week 1 — discrete signals and visualization (`LAB01_SIGNALS`)
2. Week 2 — sampling and aliasing (`LAB02_SAMPLING`)
3. Week 3 — discrete convolution (`LAB03_CONVOLUTION`)
4. Week 4 — DFT and spectral interpretation (`LAB04_DFT`)
5. Week 5 — FIR filter behavior (`LAB05_FIR`)

The intended after-class study time is approximately 15–30 minutes per weekly module. The app is an instructional support tool rather than a replacement for conventional DSP laboratory instruction or MATLAB/Python programming work.

## 3. Frozen Android build

Main-study candidate build:

- Repository commit: `9c349466e5a865398a9227f01f94640ce5349e70`
- Build artifact name: `dsp-lab-debug-apk`
- GitHub Actions run: `34569484939`
- Artifact ID: `10187276789`
- Artifact ZIP SHA-256: `0e1b9039fa7ff2b1960eec11b9dc72abfd537a1de7b9fa062e7356c0a4bc2aa0`
- Final classroom APK filename: `DSP-Lab-V1.0-final-classroom.apk`
- Final classroom APK SHA-256: `0955208b496a002cff738639651347f8d5fdc605917efbce2ce8aa133987b495`

The APK hash should be checked before classroom deployment so that every experimental participant receives the same software build.

## 4. Frozen assessment sequence

- Pre-test: Form A, 12 items.
- Post-test: Form B, 12 matched parallel-form items.
- The main study uses Form A before the intervention and Form B after the intervention.
- No item wording, key, scoring rule, or administration rule should be changed after main-study outcome collection begins unless a dated protocol amendment is recorded.

The instruments are researcher-developed parallel concept tests. Expert-review and pilot evidence should be reported as supporting evidence; they should not be described as broadly validated instruments unless the collected evidence justifies that claim.

## 5. Frozen control condition

The control group receives the same normal classroom instruction and a conventional after-class review activity matched by DSP topic and intended study duration. Control materials should use the corresponding files under `docs/control_group/`.

The contrast of interest is therefore:

> interactive mobile manipulation and immediate visualization versus conventional structured after-class review, under the same classroom instruction and comparable topic coverage.

The control group should not be turned into a no-treatment group during the study.

## 6. Frozen implementation rules

The following should remain the same for both groups unless an unavoidable deviation is documented:

- weekly topic;
- release window;
- deadline;
- reminder policy;
- access to normal classroom instruction;
- instructor availability for ordinary course questions;
- pre-test and post-test administration timing.

The instructor should not provide extra study coaching to one group solely because of its assigned condition.

## 7. Data and identifier rule

Research files use a coded participant identifier such as `S023`. Student names, university IDs, email addresses, and other direct identifiers should not be entered into app exports or the analysis dataset.

If a code-to-name mapping is required for course administration, keep it in a separate restricted file. In that situation the research data are coded/pseudonymous rather than irreversibly anonymous.

## 8. Analysis freeze

The primary outcome and primary model must not be changed in response to the observed group results. The prespecified primary effectiveness analysis remains the baseline-adjusted post-test comparison.

Negative gain, low scores, unfavorable questionnaire responses, or unusual-but-possible app duration are not by themselves reasons for exclusion. Any duplicate, corrupt, impossible, or eligibility-related exclusions must be documented using the pre-established rules.

## 9. Deviations after freeze

A change made after this freeze should be recorded with:

- date;
- affected group(s);
- affected week or assessment;
- exact change;
- reason;
- whether participants were exposed before the change;
- whether the change could influence interpretation of the primary outcome.

Do not silently replace the APK, assessment items, control activity, scoring rule, allocation rule, or main analysis after data collection starts.

## 10. Publication use

This record is an internal reproducibility document. In the paper, report the intervention version, five-week topic sequence, parallel-form pre/post design, matched control condition, and the fact that implementation deviations were documented prospectively. The full operational record does not need to be reproduced in the main manuscript.
