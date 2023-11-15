---
authors: ["Mohamed A. Sharaf", rischan-mafrur, guido-zuccon]
title: "Efficient Diversification for Recommending Aggregate Data Visualizations"
venue: IEEE Access
year: 2023
pdf: /publications/pdfs/mafrur-2023-DiVE-extended.pdf
---

## Abstract 

Visual data exploration is ubiquitous in nearly every industry and organization to support discovering data-driven actionable insights. However, unlocking those insights requires analysts to manually construct a prohibitively large number of aggregate queries and visually explore their results, looking for those valuable and insightful visualizations. Such a challenge naturally motivated the development of novel solutions that automate the visual exploration process, and recommend to analysts those particular queries that best visualize their data and reveal interesting actionable insights. In such automated solutions, there is a clear need for providing analysts with a diversified and concise set of recommended visualizations, which cover and represent a large combinatorial high-dimensional space of possible visualizations. However, directly incorporating existing diversification methods leads to a “process-first-diversify-next” approach, in which all possible data visualizations are generated first through executing a large number of aggregate queries. To address this challenge and minimize the incurred query processing costs, in this work, we propose novel optimization techniques for the efficient diversification of recommended insightful visualizations. The key idea underlying our proposed techniques is to identify and eliminate the processing of a large number of low-utility insignificant visualizations. Meanwhile, for the potentially high-utility insightful visualizations, shared multi-query optimization techniques are proposed for further reduction in data processing cost. Our extensive experimental evaluation on real datasets demonstrates the performance gains provided by our proposed techniques, in terms of minimizing the query processing cost (i.e., efficiency), as well as maximizing the quality of recommendations (i.e., effectiveness).
