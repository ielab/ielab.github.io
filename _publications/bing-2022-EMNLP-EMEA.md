---
title: "Guiding Neural Entity Alignment with Compatibility"
year: 2022
venue: 'EMNLP 2022'
authors: [bing-liu, harry-scells, "Wen Hua", guido-zuccon, "Genghong Zhao", "Xia Zhang"]
pdf: 
links:
 - url: https://github.com/uqbingliu/EMEA
   name: Code
---

## Abstract


Entity Alignment (EA) aims to find equivalent entities between two Knowledge Graphs (KGs).
While numerous neural EA models have been devised, they are mainly learned using labelled data only.
In this work, we argue that different entities within one KG should have compatible counterparts in the other KG due to the potential dependencies among the entities.
Making compatible predictions thus should be one of the goals of training an EA model along with fitting the labelled data: this aspect however is neglected in current methods.
To power neural EA models with compatibility, we devise a training framework by addressing three problems: (1) how to measure the compatibility of an EA model; (2) how to inject the property of being compatible into an EA model; (3) how to optimise parameters of the compatibility model.
Extensive experiments on widely-used datasets demonstrate the advantages of integrating compatibility within EA models. In fact, state-of-the-art neural EA models trained within our framework using just 5\% of the labelled data can achieve comparable effectiveness with supervised training using 20\% of the labelled data.  