package com.zichun2000.dsplab.lab

data class AssessmentItem(
    val id: String,
    val question: String,
    val options: List<String>,
    val correctIndex: Int
)

object LearningAssessment {
    /**
     * Form A and Form B are parallel 12-item instruments aligned with Labs 01–05.
     * They assess the same concepts with different wording/numbers to reduce recall
     * effects when the post-test is taken after the learning activities.
     *
     * Before pilot testing, the paired items were refined to keep cognitive demand
     * comparable across forms and the correct-option positions were balanced (3 A,
     * 3 B, 3 C, and 3 D in each form) to reduce answer-position bias.
     */
    val preItems = listOf(
        // Lab 01 · Discrete-time signals (2)
        AssessmentItem(
            "pre_signal_frequency",
            "For a discrete sinusoid with the same sample count, what is the main effect of increasing its frequency parameter?",
            listOf(
                "The peak amplitude must increase",
                "More oscillations appear across the displayed samples",
                "The mean must become positive",
                "The sequence becomes an exponential"
            ),
            1
        ),
        AssessmentItem(
            "pre_signal_amplitude",
            "If the amplitude of a sinusoid is doubled while frequency and phase remain unchanged, what happens to its peak-to-peak value?",
            listOf(
                "It is halved",
                "It is unchanged",
                "It doubles",
                "It becomes zero"
            ),
            2
        ),

        // Lab 02 · Sampling and aliasing (3)
        AssessmentItem(
            "pre_sampling_nyquist",
            "A band-limited signal contains no frequency above 3 kHz. Which sampling rate is safely above the Nyquist boundary?",
            listOf(
                "3 kHz",
                "5 kHz",
                "1.5 kHz",
                "8 kHz"
            ),
            3
        ),
        AssessmentItem(
            "pre_sampling_alias_frequency",
            "A 3 kHz sinusoid is sampled at 4 kHz. What alias frequency is observed in the sampled sequence?",
            listOf(
                "1 kHz",
                "0.5 kHz",
                "3 kHz",
                "4 kHz"
            ),
            0
        ),
        AssessmentItem(
            "pre_sampling_below_nyquist",
            "What is the most likely consequence when the sampling frequency is reduced below twice the signal frequency?",
            listOf(
                "The original analog frequency is always recovered exactly",
                "Aliasing may make the signal appear at a different frequency",
                "Only the signal amplitude changes",
                "The number of DFT bins automatically doubles"
            ),
            1
        ),

        // Lab 03 · Discrete convolution (2)
        AssessmentItem(
            "pre_convolution_length",
            "Two finite sequences contain 5 and 2 samples. How many samples are in their linear convolution?",
            listOf(
                "5",
                "7",
                "6",
                "10"
            ),
            2
        ),
        AssessmentItem(
            "pre_convolution_meaning",
            "Which expression best describes one sample of the discrete convolution y[n]?",
            listOf(
                "The difference between the maximum values of x and h",
                "The average of all samples in x only",
                "The DFT magnitude of h",
                "A sum of products between x[k] and a shifted version of h[n-k]"
            ),
            3
        ),

        // Lab 04 · DFT and spectrum (3)
        AssessmentItem(
            "pre_dft_bin_spacing",
            "Samples are taken at Fs = 8 kHz and an N = 64 point DFT is used. What is the frequency-bin spacing?",
            listOf(
                "125 Hz",
                "64 Hz",
                "500 Hz",
                "8000 Hz"
            ),
            0
        ),
        AssessmentItem(
            "pre_dft_resolution",
            "With Fs unchanged, the number of acquired samples N is increased from 64 to 128. What happens to the DFT bin spacing?",
            listOf(
                "It doubles",
                "It is halved",
                "It remains unchanged",
                "It becomes equal to N"
            ),
            1
        ),
        AssessmentItem(
            "pre_dft_leakage",
            "A sinusoid lies between two DFT-bin frequencies. Which spectrum is most likely for the finite record used in this lab?",
            listOf(
                "All spectral energy must remain at exactly one bin",
                "The sampling frequency becomes zero",
                "Energy appears across several neighboring bins rather than only one bin",
                "The time-domain amplitude becomes zero"
            ),
            2
        ),

        // Lab 05 · FIR low-pass filtering (2)
        AssessmentItem(
            "pre_fir_passband",
            "A low-pass FIR filter has a cutoff of 0.20Fs. Which sinusoidal component is most likely to be preserved more strongly?",
            listOf(
                "0.30Fs",
                "0.40Fs",
                "0.48Fs",
                "0.08Fs"
            ),
            3
        ),
        AssessmentItem(
            "pre_fir_length",
            "When the cutoff frequency is fixed, what is a typical effect of increasing the number of FIR filter taps?",
            listOf(
                "A sharper transition can be obtained, at the cost of more computation",
                "The filter automatically becomes high-pass",
                "The sampling frequency is reduced",
                "The impulse response becomes a single sample"
            ),
            0
        )
    )

