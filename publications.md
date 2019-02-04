# Publications

{% assign publications = site.publications | sort:"year" | reverse | group_by:"year" %}
{% for year in publications %}
<h2>{{ year.name }}</h2>
<ul>
{% assign author = site.people | where:'group', publication.authors %}
{% for publication in year.items %}
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
{% endfor %}
</ul>
{% endfor %}
