---
authors: [harry-scells, guido-zuccon, bevan-koopman, "Justin Clark"]
title: Visualising Systematic Review Search Strategies to Assist Information Specialists
venue: Proceedings of the Cochrane Colloquium 2019
year: 2019
projects: [systematic-reviews] 
---

<img src="/images/scells/tree.png" style="max-width:640px;" alt="Figure 1">
<p><small><i>Figure 1</i></small></p>

Background:
Searching for studies to include in systematic reviews involves the construction of complex search strategies. The effectiveness of these search strategies directly impacts the workload associated with conducting a systematic review. More efficient search strategies can reduce the time and resources required to screen studies therefore reducing the total time and cost of the review. Research in Information Retrieval (IR) shows that query visualisation improves the effectiveness of searching for information.

Objectives:
The development of a visualisation tool that assists information specialists in formulating more effective search strategies. 

Methods:
The visualisation tool (QueryVis) is designed in collaboration with information specialists to cater to the needs of this user group. Currently in QueryVis, it is possible to visualise search strategies using the PubMed database. Searches can be submitted in Ovid MEDLINE format or PubMed format (by automatically translating the Ovid format to PubMed). QueryVis presents queries hierarchically (Figure 1) , showing the impact that each term has on the recall and precision of a search. Recall is shown by the number of studies retrieved from a validation set, loaded via PubMed IDs. Precision is shown by total number of studies found by each term. Search strategies are compared in terms of the overlap in search terms between two searches, the total number of keywords, the total number of each Boolean operator (i.e., AND, OR, NOT), the number of MeSH keywords (and how many are exploded), and the depth in the MeSH ontology in which the MeSH keywords appear (i.e., how broad MeSH keywords are). Furthermore, each search is evaluated in terms of effectiveness: using standard IR evaluation measures (i.e., precision, recall, F-measure) and evaluation measures specific to this domain (e.g., Work Saved), and in terms of efficiency: by recording the total time spent formulating, the number of studies retrieved, and the estimated cost of the search.

Results:
QueryVis has been tested experimentally in a pilot study. It decreased irrelevant studies by as much as 40% without losing relevant studies. A wider study is planned which aims to involve more participants and capture more data.

Conclusions:
Improving the query formulation stage can have a significant impact on the rest of the systematic review creation process. An extensive user study will follow using a well-known corpus of systematic reviews with approximately 10 participants to determine precisely what effect visualisation has on the search strategy formulation process. The study will use the aforementioned methods to compare the effect visualisation has on search by comparing search strategies formulated with and without visualisation. If accepted for publication, QueryVis will be demoed during the oral presentation.

Patient or healthcare consumer involvement:
This has no direct involvement with patients or consumers, although improved efficiency of systematic review searches could be beneficial to both groups.
