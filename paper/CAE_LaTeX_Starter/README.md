# CAE LaTeX Starter

Target journal:
Computer Applications in Engineering Education (CAE), Wiley.

This is a practical authoring starter prepared to match the current CAE author instructions.
It is NOT a journal-specific official class file.

Current CAE preparation points reflected here:
- Double-blind peer review: keep the main manuscript anonymous.
- Submit title page separately.
- Main file order: title, abstract, keywords, main text, references, tables, figure legends, appendices when relevant.
- Abstract: no more than 250 words.
- Keywords: five.
- Figures are normally supplied as separate files.
- Data availability statement should be included.
- Acknowledgments/funding belong on the title page when they could identify the authors.

Official Wiley LaTeX template:
https://authors.wiley.com/author-resources/Journal-Authors/Prepare/new-journal-design.html

Official WileyDesign.zip direct package URL:
https://authors.wiley.com/asset/WileyDesign.zip

CAE Author Guidelines:
https://onlinelibrary.wiley.com/page/journal/10990542/homepage/forauthors.html

Suggested files:
- main_anonymous.tex : manuscript sent for double-blind review
- title_page.tex     : separate identifying title page
- references.bib     : BibTeX database

Compilation:
pdflatex main_anonymous
bibtex main_anonymous
pdflatex main_anonymous
pdflatex main_anonymous

For the current DSP-Lab-Android project, the section structure is intentionally tailored to:
platform design + five DSP modules + quasi-experimental/pre-post evaluation + learning outcomes.
