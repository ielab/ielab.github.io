---
authors: [shuai-wang, hang-li, guido-zuccon]
title: "MeSH Suggester: A Library and System for MeSH Term Suggestion for Systematic Review Boolean Query Construction"
venue: "The 16th ACM International Conference on Web Search and Data Mining"
year: 2023
pdf: /publications/pdfs/shuai2023meshsuggester.pdf
redirect_from: /shuai2023meshsuggester
projects: [systematic-reviews]
links:
 - url: https://github.com/ielab/meshsuggestlib
   name: Python Package
 - url: https://github.com/wshuai190/MeSH_Suggester_Server
   name: Server Repo
---

## Abstract
Boolean query construction is often critical for medical systematic review literature search. To create an effective Boolean query, sys- tematic review researchers typically spend weeks coming up with effective query terms and combinations. One challenge to creating an effective systematic review Boolean query is the selection of effective MeSH Terms to include in the query. In our previous work, we created neural MeSH term suggestion methods and compared them to state-of-the-art MeSH term suggestion methods. We found neural MeSH term suggestion methods to be highly effective.
In this demonstration, we build upon our previous work by creating (1) a Web-based MeSH term suggestion prototype system that allows users to obtain suggestions from a number of underlying methods and (2) a Python library that implements ours and others’ MeSH term suggestion methods and that is aimed at researchers who want to further investigate, create or deploy such type of methods. We describe the architecture of the web-based system and how to use it for the MeSH term suggestion task. For the Python library, we describe how the library can be used for advancing further research and experimentation, and we validate the results of the methods contained in the library on standard datasets. Our web- based prototype system is available at https://github.com/wshuai190/MeSH_Suggester_Server, while our Python library is at https://github.com/ielab/meshsuggestlib.