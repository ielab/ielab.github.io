---
layout: default
---

# People

<div class="flex">
{% for person in site.people %}
<div class="flex one four-600 card" style="padding: 1em;">
    <div>
        <div style="width: 64px; height: 64px; margin:auto; display:block">
            {% if person.image == nil %}
            <img src="/images/blank-profile-picture.png" style="max-height: 100%; width: 100%; border-radius:50%; object-fit: cover">
            {% else %}
            <img src="{{ person.image }}" style="max-height: 100%; width: 100%; border-radius:50%; object-fit: cover">
            {% endif %}
        </div>
        <a href="{{ person.id }}" style="text-align:center; display:block">{{ person.name }}</a>
    </div>        
    <div class="full half-600">
        {% for role in person.role %}
            {% if role == "phd" %}
                <i>PhD Student</i><br/>
            {% elsif role == "staff" %}
                <i>Research Staff</i><br/>
            {% elsif role == "external" %}
                <i>External Member</i><br/>
            {% elsif role == "alumni" %}
                <i>Alumni</i><br/>
            {% endif %}            
        {% endfor %}
        <p>{{ person.description }}</p>
    </div>
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