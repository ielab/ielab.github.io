---
authors: [suresh-pokharel, "Guido Zuccon", "Yu Li"]
title: "Representing EHRs with Temporal Tree and Sequential Pattern Mining for Similarity Computing"
venue: International Conference on Advanced Data Mining and Applications
year: 2020
pdf: 
---

## Abstract

The ability to rapidly identify at scale patients that are similar based on their electronic medical records (EHRs) is fundamental for a number of clinical informatics applications, such as clinical decision support, cohort selection, treatment recommendation, among others. 
The effective representation of EHR data is paramount to effective computational similarity methods. Such representation would take into account the complex properties of EHR data including temporality and multivariaty. Of critical importance for this is the modelling of: (i) compound information -- multiple medical events for a patient occur in order and may be at the same time, (ii) clinical patterns -- frequent common sequential patterns that are associated with specific sequences of clinical events. To model these, in this paper we exploit the recently proposed Temporal Tree technique to capture compound information and we further apply sequential pattern mining (SPM) with gap constraint to discover more complex clinical patterns. 
The effectiveness of the proposed EHR representation method is evaluated using a real EHR dataset, MIMIC III, based on two task types within an Intensive Care Unit setting: (i) similar patients retrieval (ii) sepsis prediction and mortality prediction. The empirical results show that representation of EHRs with Temporal Tree and SPM, used in conjunction with traditional similarity measures or more complex embedding methods, delivers significant improvements in effectiveness in the considered tasks.