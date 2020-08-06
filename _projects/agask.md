---
name: AgAsk
image: /images/projects/agask.jpg
featured: true
people: [hang-li, guido-zuccon, bevan-koopman, anton-van-der-vegt]
---

## About this project

Valuable grains R&D output is currently locked away into project reports, communications and scientific publications. This text-based information is not easily discoverable and synthesised. Thus growers are not able to put into practice these valuable insights.

AgAsk is a conversational agent that will provide personalised access to this valuable information leading directly to better, data-driven growing decisions. Through ML driven question-answering systems, AgAsk will elicit and understand growers information needs and preferences, providing contextualised access to insights in Ag RD&E. This will allow valuable GRDCs research, along with other relevant resources, to flow directly to growers  something not possible at large scale with current practices. AgAsk will also collect and analyse insightful information about growers, their pressing needs and what they access, giving insights into growers learning preferences and needs, uptake of specific GRDC resources, decision drivers and barriers to adoption.

AgAsk uses state-of-the-art ML technology to interpret natural language questions. GRDC resources will be mined from textual information and converted into a knowledge graph capturing key agricultural concepts and relations (e.g. protozoa --effective_for--> control of pest molluscs AgAsk will use this knowledge graph to formulate contextualised and interpretable answers to a growers question, e.g. how to deal with slugs in Darling Downs wheat crop

AgAsk can be deployed in the field, readily available across the wide growers sector. Growers will be included from the beginning of this project in grower-gatherings  consultation workshops to collect real-world needs, through to user acceptance testing of the system.

This project will deliver a prototype system that can be taken to the App-Store in partnership with GRDC and key influencers such as farming systems groups and other grower groups, farm advisers and agribusiness stakeholders.

### Relevant Publications 

<!-- {% for category in site.data.projects.agask.categories %}

#### {{ category.name }}

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
{% endfor %} -->

## Funding

The AgAsk project is funded by the Grains Research and Development Corporation, under grant number UOQ2003-009RTX ($765,234.8).

[_back to top_](#main)
