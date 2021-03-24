---
layout: default
---

# Grants

<div class="flex">
{% for grant in site.grants %}
<div class="flex one four-600 card" style="padding: 1em;">
    <div>
        <div style="width: 128px; height: 128x; margin:auto; display:block">
            {% if grant.image == nil %}
            <img src="/images/blank-profile-picture.png" style="max-height: 100%; width: 100%; object-fit: cover">
            {% else %}
            <img src="{{ grant.image }}" style="max-height: 100%; width: 100%; object-fit: cover">
            {% endif %}
        </div>
    </div>        
    <div class="two-third">
    	<p>{{ grant.name }}</p>
        <a href="{{ grant.id }}" style="display:block">{{ grant.description }}</a>
      	<p>Value: {{ grant.value }}</p>
     	<p>Funding years: {{ grant.years }}</p>
    </div>
</div>
{% endfor %}
</div>