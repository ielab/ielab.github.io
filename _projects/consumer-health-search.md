---
name: Consumer Health Search
image: /images/projects/chs.jpg
featured: true
people: [sebastian-cross, jimmy, guido-zuccon, bevan-koopman, joao-palotti]
---

## About this project

This project seeks to assist the general public in using search engines to make well-informed health decisions. While the general public belief that they were being effective in searching for health information online, they were, in fact, relying on incorrect health advise.

This project specifically aims to assist the general public in formulating better health queries, understanding health search results and making well-informed health decisions. See below for a list of relevant publications.

### On the effectiveness of search engines in finding medical self-diagnosis information

We have received substantial media attention for a work we have published in March 2015 at the European Conference on Information Retrieval (ECIR), titled "Diagnose this if you can: On the effectiveness of search engine in finding medical self-diagnosis information". The paper is available from the publisher (Springer), on QUT ePrints , and as a pre-print version. The QUT press release for this story can be found here.

The work described in the paper was developed by Dr Guido Zuccon (at the time at QUT), Dr Bevan Koopman (at the time at CSIRO), and Mr Joao Palotti (at the time at TUW)

#### What this study says, in few words...
In this work, we examined poorly formulated self-diagnosis queries and we found that major search engines were providing irrelevant information that could lead to incorrect self-diagnosis, self-treatment and ultimately possible harm.

#### The long story: More details
Surveys have shown people actively use search engines for finding health information online. Search engines provide a wealth of useful information about diseases and illnesses when a person query is well articulated. However, the research we present in this paper shows that for other queries that are poorly formulated and ambiguous, e.g. when a person is trying to describe their own symptoms, then search engines may fail in providing relevant, correct and understandable information. In particular the table below shows the average effectiveness of the two commercial search engines we considered for answering poorly formulated self-diagnosis queries.

The following table reports the effectiveness of two widely used commercial search engines when prompted with (circumlocutory) medical queries aimed at self-diagnosis purposes. Results are averaged over 26 queries. P@k stands for precision at rank k; ndcg@k stands for normalised discounted cumulative gain at rank k.

| **System** | **ndcg@1** |        | **ndcg@5** |        | **ndcg@10** |        | **P@5** |        | **P@10** |        |
|:----------:|:----------:|:------:|:----------:|:------:|:-----------:|:------:|:-------:|:------:|:--------:|:------:|
|            | _Rel_      | _Hrel_ | _Rel_      | _Hrel_ | _Rel_       | _Hrel_ | _Rel_   | _Hrel_ | _Rel_    | _Hrel_ |
| **Bing**   | .3846      | .2308  | .3812      | .2654  | .3802       | .2764  | .4385   | .2769  | .4308    | .2769  |
| **Google** | .3846      | .3077  | .4242      | .3142  | .4252       | .3138  | .5000   | .3154  | .4923    | .3115  |



