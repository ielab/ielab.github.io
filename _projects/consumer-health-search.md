---
name: Consumer Health Search
image: //source.unsplash.com/n8o2pt46aEI/320x320
people: [jimmy, guido-zuccon, bevan-koopman, joao-palotti]
---

## About this project

This project seeks to assist the general public in using search engines to make well-informed health decisions. While the general public belief that they were being effective in searching for health information online, they were, in fact, relying on incorrect health advise. 

This project specifically aims to assist the general public in formulating better health queries, understanding health search results and making well-informed health decisions. See below for a list of relevant publications.


### Relevant Publications 

{% for category in site.data.projects.consumer-health-search.categories %}
#### {{ category.name }}
{% for pubid in category.publications %}
<ul>
    {% assign reference =  "/publications/" | append: pubid %}
    {% for publication in site.publications %}
        {% if publication.id == reference %}
            <li>
            {% assign i = 0 %}
            {% for involved in publication.authors %}
                {% assign found = false %}
                {% for person in site.people %}
                    {% assign path = person.id | split: "/" %}
                    {% assign id = path[2] %}
                    {% if id == involved %}
                        <a href="{{ person.id }}">{{ person.name }}</a>
                        {% assign found = true %}
                    {% endif %}
                {% endfor %}
                {% if found == false %}
                    {{ involved }}
                {% endif %}
                {% assign i = i | plus: 1 %}
                {% assign l = publication.authors | size %}
                {% if i < l %}
                and
                {% endif %}
            {%endfor %}.
           {{ publication.year }}.
           <a href="{{ publication.id }}">{{ publication.title }}</a>.
           In <em>{{ publication.venue }}</em>.
           </li>
        {% endif %}
    {% endfor %}
</ul>
{% endfor %}
{% endfor %}
