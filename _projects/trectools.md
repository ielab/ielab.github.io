---
name: trectools
image: /images/projects/legal.jpg
people: [joao-palotti, harry-scells, guido-zuccon]
featured: false
redirect_from: /trectools
---

<a class="button" href="https://github.com/joaopalotti/trectools">GitHub</a>
<a class="button" href="/publications/pdfs/palotti2019trectools.pdf">Download Paper</a>

TrecTools is an open-source Python library for assisting Information Retrieval (IR) practitioners with TREC-like campaigns.

If this package helps your research somehow, please reference our paper:

```
@inproceedings{palotti2019,
 author = {Palotti, Joao and Scells, Harrisen and Zuccon, Guido},
 title = {TrecTools: an open-source Python library for Information Retrieval practitioners involved in TREC-like campaigns},
 series = {SIGIR'19},
 year = {2019},
 location = {Paris, France},
 publisher = {ACM}
}
```

## Installing
```
pip install trectools
```

## Background

IR practitioners tasked with activities like building test collections, evaluating systems, or analysing results from empirical experiments commonly have to resort to use a number of different software tools and scripts that each perform an individual functionality – and at times they even have to implement ad-hoc scripts of their own. TrecTools aims to provide a unified environment for performing these common activities.

### Features

TrecTools is implemented in Python using standard data science libraries (NumPy, SciPy, Pandas, and Matplotlib) and using the object-oriented paradigm. 
Each of the key components of an evaluation campaign is mapped to a class: classes for runs (TrecRun),topics/queries (TrecTopic), assessment pools (TrecPools), relevance assessments (TrecQrel) and the evaluation results (TrecRes). [See file format for each object below](https://github.com/joaopalotti/trec_tools#file-formats).
Evaluation results can be produced by TrecTools itself using the evaluation metrics implemented in the tool, or be imported from the output file of trec_eval and derivatives. The features that are currently implemented in TrecTools are:

- **Querying IR Systems:** Benchmark runs can be obtained directly from one of the IR toolkits that are integrated in TrecTools. There is support for issuing full-text queries to [Indri](https://www.lemurproject.org/indri/) and [Terrier](http://terrier.org/) toolkits. Future releases will include other toolkits (e.g., [Elastic-search](), [Anserini](https://dl.acm.org/citation.cfm?id=3239571), etc.) and support for specific query languages(Indri’s query language, Boolean queries). See code snipets in [Example 1](https://github.com/joaopalotti/trec_tools#example-1).

- **Pooling Techniques:** The following techniques for assessment pool creation from a runs set are implemented: [Depth@K](https://sigir.org/files/museum/pub-14/pub_14.pdf), [Comb[Min/Max/Med/Sum/ANZ/MNZ]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.100.9316&rep=rep1&type=pdf), [Take@N](https://link.springer.com/chapter/10.1007/978-3-319-56608-5_28), [RRFTake@N](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.150.2291&rep=rep1&type=pdf), [RBPTake@N](https://people.eng.unimelb.edu.au/jzobel/fulltext/acmtois08.pdf). [See Example 2](https://github.com/joaopalotti/trec_tools#example-2).

- **Evaluation Measures:** Currently  implemented  and  verified measures include: Precision at depth K, Recall at depth K, MAP, NDCG, Bpref, [uBpref](http://zuccon.net/publications/sigir2016_L2R_readability.pdf), [RBP]((https://people.eng.unimelb.edu.au/jzobel/fulltext/acmtois08.pdf)), [uRBP](https://link.springer.com/chapter/10.1007/978-3-319-30671-1_21). Implemented in TrecTools is the option to break ties using document score (i.e., similar to trec_eval), or document ranking (i.e., similar to the original implementation of [RBP](https://people.eng.unimelb.edu.au/ammoffat/abstracts/mz08acmtois.html)). Additionally, TrecTools also allows to compute the residual of the evaluation measure and analyse the relative presence of unassessed documents. [See Example 3](https://github.com/joaopalotti/trec_tools#example-3).

- **Correlation and Agreement Analysis:** The Pearson, Spearman, Kendall and τ-ap correlation between system rankings can be computed [(see Example 4)](https://github.com/joaopalotti/trec_tools#example-4). Agreement measures between relevance assessment sets can be obtained with Kappa or Jaccard [(see Example 5)](https://github.com/joaopalotti/trec_tools#example-5).

- **Fusion Techniques.** Runs can be fused using the following techniques: Comb[Max/Min/Sum/Mnz/Anz/Med] - both using the scores and document rankings, RBPFusion, RRFFusion,or BordaCountFusion. Fusion techniques are provided for meta-analysis. [See Example 6](https://github.com/joaopalotti/trec_tools#example-6).
