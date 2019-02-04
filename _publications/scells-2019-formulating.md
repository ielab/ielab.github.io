---
authors: [harry-scells, guido-zuccon, bevan-koopman]
title: "Automatic Boolean Query Refinement for Systematic Review Literature Search "
venue: Proceedings of The Web Conference 2019
year: 2019
pdf: /publications/pdfs/scells2019refining.pdf
projects: [systematic-reviews] 
---

*This is a pre-print version of the accepted paper.*

In the medical domain, systematic reviews are a highly trustworthy evidence source used to inform clinical diagnosis and treatment, and governmental policy making. Systematic reviews must be complete in that _all relevant_ literature for the research question of the review must be synthesised in order to produce a recommendation. To identify the literature to screen for inclusion in systematic reviews, information specialists construct complex Boolean queries that capture the information needs defined by the research questions of the systemic review. 
However, in the quest for total recall, these Boolean queries return many non relevant results.

In this paper, we propose automatic methods for Boolean query refinement in the context of systematic review literature retrieval with the aim of alleviating this high recall-low precision problem. To do this, we build upon current literature and define additional semantic transformations for Boolean queries in the form of query expansion and reduction. Empirical evaluation is done on a set of real systematic review queries to show how our method performs in a realistic setting.
We found that query refinement strategies produced queries that were more effective than the original in terms of six information retrieval evaluation measures. In particular, queries were refined  to increase precision, while maintaining, or even increasing, recall --- this, in turn, translates into both time and cost savings when creating laborious and expensive systematic reviews.