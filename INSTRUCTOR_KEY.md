# Control-Group Review — Instructor Key and Fidelity Notes

This file is for instructors/research staff. Do not distribute the answer key together with the student worksheets if the study protocol intends students to complete the activities independently before checking answers.

## Review 01 — Discrete-Time Signals

Suggested answers:

1. Peak-to-peak value ≈ `3`.
2. No. Phase changes horizontal/sample-index alignment, not amplitude.
3. Signal B.
4. Unit impulse.

Compare task:

- `xA[n]` and `xB[n]` have the same frequency and phase; `xB[n]` has three times the amplitude and approximately three times the peak-to-peak value.
- `xC[n]` has a larger frequency parameter than `xA[n]`, so it oscillates more rapidly across the same sample-index range.

Expected summary: amplitude changes vertical scale; frequency changes oscillation rate/cycles across the displayed samples.

## Review 02 — Sampling and Aliasing

Suggested answers:

1. Yes. `8 kHz > 2 × 3 kHz`.
2. No. `5 kHz < 6 kHz`.
3. `|5 - 8| = 3 kHz`.
4. A sufficiently high `Fs` reduces alias ambiguity and allows the sampled sequence to represent the original sinusoidal frequency correctly.

Three-case comparison for `f = 2 kHz`:

- Case A, `Fs = 6 kHz`: Nyquist frequency = 3 kHz; comfortably above Nyquist; aliasing not expected.
- Case B, `Fs = 4 kHz`: Nyquist frequency = 2 kHz; boundary case; not a robust practical sampling margin.
- Case C, `Fs = 3 kHz`: Nyquist frequency = 1.5 kHz; below Nyquist; aliasing expected; apparent lower frequency = `|2 - 3| = 1 kHz`.

Expected summary: undersampling causes multiple analog frequencies to become indistinguishable after sampling, so a higher-frequency sinusoid may appear at a lower alias frequency.

## Review 03 — Discrete Convolution

Suggested answers:

1. `5 + 4 - 1 = 8` samples.
2. For `x = [2,1]`, `h = [1,3]`: `y = [2,7,3]`.
3. `h[n-k]` represents the shifted/reversed filter sequence participating in the overlap for output index `n`.
4. As the shifted sequences begin and end overlapping, valid sums exist beyond the original support of each single sequence; support lengths add minus one.

Compare task:

- With `hA = [1]`, output is `[1,0,1]`.
- With `hB = [0.5,0.5]`, output is `[0.5,0.5,0.5,0.5]`.
- Filter B averages adjacent contributions and spreads isolated values across neighboring output samples, producing a smoothing effect.

## Review 04 — DFT and Spectrum

Suggested answers:

1. `Δf = 8000/40 = 200 Hz`.
2. `Δf = 8000/80 = 100 Hz`.
3. `N = 80` gives the finer grid.
4. Yes. `1000/125 = 8`, an integer bin index.
5. No. `1060/125 = 8.48`; energy is expected to spread across neighboring bins.

Compare task:

- `N = 128` has smaller bin spacing and a finer frequency grid than `N = 32` when `Fs` is fixed.
- Increasing `N` does not automatically eliminate leakage for an arbitrary sinusoid.
- Leakage depends on whether the observed tone aligns with the DFT grid and on the finite observation/windowing process, not only on the number of bins.

Expected summary: resolution/bin spacing concerns the frequency-grid separation `Fs/N`; leakage concerns energy spreading when a finite-duration tone does not align cleanly with the DFT basis frequencies.

## Review 05 — FIR Low-Pass Filtering

Suggested answers:

1. Frequencies below the cutoff are primarily preserved.
2. Smaller output amplitude is normally expected for a component far above the cutoff.
3. Benefit: potentially sharper transition/stronger selectivity. Cost: more computation and usually more delay.
4. The impulse response becomes longer.

Compare task:

- Narrower transition: Design B (55 taps).
- Lower computational cost: Design A (15 taps).
- Longer impulse response: Design B.
- Greater delay: Design B, assuming a comparable linear-phase implementation.
- A 55-tap filter with a 2 kHz cutoff preserves a wider low-frequency band than the otherwise similar 1 kHz-cutoff design, so components between roughly 1 and 2 kHz are more likely to pass.

## Recommended administration

### Timing

Target approximately 15–30 minutes per worksheet. Do not force students to stop at an exact minute, but avoid adding unplanned exercises that substantially increase control-group exposure.

### Feedback

Use one consistent feedback rule across all control participants. Preferred options are either:

- collect the worksheet before releasing the answer key; or
- release a brief answer key only after the student has completed the worksheet.

Do not provide one-to-one tutoring on worksheet content to only selected control students during the intervention period unless the same support is available to both conditions.

### Completion evidence

If completion is recorded, use a simple binary indicator for each worksheet. If approximate study time is collected for the control group, label it clearly as **self-reported time**, because it is not equivalent to the app's automatically recorded time-on-task.

### Avoid teaching to the outcome test

The worksheets intentionally use concepts and numerical examples that differ from the exact Form A/Form B test items. Do not replace the practice questions with the assessment questions during the study.

## Condition contrast to preserve

Experimental condition:

`structured concept task + interactive parameter manipulation + immediate plot/result feedback + app-recorded reflection/time`

Control condition:

`structured concept review + static worked example + written practice + short written summary`

This preserves comparable content coverage and cognitive engagement while keeping mobile interactivity and immediate visualization as defining intervention features.
