---
authors: [bing-liu, harry-scells, "Wen Hua", "Genghong Zhao", guido-zuccon]
title: "ActiveEA: Active Learning for Neural Entity Alignment"
venue: The 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021)
year: 2021
pdf: /publications/pdfs/bing2021emnlp-al4ea.pdf
---


## Abstract

Entity Alignment (EA) aims to match equivalent entities across different Knowledge Graphs (KGs) and is an essential step of KG fusion. Current mainstream methods -- neural EA models -- rely on training with seed alignment, i.e., a set of pre-aligned entity pairs which are very costly to annotate. %How to reduce the labour cost of annotating entities remains to study. In this paper, we devise a novel Active Learning (AL) framework for neural EA, aiming to create highly informative seed alignment to obtain more effective EA models with less annotation cost. Our framework tackles two main challenges encountered when applying AL to EA: (1) How to exploit dependencies between entities within the AL strategy. Most AL strategies assume that the data instances to sample are independent and identically distributed. However, entities in KGs are related. To address this challenge, we propose a structure-aware uncertainty sampling strategy that can measure the uncertainty of each entity as well as its impact on its neighbour entities in the KG. (2) How to recognise entities that appear in one KG but not in the other KG (i.e., bachelors). Identifying bachelors would likely save annotation budget. To address this challenge, we devise a bachelor recognizer paying attention to alleviate the effect of sampling bias. Empirical results show that our proposed AL strategy can significantly improve sampling quality with good generality across different datasets, EA models and amount of bachelors.
