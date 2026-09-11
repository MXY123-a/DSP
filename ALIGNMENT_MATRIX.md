# Experimental/Control Alignment Matrix

This matrix documents how the two study conditions are aligned while preserving the intended intervention contrast.

| Topic | Shared learning objective | Experimental condition (DSP-Lab) | Control condition (worksheet) | Target time | Main contrast |
|---|---|---|---|---|---|
| Discrete-time signals | Explain effects of amplitude/frequency/phase and identify basic sequence behavior | Manipulate signal parameters and inspect immediate waveform/summary changes | Read concept summary, study worked example, solve static comparison questions | 15–25 min | Dynamic visualization and parameter interaction |
| Sampling and aliasing | Apply Nyquist criterion and explain aliasing | Change sampling frequency and compare safe/boundary/aliasing cases with immediate output | Calculate Nyquist/alias cases and compare three static scenarios | 20–30 min | Interactive sampling exploration and immediate visual feedback |
| Convolution | Explain shifted overlap, multiplication, summation, and output length | Step through/inspect convolution cases and verify selected output samples | Hand-calculate short convolutions and explain smoothing example | 20–30 min | Interactive stepwise exploration versus written calculation |
| DFT and spectrum | Explain bin spacing, resolution, alignment, and leakage | Change N/frequency and observe spectra immediately | Calculate bin spacing and reason about bin-centered/non-centered examples | 20–30 min | Immediate spectrum response to parameter changes |
| FIR low-pass filtering | Explain cutoff/tap-count effects and passband/transition trade-offs | Change taps/cutoff and inspect impulse/frequency responses | Compare static filter designs and predict response trade-offs | 20–30 min | Interactive filter-response visualization |

## Shared elements

Both conditions should include:

- the same five DSP topic domains;
- comparable intended learning objectives;
- one structured activity per topic after the corresponding lecture;
- approximately similar expected study time;
- prediction/comparison/explanation at a basic conceptual level;
- a brief written summary/explanation component.

## Elements intentionally unique to the experimental condition

The DSP-Lab condition retains the features that constitute the intervention:

- mobile delivery;
- direct parameter manipulation;
- immediate waveform/spectrum/filter-response updates;
- rapid comparison of multiple parameter settings;
- app-based reflection submission;
- automatic learning-time and completion recording.

The control worksheets should not reproduce these features with another interactive simulator, MATLAB script, web visualization, or prerecorded parameter-sweep video during the intervention period, because doing so would weaken the intended condition contrast.

## Interpretation for the manuscript

A suitable Methods statement is:

> The control activities were aligned with the intervention in topic coverage, intended learning objectives, and approximate study time. They used conventional text-based explanations, worked examples, and written practice tasks, whereas the DSP-Lab condition additionally provided direct mobile parameter manipulation and immediate dynamic visualization. This design was intended to reduce differences in content exposure while preserving interactivity and visualization as defining characteristics of the intervention.
