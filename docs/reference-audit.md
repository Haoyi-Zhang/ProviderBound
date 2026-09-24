# Reference audit

This file records the final targeted metadata audit performed after the citation-count check. The bibliography still contains 54 entries and every key is cited, but count alone was not treated as evidence of correctness. High-risk recent, adjacent, and calibration entries were checked against publisher DOI pages, author repositories, or DBLP. The corrections below are mirrored in `paper/references.bib`, `external_resources.csv`, and the literature calibration where applicable.

| Key | Defect repaired | Verified record |
|---|---|---|
| `sad` | title and pages mismatched DOI | Version-level Third-Party Library Detection in Android Applications via Class Structural Similarity; EASE 2025, 604--615 (https://doi.org/10.1145/3756681.3756933) |
| `libhunter` | invented title attached to correct DOI | How Does Code Optimization Impact Third-party Library Detection for Android Applications?; ASE 2024, 1919--1931 (https://doi.org/10.1145/3691620.3695554) |
| `revisitcommon` | author given name and DOI incorrect | Timothée Riom; DOI 10.1016/j.jss.2019.04.065 (https://doi.org/10.1016/j.jss.2019.04.065) |
| `iccta` | DOI omitted | DOI 10.1109/ICSE.2015.48 (https://doi.org/10.1109/ICSE.2015.48) |
| `seal` | DOI omitted | DOI 10.1145/3585008 (https://doi.org/10.1145/3585008) |
| `raicc` | Alexandre Bartel omitted; DOI omitted | four authors; DOI 10.1109/ICSE43902.2021.00126 (https://doi.org/10.1109/ICSE43902.2021.00126) |
| `jucify` | six authors omitted; DOI omitted | nine authors; DOI 10.1145/3510003.3512766 (https://doi.org/10.1145/3510003.3512766) |
| `difuzer` | wrong coauthor and publication type; DOI omitted | Jordan Samhi, Li Li, Tegawendé F. Bissyandé, Jacques Klein; ICSE 2022; DOI 10.1145/3510003.3510135 (https://doi.org/10.1145/3510003.3510135) |
| `tamingreflection` | different paper title and incomplete author list attached to DOI | Taming Reflection: An Essential Step Toward Whole-program Analysis of Android Apps; six authors; TOSEM 30(3), article 32 (https://doi.org/10.1145/3440033) |

The audit does not assert that every interpretive sentence in the manuscript is a systematic-review result. It establishes bibliographic identity for the corrected records and preserves the 22-paper qualitative calibration as a separate, author-reviewable synthesis.
