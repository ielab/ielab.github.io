---
redirect_from: /publications/li-sigir-2022-nprf
authors: [hang-li, ahmed-mourad, bevan-koopman, guido-zuccon]
title: How does Feedback Signal Quality Impact Effectiveness of Pseudo Relevance Feedback for Passage Retrieval?
venue: Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR' 22)
year: 2022
links:
 - url: http://ielab.io/files/li-sigir-2022-nprf.pdf
   name: Paper PDF
 - url: http://ielab.io/files/li-sigir-2022-nprf-poster.pdf
   name: Poster
---
---
## Abstract

Pseudo-Relevance Feedback (PRF) assumes that the top results retrieved by a first-stage ranker are relevant to the original query and uses them to improve the query representation for a second round of retrieval. This assumption however is often not correct: some or even all of the feedback documents may be irrelevant. Indeed, the effectiveness of PRF methods may well depend on the quality of the feedback signal and thus on the effectiveness of the first-stage ranker. This aspect however has received little attention before.

In this paper we control the quality of the feedback signal and measure its impact on a range of PRF methods, including traditional bag-of-words methods (Rocchio), and dense vector-based methods (learnt and not learnt). Our results show the important role the quality of the feedback signal plays on the effectiveness of PRF methods. Importantly, and surprisingly, our analysis reveals that not all PRF methods are the same when dealing with feedback signals of varying quality. These findings are critical to gain a better understanding of the PRF methods and of which and when they should be used, depending on the feedback signal quality, and set the basis for future research in this area.