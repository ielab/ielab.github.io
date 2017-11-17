## Available Student Projects

These project suit Masters students for IFN701/702 or IFN665 and Honours students. Some projects could be the basis for extension for a PhD project. 



### An exploration of BM25F [assigned]

BM25F extends the BM25 weighting model to the case of fielded retrieval (e.g. in the presence of documents that have fields, like a web page).

BM25F is a rather standard technique, and has been implemented in various IR tools such as Lucene, Elasticsearch, Lemur and Terrier. However, our initial investigation has shown that the BM25F implementation of Elasticsearch and Terrier differs between each other and from that of the original BM25F model proposed by Robertson and Zaragoza. 

This project will investigate these differences both formally and empirically. The project will further extend a series of experiments we have setup on a number of test collections, and across a number of experimental variables. 
You will have to understand the current code that we have implemented, run this for the additional experiments that are required, and extend the code when relevant. The code is in Python and R; some modifications to the Elasticsearch/Terrier tools are required (they are implemented in Java).

The tasks to be performed in this project include:

1. implementing the original BM25F model in Elasticsearch and Terrier. This requires a good understanding of Java as we will need to hack the Elasticsearch and Terrier source code.
2. Use CLEF 2016, HARD 2003, HARD 2005, TREC WebTrack 2014-2015 to compare performance of BM25F implementations: Terrier, Elasticsearch BM25F and Original BM25F.
3. Summarise the results professionally in a written form, by extending a current research article draft

This project is likely to result in a co-authored journal publication at the end of the internship.


### Survey and implementation of SEO techniques

Search Engine Optimisation (SEO) aims to tweak web pages to increase their ranking on a target search engine, e.g. Google. SEO is a large market and is based on “black-magic”; SEO experts have suggested a number of techniques to guarantee to be ranked on top positions, some of these are trivial, others are no-where near what a search engine like Google would care about, others do make sense. All techniques have in common that their effectiveness has not been empirically demonstrated nor scientifically investigated. 

In this project, you will go through the relevant literature regarding SEO, including some of the non-academic, gray-literature books that have been published. You will collect the techniques that have been put forward for SEO, along with any evidence of their effectiveness. In the second part of the project, you will implement (preferably in Python) a number of the techniques you have surveyed and test them across a collection of web pages. We do not ask you collect as yet the effectiveness of these techniques in a formal way, but ensure that the techniques you implemented are working correctly.

Tasks:

1) survey the literature and write a short summary of the techniques that have been proposed
2) implement selected techniques
3) setup a test collection to test the effectiveness of the techniques

This project is unlikely to produce a publication within the scope of the internship or within short time from its conclusion.


### A study of Health Cards

When searching for health information online, Google at times displays so called Health Cards, i.e. a collection of summarised, highly curated information related to a symptom, condition or disease. 

This project will explore:

1) what triggers an health card: given a wide range of health search queries, you will record whether an health card is triggered. At this stage, you will also record the health card
2) what information is in an health card? 
3) are health cards tackling the right conditions? You will use the data collected above, to study whether the health card is relevant to the symptom, condition or disease. You may required help from a medical expert for this (we provide you with this), but you still will have to facilitate the medical expert in his analysis (may need to develop a small interface for the expert to evaluate the correctness). 
4) how are health cards helping users taking decisions, and are they improving the decision? In this part you will devise a user study for evaluating the effectiveness of the health cards. You will not run the user study (if not for testing the protocol), but you will have to setup an appropriate system and protocol. (This may require the development of appropriate web interfaces). 

This project requires the development of data acquisition methods, in Python, along with data analysis methods, both in Python and R.

This project may produce a small publication at the end of the internship, or in the immediate period after the internship is concluded. 

------------------------------------------------------------

### Simulating Users to Train Systems

Recent advances in user modelling have resulted in the creation of models that can be used to simulate user behaviour related to querying, clicking/assessing and stopping search. It has been argued that these models could be used to evaluate search effectiveness. 

In this project, we take a different view and are interested to explore the use of these models to generate data to train learning-based search engines such as learning to rank systems and deep learning systems. These systems in fact showed promising search effectiveness, but require a large quantity of training data, which is often impossible to acquire for small, specialised search engines (think about domain specific), and also for academic and research purposes. 

The tasks in this project are:

1) implement user simulation models. Some of these models have been already implemented by a third party (Java or Python)
2) implement and deploy learning to rank and deep learning models. Some of these models (learning to rank) are available in tools such as Terrier, but others are not and require implementation. (Java and Python)
3) devise experiments to train models with simulated data and evaluate them on real data, available in existing test collections
4) evaluate the models under different conditions and write up results in a professional manner

This project may produce a publication at the end of the internship, or in the immediate period after the internship is concluded; however the implementation and empirical work is quite large, thus there may be not enough time to work on a publication within the scope of the internship

------------------------------------------------------------

### Integrating Complex Operations with Word Embeddings into Retrieval Models

Word Embeddings
