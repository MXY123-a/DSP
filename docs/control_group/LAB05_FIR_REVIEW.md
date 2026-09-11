# Control Review 05 — FIR Low-Pass Filtering

**Target time:** 20–30 minutes

## Learning objective

Explain the role of cutoff frequency and filter length in an FIR low-pass filter, and relate these settings to passband preservation, high-frequency attenuation, transition width, and computational cost.

## Concept review

A low-pass FIR filter is designed to preserve low-frequency components while attenuating higher-frequency components.

Two important design variables are:

- **cutoff frequency** — determines the approximate boundary between frequencies intended to pass and frequencies intended to be attenuated;
- **number of taps** — controls the length of the impulse response.

For a fixed sampling frequency and comparable design method, increasing the number of taps can often produce a narrower transition region and stronger separation between passband and stopband, but it also increases computation and delay.

## Worked example

Suppose two low-pass FIR filters have the same cutoff frequency:

- Filter A:  nine taps
- Filter B:  forty-one taps

Filter B generally has more freedom to approximate the desired low-pass response and can therefore produce a sharper transition than Filter A. However, each output sample requires more multiply-accumulate operations.

A low-frequency sinusoid well below the cutoff should be preserved more strongly than a sinusoid well above the cutoff.

## Practice

1. For a low-pass filter, which frequency region is primarily preserved: below or above the cutoff?
2. If a sinusoid is far above the low-pass cutoff, should its output amplitude normally be larger, similar, or smaller than its input amplitude?
3. Two FIR filters use the same cutoff, but one has substantially more taps. State one likely benefit and one cost of the longer filter.
4. What happens to the impulse-response length when the number of FIR taps increases?

## Compare and explain

Consider two low-pass FIR designs operating at the same sampling frequency:

- Design A: cutoff = 1 kHz, 15 taps
- Design B: cutoff = 1 kHz, 55 taps

For each statement below, indicate which design is more likely to satisfy it, then explain why:

1. narrower transition from passband to stopband;
2. lower computational cost;
3. longer impulse response;
4. greater processing delay.

Now compare Design B with a third filter that also has 55 taps but a cutoff of 2 kHz. Explain which frequency range would be preserved by the third filter that may have been attenuated by Design B.

## Short summary

In 2–3 sentences, explain how **cutoff frequency** and **number of taps** affect different aspects of an FIR low-pass filter.
