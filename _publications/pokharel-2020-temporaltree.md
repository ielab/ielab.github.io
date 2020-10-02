---
authors: [suresh-pokharel, "Guido Zuccon", "Xue Li", "Chandra Prasetyo Utomo", "Yu Li"]
title: "Temporal Tree Representation for Similarity Computation between Medical Patients"
venue: Artificial Intelligence in Medicine
year: 2020
pdf: 
---

## Abstract

Objective
The aim of this study is to compute similarities between patient records in an electronic health record (EHR). This is an important problem because the availability of effective methods for the computation of patient similarity would allow for assistance with and automation of tasks such as patients stratification, medical prognosis and cohort selection, and for unlocking the potential of medical analytics methods for healthcare intelligence. However, health data in EHRs presents many challenges that make the automatic computation of patient similarity difficult; these include: temporal aspects, multivariate, heterogeneous and irregular data, and data sparsity.

Materials and methods
We propose a new method for EHR data representation called Temporal Tree: a temporal hierarchical representation which, based on temporal co-occurrence, preserves the compound information found at different levels in health data. In addition, this representation is augmented using the doc2vec embedding technique which here is exploited for patient similarity computation. We empirically investigate our proposed method, along with several state-of-the-art benchmarks, on a dataset of real world Intensive Care Unit (ICU) EHRs, for the task of identifying patients with a specific target diagnosis.

Results
Our empirical results show that the Temporal Trees representation is significantly better than other traditional and state-of-the-art methods for representing patients and computing their similarities.

Conclusion
Temporal trees capture the temporal relationships between medical, hierarchical data: this enables to effectively model the rich information provided within EHRs and thus the identification of similar patients.