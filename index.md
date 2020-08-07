# The Information Engineering Lab

The ielab is a collaborative group of researchers working in the area of information engineering. Much of this research is specifically on the areas of [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval), i.e. search engine technology and information seeking, data science, and health informatics.

## Highlighted Projects

<div class="flex two four-600">
{%- for project in site.projects -%}
    {%- if project.featured == true -%}
    <div>
        <article class="card">
            <img src="{{- project.image -}}">
            <footer>
                <a href="{{- project.url -}}">{{- project.name -}}</a>
            </footer>
        </article>
    </div>
    {%- endif -%}
{%- endfor -%}
</div>

A full list of projects is available at the [projects page](/projects), including associated resources (software, data).

To access a list of our **publications**, please visit the [publications page](/publications); this often includes a pre-print version of each publication.

For advertised **student projects** (including PhD, masters, and undergraduate) please visit the [student projects page](/student-projects). 

---

## News


<div class="news flex one three-1000">
<div class="two-third-1000">
{% for post in site.posts limit:5 %}
<a href="{{ post.url }}"><h3>{{ post.title }}</h3></a>
<small>{{ post.date | date_to_long_string }}</small>
<p>{{ post.excerpt }}</p>
{% endfor %}
</div>
<div>
<a class="twitter-timeline" href="https://twitter.com/IELabGroup?ref_src=twsrc%5Etfw">Tweets by IELabGroup</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
</div>
</div>


---

## People

ielab's core group includes Information Retrieval researchers at the [University of Queensland (UQ)](http://www.uq.edu.au) in Brisbane, Australia. However, the group has expanded to include researchers from the [CSIRO](http://csiro.au), [University of Strathclyde](https://www.strath.ac.uk/), [Qatar Computing Research Institute](http://www.qcri.com) and more. 

<img src="/images/groupOct2019.jpeg" style="width:70%; margin-left: 15%" alt="ielab group members at The University of Queensland.">

### Researcher Staff

<div class="flex">
{% for person in site.people %}
{% if person.role contains "staff" %}
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
{% endif %}
{% endfor %}
</div>

### Doctoral Students (PhD)

<div class="flex">
{% for person in site.people %}
{% if person.role contains "phd" %}
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
{% endif %}
{% endfor %}
</div>

### Alumni

<div class="flex">
{% for person in site.people %}
{% if person.role contains "alumni" %}
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
{% endif %}
{% endfor %}
</div>

### External members

<div class="flex">
{% for person in site.people %}
{% if person.role contains "external" %}
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
