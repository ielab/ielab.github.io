---
layout: default
---

# Posts

<div>
{% for post in site.posts limit:5 %}
<a href="{{ post.url }}"><h1>{{ post.title }}</h1></a>
<small>{{ post.date | date_to_long_string }}</small>
<p>{{ post.excerpt }}</p>
{% endfor %}
</div>