# arXiv submission metadata

Title: Coordination-Adjusted Architecture Selection for LLM Agent Systems: A Reproducible Decision Model and Local Model Case Study

Author: Goutham Siripuram

Affiliation: Independent Researcher (author to confirm at submission).

Suggested primary category: cs.MA (Multiagent Systems), because the core subject is coordinated agent architectures and their tradeoffs.

Suggested secondary category: cs.AI (Artificial Intelligence). No cs.LG cross-list is proposed: this release does not fit a learning model. Classification recommendation follows https://arxiv.org/category_taxonomy and remains subject to arXiv moderation.

## Abstract

This paper proposes an executable linear architecture decision model over six normalized task descriptors and four agent-architecture classes. Its coefficients are hand-specified hypotheses. We retain 48 seeded synthetic scenarios for sensitivity analysis and add 720 actual local episodes with two small Hugging Face checkpoints on 12 GSM8K questions. Four concrete configurations share a 512-generated-token budget, with three seeds and controlled tool-fault conditions. Across the eight clean model–configuration cells, exact-answer success ranges from 0/36 to 13/36 attempts. A frozen question-only proxy rubric evaluates the unchanged selector against constant-architecture policies using observed accuracy and generated-token use. The rubric selects planner–executor–verifier for 11 of 12 questions and hierarchical orchestration for one. This is a limited test of one operationalization, not calibration of the descriptors or coefficients. Released traces, task-cluster uncertainty, and observed-utility regret make unfavorable outcomes and identification limits inspectable. No general advantage for additional agents is claimed.

## Comments

Methodology preprint with synthetic demonstrations and a local model case study; software v0.4.0. 10 pages including references. Shared empirical data and source code are available in the repository.

## License recommendation

Recommend arXiv's non-exclusive distribution license for this submission, subject to the author's choice and any future venue requirements. The repository retains its existing license. No license selection has been submitted on the author's behalf. Review https://info.arxiv.org/help/license/index.html before choosing.

Keywords: LLM agents; multi-agent systems; architecture selection; coordination overhead; sensitivity analysis; synthetic simulation.

GitHub repository: https://github.com/GouthamSiripuram/agent-architecture-selection

## AI-assistance disclosure recommendation

Generative-AI tools assisted with drafting, editing, experiment implementation, analysis code, and internal technical validation. Goutham Siripuram is the sole human author and is responsible for the manuscript, software, references, and scientific claims. AI assistance and the internal review do not constitute independent peer review.

Status: prepared for author review and manual submission. Not submitted to arXiv; no arXiv identifier or project DOI exists in this release metadata. Moderation and endorsement, if requested, remain arXiv decisions.
