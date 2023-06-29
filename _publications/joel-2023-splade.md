---
redirect_from: /publications/joel-2023-ictir-splade
authors: [joel-mackenzie, shengyao-zhuang, guido-zuccon]
title: 'Exploring the Representation Power of SPLADE Models'
venue: The Proceedings of the 2023 ACM SIGIR on International Conference on Theory of Information Retrieval (ICTIR 2023)
year: 2023
pdf: /publications/pdfs/joel2023splade.pdf
links:
 - url: https://github.com/ielab/understanding-splade
   name: Github
---
---
## Abstract
The SPLADE (SParse Lexical AnD Expansion) model is a highly effective approach to learned sparse retrieval, where documents are represented by term impact scores derived from large language models.
During training, SPLADE applies regularization to ensure postings lists are kept sparse --- with the aim of mimicking the properties of natural term distributions --- allowing efficient and effective lexical matching and ranking.
However, we hypothesize that SPLADE may encode additional signals into common postings lists to further improve effectiveness.
To explore this idea, we perform a number of empirical analyses where we re-train SPLADE with different, controlled vocabularies and measure how effective it is at ranking passages.
Our findings suggest that SPLADE can effectively encode useful ranking signals in documents even when the vocabulary is constrained to terms that are not traditionally useful for ranking, such as stopwords or even random words.
