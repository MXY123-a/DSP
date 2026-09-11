# DSP-Lab Concept Test — Form B

**Participant code:** ____________________    **Date:** ____________________

## Instructions

Choose the **one best answer** for each question. Work independently and follow the calculator policy stated by the instructor. Do not write your name or student number on this research form.

1. With amplitude, phase, and sample count unchanged, what happens when the frequency parameter of a discrete sinusoid is reduced?
   - A. Its peak-to-peak value must become zero
   - B. Its amplitude automatically doubles
   - C. Fewer oscillations appear across the displayed samples
   - D. It becomes a unit impulse

2. A sinusoid has amplitude A. If its amplitude is changed to 3A while frequency and phase stay fixed, how does its peak-to-peak value change?
   - A. It becomes three times as large
   - B. It stays the same
   - C. It becomes twice as large
   - D. It becomes one third as large

3. A band-limited signal contains no frequency above 4 kHz. Which sampling rate is safely above the Nyquist boundary?
   - A. 5 kHz
   - B. 10 kHz
   - C. 7 kHz
   - D. 4 kHz

4. A 6 kHz sinusoid is sampled at 8 kHz. At what lower frequency will it appear after aliasing?
   - A. 1 kHz
   - B. 6 kHz
   - C. 8 kHz
   - D. 2 kHz

5. Why is increasing Fs from below 2f to well above 2f useful when sampling a sinusoid?
   - A. It guarantees the signal amplitude becomes larger
   - B. It makes every DFT coefficient identical
   - C. It reduces the risk that the sampled data represent a false lower frequency
   - D. It converts convolution into multiplication in time

6. Two finite sequences contain 4 and 3 samples. How many samples are in their linear convolution?
   - A. 6
   - B. 5
   - C. 7
   - D. 12

7. To compute y[n] in discrete convolution, what operation is performed for a chosen shift n?
   - A. Subtract the two sequence lengths
   - B. Multiply overlapping samples of x[k] and h[n-k], then add the products
   - C. Keep only the largest input sample
   - D. Average the DFT frequencies

8. Samples are taken at Fs = 12 kHz and an N = 120 point DFT is used. What is the frequency-bin spacing?
   - A. 50 Hz
   - B. 120 Hz
   - C. 1000 Hz
   - D. 100 Hz

9. With Fs unchanged, the number of acquired samples N is increased from 80 to 160. What happens to the DFT bin spacing?
   - A. It doubles
   - B. It remains unchanged
   - C. It is halved
   - D. It becomes equal to N

10. Compared with a tone located between DFT bins, a tone exactly aligned with one DFT bin generally shows what behavior?
    - A. Its spectral energy is more concentrated at the corresponding bin
    - B. Its sampling frequency becomes lower
    - C. Its time-domain amplitude must be zero
    - D. Its convolution length increases

11. A low-pass FIR filter has a cutoff of 0.30Fs. Which sinusoidal component is most likely to be attenuated strongly?
    - A. 0.10Fs
    - B. 0.45Fs
    - C. 0.20Fs
    - D. The DC component

12. Two low-pass FIR filters have the same cutoff, but one uses many more taps. Which statement is most typical?
    - A. The longer filter must become a high-pass filter
    - B. The longer filter always lowers the sampling rate
    - C. The longer filter can no longer have an impulse response
    - D. The longer filter can provide a narrower transition region but needs more computation
