---
redirect_from: /publications/arvin-2021-arxiv-tildev2
authors: [shengyao-zhuang, guido-zuccon]
title: 'Fast Passage Re-ranking with Contextualized Exact Term Matching and Efficient Passage Expansion'
venue: Arxiv preprint
year: 2021
links:
 - url: https://arxiv.org/pdf/2108.08513.pdf
   name: Arvix
 - url: https://github.com/ielab/TILDE/tree/main/TILDEv2
   name: Github
---
---
## Abstract
BERT-based information retrieval models are expensive, in both time (query latency) and computational resources (energy, hardware cost), making many of these models impractical especially under resource constraints. The reliance on a query encoder that only performs tokenization and on the pre-processing of passage representations at indexing, has allowed the recently proposed TILDE method to overcome the high query latency issue typical of BERT-based models.  This however is at the expense of a lower effectiveness compared to other BERT-based re-rankers and dense retrievers. In addition, the original TILDE method is characterised by indexes with a very high memory footprint, as it expands each passage into the size of the BERT vocabulary.

In this paper, we propose TILDEv2, a new model that stems from the original TILDE but that addresses its limitations.
	TILDEv2 relies on contextualized exact term matching with expanded passages. This requires to only store in the index the score of tokens that appear in the expanded passages (rather than all the vocabulary), thus producing indexes that are 99% smaller than those of TILDE. This matching mechanism also improves ranking effectiveness by 24%, without adding to the query latency. This makes TILDEv2 the state-of-the-art passage re-ranking method for CPU-only environments, capable of maintaining query latency below 100ms on commodity hardware.
	
One potential drawback of TILDEv2, compared to the original TILDE, is the extra passage expansion process required at indexing. This is an expensive process if performed using current passage expansion methods. However, we address this by adapting the original TILDE model to serve as a passage expansion method. Compared to current expansion methods, our proposed method reduces the passage expansion time by 98% with only less than 1% effectiveness loss on the MS MARCO passage ranking dataset (and even improvements on other datasets). We further show that our expansion approach generalises to other ranking methods that rely on expansion. 