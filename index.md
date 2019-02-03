# The Information Engineering Lab

The ielab is a collaborative group of researchers working in the area of information engineering. Much of this research is specifically on the areas of [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval), i.e. search, and health informatics.

## Current Projects

<div class="flex four">
{% for project in site.projects %}
<div>
    <article class="card">
        <img src="{{ project.image }}">
        <footer>
            <a href="{{ project.url }}">{{ project.name }}</a>
        </footer>
    </article>
</div>
{% endfor %}
</div>

For advertised **student projects** (including PhD, masters, and undergraduate) please visit the [student projects page](/student-projects). 

A full list of projects is available at the [projects page](/projects)

To view a list of the group **publications**, please visit the [publications page](/publications).

---

## News


<div class="news">
{% for post in site.posts limit:5 %}
<small>{{ post.date | date_to_long_string }}</small>
<a href="{{ post.url }}"><h3>{{ post.title }}</h3></a>
<p>{{ post.excerpt }}</p>
{% endfor %}
</div>

---

## People

ielab was started as a group of Information Retrieval researchers at the [University of Queensland (UQ)](http://www.uq.edu.au) in Brisbane, Australia. However, the group has expanded to include researchers from [CSIRO](http://csiro.au), [University of Strathclyde](https://www.strath.ac.uk/), [Vienna University of Technology](https://www.tuwien.ac.at/en/), [Qatar Computing Research Institute](http://www.qcri.com) and more. From October 1, 2018, the core of the ielab research group will be hosted at the [University of Queensland (UQ)](http://www.uq.edu.au), among the world's top-50 universities.

### Researcher Staff

<div class="flex">
{% for person in site.people %}
{% if person.role == "staff" %}
<div class="flex four card" style="padding: 1em;">
    <div>
        {% if person.image == nil %}
        <img width="64px" height="auto" src="/images/blank-profile-picture.png" style="border-radius:50%; margin:auto; display:block">
        {% else %}
        <img width="64px" height="auto" src="{{ person.image }}" style="border-radius:50%; margin:auto; display:block">
        {% endif %}
        <a href="{{ person.id }}" style="text-align:center; display:block">{{ person.name }}</a>
    </div>        
    <div class="half">{{ person.description }}</div>
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
{% endif %}
{% endfor %}
</div>

### Doctoral Students (PhD)
<div class="flex">
{% for person in site.people %}
{% if person.role == "phd" %}
<div class="flex four card" style="padding: 1em;">
    <div>
        {% if person.image == nil %}
        <img width="64px" height="auto" src="/images/blank-profile-picture.png" style="border-radius:50%; margin:auto; display:block">
        {% else %}
        <img width="64px" height="auto" src="{{ person.image }}" style="border-radius:50%; margin:auto; display:block">
        {% endif %}
        <a href="{{ person.id }}" style="text-align:center; display:block">{{ person.name }}</a>
    </div>        
    <div class="half">{{ person.description }}</div>
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
{% endif %}
{% endfor %}
</div>
### Honours Students

* [completed 2017] Liam Cripwell. Honours student, QUT: Generating Clinical Queries from Patient Narratives
* [completed 2016] Harrisen Scells. Honours student, QUT: Investigating Methods Of Annotating Lifelogs For Use In Search

### Masters Students

[completed 2017]:
* Doyoo Baek: A predictive analysis of heavy machinery deterioration (Industrial CEED collaboration with Hastings Deering Pty Ltd)
* Xiaoran Chu: OMG! The Amazing Result of Using Machine Learning to Build Classifiers for Clickbait Detection
* Linni Qin: Forecating Zestimate Error
* Zhiying Zhou: Educational Data Mining: Analyze and Predict student’s academic performance
* Harmandeep Kaur Bhullar: Data Analysis of an European Soccer Database
* Harshita Jain: An Analysis of Spam SMS Features
* Davinder Kaur: Symptoms of Lower Back Pain - A Data Analysis and Research Project
