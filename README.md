# Coordination-Adjusted Architecture Selection for LLM Agent Systems

**Author:** Goutham Siripuram  
**Version:** 0.2.0

This repository accompanies the methodology preprint **Coordination-Adjusted Architecture Selection for LLM Agent Systems: A Reproducible Decision Model and Simulation Benchmark**.

## Scope
The model compares four architecture classes using six task properties: decomposability, specialization need, verification value, coordination burden, error-propagation risk, and resource sensitivity.

## Scientific status
The v0.2 coefficients are transparent **hypotheses**, not learned empirical constants. The bundled scenarios are synthetic design probes. Real benchmark calibration is required before predictive claims.

## Contents
- `src/agent_arch_select/` â€” v0.2 executable decision model.
- `scripts/generate_architecture_scenarios.py` â€” independently varied synthetic scenario generator.
- `data/` â€” synthetic scenarios.
- `notebooks/reproduce_results.ipynb` â€” sensitivity/recommendation notebook.
- `paper/` â€” LaTeX preprint source, BibTeX, and compiled PDF.
- `tests/` â€” validation tests.

## Run
```bash
python -m pip install -e ".[validation]"
python -m pytest -q
jupyter notebook notebooks/reproduce_results.ipynb
```

## Integrity note
Do not describe the coefficients as trained or validated on real agents. The internal seven-role review is AI-assisted internal QA, not independent human peer review.

## Publication status and limitations

Repository: https://github.com/GouthamSiripuram/agent-architecture-selection

This is an AI-assisted methodology and synthetic demonstration release, not a peer-reviewed or empirically validated model benchmark. See `SEVEN_ROLE_INTERNAL_REVIEW.md` for the internal review and `VALIDATION.md` for release checks.

The supplied `paper/main.pdf` is preserved, but its original build has unresolved citations because BibTeX was unavailable. Treat it as a draft. Rebuild from `paper/main.tex` and `paper/references.bib` with `pdflatex main`, `bibtex main`, then `pdflatex main` twice before paper submission.

