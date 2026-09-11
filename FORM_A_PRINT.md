# DSP-Lab Concept Test — Form A

**Participant code:** ____________________    **Date:** ____________________

## Instructions

Choose the **one best answer** for each question. Work independently and follow the calculator policy stated by the instructor. Do not write your name or student number on this research form.

1. For a discrete sinusoid with the same sample count, what is the main effect of increasing its frequency parameter?
   - A. The peak amplitude must increase
   - B. More oscillations appear across the displayed samples
   - C. The mean must become positive
   - D. The sequence becomes an exponential

2. If the amplitude of a sinusoid is doubled while frequency and phase remain unchanged, what happens to its peak-to-peak value?
   - A. It is halved
   - B. It is unchanged
   - C. It doubles
   - D. It becomes zero

3. A band-limited signal contains no frequency above 3 kHz. Which sampling rate is safely above the Nyquist boundary?
   - A. 3 kHz
   - B. 5 kHz
   - C. 1.5 kHz
   - D. 8 kHz

4. A 3 kHz sinusoid is sampled at 4 kHz. What alias frequency is observed in the sampled sequence?
   - A. 1 kHz
   - B. 0.5 kHz
   - C. 3 kHz
   - D. 4 kHz

5. What is the most likely consequence when the sampling frequency is reduced below twice the signal frequency?
   - A. The original analog frequency is always recovered exactly
   - B. Aliasing may make the signal appear at a different frequency
   - C. Only the signal amplitude changes
   - D. The number of DFT bins automatically doubles

6. Two finite sequences contain 5 and 2 samples. How many samples are in their linear convolution?
   - A. 5
   - B. 7
   - C. 6
   - D. 10

7. Which expression best describes one sample of the discrete convolution y[n]?
   - A. The difference between the maximum values of x and h
   - B. The average of all samples in x only
   - C. The DFT magnitude of h
   - D. A sum of products between x[k] and a shifted version of h[n-k]

8. Samples are taken at Fs = 8 kHz and an N = 64 point DFT is used. What is the frequency-bin spacing?
   - A. 125 Hz
   - B. 64 Hz
   - C. 500 Hz
   - D. 8000 Hz

9. With Fs unchanged, the number of acquired samples N is increased from 64 to 128. What happens to the DFT bin spacing?
   - A. It doubles
   - B. It is halved
   - C. It remains unchanged
   - D. It becomes equal to N

10. A sinusoid lies between two DFT-bin frequencies. Which spectrum is most likely for the finite record used in this lab?
    - A. All spectral energy must remain at exactly one bin
    - B. The sampling frequency becomes zero
    - C. Energy appears across several neighboring bins rather than only one bin
    - D. The time-domain amplitude becomes zero

11. A low-pass FIR filter has a cutoff of 0.20Fs. Which sinusoidal component is most likely to be preserved more strongly?
    - A. 0.30Fs
    - B. 0.40Fs
    - C. 0.48Fs
    - D. 0.08Fs

12. When the cutoff frequency is fixed, what is a typical effect of increasing the number of FIR filter taps?
    - A. A sharper transition can be obtained, at the cost of more computation
    - B. The filter automatically becomes high-pass
    - C. The sampling frequency is reduced
    - D. The impulse response becomes a single sample
