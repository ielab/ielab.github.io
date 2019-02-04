---
layout: default
---

# People

<div class="flex">
{% for person in site.people %}
<div class="flex one four-600 card" style="padding: 1em;">
    <div>
        {% if person.image == nil %}
        <img width="64px" height="auto" src="/images/blank-profile-picture.png" style="border-radius:50%; margin:auto; display:block">
        {% else %}
        <img width="64px" height="auto" src="{{ person.image }}" style="border-radius:50%; margin:auto; display:block">
        {% endif %}
        <a href="{{ person.id }}" style="text-align:center; display:block">{{ person.name }}</a>
    </div>        
    <div class="full half-600">{{ person.description }}</div>
    <div>
        <ul>
            {% if person.website != nil %}
            <li><a href="{{ person.website }}">Personal Website</a></li>
            {% endif %}
            {% if person.scholar != nil %}
            <li><a href="{{ person.scholar }}">Google Scholar</a></li>
            {% endif %}
            {% if person.twitter != nil %}
            <li><a href="{{ person.twitter }}">Twitter</a></li>
            {% endif %}                
            {% if person.github != nil %}
            <li><a href="{{ person.github }}">GitHub</a></li>
            {% endif %}   
        </ul>
    </div>
</div>
{% endfor %}
</div>