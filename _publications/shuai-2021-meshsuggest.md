---
redirect_from: /shuai2021meshsuggest
authors: [shuai-wang, hang-li, harry-scells, daniel-locke, guido-zuccon]
title: 'MeSH Term Suggestion for Systematic Review Literature Search'
venue: Australasian Document Computing Symposium (ADCS 2021)
year: 2021
pdf: /publications/pdfs/shuai2021meshsuggest.pdf
projects: [systematic-reviews] 
links:
 - url: https://github.com/ielab/meshsuggestlib
   name: Python Package
 - url: https://github.com/wshuai190/MeSH_Suggester_Server
   name: Server Repo
 - url: https://www.youtube.com/channel/UC7mjnKA-liXtRJQegFmW4bA
   name: Video
---

## Abstract
High-quality medical systematic reviews require comprehensive literature searches to ensure the recommendations and outcomes are sufficiently reliable. Indeed, searching for relevant medical literature is a key phase in constructing systematic reviews and often involves domain (medical researchers) and search (information specialists) experts in developing the search queries. Queries in this context are highly complex, based on Boolean logic, include free-text terms and index terms from standardised terminologies (e.g., MeSH), and are difficult and time-consuming to build. The use of MeSH terms, in particular, has been shown to improve the quality of the search results. However, identifying the correct MeSH terms to include in a query is difficult: information experts are often unfamiliar with the MeSH database and unsure about the appropriateness of MeSH terms for a query. Naturally, the full value of the MeSH terminology is often not fully exploited.

This paper investigates methods to suggest MeSH terms based on an initial Boolean query that includes only free-text terms. These methods promise to automatically identify highly effective MeSH terms for inclusion in a systematic review query. Our study contributes an empirical evaluation of several MeSH term suggestion methods. We perform an extensive analysis of the retrieval, ranking, and refinement of MeSH term suggestions for each method and how these suggestions impact the effectiveness of Boolean queries.