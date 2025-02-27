---
authors: [xinyu-mao, "Teerapong Leelanupab", harry-scells, guido-zuccon]
title: "DenseReviewer: A Screening Prioritisation Tool for Systematic Review based on Dense Retrieval"
venue: Proceedings of the 47th European Conference on Information Retrieval (ECIR 2025)
year: 2025
pdf: /publications/pdfs/mao2025densereviewer.pdf
redirect_from: /mao2025densereviewer
projects: [systematic-reviews]
---

## Abstract

Screening is a time-consuming and labour-intensive yet required task for medical systematic reviews, as tens of thousands of studies often need to be screened. Prioritising relevant studies to be screened allows downstream systematic review creation tasks to start earlier and save time. In previous work, we developed a dense retrieval method to prioritise relevant studies with reviewer feedback during the title and abstract screening stage. 

Our method outperforms previous active learning methods in both effectiveness and efficiency. In this demo, we extend this prior work by creating (1) a web-based screening tool that enables end-users to screen studies exploiting state-of-the-art methods and (2) a Python library that integrates models and feedback mechanisms and allows researchers to develop and demonstrate new active learning methods. We describe the tool's design and showcase how it can aid screening. 

The tool is available at https://densereviewer.ielab.io. The source code is also open sourced at https://github.com/ielab/densereviewer.