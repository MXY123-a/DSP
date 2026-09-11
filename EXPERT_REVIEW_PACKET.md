# DSP-Lab Parallel Concept Test — Expert Review Packet

## Purpose

This packet is intended for **2–3 university instructors with experience teaching undergraduate Digital Signal Processing (DSP)**. It supports content review of the researcher-developed parallel concept tests used in the DSP-Lab teaching study:

- **Form A**: 12-item pre-test
- **Form B**: 12-item post-test

The goal of the expert review is to determine whether the item pairs are appropriate for the intended undergraduate DSP population before student pilot testing. The review does **not** by itself establish full psychometric validation.

## Reviewer profile

Please record only professional information needed to describe the expert panel in the manuscript.

- Reviewer code: __________
- Academic rank / role: ______________________________
- Highest degree: ______________________________
- Years teaching DSP or closely related signal-processing courses: ______
- Approximate number of DSP course offerings taught: ______
- Main teaching/research area: ______________________________

Do not enter unnecessary personal identifiers.

## Rating scale

Use the following 4-point scale for each criterion:

1 = not acceptable / major revision required  
2 = partly acceptable / substantial revision required  
3 = acceptable / minor revision may be useful  
4 = highly acceptable / no revision required

Please rate:

- **Relevance** — Does the item measure the intended DSP concept?
- **Clarity** — Is the wording unambiguous for the target students?
- **Distractor quality** — Are incorrect options plausible but clearly incorrect to a knowledgeable student?
- **Parallel-form equivalence** — Do the paired Form A/B items assess the same construct at approximately the same cognitive level and difficulty?

For content-validity summaries, ratings of 3 or 4 may be coded as an endorsement. With exactly three reviewers, an I-CVI above 0.78 effectively requires all three reviewers to endorse the item.

---

# Pair 1 — Discrete-Time Signals: Frequency and visible oscillation rate

**Learning objective:** Relate the sinusoidal frequency parameter to the number of visible oscillations across a fixed sample window.

### Form A — `pre_signal_frequency`
For a discrete sinusoid with the same sample count, what is the main effect of increasing its frequency parameter?

A. The peak amplitude must increase  
B. More oscillations appear across the displayed samples  
C. The mean must become positive  
D. The sequence becomes an exponential

**Key:** B

### Form B — `post_signal_frequency`
With amplitude, phase, and sample count unchanged, what happens when the frequency parameter of a discrete sinusoid is reduced?

A. Its peak-to-peak value must become zero  
B. Its amplitude automatically doubles  
C. Fewer oscillations appear across the displayed samples  
D. It becomes a unit impulse

**Key:** C

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 2 — Discrete-Time Signals: Amplitude and peak-to-peak value

**Learning objective:** Apply proportional amplitude scaling to the peak-to-peak value of a sinusoid.

### Form A — `pre_signal_amplitude`
If the amplitude of a sinusoid is doubled while frequency and phase remain unchanged, what happens to its peak-to-peak value?

A. It is halved  
B. It is unchanged  
C. It doubles  
D. It becomes zero

**Key:** C

### Form B — `post_signal_amplitude`
A sinusoid has amplitude A. If its amplitude is changed to 3A while frequency and phase stay fixed, how does its peak-to-peak value change?

A. It becomes three times as large  
B. It stays the same  
C. It becomes twice as large  
D. It becomes one third as large

**Key:** A

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 3 — Sampling: Nyquist boundary

**Learning objective:** Select a sampling rate safely above the Nyquist boundary for a band-limited signal.

### Form A — `pre_sampling_nyquist`
A band-limited signal contains no frequency above 3 kHz. Which sampling rate is safely above the Nyquist boundary?

A. 3 kHz  
B. 5 kHz  
C. 1.5 kHz  
D. 8 kHz

**Key:** D

### Form B — `post_sampling_nyquist`
A band-limited signal contains no frequency above 4 kHz. Which sampling rate is safely above the Nyquist boundary?

A. 5 kHz  
B. 10 kHz  
C. 7 kHz  
D. 4 kHz

**Key:** B

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 4 — Sampling: Alias frequency

