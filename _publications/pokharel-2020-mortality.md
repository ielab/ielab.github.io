---
authors: [suresh-pokharel, "Zhenkun Shi", guido-zuccon, "Yu Li"]
title: "Discriminative Features Generation for Mortality Prediction in ICU"
venue: International Conference on Advanced Data Mining and Applications
year: 2020
pdf: 
---

## Abstract

Effective methods for mortality prediction for Intensive Care Unit (ICU) patients assist health professionals by producing alerts ahead of time regarding the critical changing degeneration of a patient’s health. This can guide health professionals to take immediate interventions to rescue the lives of patients. However, existing methods only use raw clinical features and ignore the compound information exhibited by Electronic Health Records (EHRs) data, i.e., the co-occurrence of different clinical events at the same point of time (or within a short time interval). In this paper we use a recently proposed method, called Temporal Tree, to capture the compound information and use them as discriminative features. In addition, to test the impact of preserving temporal information, we capture compound information in terms of patient situations (i.e., the patient’s medical condition at particular point of time), and represent a patient as a sequence of patient situations. This is contrasted with the baseline approach of representing a patient by the associated sequence of clinical events (bag-of-words like). These representations are further processed to obtain low dimensional embeddings used to represent patients and their situations.
The effectiveness of the proposed methods is evaluated using a real ICU dataset with nine different baselines and state-of-the-art classifiers. The empirical results show the Temporal Tree method is able to generate discriminative patient representations. Classifiers that exploited the compounded information significantly improved the quality of ICU mortality predictions, in all cases and across both bag-of-words (up to 7.814% improvements) and patient situations representations (up to 2.720% improvements).