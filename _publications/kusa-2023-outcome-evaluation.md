---
redirect_from: /outcome-evaluation
authors: [wojciech-kusa, guido-zuccon, petr-knoth, allan-hanbury]
title: "Outcome-based Evaluation of Systematic Review Automation?"
venue: Proceedings of the the 13th International Conference on the Theory of Information Retrieval (ICTIR '23)
year: 2023
pdf: /publications/pdfs/kusa2023outcome-based-evaluation-ictir.pdf

---

## Abstract


Current methods for evaluating search strategies and automated citation screening of systematic literature reviews typically rely on counting the number of relevant publications (i.e. those to be included in the review) and not relevant publications (i.e. those to be excluded). Significant importance is put into promoting the retrieval of all relevant publications through great attention to recall-oriented measures, and demoting the retrieval of non-relevant publications through precision-oriented or cost metrics. This established practice, however, does not accurately reflect the reality of conducting a systematic review, because not all included publications have the same influence on the final outcome of the systematic review. More specifically, if an important publication gets excluded or included, this might significantly change the overall review outcome, while not including or excluding less influential studies may only have a limited impact. However, in terms of evaluation measures, all inclusion and exclusion decisions are treated equally and, therefore, failing to retrieve publications with little to no impact on the review outcome leads to the same decrease in recall as failing to retrieve crucial publications.
We propose a new evaluation framework that takes into account the impact of the reported study on the overall systematic review outcome. We demonstrate the framework by extracting review meta-analysis data and estimating outcome effects using predictions from ranking runs on systematic reviews of interventions from CLEF TAR 2019 shared task. We further measure how closely the obtained outcomes are to the outcomes of the original review if the arbitrary rankings were used. We evaluate 74 runs using the proposed framework and compare the results with those obtained using standard IR measures. We find that accounting for the difference in review outcomes leads to a different assessment of the quality of a system than if traditional evaluation measures were used. Our analysis provides new insights into the evaluation of retrieval results in the context of systematic review automation, emphasising the importance of assessing the usefulness of each document beyond binary relevance.
