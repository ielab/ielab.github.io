---
authors: [anton-van-der-vegt, guido-zuccon, bevan-koopman]
title: "Learning Inter-Sentence, Disorder-Centric, Biomedical Relationships from Medical Literature"
venue: AMIA'19 Proceedings
year: 2019
pdf: /publications/pdfs/vandervegt-2019-AMIA.pdf
links: 
 - url: http://ielab-data.uqcloud.net/dataset/2019-amia-learning-relationships
   name: Download site for crowd-sourced biomedical relationship label data
---

## Abstract

Relationships between disorders and their associated tests, treatments and symptoms underpin essential information needs of clinicians and can support biomedical knowledge bases, information retrieval and ultimately clinical decision support. These relationships exist in the biomedical literature, however they are not directly available and have to be extracted from the text.  Existing, automated biomedical relationship extraction methods tend to be narrow in scope, e.g., protein-protein interactions, and pertain to intra-sentence relationships. The proposed approach targets intra and inter-sentence, disorder-centric relationship extraction. It employs an LSTM deep learning model that utilises a novel, sequential feature set, including medical concept embeddings. The LSTM model outperforms rule based and co-occurrence models by at least +78% in F1 score, suggesting that inter-sentence relationships are an important subset of all disorder-centric relations and that our approach shows promise for inter-sentence relationship extraction in this and possibly other domains.