**Learning objective:** Determine the lower-frequency alias produced when a sinusoid is sampled below the Nyquist rate.

### Form A — `pre_sampling_alias_frequency`
A 3 kHz sinusoid is sampled at 4 kHz. What alias frequency is observed in the sampled sequence?

A. 1 kHz  
B. 0.5 kHz  
C. 3 kHz  
D. 4 kHz

**Key:** A

### Form B — `post_sampling_alias_frequency`
A 6 kHz sinusoid is sampled at 8 kHz. At what lower frequency will it appear after aliasing?

A. 1 kHz  
B. 6 kHz  
C. 8 kHz  
D. 2 kHz

**Key:** D

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 5 — Sampling: Consequence of crossing the Nyquist boundary

**Learning objective:** Explain why insufficient sampling can make sampled data represent a false lower frequency.

### Form A — `pre_sampling_below_nyquist`
What is the most likely consequence when the sampling frequency is reduced below twice the signal frequency?

A. The original analog frequency is always recovered exactly  
B. Aliasing may make the signal appear at a different frequency  
C. Only the signal amplitude changes  
D. The number of DFT bins automatically doubles

**Key:** B

### Form B — `post_sampling_above_nyquist`
Why is increasing Fs from below 2f to well above 2f useful when sampling a sinusoid?

A. It guarantees the signal amplitude becomes larger  
B. It makes every DFT coefficient identical  
C. It reduces the risk that the sampled data represent a false lower frequency  
D. It converts convolution into multiplication in time

**Key:** C

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 6 — Convolution: Output length

**Learning objective:** Apply the finite linear-convolution length rule, L + M - 1.

### Form A — `pre_convolution_length`
Two finite sequences contain 5 and 2 samples. How many samples are in their linear convolution?

A. 5  
B. 7  
C. 6  
D. 10

**Key:** C

### Form B — `post_convolution_length`
Two finite sequences contain 4 and 3 samples. How many samples are in their linear convolution?

A. 6  
B. 5  
C. 7  
D. 12

**Key:** A

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 7 — Convolution: Shifted-overlap sum of products

**Learning objective:** Explain the operation used to calculate one sample of discrete linear convolution.

### Form A — `pre_convolution_meaning`
Which expression best describes one sample of the discrete convolution y[n]?

A. The difference between the maximum values of x and h  
B. The average of all samples in x only  
C. The DFT magnitude of h  
D. A sum of products between x[k] and a shifted version of h[n-k]

**Key:** D

### Form B — `post_convolution_meaning`
To compute y[n] in discrete convolution, what operation is performed for a chosen shift n?

A. Subtract the two sequence lengths  
B. Multiply overlapping samples of x[k] and h[n-k], then add the products  
C. Keep only the largest input sample  
D. Average the DFT frequencies

**Key:** B

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 8 — DFT: Frequency-bin spacing

**Learning objective:** Compute DFT frequency-bin spacing, Δf = Fs/N.

### Form A — `pre_dft_bin_spacing`
Samples are taken at Fs = 8 kHz and an N = 64 point DFT is used. What is the frequency-bin spacing?

A. 125 Hz  
B. 64 Hz  
C. 500 Hz  
D. 8000 Hz

**Key:** A

### Form B — `post_dft_bin_spacing`
Samples are taken at Fs = 12 kHz and an N = 120 point DFT is used. What is the frequency-bin spacing?

A. 50 Hz  
B. 120 Hz  
C. 1000 Hz  
D. 100 Hz

**Key:** D

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 9 — DFT: Effect of N on bin spacing

**Learning objective:** Interpret how increasing the number of acquired samples at fixed Fs changes DFT bin spacing.

### Form A — `pre_dft_resolution`
With Fs unchanged, the number of acquired samples N is increased from 64 to 128. What happens to the DFT bin spacing?

A. It doubles  
B. It is halved  
C. It remains unchanged  
D. It becomes equal to N

**Key:** B

### Form B — `post_dft_resolution`
With Fs unchanged, the number of acquired samples N is increased from 80 to 160. What happens to the DFT bin spacing?

