---
authors: [shengyao-zhuang, hang-li, shuai-wang, guido-zuccon]
title: IELAB at TREC Deep Learning Track 2021
venue: TREC 2021 Deep Learning Track
year: 2021
pdf: /publications/pdfs/arvin2021trecdl.pdf
---
## Abstract

We describe the methods used by the IELAB in the TREC Deep Learning Track (TREC DL) 2021. The IELAB investigated three BERT-based ranking models to improve both the retrieval and the re-ranking stages of the passage ranking system. As for the passage retrieval runs, the methods used were: a novel learned sparse index method called uniCOIL, a dense retriever method called ADORE, and the combination of the two (hybrid). For the passage re-ranking run, TILDEv2, a fast yet effective passage re-ranking method, was used. Both uniCOIL and TILDEv2 rely on passage expansion. Com- mon practice is to use the docTquery-T5 for passage expansion – however this method does not scale well. In fact, performing the expansion for the newly released MS MARCOv2 passage collection, which is 15.6 times larger than the old v1 collection, was not pos- sible within the timeframe of the TREC DL 2021 task. To address this issue, we adapt the TILDE model to serve as the passage expan- sion method: compared to docTquery-T5, TILDE reduces passage expansion time by 98%.