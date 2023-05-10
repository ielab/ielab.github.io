---
authors: [shuai-wang, guido-zuccon]
title: "Balanced Topic Aware Sampling for Effective Dense Retriever: A Reproducibility Study"
venue: Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2023)
year: 2023
pdf: /publications/pdfs/shuai2023balancetrain.pdf
redirect_from: /shuai2023balancetrain
projects: [systematic-reviews]
links:
 - url: https://github.com/ielab/TAS-B-Reproduction
   name: Code
---

## Abstract
Knowledge distillation plays a key role in boosting the effectiveness of rankers based on pre-trained language models (PLMs); this is achieved using an effective but inefficient large model to teach a more efficient student model. In the context of knowledge distilla- tion for a student dense passage retriever, the balanced topic-aware sampling method has been shown to provide state-of-the-art ef- fectiveness. This method intervenes in the creation of the training batches by creating batches that contain positive-negative pairs of passages from the same topic, and balancing the pairwise margins of the positive and negative passages.
In this paper, we reproduce the balanced topic-aware sampling method; we do so for both the dataset used for evaluation in the original work (MS MARCO) and for a dataset in a different do- main, that of product search (Amazon shopping queries dataset) to study whether the original results generalize to a different context. We show that while we could not replicate the exact results from the original paper, we do confirm the original findings in terms of trends: balanced topic-aware sampling indeed leads to highly effec- tive dense retrievers. These results partially generalize to the other search task we investigate, product search: although we observe the improvements are less significant compared to MS MARCO.
In addition to reproducing the original results and studying how the method generalizes to a different dataset, we also investigate a key aspect that influences the effectiveness of the method: the use of a hard margin threshold for negative sampling. This aspect was not studied in the original paper. With respect to hard margins, we find that while setting different hard margin values significantly influences the effectiveness of the student model, this impact is dataset-dependent – and indeed, it does depend on the score distri- butions exhibited by retrieval models on the dataset at hand. Our reproducibility code is available at https://github.com/ielab/TAS-B-Reproduction.