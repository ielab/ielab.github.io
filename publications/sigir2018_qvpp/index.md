# Query Variation Performance Prediction for Systematic Reviews

When conducting systematic reviews, medical researchers heavily deliberate over the final query to pose to the information retrieval system. Given the possible query variations that they could construct, selecting the best performing query is difficult.
This motivates a new type of query performance prediction (QPP) task where the challenge is to estimate the performance of a set of query variations given a particular topic. Query variations are the reductions, expansions and modifications of a given seed query under the hypothesis that there exists some variations (either generated from permutations or hand crafted) which will improve retrieval effectiveness over the original query. We use the CLEF 2017 TAR Collection, to evaluate sixteen pre and post retrieval predictors for the task of Query Variation Performance Prediction (QVPP).
Our findings show the IDF based QPPs exhibits the strongest correlations with performance. However, when using QPPs to select the best query, little improvement over the original query can be obtained, despite the fact that there are query variations which perform significantly better. Our findings highlight the difficulty in identifying effective queries within the context of this new task, and motivates further research to develop more accurate methods to help systematic review researchers in the query selection process.

[Download paper](https://scells.me/publications/sigir2018_qvpp.pdf)

## Poster 

![QVPP Poster](sigir2018_qvpp.png)

[Download poster](sigir2018_qvpp.pdf)

## Citing This Work

Please cite this work as

```
@inproceedings{scells2018qvpp,
Author = {Scells, Harrisen and Azzopardi, Leif and Zuccon, Guido and Koopman, Bevan},
Booktitle = {Proceedings of the 41st international ACM SIGIR conference on Research and development in Information Retrieval},
Organization = {ACM},
Title = {Query Variation Performance Prediction for Systematic Reviews},
Year = {2018}
}
```

## Contact Authors

Please email [harrisen.scells@hdr.qut.edu.au](mailto:harrisen.scells@hdr.qut.edu.au).

Follow [@ielabgroup](https://twitter.com/ielabgroup) on twitter.

## Related Work

 - [Generating Better Queries for Systematic Reviews](https://ielab.io/publications/sigir2018_generating/)
 - [A Test Collection for Evaluating Retrieval of Studies for Inclusion in Systematic Reviews](https://scells.me/research/pico/)
 - [An Information Retrieval Experiment Framework for Domain Specific Applications](https://ielab.io/querylab/)
