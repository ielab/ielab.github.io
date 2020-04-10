---
authors: [harry-scells, guido-zuccon, "Mohamed A. Sharaf", bevan-koopman]
title: Sampling Query Variations for Learning to Rank to Improve Automatic Boolean Query Generation in Systematic Reviews
venue: Proceedings of The Web Conference 2020
year: 2020
pdf: /publications/pdfs/scells2020sampling.pdf
projects: [systematic-reviews] 
redirect_from: /www-sampling
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/C4LA-UNgakw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Searching medical literature for synthesis in a systematic review is a complex and labour intensive task. In this context, expert searchers construct lengthy Boolean queries. The universe of possible query variations can be massive: a single query can be composed of hundreds of field-restricted search terms/phrases or ontological concepts, each grouped by a logical operator nested to depths of sometimes five or more levels deep. With the many choices about how to construct a query, it is difficult to both formulate and recognise effective queries. To address this challenge, automatic methods have recently been explored for generating and selecting effective Boolean query variations for systematic reviews. The limiting factor of these methods is that it is computationally infeasible to process all query variations for training the methods. To overcome this, we propose novel query variation sampling methods for training Learning to Rank models to rank queries. Our results show that query sampling methods do directly impact the ability of a Learning to Rank model to effectively identify good query variations. Thus, selecting appropriate query sampling methods is a key problem for the automatic reformulation of effective Boolean queries for systematic review literature search. We find that the best sampling strategies are those which balance the diversity of queries with the quantity of queries.