    val postItems = listOf(
        // Lab 01 · Discrete-time signals (2)
        AssessmentItem(
            "post_signal_frequency",
            "With amplitude, phase, and sample count unchanged, what happens when the frequency parameter of a discrete sinusoid is reduced?",
            listOf(
                "Its peak-to-peak value must become zero",
                "Its amplitude automatically doubles",
                "Fewer oscillations appear across the displayed samples",
                "It becomes a unit impulse"
            ),
            2
        ),
        AssessmentItem(
            "post_signal_amplitude",
            "A sinusoid has amplitude A. If its amplitude is changed to 3A while frequency and phase stay fixed, how does its peak-to-peak value change?",
            listOf(
                "It becomes three times as large",
                "It stays the same",
                "It becomes twice as large",
                "It becomes one third as large"
            ),
            0
        ),

        // Lab 02 · Sampling and aliasing (3)
        AssessmentItem(
            "post_sampling_nyquist",
            "A band-limited signal contains no frequency above 4 kHz. Which sampling rate is safely above the Nyquist boundary?",
            listOf(
                "5 kHz",
                "10 kHz",
                "7 kHz",
                "4 kHz"
            ),
            1
        ),
        AssessmentItem(
            "post_sampling_alias_frequency",
            "A 6 kHz sinusoid is sampled at 8 kHz. At what lower frequency will it appear after aliasing?",
            listOf(
                "1 kHz",
                "6 kHz",
                "8 kHz",
                "2 kHz"
            ),
            3
        ),
        AssessmentItem(
            "post_sampling_above_nyquist",
            "Why is increasing Fs from below 2f to well above 2f useful when sampling a sinusoid?",
            listOf(
                "It guarantees the signal amplitude becomes larger",
                "It makes every DFT coefficient identical",
                "It reduces the risk that the sampled data represent a false lower frequency",
                "It converts convolution into multiplication in time"
            ),
            2
        ),

        // Lab 03 · Discrete convolution (2)
        AssessmentItem(
            "post_convolution_length",
            "Two finite sequences contain 4 and 3 samples. How many samples are in their linear convolution?",
            listOf(
                "6",
                "5",
                "7",
                "12"
            ),
            0
        ),
        AssessmentItem(
            "post_convolution_meaning",
            "To compute y[n] in discrete convolution, what operation is performed for a chosen shift n?",
            listOf(
                "Subtract the two sequence lengths",
                "Multiply overlapping samples of x[k] and h[n-k], then add the products",
                "Keep only the largest input sample",
                "Average the DFT frequencies"
            ),
            1
        ),

        // Lab 04 · DFT and spectrum (3)
        AssessmentItem(
            "post_dft_bin_spacing",
            "Samples are taken at Fs = 12 kHz and an N = 120 point DFT is used. What is the frequency-bin spacing?",
            listOf(
                "50 Hz",
                "120 Hz",
                "1000 Hz",
                "100 Hz"
            ),
            3
        ),
        AssessmentItem(
            "post_dft_resolution",
            "With Fs unchanged, the number of acquired samples N is increased from 80 to 160. What happens to the DFT bin spacing?",
            listOf(
                "It doubles",
                "It remains unchanged",
                "It is halved",
                "It becomes equal to N"
            ),
            2
        ),
        AssessmentItem(
            "post_dft_leakage",
            "Compared with a tone located between DFT bins, a tone exactly aligned with one DFT bin generally shows what behavior?",
            listOf(
                "Its spectral energy is more concentrated at the corresponding bin",
                "Its sampling frequency becomes lower",
                "Its time-domain amplitude must be zero",
                "Its convolution length increases"
            ),
            0
        ),

        // Lab 05 · FIR low-pass filtering (2)
        AssessmentItem(
            "post_fir_passband",
            "A low-pass FIR filter has a cutoff of 0.30Fs. Which sinusoidal component is most likely to be attenuated strongly?",
            listOf(
                "0.10Fs",
                "0.45Fs",
                "0.20Fs",
                "The DC component"
            ),
            1
        ),
        AssessmentItem(
            "post_fir_length",
            "Two low-pass FIR filters have the same cutoff, but one uses many more taps. Which statement is most typical?",
            listOf(
                "The longer filter must become a high-pass filter",
                "The longer filter always lowers the sampling rate",
                "The longer filter can no longer have an impulse response",
                "The longer filter can provide a narrower transition region but needs more computation"
            ),
            3
        )
    )

    // Kept for dashboard fallback compatibility; both forms contain the same number of items.
    val prePostItems: List<AssessmentItem> = preItems

    fun score(items: List<AssessmentItem>, answers: Map<String, Int>): Int =
        items.count { answers[it.id] == it.correctIndex }
}
