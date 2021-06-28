---
name: Neural Relevance Feedback
image: /images/projects/nrf.jpg
featured: true
people: [hang-li, ahmed-mourad, shengyao-zhuang, guido-zuccon, bevan-koopman]
---

## About this project

To be filled

## Relevant Publications 

{% for category in site.data.projects.nrf.categories %}

### {{ category.name }}

{% for pubid in category.publications %}
<ul>
    {%- assign reference =  "/publications/" | append: pubid -%}
    {%- for publication in site.publications -%}
        {%- if publication.id == reference -%}
            <li>
            {%- assign i = 0 -%}
            {%- for involved in publication.authors -%}
                {%- assign found = false -%}
                {%- for person in site.people -%}
                    {%- assign path = person.id | split: "/" -%}
                    {%- assign id = path[2] -%}
                    {%- if id == involved -%}
                        <a href="{{ person.id }}">{{ person.name }}</a>
                        {%- assign found = true -%}
                    {%- endif -%}
                {%- endfor -%}
                {%- if found == false -%}
                    {{ involved }}
                {%- endif -%}
                {%- assign i = i | plus: 1 -%}
                {%- assign l = publication.authors | size -%}
                {% if i < l %} and {% endif %}
            {%-endfor -%}.
           {{ publication.year }}.
           <a href="{{ publication.id }}">{{ publication.title }}</a>.
           In <em>{{ publication.venue }}</em>.
           </li>
        {%- endif -%}
    {%- endfor -%}
</ul>
{% endfor %}
{% endfor %}

## Funding

This project is funded by the Grains Research and Development Corporation, under grant number UOQ2003-009RTX ($765,234.8).

[_back to top_](#main)
