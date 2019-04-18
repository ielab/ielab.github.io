---
name: Building Economic Models and Measures of Search
venues: [SIGIR2019]
people:
 - name: leif-azzopardi
 - name: "Alistair Moffat"
   image: /images/alistair-moffat.jpg
 - name: "Paul Thomas"
   image: /images/paul-thomas.jpg
 - name: guido-zuccon
description: Material for the Building Economic Models and Measures of Search tutorial at SIGIR 2019
links: 
 - url: https://github.com/ielab/bemms2019
   name: GitHub
---



Economics provides an intuitive and natural way to formally represent the costs and benefits of interacting with applications, interfaces and devices. By using economic models it is possible to reason about interaction, make predictions about how changes to the system will affect performance and behavior, and measure the performance of people's interactions with the system.  In this course, we will first provide an overview of relevant economic theories e.g., information foraging theory and the microeconomics of search. This will be then followed by a session showing how economics can be used to model interaction with search systems to generate hypotheses about behaviour and performance which can be used to inform design and guide experimentation. The third session will focus on how economics has been used to underpin the measurement of information retrieval systems and applications using the CWL framework (which reports the expected utility, expected total utility, expected total cost, etc.) - and how  different models of user interaction lead to different metrics. We then will show how information foraging theory can be used to measure the performance of an information retrieval system - connecting the theory of how people search with how we measure it. The final session of the day will be spent building economic models and measures of search. Here sample problems will be provided to challenge participants, or participants can bring their own.


## Session 1 -- Economics in IR

The first session will focus on providing a grounding in economics and optimization models [12, 18], why we need such models, and how they can be used to gain insights about search performance and search behaviour. We will then provide an high level overview of how different economics concepts and theories have been utilized within the field of Information Retrieval, in terms of: (1) ranking documents, (2) modelling user behaviour and (3) measuring performance. Specifically, we will discuss how various models of user behavior have been proposed over the years (e.g., reading models, click models, cascade model, etc.), and how they they have been formally and informally incorporated into ranking models, principles and evaluation measures. Here we will describe how models of user behaviour underpin document ranking principles and common metrics like precision at k and discounted cumulative gain.

For the remainder of the session, we will take a deeper dive into the economics behind ranking principles - specifically starting from the probability ranking principle (PRP), and how this decision theoretic approach to ranking and the assumptions it makes about user behaviour lead to how documents can be ranked optimally. We will then explain how the PRP’s assumptions about user behaviour can be relaxed and how it can be extended to consider interaction via the Interactive Probability Ranking Principle [11] and the Generalized PRP, i.e., the Card Model [28], which leads to a more game theoretic approach to IR [27]. This session will provide the foundations for understanding how economics has guided and underpinned the development of ranking models, and how the recently proposed principles provide the foundations for future advancements.


## Session 2 – Economic Models of Search

In session two, we will change focus, and examine models that are more user-focused. That is we will provide an overview of economic models that aim to explain and predict user search behaviour and interaction [2, 3, 6, 19]. We will then focus on Information Foraging Theory [19, 20, 23, 24] (IFT), which applies economics to how people find and forage for information (based on Optimal Foraging Theory [25] from ecology). We will explain how IFT can more generally be used to model how people attempt to maximize the benefit they receive from their interactions with the system over time (e.g., maximize the rate of gain over time). While IFT has been used to motivate experimentation at the high level, we will explain more concretely how IFT can be used to derive testable hypotheses about how people will interact with a search system, and how people try to maximise their performance (using Charnov’s Marginal Value Theorem [9]), and how their behavior will adapt to varying circumstances. To ground the session, we describe examples based on exploratory search [1, 22].


We will then continue working through different economic models that have been developed to formally model different interfaces, features and scenarios. This session puts the theory into practice and will show participants a series of models that provide insights into the trade-off between interactions and the choices between interactions (i.e., when users will select one option over another). To this end, we provide a series of models relating to search interfaces and search functionality. For example, we present: (a) the trade-off between querying and assessing [3] and (b) the trade-off between how much time a user should invest in the system vs. the system or another user (in a collaborative setting) [10]. Then we show how different functionalities can be analyzed to decide when and how people should give recommender systems feedback, when they should take query suggestions, and how long their queries should be [6, 7]. These examples will show participants how economic models can be used to draw actionable insights regarding how to improve the system’s features and functionality, by identifying how the different costs and benefits impact usage, behavior and performance.


