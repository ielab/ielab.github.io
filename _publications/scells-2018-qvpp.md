---
authors: [harry-scells, leif-azzopardi, guido-zuccon, bevan-koopman]
title: "Query Variation Performance Prediction for Systematic Reviews"
venue: The 41st International ACM SIGIR Conference on Research & Development in Information Retrieval
year: 2018
pdf: /publications/pdfs/scells2018qvpp.pdf
---

## Abstract

When conducting systematic reviews, medical researchers heavily deliberate over the final query to pose to the information retrieval system. Given the possible query variations that they could construct, selecting the best performing query is difficult.
This motivates a new type of query performance prediction (QPP) task where the challenge is to estimate the performance of a set of query variations given a particular topic. Query variations are the reductions, expansions and modifications of a given seed query under the hypothesis that there exists some variations (either generated from permutations or hand crafted) which will improve retrieval effectiveness over the original query. We use the CLEF 2017 TAR Collection, to evaluate sixteen pre and post retrieval predictors for the task of Query Variation Performance Prediction (QVPP).
Our findings show the IDF based QPPs exhibits the strongest correlations with performance. However, when using QPPs to select the best query, little improvement over the original query can be obtained, despite the fact that there are query variations which perform significantly better. Our findings highlight the difficulty in identifying effective queries within the context of this new task, and motivates further research to develop more accurate methods to help systematic review researchers in the query selection process.