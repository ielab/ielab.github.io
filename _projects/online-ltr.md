---
name: Online Learning to Rank
image: /images/projects/oltr.png
featured: true
people: [shengyao-zhuang, guido-zuccon]
---

## About this project

To be updated

####Methods for Effective Online Learning to Rank: Joining Counterfactual and Online Learning

To be updated



####Methods for Effective Online Learning to Rank: exploit Reinforcement Learning

To be updated



####Does OLTR adapt to intent changes?

To be updated







## Relevant Publications 

{% for category in site.data.projects.oltr.categories %}

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



[_back to top_](#main)
