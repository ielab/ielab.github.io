# Tutorials

<div class="flex two">
{% for project in site.tutorials %}
<div>
    <article class="card">
        <header>
            <a href="{{ project.url }}">{{ project.name }}</a>
        </header>
        <footer>
        <img src="{{ project.image }}">
            <div>{{ project.description }}</div>
        </footer>
    </article>
</div>
{% endfor %}
</div>