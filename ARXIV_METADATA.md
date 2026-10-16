# arXiv metadata — author review required

Title: Question-Only Selection of Bounded Reasoning Workflows: Baselines, Budget Transfer, and a Local Evaluation

Authors: Goutham Siripuram; Akshitha Mulastam

Author contributions: Both authors contributed equally to this work.

Suggested primary category: cs.AI
Suggested secondary category: cs.LG (subject to arXiv classification)

Abstract:
Choosing a reasoning workflow from a question requires evidence that selection improves on a simpler fixed policy. We evaluate a question-only ridge baseline against a training-selected constant workflow using two local checkpoints, four workflows, two seeds, separate GSM8K training and test cohorts, and SVAMP transfer questions. The 4,096 recorded executions include a larger output-allowance condition on GSM8K. At the primary 512-token allowance, router-minus-constant utility is -0.00894 for Qwen3 and -0.04075 for Qwen2.5; the study does not establish a consistent routing advantage. A separately specified parsing heuristic also changes the interpretation of Qwen2.5 workflow rankings. The contribution is a constrained negative evaluation with explicit training isolation, budget transfer, and scoring sensitivity, rather than a new routing algorithm. The results motivate checking simple baselines and outcome definitions before attributing gains to workflow selection.

Comments: 7 pages, 1 figure. Local benchmark evaluation; code and execution records accompany the research release.

License recommendation: CC BY 4.0 for the manuscript, consistent with TMLR submission licensing. Author must select the license. Third-party assets retain their upstream licenses.

Keywords: workflow selection; language models; local inference; evaluation; scoring sensitivity

GitHub repository: https://github.com/GouthamSiripuram/agent-architecture-selection

AI-assistance disclosure: Generative AI assisted drafting, code development, editing, and internal technical validation. The human authors are responsible for the manuscript and its scientific claims. This assistance is not independent peer review.

Status: prepared preprint; not submitted to arXiv or TMLR. No arXiv ID or DOI has been assigned. The anonymous review template's standard header does not mean a submission has occurred.