## Session 3 – Economic Measures of Search

In the third session, we will examine how economics can be used to evaluate the user-system interactions and describe how economics measurements of search can be developed. Essentially, most metrics report the expected utility (or rate of gain) given the ranked list and model of user behaviour. Here we will link the models of search behaviour with how we measure search performance by describing and explaining the C/W/L framework which utilizes economics theory to provide the theoretical basis for measurement. The C/W/L framework, proposed by Moffat et al. [15, 16], provides a standardised and intuitive way to encode a wide range of metrics. We will describe the mathematical basis behind the framework and show how it enables the reporting of not just Expected Utility per item inspected, i.e. the rate at which gain is acquired, but also the re- lated measurements of Expected Total Utility, the gain accumulated from the whole list; Expected Cost per item inspected; Expected Total Cost, the cost incurred in examining the results list; and Expected Depth, the number of items a searcher examines given the user model encoded within the metric [4, 14–16].

We will then take a deeper dive into the C/W/L framework and explain the user model employed by different metrics and how these are encoded within the framework in order to measure performance (as well as how to design one’s own metric). Here we will describe the user models and basis for P@k, DCG, RBP, INST, etc. Finally, we will conclude the session by showing how models of search behaviour (i.e. IFT) can be used to develop an economics metric within the C/W/L framework - connecting the how we model search with how we measure search.


## Session 4 – Practical Session

The final session of the tutorial will be dedicated to a hands-on practical session where we will challenge participants to apply economics modelling techniques to different scenarios - where they will need to model user behaviour in order to hypothesize about how people will interact with the system or to evaluate how well people perform using the system. We will also invite participants to bring their own problems to the tutorial to discuss how the theory can be applied to their problems. This session will be performed in small groups and participants will present their model and/or metric at the end of the day.

To kick the session off, we will start by introducing a problem, and then collaboratively model user interaction, the costs and benefits, based on the interfaces and its affordances. This will help to guide participants showing them how they can model a new problem, before going off in groups to tackle their own problem or a supplied example problem.


