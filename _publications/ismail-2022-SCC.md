---
redirect_from: /publications/ismail-2022-SCC
authors: [ismail-sabei,ahmed-mourad, guido-zuccon]
title: "SCC - A Test Collection for Search in Chat Conversations"
venue: Proceedings of the 31st ACM International Conference on Information & Knowledge Management October 2022 (CIKM 22)
year: 2022
pdf: /publications/pdfs/ismail-2022-SCC.pdf
links:
 - url: https://github.com/ielab/SCC
   name: Code and Data
---
We present SCC, a test collection for evaluating search in chat conversations. Chat applications such as Slack, WhatsApp and Wechat have become popular communication methods. 
Typical search requirements in these applications revolve around the task of known item retrieval, i.e. find information that the user has previously experienced in their chats. 
However, the search capabilities of these chat applications are often very basic. Our collection aims to support new research into building effective methods for chat conversations search.
We do so by building a collection with 114 known item retrieval topics for searching over 437,893 Slack chat messages. 
An important aspect when searching through conversations is the unit of indexing (indexing granularity), e.g., it being a single message vs. an entire conversation. 
To support researchers to investigate this aspect and its influence on retrieval effectiveness, the collection has been processed with conversation disentanglement methods: these mark cohesive segments in which each conversation consists of messages whose senders interact with each other regarding a specific event or topic. This results in a total of 38,955 multi-participant conversations being contained in the collection. Finally, we also provide a set of baselines with related empirical evaluation, including traditional bag-of-words methods and zero-shot neural methods, at both indexing granularity levels.