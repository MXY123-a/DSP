# Control Review 02 — Sampling and Aliasing

**Target time:** 20–30 minutes

## Learning objective

Apply the Nyquist sampling criterion and explain why undersampling can make a high-frequency sinusoid appear as a lower-frequency sequence.

## Concept review

For a band-limited signal with highest frequency `Fmax`, the sampling frequency should be greater than twice that highest frequency to avoid aliasing:

`Fs > 2Fmax`.

If the sampling frequency is too low, different analog frequencies can produce the same sampled sequence. This ambiguity is called **aliasing**.

For a sinusoid, a useful way to identify a first-order alias is to find an equivalent frequency inside the interval from 0 to `Fs/2`.

## Worked example

A 2.5 kHz sinusoid is sampled at 4 kHz.

The Nyquist frequency is:

`Fs/2 = 2 kHz`.

Because 2.5 kHz is above 2 kHz, aliasing occurs. The apparent lower frequency is:

`|2.5 - 4| = 1.5 kHz`.

Therefore the sampled data can resemble a 1.5 kHz sinusoid.

## Practice

1. A signal contains no component above 3 kHz. Is `Fs = 8 kHz` sufficient to satisfy the Nyquist requirement? Explain.
2. Is `Fs = 5 kHz` sufficient for the same 3 kHz signal? Why or why not?
3. A 5 kHz sinusoid is sampled at 8 kHz. Determine the apparent lower alias frequency.
4. Why can increasing `Fs` from below `2f` to well above `2f` improve the fidelity of sampled data?

## Compare three cases

A 2 kHz sinusoid is considered under three sampling frequencies:

- Case A: `Fs = 6 kHz`
- Case B: `Fs = 4 kHz`
- Case C: `Fs = 3 kHz`

For each case:

1. calculate the Nyquist frequency `Fs/2`;
2. classify the case as comfortably above Nyquist, at the boundary, or below Nyquist;
3. state whether aliasing is expected;
4. for the below-Nyquist case, determine the apparent lower frequency.

## Short summary

In 2–3 sentences, explain why a sampled sinusoid can appear to have a frequency different from the original analog sinusoid when the sampling frequency is too low.
