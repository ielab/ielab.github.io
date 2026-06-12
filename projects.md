---
layout: default
title: Projects
permalink: /projects/
redirect_from:
  - /projects.html
---
{% include page-hero.html
   eyebrow="What we build"
   title="Projects"
   lead="The ielab works on a diversity of research projects in information retrieval, data science, and health informatics — many with associated open-source software and datasets." %}

<div class="section" style="padding-top: 56px;">
  <div class="container">

    <div class="grid grid-3">
      {%- for project in site.projects -%}
        {%- if project.featured == true -%}
          {% include project-card.html project=project %}
        {%- endif -%}
      {%- endfor -%}
      {%- for project in site.projects -%}
        {%- unless project.featured == true -%}
          {% include project-card.html project=project %}
        {%- endunless -%}
      {%- endfor -%}
    </div>

    <div class="prose" style="margin-top: 4rem;">
      <h2>Open-Source Software &amp; Demonstrators</h2>
      <p>GitHub repositories associated with ielab projects and initiatives:</p>
      <ul>
        <li><a href="https://ielab.io/publications/agask-agent">AgAsk</a>: An agricultural conversational search agent for answering comprehensive questions.</li>
        <li><a href="https://ielab.io/searchrefiner">searchrefiner</a>: A query visualisation and understanding tool for systematic reviews.</li>
        <li><a href="https://ielab.io/querylab">querylab</a>: A query visualisation and understanding tool for systematic reviews.</li>
        <li><a href="https://github.com/ielab/inst_eval">INST eval</a>: Python implementation of the INST evaluation measure from Moffat et al.</li>
        <li><a href="https://github.com/ielab/relevation">Relevation</a>: Information retrieval relevance judging system.</li>
        <li><a href="https://github.com/ielab/query_generation">query generation</a>: An annotator toolkit for creating manual queries from clinical decision support scenarios.</li>
        <li><a href="https://github.com/ielab/adcs2015-NTLM">NLTM</a>: Implementation of Neural Translation Language Models, along with embeddings and experimental data/results, associated with the article by <a href="/people/guido-zuccon">G. Zuccon</a>, <a href="/people/bevan-koopman">B. Koopman</a>, P. Bruza, <a href="/people/leif-azzopardi">L. Azzopardi</a>, "Integrating and Evaluating Neural Word Embeddings in Information Retrieval", ADCS 2015.</li>
      </ul>

      <h2>Collections &amp; Datasets</h2>
      <ul>
        <li><a href="https://github.com/ielab/ussc-caselaw-collection">USSC Caselaw Collection</a>: A collection for evaluating case law IR systems.</li>
        <li><a href="https://github.com/ielab/SIGIR2017-PICO-Collection">SIGIR2017 Systematic Reviews Collection</a>: A collection for evaluating IR systems for systematic reviews, with PICO annotations.</li>
      </ul>

      <p>Find more on the <a href="https://github.com/ielab">ielab GitHub organisation →</a></p>
    </div>

  </div>
</div>
