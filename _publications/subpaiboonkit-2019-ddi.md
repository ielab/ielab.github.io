---
authors: [sitthichoke-subpaiboonkit, "Xue Li", "Xin Zhao", harry-scells, guido-zuccon]
title: "Causality Discovery with Domain Knowledge for Drug-Drug Interactions Discovery"
venue: The 15th International Conference on Advanced Data Mining and Applications
year: 2019
pdf: /publications/pdfs/subpaiboonkit2019ddi.pdf
---

## Abstract

Bayesian Network Probability Graphs have recently been applied to the problem of discovery drug-drug interactions, i.e., the identification of drugs that, when consumed together, produce an unwanted side effect. These methods have the advantage of being explainable: the cause of the interaction is made explicit. 
However, they suffer from two intrinsic problems: (1) the high time-complexity for computing causation, i.e., this problem is NP-hard; and (2) the difficult identification of causality directions, i.e., it is difficult to identify in drug-drug interactions databases whether a drug causes an adverse effect -- or vice versa, an adverse effect causes a drug consumption. While solutions for addressing the causality direction identification exist, e.g., the CARD method, these assume statistical independence between drsug pairs considered for interaction: real data often does not satisfy this condition. 

In this paper, we propose a novel causality discovery algorithm for drug-drug interactions that goes beyond these limitations: Domain-knowledge-driven Causality Discovery (DCD). In DCD, a knowledge base that contains known drug-side effect pairs is used to prime a greedy drug-drug interaction algorithm that detects the drugs that, when consumed together, cause a side effect. This algorithm resolves the drug-drug interaction discovery problem in O(n^2) time and provides the causal direction of combined causes and their effect, without resorting to assuming statistical independence of drugs intake. 
Comprehensive experiments on real-world and synthetic datasets show the proposed method is more effective and efficient than current state-of-the-art solutions.
