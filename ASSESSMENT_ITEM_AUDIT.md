# DSP-Lab Parallel Assessment Item Audit

Last revised: 2026-09-11

Purpose: publication-oriented review of the 12-item Form A pre-test and 12-item Form B post-test before expert review and student pilot testing. The goal is not to claim that the instrument is validated. The goal is to improve alignment, parallel-form equivalence, wording accuracy, response-key balance, and pilot readiness.

## Overall judgment

The 12-pair blueprint is adequate for a compact CAE teaching study because it samples all five intervention domains while keeping the test short enough for a pre/post classroom protocol. The revised forms retain the planned distribution:

- Discrete-time signals: 2 pairs
- Sampling and aliasing: 3 pairs
- Convolution: 2 pairs
- DFT and spectrum: 3 pairs
- FIR low-pass filtering: 2 pairs

The forms should still be described as **researcher-developed parallel concept tests** until expert review and pilot evidence are available.

## Main pre-pilot revisions made

1. **Matched cognitive demand more closely across forms.** Formula-recall items in Form A were converted to numerical/application items where Form B already required calculation (Nyquist, convolution length, and DFT bin spacing).
2. **Removed avoidable wording ambiguity around the Nyquist boundary.** Items now ask for a sampling rate that is *safely above* the boundary rather than relying on a strict-versus-nonstrict inequality convention.
3. **Separated DFT bin spacing from an over-broad claim about “true resolution.”** The revised pair asks directly about bin spacing when the number of acquired samples increases.
4. **Improved the leakage item.** The earlier Form A item effectively answered itself with “because of spectral leakage.” The revised item asks students to interpret the expected spectrum for a between-bin tone.
5. **Made the FIR passband pair application-based.** Both forms now require interpreting a cutoff relative to candidate sinusoidal components.
6. **Balanced correct-option positions.** Each form now contains exactly three correct answers in each position A, B, C, and D. This reduces answer-position patterns and guessing cues.

## Pair-by-pair audit

| Pair | Domain | Target learning objective | Form A demand | Form B demand | Alignment with intervention | Pre-pilot status |
|---|---|---|---|---|---|---|
| 1 | Signals | Relate sinusoidal frequency to visible oscillation rate | Interpret parameter change | Interpret opposite parameter change | Directly aligned with Lab 01 frequency comparison | Keep; intentionally easy anchor item |
| 2 | Signals | Relate amplitude to peak-to-peak value | Apply proportional scaling | Apply proportional scaling | Directly aligned with Lab 01 amplitude comparison | Keep; easy anchor item |
| 3 | Sampling | Apply Nyquist boundary to a band-limited signal | Numerical application | Numerical application | Directly aligned with Safe/Boundary/Aliasing comparison | Revised; now better matched |
| 4 | Sampling | Determine alias frequency | Numerical calculation/interpretation | Numerical calculation/interpretation | Directly aligned with observed alias-frequency display | Keep |
| 5 | Sampling | Explain consequence of crossing below/above 2f | Conceptual interpretation | Conceptual interpretation | Directly aligned with guided three-case comparison | Keep |
| 6 | Convolution | Determine output length of finite linear convolution | Numerical application | Numerical application | Supports basic convolution understanding | Revised; now better matched |
| 7 | Convolution | Explain the shifted-overlap sum-of-products operation | Conceptual mechanism | Conceptual mechanism | Directly aligned with manual one-sample verification | Keep |
| 8 | DFT | Compute DFT bin spacing Fs/N | Numerical calculation | Numerical calculation | Directly aligned with Lab 04 resolution readout | Revised; now better matched |
| 9 | DFT | Interpret effect of increasing acquired N on bin spacing | Relational interpretation | Relational interpretation | Directly aligned with N comparison task | Revised wording to avoid overclaiming “true resolution” |
| 10 | DFT | Interpret bin alignment and leakage pattern | Spectrum interpretation | Spectrum interpretation | Directly aligned with 1000-Hz vs between-bin comparison | Revised; removes circular wording |
| 11 | FIR | Interpret low-pass cutoff relative to signal components | Cutoff application | Cutoff application | Directly aligned with cutoff manipulation in Lab 05 | Revised; less trivial than naming “low frequencies” |
| 12 | FIR | Explain tap-count/transition-width trade-off | Conceptual trade-off | Conceptual trade-off | Directly aligned with N=11/41/61 comparison | Keep |

## What the pilot must determine

The present audit can improve face/content alignment, but it cannot establish empirical item quality. Before the main study, the pilot should inspect the following:

### Item difficulty

For each binary item, calculate the proportion correct, p. A practical target for this short concept test is to avoid a concentration of items at extreme difficulty. Items with p below about 0.20 or above about 0.90 should be reviewed, especially if several items show the same pattern.

### Item discrimination

Calculate corrected item-total correlation within each form. Very low or negative discrimination should trigger review of wording, distractors, scoring key, or construct mismatch. With a small pilot, values should be interpreted cautiously rather than treated as hard pass/fail thresholds.

### Form-level comparability

Compare Form A and Form B total-score means, standard deviations, score ranges, and reliability. The objective is approximate equivalence, not statistically proving identical difficulty. A practically important mean difference between forms should lead to item revision before the main study.

### Internal consistency

Report KR-20 or Cronbach's alpha for the 12 binary items. Because the test intentionally samples five DSP domains with only 12 items, very high alpha should not be expected. Reliability should be interpreted together with content coverage and item statistics.

### Ceiling/floor effects

Pairs 1 and 2 are deliberately easier anchor items. If the pilot shows severe ceiling effects across many items, revise one or two additional items rather than increasing the total test length.

## Expert-review focus

Experts should be asked to judge:

- whether each item genuinely measures the stated DSP concept;
- whether the distractors are plausible but not misleading;
- whether Form A and Form B are at approximately the same cognitive level;
- whether any item depends on a convention not made explicit in the course;
- whether terminology such as *Nyquist boundary*, *DFT bin spacing*, *spectral leakage*, and *cutoff* matches the course language;
- whether the 12-item coverage is adequate for the five intervention modules.

## Publication wording after pilot

A conservative Methods statement can use wording such as:

> Two researcher-developed parallel 12-item concept tests were used as the pre-test and post-test. The forms sampled the same five DSP domains using different numerical values and surface wording. Before the main study, content relevance and form equivalence were reviewed by DSP instructors, and a student pilot was used to inspect item difficulty, discrimination, internal consistency, and approximate Form A/Form B comparability.

Do not write “validated test” unless the evidence obtained is sufficient to justify that stronger claim.

## Decision for the current software version

The revised 12+12 items are ready for **expert review and pilot testing**. No additional assessment items should be added before the pilot unless expert reviewers identify a specific content gap. Keeping the instrument compact is preferable to expanding it without evidence that more items are needed.
