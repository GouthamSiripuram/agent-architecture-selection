# arXiv submission metadata

Title: Coordination-Adjusted Architecture Selection for LLM Agent Systems: A Reproducible Decision Model and Simulation Benchmark

Author: Goutham Siripuram

Affiliation: Independent Researcher (author to confirm at submission).

Suggested primary category: cs.MA (Multiagent Systems), because the core subject is coordinated agent architectures and their tradeoffs.

Suggested secondary category: cs.AI (Artificial Intelligence). No cs.LG cross-list is proposed: this release does not fit a learning model. Classification recommendation follows https://arxiv.org/category_taxonomy and remains subject to arXiv moderation.

## Abstract

Choosing an LLM agent architecture requires assumptions about the value of decomposition, specialization, and verification relative to coordination, error propagation, and resource costs. This paper proposes an executable linear decision model over six normalized task descriptors and four architecture classes. All coefficients are hand-specified design hypotheses. A seeded generator supplies 48 synthetic scenarios with independently sampled features, and a sensitivity analysis reports how the resulting recommendations change with resource aversion. These calculations describe the behavior of the specified model; they do not measure agent performance or establish which architecture is best in practice. We make the coefficient table, tie policy, reproduction procedure, and identification limitations explicit, and outline training, held-out evaluation, and baseline comparisons needed for empirical calibration. The contribution is a transparent decision-model template and simulation artifact, not an empirically validated architecture selector.

## Comments

6 pages, including references; methodology preprint with reproducible synthetic demonstrations; software v0.3.0. No real-agent empirical validation. Source code and data available at the repository below.

## License recommendation

Recommend arXiv's non-exclusive distribution license for this submission, subject to the author's choice and any future venue requirements. The repository retains its existing license. No license selection has been submitted on the author's behalf. Review https://info.arxiv.org/help/license/index.html before choosing.

Keywords: LLM agents; multi-agent systems; architecture selection; coordination overhead; sensitivity analysis; synthetic simulation.

GitHub repository: https://github.com/GouthamSiripuram/agent-architecture-selection

## AI-assistance disclosure recommendation

Generative-AI tools assisted with drafting, editing, code review, and internal technical validation. Goutham Siripuram is the sole human author and is responsible for the manuscript, software, references, and scientific claims. AI assistance and the internal review do not constitute independent peer review.

Status: prepared for author review and manual submission. Not submitted to arXiv; no arXiv identifier or project DOI exists in this release metadata. Moderation and endorsement, if requested, remain arXiv decisions.
