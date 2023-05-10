---
authors: [shuai-wang, harry-scells, bevan-koopman, guido-zuccon]
title: "Neural Rankers for Effective Screening Prioritization in Medical Systematic Review Literature Search"
venue: "Australasian Document Computing Symposium (ADCS 2022)"
year: 2022
pdf: /publications/pdfs/shuai2022neuralsr.pdf
redirect_from: /shuai2022neuralsr
projects: [systematic-reviews]
---

## Abstract
Medical systematic reviews typically require that all the documents retrieved by a search are assessed. The reason is two-fold: the task aims for “total recall”; and documents retrieved using Boolean search are an unordered set and thus it is unclear how an assessor could examine only a subset. Screening prioritisation is the process of actually ranking the (unordered) set of retrieved documents, allowing assessors to begin the downstream processes of the systematic review creation earlier, leading to an earlier completion of the review; or even to avoid assesses documents ranked least relevant.
Screening prioritisation requires an highly effective ranking methods. Pre-trained language models are the state-of-the-art on many IR tasks, but have not been applied to the specific task of systematic review screening prioritisation. In this paper, we apply several pre-trained language models on the systematic review document ranking task, both directly and fine-tuned. An empirical analysis compares how effective neural methods compare to traditional methods for this task. We also investigate different types of document representations for neural methods and their impact on ranking performance.
Our results show that BERT-based rankers outperform the current state-of-the-art screening prioritisation methods. However, BERT rankers and existing methods can actually be complementary and thus further improvements may be achieved if used in conjunction.
