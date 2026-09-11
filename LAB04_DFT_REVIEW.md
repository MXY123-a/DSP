# Control Review 04 — DFT and Spectrum

**Target time:** 20–30 minutes

## Learning objective

Explain DFT frequency-bin spacing, the effect of transform length on frequency resolution, and the difference between bin-centered tones and spectral leakage.

## Concept review

For an `N`-point DFT of data sampled at frequency `Fs`, the spacing between adjacent frequency bins is

`Δf = Fs / N`.

When `Fs` is fixed, increasing `N` decreases `Δf`, providing a finer frequency grid.

A sinusoid whose frequency exactly matches a DFT-bin frequency tends to concentrate its spectral energy at that bin. A sinusoid that lies between bin frequencies generally spreads energy across several neighboring bins; this behavior is associated with **spectral leakage**.

## Worked example

Suppose

`Fs = 10 kHz`

and

`N = 100`.

Then

`Δf = 10000 / 100 = 100 Hz`.

So the DFT grid contains frequencies such as 0, 100, 200, ... Hz.

A 1000 Hz sinusoid lies exactly on bin 10. A 1050 Hz sinusoid lies between bins 10 and 11, so its energy is less concentrated in a single bin.

## Practice

1. Calculate `Δf` for `Fs = 8 kHz` and `N = 40`.
2. Keeping `Fs = 8 kHz`, calculate `Δf` for `N = 80`.
3. Which of the two DFT lengths above provides the finer frequency grid?
4. If `Δf = 125 Hz`, is a 1000 Hz sinusoid bin-centered? Show the bin index.
5. With the same `Δf`, would a 1060 Hz sinusoid be bin-centered? What qualitative spectral behavior would you expect?

## Compare and explain

For a fixed sampling frequency, compare an `N = 32` DFT with an `N = 128` DFT.

Write down:

- which one has smaller bin spacing;
- which one gives the finer frequency grid;
- whether increasing `N` automatically eliminates spectral leakage for an arbitrary sinusoid;
- why a non-bin-centered tone can still leak even when `N` is large.

## Short summary

In 2–3 sentences, distinguish **frequency-bin spacing/resolution** from **spectral leakage**. Explain why they are related to different aspects of the DFT.
