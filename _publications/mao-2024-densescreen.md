---
authors: [xinyu-mao, shengyao-zhuang, bevan-koopman, guido-zuccon]
title: "Dense Retrieval with Continuous Explicit Feedback for Systematic Review Screening Prioritisation"
venue: Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2024)
year: 2024
pdf: /publications/pdfs/mao2024densescreen.pdf
redirect_from: /mao2024densescreen
projects: [systematic-reviews]
---

## Abstract

The goal of screening prioritisation in systematic reviews is to identify relevant documents with high recall and rank them in early positions for review. This saves reviewing effort if paired with a stopping criterion, and speeds up review completion if performed alongside downstream tasks. Recent studies have shown that neural models have good potential on this task, but their time-consuming fine-tuning and inference discourage their widespread use for screening prioritisation. 

In this paper, we propose an alternative approach that still relies on neural models, but leverages dense representations and relevance feedback to enhance screening prioritisation, without the need for costly model fine-tuning and inference. This method exploits continuous relevance feedback from reviewers during document screening to efficiently update the dense query representation, which is then applied to rank the remaining documents to be screened. We evaluate this approach across the CLEF TAR datasets for this task. Results suggest that the investigated dense query-driven approach is more efficient than directly using neural models and shows promising effectiveness compared to previous methods developed on the considered datasets. 

Our code is available at https://github.com/ielab/dense-screening-feedback.
