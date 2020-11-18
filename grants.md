---
layout: default
---

# Grants

<div class="flex">
{% for grant in site.grants %}
<div class="flex one four-600 card" style="padding: 1em;">
    <div>
        <div style="width: 64px; height: 64px; margin:auto; display:block">
            {% if grant.image == nil %}
            <img src="/images/blank-profile-picture.png" style="max-height: 100%; width: 100%; border-radius:50%; object-fit: cover">
            {% else %}
            <img src="{{ grant.image }}" style="max-height: 100%; width: 100%; border-radius:50%; object-fit: cover">
            {% endif %}
        </div>
        <a href="{{ grant.id }}" style="text-align:center; display:block">{{ grant.name }}</a>
    </div>        
    <div class="full half-600">
        <p>{{ grant.description }}</p>
      	<p>{{ grant.value }}</p>
     		<p>Funding years: {{ grant.years }}</p>
    </div>
</div>
{% endfor %}
</div>