The study was conducted using 26 queries that people would issue to search engines when they can observe a symptom but do not know the medical diagnosis; these queries were collected by [a previous study](https://theory.stanford.edu/~nmishra/Papers/circumlocutionDiagnosticMedicalQueries.pdf) by Dr Isabelle Stanton and colleagues. While these are not real queries that were submitted to a search engine, we believe they are a good approximation of the actual queries people use to search for self-diagnosis information. In addition, while this is a small set of queries (and thus the results have to be taken with caution as they may not generalise to other symptoms and conditions), we believe they are a good representative of the type of queries people use for this task. Note that after this study we have collected, as part of the CLEF 2015 eHealth Lab Task 2 exercise, a larger number of queries people would use when trying to self-diagnose. These queries show similarities in form to those used in the study presented at ECIR 2015; an initial analysis of the CLEF 2015 results confirms search engines struggle in providing quality information for these searches.


If you think this research is important and you are happy to share the queries you have issued to a search engine to find medical information or your experience when doing so, then please get in touch with us!


Resources associated with the paper are available on the [dedicated space in GitHub](https://github.com/ielab/ecir2015-DignoseThisIfYouCan).

#### FAQs

Q: Why do you think online users are turning to Dr Google? (thanks to [Jackson Stiles](https://twitter.com/jacksonstiles) for this question)
A: Search engine usage data has always shown that a portion of the query traffic is aimed at finding health advice online: this the of queries were observed also a decade or more ago. However, recently there has been a consistent increase of this trend. I personally believe it is due to the fact that search engine quality has largely improved; these technologies have become part of our everyday life and thus people tend to trust and rely increasingly more on search engines. The limited time available to seek medical advice in other forms (e.g. Going to the GP) and, in some parts of the world, the increase of healthcare costs (even simply a visit to the GP) may have pushed consumers to alternative ways of seeking health information: using search engines being the more prominent.


Q: People increasingly turn to search engines to find medical advice. Is this a helpful or harmful trend? Why? (thanks to [Jackson Stiles](https://twitter.com/jacksonstiles) for this question)
A: I think search engines have come a long way from their early days. We have seen increasing improvements in the way commercial search engines present health-related information. Current search engines are great for providing a wealth of information about illnesses and diseases, if you can clearly name these in your queries. For example, in the US Google is currently experimenting returning clear health cards at the top of their search results for queries about specific conditions or diseases, ranging from headache to tonsillitis, celiac disease and so on. This information has been fact-checked by doctors, it shows the incidence of the conditions on the population and a lot of other useful information. However, as our study shows, there is yet a lot of road to do before getting very reliable search engines for finding information about health concerns, in particular for self-diagnosis and treatment, where you don’t know exactly what you have, and therefore you issue more ambiguous, underspecified queries. Indeed, answering these type of searches is difficult because the search engine cannot rely on simple keyword matching or more sophisticated techniques search engines currently use; the queries instead require a profound understanding of language and medical information, and possibly more information about the user and their conditions. Thus, searching for health advice can often lead you to very good and helpful information, often curated by experts and produced by health organisations. This information can help you better understand your medical conditions and often improve the way you face them. However, replacing a doctor with a search engine is not a good idea: our research has shown that, with the current search engines, if you attempt to self diagnose yourself, you often end up finding incorrect or misleading information, which indeed could be detrimental to your health.


Q: It looks like you found that Google produced better results than Bing. Is this right? Are you able to say whether it's a significant difference? (thanks to Elizabeth Preston for this question)
A: Our results are not reliable enough for judging the effectiveness of Google over Bing. To do a significant comparison between the two search engines you will need in first instance a larger amount of queries, which we had not at our disposal in this study. If you had a large amount of queries, then you may be able to say something about the difference between the two search engines. Note also that we attempted to use the search engines in a configuration that avoided as much personalisation and localisation of the search results as possible, in an attempt to be able to have some generality in our study. This means that for the same queries, Bing may have answered better than Google (or not) if they were personalising the information to you (i.e. Using your query history, what they know about you, etc). (Search engines are a very complex machinery: we attempted to remove some of the variability given by personalisation to better generalise our findings. For example, in the US Google is trailing the use of health cards on the top of the search page: we do not have access to health cards in Australia for now. However, we do not expect that currently Google would produce health cards for the queries studied in our work.) So, in summary, we do not have enough empirical data to comment on the differences between the search engines. However, despite the small number of queries we looked at in this initial study, we feel that the trends observed in terms of effectiveness of the two search engines for this specific type of queries (self-diagnosis, circumlocutory) can be generally extended to other queries in this category (i.e. self-diagnosis, circumlocutory).


Q: Were you surprised by how few of the top search results were helpful? (Or maybe it was more than you expected!) (thanks to Elizabeth Preston for this question)
A: We did not have a set expectation when we started this work. From looking to previous surveys and talking with everyday people, we understood that these types of searches are often performed by people with limited (or no) medical knowledge. We know current search engines are doing a good job in answering clearly formulated medical queries (e.g. Celiac disease), and companies like Google are deploying better and better solutions for supporting these queries. In the past 2 years the research community that makes research into search engine technologies (the field is called Information Retrieval) has produced a number of innovative search algorithms to improve this type of search (i.e. Clearly formulated medical queries). However, little research has been done on answering more complex health queries, like those circumlocutory (using a roundabout way to express your query rather than using the correct medical terms) health queries we considered here. Interestingly, research on this type of queries was started few months ago by researchers at Microsoft Research (some of which now at Google): we cite that paper in our article (the paper is from SIGIR 2014). Thus, we were driven by the curiosity of finding out if these queries are problematic for current state-of-the-art search engine technologies, and if they were, find out why it is so and how we can improve them (i.e. Develop tailored solutions to answer these queries).


Q: Are you (or other groups) looking into ways to address this problem? (thanks to Elizabeth Preston for this question)
A: Yes, we are looking into devising better search technologies to address these types of queries. For example, we are developing methods that return pages that are easier to understand, while maintaining the relevancy and correctness of the medical information. We are also developing methods that elicit the meaning behind medical terms so to improve the matching with the plain and circumlocuted language used by the searchers. Like us, other members of our research community are working on this topic and building sophisticated methods for more accurate search. We are currently leading a research task that involves researchers from around the world and that is aimed at evaluating search solutions to answer to this types of queries. The task is called CLEF 2015 eHealth Task 2 and currently involves research teams from 12 institutions around the world. (In previous editions of this task, called CLEF eHealth Task 3 and that ran in 2013 and 2014, we studied the more simple health queries I mentioned at the top of the email, i.e. Clearly formulated queries such as celiac disease, and at the end of the second year we found that some of the technologies developed by the research teams involved were very effective in providing accurate medical advice.)


Q: Based on your research, what advice would you give people who are trying to self-diagnose using the internet? (thanks to Elizabeth Preston for this question)
A: The first advice is to remember that, as great as search engines are, they are not meant as a replacement for a medical professional. (Although we do believe search engines have an important role to play in supporting the experience of people seeking to understand they health conditions). The second advice is that when performing self-diagnosis-like searchers, they are effectively attempting to explore a new information space, where you start with a very limited knowledge of both the information space itself and the vocabulary. Thus, they need to be aware that the results they find may be affected by this limited knowledge and that they may need many interactions with the search system (issuing queries, reading documents, etc) to find useful information and that the information they found along the exploration may not all be appropriate to their case, although it may look like that at first instance. A third, obvious, advice is to issue good queries. We have observed that search engines often provide good quality results when you use good, clearly formulated queries, while the result quality is often poor when the queries are ambiguous, underspecified, poorly formulated. It is difficult though to come up with general suggestions that can help formulating better queries. We think that paying attention to the query suggestions provided by the search engines (for example, Google provides those at the bottom of the queries, and calls them related searches) is important to understand how the search engine is interpreting your query and which directions you can explore based on the query you have just issued. Finally, be mindful to take into consideration where the documents are coming from, i.e. Who is the source of the information: of course, prefer reputable sources.


Q: How would you define 'cyberchondria'?
A: Cyberchondria is a term coined by [Dr Ryen White at Microsoft Research](http://research.microsoft.com/en-us/um/people/ryenw/); it indicates an escalation of concerns about common symptoms that are actually unfounded. You can find more examples, studies and discussions of cybercondria in White and Horvitz's ['Cyberchondria: Studies of the Escalation of Medical Concerns in Web Search'](http://research.microsoft.com/apps/pubs/?id=76529).

#### Media Coverage
This publication received wide media coverage; reports can be found [here](files/DiagnoseThis-MediaCoverage/DrGoogleMediaCoverage1.pdf) and [here](files/DiagnoseThis-MediaCoverage/DrGoogleMediaCoverage2.pdf).


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
