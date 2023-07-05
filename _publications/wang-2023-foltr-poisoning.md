---
redirect_from: /foltr-poisoning
authors: [shuyi-wang, guido-zuccon]
title: "An Analysis of Untargeted Poisoning Attack and Defense Methods for Federated Online Learning to Rank Systems"
venue: Proceedings of the 2023 ACM SIGIR International Conference on the Theory of Information Retrieval (ICTIR ’23)
year: 2023
pdf: /publications/pdfs/wang2023foltr-poisoning.pdf

---

## Abstract

Federated online learning to rank (FOLTR) aims to preserve user privacy by not sharing their searchable data and search interactions, while guaranteeing high search effectiveness, especially in contexts where individual users have scarce training data and interactions. For this, FOLTR trains learning to rank models in an online manner -- i.e. by exploiting users' interactions with the search systems (queries, clicks), rather than labels -- and federatively -- i.e. by not aggregating interaction data in a central server for training purposes, but by training instances of a model on each user device on their own private data, and then sharing the model updates, not the data, across a set of users that have formed the federation. Existing FOLTR methods build upon advances in federated learning.

While federated learning methods have been shown effective at training machine learning models in a distributed way without the need of data sharing, they can be susceptible to attacks that target either the system's security or its overall effectiveness. 

In this paper, we consider attacks on FOLTR systems that aim to compromise their search effectiveness. Within this scope, we experiment with and analyse data and model poisoning attack methods to showcase their impact on FOLTR search effectiveness. We also explore the effectiveness of defense methods designed to counteract attacks on FOLTR systems. We contribute an understanding of the effect of attack and defense methods for FOLTR systems, as well as identifying the key factors influencing their effectiveness.
