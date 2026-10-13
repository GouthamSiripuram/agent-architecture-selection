# Coordination-Adjusted Architecture Selection for LLM Agent Systems: A Reproducible Decision Model and Simulation Benchmark

**Author: Goutham Siripuram | Version: 0.3.0**

**Scientific status: proposed methodology with synthetic demonstrations only.** No bundled numbers are measurements of real LLMs or deployed agents. The current preprint is prepared for author review and manual arXiv submission; it has not been submitted to arXiv, and no arXiv ID or DOI is claimed.

The decision model compares four conceptual architecture classes using six normalized task descriptors. Coefficients are hand-specified hypotheses. Recommendation counts describe the simulation, not real architecture superiority or predictive accuracy.

## Paper and submission files

- [Compiled preprint](paper/main.pdf)
- [Self-contained arXiv source ZIP](submission/agent_architecture_selection_arxiv_submission.zip)
- [arXiv metadata](ARXIV_METADATA.md)
- [Bibliography verification](BIBLIOGRAPHY_AUDIT.md) and [claim audit](CLAIM_AUDIT.md)
- [Validation record](VALIDATION.md) and [release notes](RELEASE_NOTES.md)

Suggested primary category: **cs.MA**, with **cs.AI** as a secondary category. The author must review the manuscript and arXiv-generated PDF before manually submitting. Technical readiness does not imply acceptance or empirical validation.

## Reproduce the calculations

Use Python 3.12 for the recorded environment (the package supports Python >=3.10). From the repository root:

```bash
python -m venv .venv
# Activate .venv using your platform's activation command.
python -m pip install -r requirements-reproduction.txt
python -m pip install -e .
python -m pytest -q
python scripts/reproduce_paper.py
```

The last command regenerates the manuscript tables, sensitivity figure, and machine-readable summaries in `results/`. Direct reproduction dependencies are version-pinned; this is not a full transitive lockfile. Optional interactive notebook support is available with `python -m pip install -e ".[validation]"`, then `jupyter notebook notebooks/reproduce_results.ipynb`.

Run `python scripts/generate_architecture_scenarios.py` to regenerate the 48 scenarios using seed 260907. Independent draws remove the earlier hard-wired feature coupling; they do not establish independence of real task properties.

## Build the paper

From `paper/`, use a standard LaTeX installation:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The release uses Tectonic 0.17.0 (automatic bibliography and LaTeX reruns): `tectonic --untrusted --keep-logs --keep-intermediates main.tex`. The source uses standard article/LaTeX packages and PDF figures. Submission ZIPs include `main.bbl` as well as `references.bib`.

## How to cite

Use [CITATION.cff](CITATION.cff) or cite: Goutham Siripuram (2026), *Coordination-Adjusted Architecture Selection for LLM Agent Systems: A Reproducible Decision Model and Simulation Benchmark*, methodology preprint and software, version 0.3.0, https://github.com/GouthamSiripuram/agent-architecture-selection. Cite the exact commit used when no release tag is available. No DOI should be added until one is actually issued.

## Provenance and limitations

Generative-AI tools assisted with drafting, editing, code review, and internal technical validation. Goutham Siripuram is the sole human author and is responsible for the claims and artifacts. The seven-role AI-assisted internal review is **not independent human peer review**.

The original [internal review](SEVEN_ROLE_INTERNAL_REVIEW.md) remains unchanged. Earlier build warnings, draft sources/PDF, and validation records are preserved in `validation/v0.2.0/`; their historical status does not describe the rebuilt v0.3.0 paper. Real-agent studies, calibration, and independent evaluation remain future work.
