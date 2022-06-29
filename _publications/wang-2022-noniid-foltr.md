---
redirect_from: /noniid-foltr
authors: [shuyi-wang, guido-zuccon]
title: "Is Non-IID Data a Threat in Federated Online Learning to Rank?"
venue: Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '22)
year: 2022
pdf: /publications/pdfs/wang2022noniidfoltr.pdf

---

## Abstract

In this perspective paper we study the effect of non independent and identically distributed (non-IID) data on federated online learning to rank (FOLTR) and chart directions for future work in this new and largely unexplored research area of Information Retrieval.  In the FOLTR process, clients join a federation to jointly create an effective ranker from the implicit click signal originating in each client, without the need to share data (documents, queries, clicks). A well-known factor that affects the performance of federated learning systems, and that poses serious challenges to these approaches, is the fact that there may be some type of bias in the way the data is distributed across clients. While FOLTR systems are on their own rights a type of federated learning system, the presence and effect of non-IID data in FOLTR has not been studied. To this aim, we first enumerate possible data distribution settings that may showcase data bias across clients and thus give rise to the non-IID problem. Then, we study the impact of each of these settings on the performance of the current state-of-the-art FOLTR approach, the Federated Pairwise Differentiable Gradient Descent (FPDGD), and we highlight which data distributions may pose a problem for FOLTR methods. We also explore how common approaches proposed in the federated learning literature address non-IID issues in FOLTR. This allows us to unveil new research gaps that, we argue, future research in FOLTR should consider. This is an important contribution to the current state of the field of FOLTR because, for FOLTR systems to be deployed, the factors affecting their performance, including the impact of non-IID data, need to thoroughly be understood.
