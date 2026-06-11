---
layout: default
title: Tutorials
permalink: /tutorials/
redirect_from:
  - /tutorials.html
---
{% include page-hero.html
   eyebrow="Teaching & outreach"
   title="Tutorials"
   lead="Tutorials and courses presented by ielab members at international conferences and summer schools." %}

<div class="section" style="padding-top: 56px;">
  <div class="container">

    <div class="grid grid-2">
      {%- for tutorial in site.tutorials -%}
      <div class="card" data-reveal>
        <div class="card-body">
          {%- if tutorial.venues and tutorial.venues.size > 0 -%}
          <div class="meta-chips" style="margin: 0 0 0.8rem;">
            {%- for venue in tutorial.venues -%}
            <span class="chip">{{ venue }}</span>
            {%- endfor -%}
          </div>
          {%- endif -%}
          <h3 style="font-size: 1.15rem;"><a href="{{ tutorial.url | relative_url }}" style="color: var(--text);">{{ tutorial.name }}</a></h3>
          <p style="font-size: 0.92rem; color: var(--text-soft); display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; margin: 0;">{{ tutorial.description | strip_html | truncate: 260 }}</p>
        </div>
      </div>
      {%- endfor -%}
    </div>

  </div>
</div>
