---
authors: [harry-scells, guido-zuccon]
title: "Generating Better Queries for Systematic Reviews"
venue: The 41st International ACM SIGIR Conference on Research & Development in Information Retrieval
year: 2018
pdf: /publications/pdfs/scells2018generating.pdf
---

## Abstract

Systematic reviews form the cornerstone of evidence based medicine, aiming to answer complex medical questions based on all evidence currently available. Key to the effectiveness of a systematic review is an (often large) Boolean query used to search large publication repositories. These Boolean queries are carefully crafted by researchers and information specialists, and often reviewed by a panel of experts. However, little is known about the effectiveness of the Boolean queries at the time of formulation.

In this paper we investigate whether a better Boolean query than that defined in the protocol of a systematic review, can be created, and we develop methods for the transformation of a given Boolean query into a more effective one. Our approach involves defining possible transformations of Boolean queries and their clauses. It also involves casting the problem of identifying a transformed query that is better than the original into: (i) a classification problem; and (ii) a learning to rank problem. Empirical experiments are conducted on a real set of systematic reviews. Analysis of results shows that query transformations that are better than the original queries do exist, and that our approaches are able to select more effective queries from the set of possible transformed queries so as to maximise different target effectiveness measures.
