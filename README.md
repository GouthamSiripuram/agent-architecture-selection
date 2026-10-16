# Question-Only Selection of Bounded Reasoning Workflows: Baselines, Budget Transfer, and a Local Evaluation

Authors: Goutham Siripuram and Akshitha Mulastam (equal contribution). Research revision **0.5.0**. Prepared preprint and submission materials; **not submitted to arXiv or TMLR**, and not peer reviewed.

Choosing a reasoning workflow from a question requires evidence that selection improves on a simpler fixed policy. We evaluate a question-only ridge baseline against a training-selected constant workflow using two local checkpoints, four workflows, two seeds, separate GSM8K training and test cohorts, and SVAMP transfer questions. The 4,096 recorded executions include a larger output-allowance condition on GSM8K. At the primary 512-token allowance, router-minus-constant utility is -0.00894 for Qwen3 and -0.04075 for Qwen2.5; the study does not establish a consistent routing advantage. A separately specified parsing heuristic also changes the interpretation of Qwen2.5 workflow rankings. The contribution is a constrained negative evaluation with explicit training isolation, budget transfer, and scoring sensitivity, rather than a new routing algorithm. The results motivate checking simple baselines and outcome definitions before attributing gains to workflow selection.

## Evidence and limits

This revision uses actual local Qwen3-0.6B and Qwen2.5-1.5B-Instruct executions on public arithmetic benchmark questions. It is a bounded case study, not production or enterprise validation. Earlier synthetic demonstrations remain synthetic and are preserved in the original directories and Git history. The v0.4 pilot is historical and is not pooled into v0.5 primary results. The related paper shares research ancestry and software but has different primary tasks and interventions.

## Files and reproduction

- [Preprint PDF](submission/v0.5.0/agent_architecture_selection_preprint.pdf)
- [Self-contained arXiv source](submission/v0.5.0/agent_architecture_selection_arxiv_submission.zip)
- [Execution evidence and frozen code](submission/v0.5.0/agent_architecture_selection_tmlr_supplement.zip)
- [Validation report](study_v05/FINAL_VALIDATION.md)
- [arXiv metadata](ARXIV_METADATA.md)

Extract the evidence ZIP into a separate directory. It contains completed records, unchanged source hashes, task data, dependency versions, provenance and notices. Install requirements-lock.txt in an isolated environment. Run `python -m pytest test_research.py test_analysis.py`, then `python analysis.py --study architecture`. This recomputes results without inference. Full local-inference instructions are in its README. Never overwrite supplied records or run duplicate GPU jobs.

The published source ZIP compiled independently. Identified and anonymous PDFs have been visually checked. An anonymous review PDF is supplied separately to the author; the public preprint is not the anonymous upload. Author review and submission declarations remain required. Technical checks do not guarantee acceptance.

## Citation and authorship

Cite Goutham Siripuram and Akshitha Mulastam, *Question-Only Selection of Bounded Reasoning Workflows: Baselines, Budget Transfer, and a Local Evaluation*, research software/preprint revision 0.5.0, 2026, this repository. See CITATION.cff. No DOI or arXiv ID has been assigned.

Goutham Siripuram and Akshitha Mulastam contributed equally to this work. Generative AI assisted drafting, code development, editing and internal technical validation; the human authors are responsible for the manuscript and its scientific claims. The historical seven-role AI review was not independent human peer review. Original code remains under the repository MIT license; third-party material retains its notices. Manuscript licensing is an author submission decision; CC BY 4.0 is recommended for TMLR compatibility.
