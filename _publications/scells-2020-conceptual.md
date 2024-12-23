---
authors: [harry-scells, guido-zuccon, bevan-koopman, "Justin Clark"]
title: Automatic Boolean Query Formulation for Systematic Review Literature Search
venue: Proceedings of The Web Conference 2020
year: 2020
pdf: /publications/pdfs/scells2020conceptual.pdf
projects: [systematic-reviews] 
redirect_from: /www-conceptual
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/kx91200mNXk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Formulating Boolean queries for systematic review literature search is a challenging task. Commonly, queries are formulated by information specialists using the protocol specified in the review and interactions with the research team. Information specialists have in-depth  experience on how to formulate queries in this domain, but may not have in-depth knowledge about the reviews' topics. Query formulation requires a significant amount of time and effort, and is performed interactively; specialists repeatedly formulate queries, attempt to validate their results, and reformulate specific Boolean clauses.
In this paper, we investigate the possibility of automatically formulating a Boolean query from the systematic review protocol. We propose a novel five-step approach to automatic query formulation, specific to Boolean queries in this domain, which approximates the process by which information specialists formulate queries. In this process, we use syntax parsing to derive the logical structure of high-level concepts in a query, automatically extract and map concepts to entities in order to perform entity expansion, and finally apply post-processing operations (such as stemming and search filters).

Automatic query formulation for systematic review literature search has several benefits: (i) it can provide reviewers with an indication of the types of studies that will be retrieved, without the involvement of an information specialist, (ii) it can provide information specialists with an initial query to begin the formulation process, (iii) it can provide researchers that perform rapid reviews with a method to quickly perform searches.
