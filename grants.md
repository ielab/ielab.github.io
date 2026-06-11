---
layout: default
title: Grants
permalink: /grants/
redirect_from:
  - /grants.html
---
{% include page-hero.html
   eyebrow="Funding"
   title="Grants"
   lead="Our research is supported by competitive national and international funding schemes, industry partnerships, and philanthropic programs." %}

<div class="section" style="padding-top: 56px;">
  <div class="container">

    <div class="grid grid-2">
      {%- for grant in site.grants -%}
      <div class="card grant-card" data-reveal>
        {%- if grant.image and grant.image != "" -%}
        <img class="grant-logo" src="{{ grant.image | relative_url }}" alt="" loading="lazy">
        {%- endif -%}
        <div>
          <h3><a href="{{ grant.url | relative_url }}">{{ grant.description }}</a></h3>
          <div class="scheme">{{ grant.name }}</div>
          <div class="grant-meta">
            {%- if grant.value -%}<span class="chip">{{ grant.value }}</span>{%- endif -%}
            {%- if grant.years -%}<span class="chip chip-outline">{{ grant.years }}</span>{%- endif -%}
          </div>
        </div>
      </div>
      {%- endfor -%}
    </div>

  </div>
</div>
