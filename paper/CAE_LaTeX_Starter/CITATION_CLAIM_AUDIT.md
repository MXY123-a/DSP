# Citation-to-claim audit for the CAE manuscript

Last checked: 2026-09-11

Purpose: keep every substantive literature claim in the manuscript no stronger than the evidence in the cited source. This file is an internal writing aid, not part of the submitted manuscript.

## Publication-positioning guardrail

The paper should **not** claim that DSP-Lab is the first mobile DSP application, the first interactive DSP teaching tool, or the first controlled evaluation of software in DSP education. Prior work already includes Web-based J-DSP, a conventional-comparison DSP instructional-software study, a Windows DSP teaching toolkit, Android AJDSP, and Jupyter–Python DSP teaching. The defensible novelty is narrower: a compact **after-class self-directed mobile intervention**, five concept-focused modules, a **topic-matched conventional-review control condition**, parallel concept-test forms, and a prespecified baseline-adjusted primary analysis.

## Core source audit

| Key | Verified source | What the source directly supports | Safe manuscript use | Do not overclaim |
|---|---|---|---|---|
| `spanias2005` | IEEE Transactions on Education 48(4), 735–749. DOI: 10.1109/TE.2005.854569 | J-DSP is a Web-based interactive DSP simulation/laboratory environment used with undergraduate laboratory exercises. | Foundational precedent for interactive/remote DSP learning. | Do not cite it alone as proof that mobile learning improves achievement. |
| `alajlouni2010` | Computer Applications in Engineering Education 18(4), 703–708. DOI: 10.1002/cae.20275 | Interactive instructional software for an undergraduate DSP course was compared with conventional teaching. | Direct precedent for a comparison-based DSP educational evaluation. | Do not call the present study the first controlled DSP software study; do not state randomization unless verified from the full method. |
| `joseph2017` | Computer Applications in Engineering Education 25(3), 530–541. DOI: 10.1002/cae.21819 | A Windows Store teaching aid included convolution, FFT, FIR design, and DSP-processor modules; student feedback was positive. | Direct precedent for a multipurpose undergraduate DSP teaching toolkit. | Positive feedback is not equivalent to a controlled learning-effect estimate. |
| `ranganath2019` | Computers in Education Journal 10(2), 2019; verified through Arizona State University record and ASEE journal PDF. | AJDSP is an Android DSP environment supporting signal generation/analysis/processing, convolution, Fourier transforms, z-transform, and filter design; quantitative and qualitative assessments were reported. | Direct mobile-DSP predecessor and strong reason not to claim platform novelty. | No DOI was confirmed; do not invent one. Do not describe its assessment as a matched-control learning trial without evidence. |
| `zuniga2020` | Computer Applications in Engineering Education 28, 1045–1057. DOI: 10.1002/cae.22277 | Jupyter–Python notebooks combined theoretical material, code, simulations, and graphical output for undergraduate DSP learning. | Precedent for integrated code/simulation/visualization in a DSP course. | Do not cite it as evidence for the specific causal effect of a mobile intervention. |
| `sung2016` | Computers & Education 94, 252–275. DOI: 10.1016/j.compedu.2015.11.008 | Meta-analysis of 110 experimental/quasi-experimental journal articles; moderate mean effect of mobile-device integration (reported effect size 0.523). | Broad evidence that mobile-device integration can support learning. | Do not imply the effect transfers automatically to DSP-Lab or to every implementation. |
| `garzon2025` | Computers & Education 238, 105415. DOI: 10.1016/j.compedu.2025.105415 | Meta-analysis of 253 empirical studies; large positive average learning effect and high heterogeneity. | Recent broad mobile-learning evidence and justification for testing the specific intervention rather than assuming effectiveness. | Do not omit heterogeneity when using the large average effect to motivate the study. |
| `zhang2023` | Computer Applications in Engineering Education 31, 620–633. DOI: 10.1002/cae.22604 | Mobile learning was integrated with a SPOC-based flipped-classroom design in an engineering course; final-exam and questionnaire outcomes improved. | Recent CAE example showing mobile learning embedded in a structured engineering-course design. | The intervention was bundled; do not attribute all improvement uniquely to mobile learning. |
| `singh2021` | Computer Applications in Engineering Education 29(1), 229–243. DOI: 10.1002/cae.22333 | Experimental study with 65 engineering students, treatment n=33 and control n=32; VR electronics-lab training improved reported knowledge, motivation, and cognition relative to conventional teaching. | Strong engineering-education example of a technology intervention evaluated against a conventional control. | It is VR/electronics-lab training, not DSP or after-class mobile learning. |
| `nolen2018` | IEEE Transactions on Education 61(3), 226–233. DOI: 10.1109/TE.2018.2791445 | Virtual and physical engineering laboratory projects were compared; engagement/motivation differed and results were interpreted through instructional affordances. | Supports an affordance-based interpretation rather than technology novelty. | Do not cite it as a direct causal learning-achievement result for DSP. |
| `potkonjak2016` | Computers & Education 95, 309–327. DOI: 10.1016/j.compedu.2016.02.002 | Review of virtual laboratories for science, technology, and engineering education. | Broad background on virtual-lab design, access, and technological approaches. | Avoid assigning a single quantitative learning effect to this review. |
| `reeves2021` | Journal of Science Education and Technology 30(1), 16–30. DOI: 10.1007/s10956-020-09866-0 | Systematic review of 25 empirical V-Lab studies (2009–2019); identified limited theoretical/methodological variety and many principally evaluative studies narrowly focused on content-knowledge change. | Supports the argument that technology-supported laboratory research benefits from stronger design/theoretical alignment and careful evaluation. | Do not use third-party metadata that incorrectly lists the article as issue 6; DOI/publisher metadata support 30(1), 16–30. |
| `li2024` | PLOS ONE 19(12), e0316269. DOI: 10.1371/journal.pone.0316269 | Meta-analysis included 46 studies from 22 publications; overall Hedges' g=0.686 (95% CI 0.414–0.959); authors state virtual labs do not completely replace hands-on labs and are valuable auxiliary tools. | Supports positive engineering virtual-lab effects and the complementary—not replacement—positioning. | Do not generalize the meta-analytic estimate directly to mobile DSP conceptual learning. |
| `freeman2014` | PNAS 111(23), 8410–8415. DOI: 10.1073/pnas.1319030111 | Meta-analysis of 225 undergraduate STEM studies; active learning improved examination/concept-inventory performance on average. | Broad pedagogical rationale for active student engagement. | It does not validate the specific DSP-Lab learning cycle or establish which component causes any DSP-Lab effect. |
| `balamuralithara2009` | Computer Applications in Engineering Education 17(1), 108–118. DOI: 10.1002/cae.20186 | Review of simulation and remote laboratories and key issues in engineering education. | Historical engineering virtual-lab framing. | Online-first year was 2008, but the journal volume citation is 2009; retain 2009 in BibTeX. |

