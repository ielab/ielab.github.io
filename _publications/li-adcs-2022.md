---
redirect_from: /publications/li-adcs-2022
authors: [hang-li, shengyao-zhuang, "Xueguang Ma", "Jimmy Lin", guido-zuccon]
title: "Pseudo-Relevance Feedback with Dense Retrievers in Pyserini"
venue: Proceedings of the 26th Australasian Document Computing Symposium (ADCS 2022)
year: 2022
pdf: /publications/pdfs/li2022adcs-vprf-demo.pdf
links:
 - url: https://github.com/castorini/pyserini/blob/master/docs/experiments-vector-prf.md
   name: Github
---
---
## Abstract

Transformer-based Dense Retrievers (DRs) are attracting extensive attention because of their effectiveness paired with high efficiency. In this context, few Pseudo-Relevance Feedback (PRF) methods applied to DRs have emerged. However, the absence of a general framework for performing PRF with DRs has made the empirical evaluation, comparison and reproduction of these methods challenging and time-consuming, especially across different DR models developed by different teams of researchers. 

To tackle this and speed up research into PRF methods for DRs, we showcase a new PRF framework that we implemented as a feature in \textit{Pyserini} -- an easy-to-use Python Information Retrieval toolkit. In particular, we leverage Pyserini's DR framework and expand it with a PRF framework that abstracts the PRF process away from the specific DR model used. This new functionality in Pyserini allows to easily experiment with PRF methods across different DR models and datasets. Our framework comes with a number of recently proposed PRF methods built into it. Experiments  within our framework show that this new PRF feature improves the effectiveness of the DR models currently available in Pyserini.