---
title: "Dependency-aware Self-training for Entity Alignment"
year: 2023
venue: 'WSDM 2023'
authors: [bing-liu, "Tiancheng Lan", "Wen Hua", guido-zuccon]
pdf: 
links:
 - url: https://github.com/uqbingliu/STEA
   name: Code
---

## Abstract


Entity Alignment (EA), which aims to detect entity mappings (i.e. equivalent entity pairs) in different Knowledge Graphs (KGs), is critical for KG fusion.
Neural EA methods dominate current EA research but still suffer from their reliance on labelled mappings.
To solve this problem, a few works have explored boosting the training of EA models with self-training, which adds confidently predicted mappings into the training data iteratively.
Though the effectiveness of self-training can be glimpsed in some specific settings, we still have very limited knowledge about it.
One reason is the existing works concentrate on devising EA models and only treat self-training as an auxiliary tool.
To fill this knowledge gap, we change the perspective to self-training to shed light on it.
In addition, the existing self-training strategies have limited impact because they introduce either much False Positive noise or a low quantity of True Positive pseudo mappings.
To improve self-training for EA, we propose exploiting the dependencies between entities, a particularity of EA, to suppress the noise without hurting the recall of True Positive mappings.
Through extensive experiments, we show that the introduction of dependency makes the self-training strategy for EA reach a new level.
The value of self-training in alleviating the reliance on annotation is actually much higher than what has been realised.
Furthermore, we suggest future study on smart data annotation to break the ceiling of EA performance.
