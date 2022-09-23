# Projects

The ielab works on a diversity of research projects in the fields of information retrieval, data science, and health informatics. Research strengths include:

* **Formal models of Information Retrieval:** retrieval models, learning to rank, deep learning, user models, evaluation of information retrieval systems. 
* **Health Search and Health Data Science:** models, systems, evaluation for tasks in consumer health search, clinical decision support, precision medicine, search for systematic review compilation, cohort selection for clinical trials.
* **Domain-specific search:** case law retrieval.

## Current highlighted projects

<div class="flex two four-600">
{%- for project in site.projects -%}
    {%- if project.featured == true -%}
    <div>
        <article class="card">
            <img src="{{- project.image -}}">
            <footer>
                <a href="{{- project.url -}}">{{- project.name -}}</a>
            </footer>
        </article>
    </div>
    {%- endif -%}
{%- endfor -%}
</div>

### GitHub repositories associated to ielab projects and initiatives

#### Tools, software and demonstrators

* [AgAsk](https://ielab.io/agask-agent): A Agricultural conversational search agent for answering comprehensive questions.
* [searchrefiner](https://ielab.io/searchrefiner): A Query Visualisation and Understanding tool for Systematic Reviews.
* [querylab](https://ielab.io/querylab): A Query Visualisation and Understanding tool for Systematic Reviews.
* [INST eval](https://github.com/ielab/inst_eval): Python implementation of the INST evaluation measure from Moffat et al.
* [Relevation](https://github.com/ielab/relevation): Information Retrieval Relevance Judging System
* [query generation](https://github.com/ielab/query_generation): An annotator toolkit for creating manual queries from clinical decision support scenarios.
* [NLTM](https://github.com/ielab/adcs2015-NTLM): Implementation of Neural Translation Language Models, along with embeddings and experimental data/results, associated with the article by [G. Zuccon](/people/guido-zuccon), [B. Koopman](/people/bevan-koopman), P. Bruza, [L. Azzopardi](/people/leif-azzopardi), "Integrating and Evaluating Neural Word Embeddings in Information Retrieval", ADCS 2015.

#### Collections and datasets

* [USSC Caselaw Collection](https://github.com/ielab/ussc-caselaw-collection): A collection for evaluating Case Law IR systems
* [SIGIR2017 Systematic Reviews Collection](https://github.com/ielab/SIGIR2017-PICO-Collection): A collection for evaluating IR systems for Systematic Reviews, with PICO annotations
