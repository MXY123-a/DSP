# Control Review 01 — Discrete-Time Signals

**Target time:** 15–25 minutes

## Learning objective

Explain how signal type and parameters such as amplitude, frequency, and phase affect a discrete-time sequence.

## Concept review

A discrete-time sinusoid can be written as

`x[n] = A sin(ωn + φ)`.

- `A` controls amplitude.
- `ω` controls how rapidly the sequence oscillates across sample index `n`.
- `φ` shifts the phase of the sinusoid.
- The peak-to-peak value of an ideal sinusoid is approximately `2A`.

Other common discrete-time signals include the unit impulse, unit step, and exponential sequence. Their shapes are determined by their definitions rather than by sinusoidal frequency.

## Worked example

Consider

`x[n] = 2 sin(0.3πn)`.

If the amplitude changes from 2 to 4 while the frequency term remains unchanged:

- the locations of peaks and zero crossings do not change;
- the vertical scale doubles;
- the peak-to-peak value changes from approximately 4 to approximately 8.

If instead the frequency term increases while amplitude remains 2, the sequence completes more oscillations over the same number of displayed samples.

## Practice

1. A sinusoid has amplitude 1.5. What is its approximate peak-to-peak value?
2. If only the phase changes, should the amplitude of the sinusoid change? Explain briefly.
3. Two discrete sinusoids have equal amplitude and sample count. Signal B completes more cycles across the sample range than Signal A. Which signal has the larger frequency parameter?
4. Which of the following is most directly associated with one nonzero sample at `n = 0`: sinusoid, unit impulse, unit step, or exponential?

## Compare and explain

Suppose Signal A is

`xA[n] = sin(0.2πn)`

and Signal B is

`xB[n] = 3 sin(0.2πn)`.

Write two sentences explaining what is the same and what is different between the two sequences.

Then compare

`xC[n] = sin(0.5πn)`

with Signal A. Explain which parameter changed and what qualitative waveform difference you would expect.

## Short summary

In 2–3 sentences, explain how changing **amplitude** differs from changing **frequency** in a discrete-time sinusoid.
