---
authors: [harry-scells, guido-zuccon, bevan-koopman, "Justin Clark"]
title: Automatic Search Strategy Reformulation Interface for Systematic Reviews
venue: Proceedings of the Cochrane Colloquium 2019
year: 2019
projects: [systematic-reviews] 
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/A1GtoNFWN0c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Background:
Within the last decade the rise of digital publishing has become widespread, enabling publications to be edited and updated after-the-fact. In the medical domain, systematic reviews are one type of digital document that is often updated after initial publication. This is usually because new evidence has been discovered and must be re-synthesised into the existing review. A problem, however, is that the initial search strategy used to identify the originally relevant studies may not be sufficient in capturing new studies, or may capture too many irrelevant studies. This means that time and effort must be spent reformulating new or variant search strategies. While this problem may be particularly pronounced in “living systematic reviews”, the problem of finding all relevant studies while minimising irrelevant studies for typical systematic reviews is also difficult. This overarching problem signifies a gap to be filled with a system for automatic search strategy reformulation.

Objectives:
The development of an automatic, interactive search strategy reformulation tool that assists researchers in updating systematic reviews and to improve existing search strategies.

Methods:
The system proposed uses a recognised and effective theoretical framework which automatically generates search strategy reformulations and selects the most effective variation. In this work, a user interface (Figure 1)  is developed with the goal to insert a human-in-the-loop to drive the selection of the most effective search strategy. This interface is capable of: (i) tracking the effectiveness of reformulations over time, allowing users to manage their reformulation history by backtracking and jumping to previous search strategies, (ii) evaluating the effectiveness of reformulations using standard Information Retrieval measures (e.g., precision, recall, F-measure), and domain-specific evaluation measures (e.g., Work Saved) by loading in a validation set of studies, and (iii) filtering out studies which have already been screened (also by loading separately) in order to only show new studies.

Results:
The theoretical framework for which the generation and selection of search strategy reformulations is based on is shown to significantly improve the effectiveness of existing queries. Queries are shown to increase in effectiveness upwards of 100-200% and beyond depending on the automatic selection process and evaluation measure.

Conclusions:
A human-in-the-loop for the selection of search strategy reformulation allows users to have fine-grained control over the reformulation process. Allowing humans to drive the selection process in this framework is a new and novel approach, which has not yet been attempted. Finally, automatically generating reformulations removes possible human bias and error, and reduces the time and effort required to update a review.

Patient or healthcare consumer involvement:
This has no direct involvement with patients or consumers, although improved efficiency of systematic review searches could be beneficial to both groups.
