---
name: Transformers for Information Retrieval
image: /images/projects/transformers-IR.jpeg
featured: false
people: [shengyao-zhuang, hang-li, shuai-wang, guido-zuccon]
redirect_from: /neuralIR
---

## About this project

To be updated

#### Methods for Effective Passage Ranking: TILDE and TILDEv2

To be updated



#### Methods for Effective Passage Ranking: the QLM-T5

To be updated



#### Exploit Relevance Feedback with Transformer-based pre-trained LMs

To be updated



#### Do Dense Retrievers Require Interpolation with bag-of-words?

To be updated







## Relevant Publications 

{% for category in site.data.projects.transformer4IR.categories %}

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