A. It doubles  
B. It remains unchanged  
C. It is halved  
D. It becomes equal to N

**Key:** C

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 10 — DFT: Bin alignment and leakage

**Learning objective:** Interpret the spectral pattern of a tone located on a DFT bin versus between DFT bins for the finite record used in the learning activity.

### Form A — `pre_dft_leakage`
A sinusoid lies between two DFT-bin frequencies. Which spectrum is most likely for the finite record used in this lab?

A. All spectral energy must remain at exactly one bin  
B. The sampling frequency becomes zero  
C. Energy appears across several neighboring bins rather than only one bin  
D. The time-domain amplitude becomes zero

**Key:** C

### Form B — `post_dft_leakage`
Compared with a tone located between DFT bins, a tone exactly aligned with one DFT bin generally shows what behavior?

A. Its spectral energy is more concentrated at the corresponding bin  
B. Its sampling frequency becomes lower  
C. Its time-domain amplitude must be zero  
D. Its convolution length increases

**Key:** A

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 11 — FIR: Passband/stopband interpretation relative to cutoff

**Learning objective:** Interpret whether a sinusoidal component lies well below or above a low-pass cutoff.

### Form A — `pre_fir_passband`
A low-pass FIR filter has a cutoff of 0.20Fs. Which sinusoidal component is most likely to be preserved more strongly?

A. 0.30Fs  
B. 0.40Fs  
C. 0.48Fs  
D. 0.08Fs

**Key:** D

### Form B — `post_fir_passband`
A low-pass FIR filter has a cutoff of 0.30Fs. Which sinusoidal component is most likely to be attenuated strongly?

A. 0.10Fs  
B. 0.45Fs  
C. 0.20Fs  
D. The DC component

**Key:** B

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Pair 12 — FIR: Tap count and transition-width trade-off

**Learning objective:** Explain the typical trade-off between FIR tap count, transition sharpness, and computational cost when cutoff is held fixed.

### Form A — `pre_fir_length`
When the cutoff frequency is fixed, what is a typical effect of increasing the number of FIR filter taps?

A. A sharper transition can be obtained, at the cost of more computation  
B. The filter automatically becomes high-pass  
C. The sampling frequency is reduced  
D. The impulse response becomes a single sample

**Key:** A

### Form B — `post_fir_length`
Two low-pass FIR filters have the same cutoff, but one uses many more taps. Which statement is most typical?

A. The longer filter must become a high-pass filter  
B. The longer filter always lowers the sampling rate  
C. The longer filter can no longer have an impulse response  
D. The longer filter can provide a narrower transition region but needs more computation

**Key:** D

Relevance A: ___  Clarity A: ___  Distractors A: ___  
Relevance B: ___  Clarity B: ___  Distractors B: ___  
A/B equivalence: ___  
Comments: ____________________________________________________________

---

# Global review

Please rate each item from 1–4 and add comments where useful.

| Criterion | Rating | Comment |
|---|---:|---|
| Coverage of the five DSP domains is appropriate for the intervention |  |  |
| Overall Form A difficulty appears suitable for the target undergraduates |  |  |
| Overall Form B difficulty appears suitable for the target undergraduates |  |  |
| Form A and Form B appear approximately equivalent in cognitive demand |  |  |
| Distractors are generally plausible and non-misleading |  |  |
| Terminology matches standard undergraduate DSP instruction |  |  |
| Twelve items per form is a reasonable testing burden |  |  |

## Final recommendation

Select one:

- [ ] Accept for pilot testing without revision
- [ ] Accept for pilot testing after minor revision
- [ ] Major revision required before pilot testing

### Items that should definitely be revised

____________________________________________________________________

### Concepts that are missing or overrepresented

____________________________________________________________________

### Additional comments on A/B equivalence

____________________________________________________________________

## Research-use note

The research team should retain reviewer codes, ratings, comments, and a revision log. In the manuscript, report the number and relevant expertise of reviewers, the review criteria, the content-validity summary used, and what was revised. Do not identify reviewers by name unless explicit permission and institutional policy allow it.