## Current manuscript claims checked against source evidence

### Safe as currently phrased

- J-DSP as a browser/Web-based DSP simulation and undergraduate laboratory precedent.
- Al-Ajlouni et al. as an undergraduate DSP instructional-software study compared with conventional teaching.
- Joseph et al. as a Windows DSP teaching toolkit covering convolution, FFT, and FIR design.
- AJDSP as a direct Android/mobile DSP predecessor with broad DSP simulation functions and educational assessment.
- Jupyter–Python notebooks as a DSP teaching environment combining theory, code, simulation, and graphical output.
- Sung et al. as a 110-study mobile-learning meta-analysis with a moderate average effect.
- Garzón et al. as a 253-study meta-analysis reporting positive average gains with high heterogeneity.
- Singh et al. as a 65-student controlled electronics-engineering VR study.
- Reeves and Crippen as evidence that much virtual-lab research was principally evaluative and methodologically/theoretically narrow.
- Li and Liang as evidence that virtual laboratories show positive engineering-education effects but should not be treated as complete replacements for hands-on laboratories.

### Wording to keep deliberately conservative

1. Say **“supports the plausibility of the approach”**, not “proves DSP-Lab will improve learning.”
2. Say **“direct mobile-DSP predecessor”** for AJDSP, not “the only prior mobile DSP tool.”
3. Say **“comparison-based”** for Al-Ajlouni et al. unless the exact allocation method is confirmed from the full text.
4. Say **“reported improved outcomes in an integrated mobile/SPOC design”** for Zhang et al., not “mobile learning caused the improvement.”
5. Treat questionnaire satisfaction/usefulness as secondary perception evidence, not as evidence of learning effectiveness.
6. Keep the primary novelty in the **study design and instructional positioning**, not in claiming a new algorithm or a first-ever mobile implementation.

## Final pre-submission audit procedure

Before submission, for every entry in `references.bib`:

1. Open the publisher/DOI record and verify author order, title, journal, year, volume, issue, pages/article number, and DOI.
2. Search the manuscript for every citation key and check that the surrounding sentence is supported by the cited source.
3. Remove uncited bibliography entries and citations that do not materially support a claim.
4. For a claim involving a numerical sample size/effect size, verify the number in the original article or publisher abstract, not a secondary webpage.
5. Preserve the distinction among platform description, student perception, observational association, quasi-experimental comparison, randomized comparison, systematic review, and meta-analysis.

This audit is intentionally conservative because the manuscript's credibility depends more on precise claim-to-source matching than on a long reference list.
