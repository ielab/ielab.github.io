---
name: ACM CHIIR UMMMS 2021
venues: [CHIIR 2021]
people:
 - name: leif-azzopardi
 - name: "Alistair Moffat"
   image: /images/alistair-moffat.jpg
 - name: "Paul Thomas"
   image: /images/paul-thomas.jpg
 - name: guido-zuccon
description: Material for the User Models, Metrics and Measures of Search, Tutorial on the CWL Evaluation Framework; ACM CHIIR UMMMS 2021
links: 
 - url: https://dl.acm.org/doi/10.1145/3406522.3446049
   name: Download Paper
 - url: https://colab.research.google.com/drive/1CseqG6G7k8falu5NHd2GGrEiOBZ-jT9D?usp=sharing
   name: cwl-eval demo
 - url: https://www.youtube.com/playlist?list=PLgrOo-AsKcmV3pzpvFbd5SUpUMWUv2fQr
   name: Online Videos

---



Evaluation is central to Information Retrieval, and is how we compare the quality of systems. One important principle of evaluation is that the measured score should reflect the user’s experience with
the system. Hence, there should be direct connection between how users interact with the system and the characteristics of the metric.

In this tutorial we introduce the C/W/L approach to user modeling and show how different user models lead to different metrics. We then describe the recent innovations and approaches to evaluation that it has facilitated. The tutorial is presented as a mix of on-line synchronous lecture, pre-recorded in-depth videos, and hands-on activities using the C/W/L toolkit for participants’ own evaluation tasks. A followup consultation session is also provided, to allow extended questions and individual discussion with the four
presenters.


## Learning outcomes

As a result of attending this tutorial, participants will be able to:

- formally define the C/W/L framework and how to calculate the Expected Utility (also known as expected rate of gain) of a result list;
- define the User Browsing Models (continuation functions) of different metrics;
- show how new metrics can be defined via the UBM;
- explain how the C/W/L framework can be extended to produce different measurements;
- describe further extensions to the C/W/L framework to include snippet-based and session-based measurements;
- show how the C/W/L framework can be used to evaluate results and analyze Continuation functions, Weighting functions, and Last Likelihood functions;
- use the “cwl_eval” toolkit to perform TREC-like evaluations on typical IR system experimental outputs.


## Tutorial Slides:

- [Part 1: Introduction to evaluation](/files/1-ummms-introduction.pdf)
- [Part 2: The C/W/L Framework](/files/2-ummms-cwl.pdf)
- [Part 3: C/W/L Extensions and Future Research](/files/3-ummms-extensions-and-research.pdf)
- [Part 4: C/W/L in practice](/files/4-ummms-cwl-demo.pdf)
- [Online videos](https://www.youtube.com/playlist?list=PLgrOo-AsKcmV3pzpvFbd5SUpUMWUv2fQr)
- [C/W/L demonstration tool](https://colab.research.google.com/drive/1CseqG6G7k8falu5NHd2GGrEiOBZ-jT9D?usp=sharing)

