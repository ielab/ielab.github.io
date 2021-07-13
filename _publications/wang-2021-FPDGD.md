---
redirect_from: /FPDGD
authors: [shuyi-wang, bing-liu, shengyao-zhuang, guido-zuccon]
title: "Effective and Privacy-preserving Federated Online Learning to Rank"
venue: The Proceedings of the 2021 ACM SIGIR on International Conference on Theory of Information Retrieval (ICTIR 2021)
year: 2021
pdf: /publications/pdfs/wang2021fpdgd.pdf
links:
 - url: https://github.com/ielab/fpdgd-ictir2021
   name: Github
 - url: https://youtu.be/akT2EFBTs3g
   name: Presentation on Youtube 
---

## Abstract

Online Learning to Rank (OLTR) has been primarily studied in the centralised setting, where a central server is responsible to index the searchable data, collect the users’ queries and search interactions, and optimize ranking models. A drawback of such as a centralised OLTR paradigm is that it cannot guarantee user’s privacy as all data (both the searchable one and the one related to user interactions) is collected by the server.

In this paper, we propose a Federated OLTR method, called FPDGD, which leverages the state-of-the-art Pairwise Differentiable Gradient Descent (PDGD) and casts it with the Federated Averaging framework. For a strong privacy guarantee, we further introduce a noise-adding clipping technique based on the theory of differential privacy to be used in combination with FPDGD.

Empirical evaluation shows FPDGD significantly outperforms the only other federated OLTR method. In addition, FPDGD is more robust across different privacy guarantee requirements than the current method: our method is therefore more reliable for real-life applications.
