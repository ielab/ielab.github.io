---
layout: default
title: Publications
permalink: /publications/
redirect_from:
  - /publications.html
---
{%- comment -%}
  The publication list is the deduplicated union of every member's record in
  _data/openalex.json (ground truth: each member's Google Scholar profile,
  enriched with OpenAlex metadata; papers since ielab's founding in 2019 —
  see README §4.0). If the synced data is unavailable it falls back to the
  curated _publications collection.
{%- endcomment -%}
{%- assign oa_meta = site.data.openalex["_meta"] -%}
{%- if oa_meta and oa_meta.works.size > 0 -%}
  {%- assign use_oa = true -%}
  {%- assign total = oa_meta.unique_works_display -%}
  {%- assign by_year = oa_meta.works | group_by: "year" -%}
  {%- assign core_works = oa_meta.works | where_exp: "item", "item.core == 1" -%}
  {%- assign chips_by_year = core_works | group_by: "year" -%}
{%- else -%}
  {%- assign use_oa = false -%}
  {%- assign total = site.publications | size -%}
  {%- assign by_year = site.publications | sort: "year" | reverse | group_by: "year" -%}
  {%- assign chips_by_year = by_year -%}
{%- endif -%}

{%- capture hero_lead -%}
The publication record of our current members since the lab's founding in
{{ oa_meta.min_year | default: 2019 }} — {{ total }} works published at the premier venues
in information retrieval and beyond{% if use_oa %}, synced automatically from members'
Google Scholar profiles and enriched via <a href="https://openalex.org">OpenAlex</a>
(updated {{ oa_meta.updated }}). A further {{ oa_meta.extended_works_display }} papers by
alumni and external members are not listed by default — find them via the search box
below, or on their <a href="/people/">profile pages</a>{% endif %}.
{%- endcapture -%}

{% include page-hero.html
   eyebrow="Research output"
   title="Publications"
   lead=hero_lead %}

<div class="section" style="padding-top: 48px;">
  <div class="container">

    <div class="pub-toolbar">
      <div class="search-field">
        {% include icon.html name="search" size=18 %}
        <input type="search" id="pub-search" placeholder="Search all publications by title, author, or venue…" aria-label="Search publications">
      </div>
      <div class="filter-row">
        <button class="filter-chip active" type="button" data-year="all">All years</button>
        {%- for year in chips_by_year -%}
        <button class="filter-chip" type="button" data-year="{{ year.name }}">{{ year.name }}</button>
        {%- endfor -%}
      </div>
      <span class="results-count" aria-live="polite"></span>
    </div>

    {%- for year in by_year -%}
    {%- if use_oa -%}
      {%- assign year_core = year.items | where_exp: "item", "item.core == 1" -%}
    {%- else -%}
      {%- assign year_core = year.items -%}
    {%- endif -%}
    <div class="pub-year-group">
      <div class="pub-year-head">
        <h2>{{ year.name }}</h2>
        {%- if year_core.size > 0 -%}
        <span class="count">{{ year_core.size }} publication{% if year_core.size != 1 %}s{% endif %}</span>
        {%- endif -%}
      </div>
      <ul class="pub-list">
        {%- if use_oa -%}
          {%- for work in year.items -%}
          {% include oa-pub-item.html work=work %}
          {%- endfor -%}
        {%- else -%}
          {%- for pub in year.items -%}
          {% include pub-item.html pub=pub %}
          {%- endfor -%}
        {%- endif -%}
      </ul>
    </div>
    {%- endfor -%}

    <div class="pubs-empty">
      <h3>No matching publications</h3>
      <p>Try a different search term, or clear the year filter.</p>
    </div>

  </div>
</div>
