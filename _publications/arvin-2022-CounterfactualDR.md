---
redirect_from: /publications/arvin-2022-sigir-CounterfactualDR
authors: [shengyao-zhuang, hang-li, guido-zuccon]
title: 'Implicit Feedback for Dense Passage Retrieval: A Counterfactual Approach'
venue: The 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '22)
year: 2022
links:
 - url: https://arxiv.org/pdf/2204.00718.pdf
   name: Arxiv
 - url: https://github.com/ielab/Counterfactual-DR
   name: Github
---
---
## Abstract

In this paper we study how to effectively exploit implicit feedback in Dense Retrievers (DRs). We consider the specific case in which click data from a historic click log is available as implicit feedback. We then exploit such historic implicit interactions to improve the effectiveness of a DR. 
A key challenge that we study is the effect that biases in the click signal, such as position bias, have on the DRs. To overcome the problems associated with the presence of such bias, we propose the Counterfactual Rocchio (CoRocchio) algorithm for exploiting implicit feedback in Dense Retrievers. We demonstrate both theoretically and empirically that dense query representations learnt with CoRocchio are unbiased with respect to position bias and lead to higher retrieval effectiveness.
