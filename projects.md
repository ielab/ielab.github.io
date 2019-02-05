# Projects

The ielab works on a diversity of research projects in the fields of information retrieval, data science, and health informatics. Research strengths include:

* **Formal models of Information Retrieval:** retrieval models, learning to rank, deep learning, user models, evaluation of information retrieval systems. 
* **Health Search and Health Data Science:** models, systems, evaluation for tasks in consumer health search, clinical decision support, precision medicine, search for systematic review compilation, cohort selection for clinical trials.
* **Domain-specific search:** case law retrieval.

## Current highlighted projects

<div class="flex four">
{% for project in site.projects %}
<div>
    <article class="card">
        <img src="{{ project.image }}">
        <footer>
            <a href="{{ project.url }}">{{ project.name }}</a>
        </footer>
    </article>
</div>
{% endfor %}
</div>

### GitHub repositories associated to ielab projects and initiatives

#### Tools, software and demonstrators

* [searchrefiner](https://ielab.io/searchrefiner): A Query Visualisation and Understanding tool for Systematic Reviews.
* [querylab](https://ielab.io/querylab): A Query Visualisation and Understanding tool for Systematic Reviews.
* [INST eval](https://github.com/ielab/inst_eval): Python implementation of the INST evaluation measure from Moffat et al.
* [Relevation](https://github.com/ielab/relevation): Information Retrieval Relevance Judging System
* [query generation](https://github.com/ielab/query_generation): An annotator toolkit for creating manual queries from clinical decision support scenarios.
* [NLTM](https://github.com/ielab/adcs2015-NTLM): Implementation of Neural Translation Language Models, along with embeddings and experimental data/results, associated with the article by [G. Zuccon](/people/guido-zuccon), [B. Koopman](/people/bevan-koopman), P. Bruza, [L. Azzopardi](/people/leif-azzopardi), "Integrating and Evaluating Neural Word Embeddings in Information Retrieval", ADCS 2015.

#### Collections and datasets

* [USSC Caselaw Collection](https://github.com/ielab/ussc-caselaw-collection): A collection for evaluating Case Law IR systems
* [SIGIR2017 Systematic Reviews Collection](https://github.com/ielab/SIGIR2017-PICO-Collection): A collection for evaluating IR systems for Systematic Reviews, with PICO annotations


#### Research tutorials and teaching material

* [Elastic4IR](https://github.com/ielab/elastic4IR): Tutorial and resources for using Elastic for information retrieval experiments. The tutorial was designed for the [SIGIR 2017 Lucene for Information Access and Retrieval Research (LIARR)](https://liarr2017.github.io/).
* [Health Search Tutorial](https://github.com/ielab/health-search-tutorial): Tutorials and resources on health information retrieval problems, methods and resources, covering aspects from clinicians to consumers. This tutorial has been given, in different formats, at SIGIR 2018, RUSSIR 2018, AFIRM 2018, WSDM 2019.
* [AFIRM 2019 IR in Practice](https://github.com/ielab/afirm2019): Material about using Elasticsearch for information retrieval experiments, presented at the 2019 ACM SIGIR/SIGKDD Africa Summer School on Machine Learning for Data Mining and Search.