### References

    - [1] Kumaripaba Athukorala, Antti Oulasvirta, Dorota Glowacka, Jilles Vreeken, and Giulio Jacucci. 2014. Narrow or Broad?: Estimating Subjective Specificity in Exploratory Search. In Proc. of the 23rd ACM CIKM. 819–828.
    - [2] Leif Azzopardi. 2011. The Economics in Interactive Information Retrieval. In Proc. SIGIR. 15–24.
    - [3] Leif Azzopardi. 2014. Modelling Interaction with Economic Models of Search. In Proc. SIGIR. 3–12.
    - [4] Leif Azzopardi, Paul Thomas, and Nick Craswell. 2018. Measuring the Utility of Search Engine Result Pages: An Information Foraging Based Measure. In The 41st International ACM SIGIR Conference on Research &#38; Development in Information Retrieval (SIGIR ’18). 605–614.
    - [5] Leif Azzopardi and Guido Zuccon. 2015. An Analysis of Theories of Search and Search Behavior. In Proceedings of the 2015 International Conference on The Theory of Information Retrieval (ICTIR ’15). 81–90.
    - [6] Leif Azzopardi and Guido Zuccon. 2016. An Analysis of the Cost and Benefit of Search Interactions. In Proceedings of the 2016 ACM International Conference on the Theory of Information Retrieval (ICTIR ’16). 59–68.
    - [7] Leif Azzopardi and Guido Zuccon. 2016. Two Scrolls or One Click: A Cost Model for Browsing Search Results.
    - [8] Leif Azzopardi and Guido Zuccon. 2018. Computational Interaction. Oxford University Press, Chapter Economics models of interaction: a tutorial on modeling interaction using economics.
    - [9] Eric L Charnov. 1976. Optimal Foraging, the Marginal Value Theorem. Theoretical population biology 9, 2 (1976), 129–136.
    - [10] Michael D. Cooper. 1972. A cost model for evaluating information retrieval systems. Journal of the American Society for Information Science (1972), 306–312. 
    - [11] Norbert Fuhr. 2008. A probability ranking principle for interactive information retrieval. Information Retrieval 11, 3 (2008), 251–265.
    - [12] Frederick S Hillier and Gerald J Lieberman. 2001. Introduction to operations research. NY, US (2001).
    - [13] Kalervo Järvelin and Jaana Kekäläinen. 2002. Cumulated Gain-based Evaluation of IR Techniques. ACM Trans. Inf. Syst. 20, 4 (Oct. 2002), 422–446.
    - [14] Alistair Moffat, Peter Bailey,Falk Scholer,and Paul Thomas. 2015. INST:An Adaptive Metric for Information Retrieval Evaluation. In Proc. Australasian Document Computing Symposium. Article 5, 4 pages.
    - [15] Alistair Moffat, Peter Bailey, Falk Scholer, and Paul Thomas. 2017. Incorporating User Expectations and Behavior into the Measurement of Search Effectiveness. ACM Trans. Inf. Syst. 35, 3, Article 24 (2017), 38 pages.
    - [16] Alistair Moffat, Paul Thomas, and Falk Scholer.2013.UsersVersusModels:What Observation Tells Us About Effectiveness Metrics. In Proc. CIKM. 659–668.
    - [17] Alistair Moffat and Justin Zobel. 2008. Rank-Biased Precision for Measurement of Retrieval Effectiveness. ACM Trans. on Information Systems 27, 1 (2008), 2:1–2:27. [18] Katta G Murty. 2003. Optimization Models For Decision Making: Volume. Uni- versity of Michigan, Ann Arbor (2003).
    - [19] Peter Pirolli and Stuart Card. 1999. Information Foraging. Psychological Review 106 (1999), 643–675. Issue 4.
    - [20] Howard L Resnikoff. 1989. The illusion of reality. Springer-Verlag New York.
    - [21] Stephen E Robertson. 1977. The probability ranking principle in IR. Journal of documentation 33, 4 (1977), 294–304.
    - [22] Tuukka Ruotsalo, Kumaripaba Athukorala, Dorota Glowacka, Ksenia Konyushkova, Antti Oulasvirta, Samuli Kaipiainen, Samuel Kaski, and Giulio Jacucci. 2013. Supporting Exploratory Search Tasks with Interactive User Modeling. In Proceedings of the 76th ASIS&T Annual Meeting (ASIST ’13). Article 39, 10 pages.
    - [23] Daniel M. Russell, Mark J. Stefik, Peter Pirolli, and Stuart K. Card. 1993. The cost structure of sensemaking. In Proceedings of the INTERACT and SIGCHI Conference. 269–276.
    - [24] Pamela Effrein Sandstrom. 1994. An optimal foraging approach to information seeking and use. The library quarterly (1994), 414–449.
    - [25] D W Stephens and J R Krebs. 1986. Foraging Theory. Princeton University Press 1, 10 (1986), 100.
    - [26] Jun Wang and Jianhan Zhu. 2009. Portfolio theory of information retrieval. In Proceedings of the 32nd international ACM SIGIR conference. ACM, 115–122.
    - [27] ChengXiang Zhai. 2015. Towards a game-theoretic framework for information retrieval. In Proceedings of the 38th International ACM SIGIR Conference on Research and Development in Information Retrieval. ACM, 543–543.
    - [28] Yinan Zhang and Chengxiang Zhai. 2015. Information Retrieval As Card Playing: A Formal Model for Optimizing Interactive Retrieval Interface. In Proceedings of the 38th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’15). 685–694.
    - [29] Guido Zuccon, Leif Azzopardi, Dell Zhang, and Jun Wang. 2012. Top-k retrieval using facility location analysis. In Proc. of ECIR. 305–316.

