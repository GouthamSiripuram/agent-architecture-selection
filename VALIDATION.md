# Publication validation

Python 3.12.14 on Windows.

## Tests

```text
....                                                                     [100%]
4 passed in 0.05s
```

## Notebook

All 2 code cells in `notebooks/reproduce_results.ipynb` executed successfully using an in-process IPython interpreter; outputs saved. A separate Jupyter kernel was not launched. Results describe synthetic demonstrations only.

## Data generation

`generate_architecture_scenarios.py` executed successfully. Generated `architecture_scenarios_v0_2.jsonl` matches the supplied records: True.

## Limits

The supplied paper PDF has unresolved citations; original PDF and source are preserved. No empirical model experiments or independent human peer review were performed.

## Environment

- pandas: 3.0.1
- pytest: 9.1.1
- nbformat: 5.11.1
- IPython: 9.17.1
