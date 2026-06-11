---
layout: default
title: People
permalink: /people/
redirect_from:
  - /people.html
---
{% include page-hero.html
   eyebrow="Our team"
   title="People"
   lead="ielab's core group is based at The University of Queensland in Brisbane, Australia, with members and collaborators at CSIRO, the University of Strathclyde, and research labs around the world." %}

<div class="section" style="padding-top: 56px;">
  <div class="container">

    <h2>Research Staff</h2>
    <div class="grid grid-4 mb-2">
      {%- for person in site.people -%}
        {%- unless person.role contains "alumni" or person.alumni -%}
          {%- if person.role contains "staff" -%}
            {% include person-card.html person=person %}
          {%- endif -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>

    <h2 style="margin-top: 3rem;">PhD &amp; MPhil Students</h2>
    <div class="grid grid-4 mb-2">
      {%- for person in site.people -%}
        {%- unless person.role contains "alumni" or person.alumni -%}
          {%- if person.role contains "phd" or person.role contains "mphil" -%}
            {% include person-card.html person=person %}
          {%- endif -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>

    <h2 style="margin-top: 3rem;">External Members</h2>
    <div class="grid grid-4 mb-2">
      {%- for person in site.people -%}
        {%- unless person.role contains "alumni" or person.alumni -%}
          {%- if person.role contains "external" -%}
            {% include person-card.html person=person %}
          {%- endif -%}
        {%- endunless -%}
      {%- endfor -%}
    </div>

    <h2 style="margin-top: 3rem;">Alumni</h2>
    <div class="grid grid-4 mb-2">
      {%- for person in site.people -%}
        {%- if person.role contains "alumni" or person.alumni -%}
          {% include person-card.html person=person %}
        {%- endif -%}
      {%- endfor -%}
    </div>

    <div class="prose" style="margin-top: 3.5rem;">
      <h2>Past Honours Students</h2>
      <ul>
        <li>[completed 2017] Liam Cripwell. Honours student, QUT: Generating Clinical Queries from Patient Narratives</li>
        <li>[completed 2016] Harrisen Scells. Honours student, QUT: Investigating Methods Of Annotating Lifelogs For Use In Search</li>
      </ul>

      <h2>Past Masters Students</h2>
      <p>[completed 2017]:</p>
      <ul>
        <li>Doyoo Baek: A predictive analysis of heavy machinery deterioration (Industrial CEED collaboration with Hastings Deering Pty Ltd)</li>
        <li>Xiaoran Chu: OMG! The Amazing Result of Using Machine Learning to Build Classifiers for Clickbait Detection</li>
        <li>Linni Qin: Forecasting Zestimate Error</li>
        <li>Zhiying Zhou: Educational Data Mining: Analyze and Predict student's academic performance</li>
        <li>Harmandeep Kaur Bhullar: Data Analysis of an European Soccer Database</li>
        <li>Harshita Jain: An Analysis of Spam SMS Features</li>
        <li>Davinder Kaur: Symptoms of Lower Back Pain — A Data Analysis and Research Project</li>
      </ul>

      <p><a href="/history">Lab photo history archive →</a></p>
    </div>

  </div>
</div>
