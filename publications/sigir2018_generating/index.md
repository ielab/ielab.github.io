# Generating Better Queries for Systematic Reviews

Systematic reviews form the cornerstone of evidence based medicine, aiming to answer complex medical questions based on all evidence currently available. Key to the effectiveness of a systematic review is an (often large) Boolean query used to search large publication repositories. These Boolean queries are carefully crafted by researchers and information specialists, and often reviewed by a panel of experts. However, little is known about the effectiveness of the Boolean queries at the time of formulation.

In this paper we investigate whether a better Boolean query than that defined in the protocol of a systematic review, can be created, and we develop methods for the transformation of a given Boolean query into a more effective one. Our approach involves defining possible transformations of Boolean queries and their clauses. It also involves casting the problem of identifying a transformed query that is better than the original into: (i) a classification problem; and (ii) a learning to rank problem. Empirical experiments are conducted on a real set of systematic reviews. Analysis of results shows that query transformations that are better than the original queries do exist, and that our approaches are able to select more effective queries from the set of possible transformed queries so as to maximise different target effectiveness measures.

[Download paper](https://scells.me/publications/sigir2018_generating.pdf)

## Citing This Work

Please cite this work as

```
@inproceedings{scells2018generating,
Author = {Scells, Harrisen and Zuccon, Guido},
Booktitle = {Proceedings of the 41st international ACM SIGIR conference on Research and development in Information Retrieval},
Organization = {ACM},
Title = {Generating Better Queries for Systematic Reviews},
Year = {2018}
}
```

## Contact Authors

Please email [harrisen.scells@hdr.qut.edu.au](mailto:harrisen.scells@hdr.qut.edu.au).

Follow [@ielabgroup](https://twitter.com/ielabgroup) on twitter.

## Related Work

 - [Query Variation Performance Prediction for Systematic Reviews](https://ielab.io/publications/sigir2018_qvpp/)
 - [A Test Collection for Evaluating Retrieval of Studies for Inclusion in Systematic Reviews](https://scells.me/research/pico/)
 - [An Information Retrieval Experiment Framework for Domain Specific Applications](https://ielab.io/querylab/)

