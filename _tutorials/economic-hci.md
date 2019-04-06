---
name: Building Economic Models of HCI
venues: [CHI2019]
people: [guido-zuccon, leif-azzopardi]
description: Tutorials and resources on building economic models of how people interact with interfaces and systems.
links: 
 - url: https://github.com/ielab/economic-hci-tutorial
   name: GitHub
---


<h2>Course Overview</h2>
Economics provides an intuitive and natural way to formally represent the cost and benefits of interacting with applications, interfaces and devices. By using economics models it is possible to reason about interaction and make predictions about how changes to the system will affect performance and behavior. In this course, we provided an overview of relevant economic concepts and then showed how economics can be used to model human computer interaction to generated hypotheses about interaction which can be used to inform design and guide experimentation. As a case study, we demonstrate how various interactions with search and recommender applications can be modeled, before concluding the day with a hands-on modeling session using example and participant problems.




The full day course included the following four sessions.

<h2>Session 1 – Building Economic Models</h2>
The first session focused on providing a grounding in economic and optimization models [11, 12], how to build such models [12, 20], and how to use them to gain insights about the phenomena under examination. Starting with a simple example of modeling different interfaces to browse through items, we showed how the costs of different interactions can be described within a cost function to compare different interfaces and user interaction strategies where the goal is to minimize the task completion time [8]. Then we showed how more sophisticated models can be developed which investigate the trade-offs between different interactions due to the associated costs and benefits. For example, how much more benefit/satisfaction a user receives from the interactions which comes at a cost, such as the trade-off between the length of a query and the performance of the query, or the trade-off between the amount of novel information found and the time taken to find it [2]. We then discussed the limitations of such approaches due to the modeling assumption that people act rationally, and so we described alternatives to economic models based on expected utility (i.e. prospect theory [19], etc.).


<h2>Session 2 – Information Foraging Theory</h2> 
Following on from Economic Models, we introduced concepts from Information Foraging Theory [13, 14, 16, 17] (IFT), which applies economics to how people find and forage for information (based on Optimal Foraging Theory [18] from Ecology). We explained how IFT can more generally be used to model how people attempt to maximize the benefit they receive from their interactions with the system over time (e.g., maximize the rate of gain over time). While IFT has been used to motivate experimentation at the high level, we explained how formal models can be built using IFT, and how they can be used to derive testable hypotheses about how people will interact with a given system (using Charnov’s Marginal Value Theorem [9]), and how their behavior will adapt to varying circumstances. To ground the session, we described examples based on exploratory search [1, 15].


<h2>Session 3 – Models: Theory to Practice</h2>
In this third session, we continued working through different economic models that have been developed to formally model different interfaces, features and scenarios. This session put the theory into practice and showed participants a series of models that provide insights into the trade-off between interactions and the choices between interactions (i.e.
when users will select one option over another). To this end, we provided a series of models relating to search interfaces and search functionality, for example, we presented: (a) the trade-off between querying and assessing [3] and (b) the trade-off between how much time a user should invest in the system vs. the system or another user (in a collaborative setting) [10]. Then showed how different functionalities can be analyzed to decide when and how people should give recommender systems feedback, when they should take query suggestions, and how long their queries should be [6, 7]. These examples showed how formal models lead to actionable insights regarding how to improve the system’s features and functionalities, by identifying how the different costs and benefits impact usage, behavior and performance.


<h2>Session 4 – Practical Session</h2>
The final session of the tutorial was dedicated to building models. Participants were given a range of design problems/contexts. For example, to decide on the layout and number of application icons to display on a mobile phone screen, along with the task setting i.e. that the user wants to navigate and open a particular application (app). The focus was on building different cost functions to model a variety of ways in which users can find the apps on their devices, e.g., search, browse, etc. To add realism to the scenario, we considered different types of user scenarios such as whether the user remembered (or not) where the app was, and how that affects the cost of re-finding, and introduced trade-offs between accuracy and speed. Participants were encouraged to identify the main variables that are likely to influence the interaction (i.e., the number of apps on the phone, the number of apps per screen, the cost of moving between screens, and so forth) and to consider how these factors affect the optimal solution/design. The participants then presented their solutions to the group. More advance design considerations were then discussed, such as presenting the most used apps first, or using hierarchical browsing structure, and to determine under what conditions such innovations were likely to improve the user’s performance. This scenario provided an excellent opportunity to reinforce the concepts learned during the day and show the potential and applicability of the approach.
Instructors background

<h2>References</h2>
<p>[1] Kumaripaba Athukorala, Antti Oulasvirta, Dorota Glowacka, Jilles Vreeken, and Giulio Jacucci. 2014. Narrow or Broad?: Estimating Subjective Specificity in Exploratory Search. In Proc. of the 23rd ACM CIKM. 819–828.
<p>[2] Leif. Azzopardi. 2011. The economics in interactive information retrieval. In Proc. of SIGIR. ACM, 15–24.
<p>[3] Leif. Azzopardi. 2014. Modelling Interaction with Economic Models of Search. In Proc. of SIGIR. 3–12.
<p>[4] Leif Azzopardi. 2017. Building Cost-Benefit Models of Information Interactions. In Proceedings of the 2017 Conference on
Conference Human Information Interaction and Retrieval (CHIIR ’17). 425–428.
<p>[5] Leif Azzopardi and Guido Zuccon. 2015. An Analysis of Theories of Search and Search Behavior. In Proceedings of the 2015
International Conference on The Theory of Information Retrieval (ICTIR ’15). 81–90.
<p>[6] Leif Azzopardi and Guido Zuccon. 2016. An Analysis of the Cost and Benefit of Search Interactions. In Proceedings of the
2016 ACM International Conference on the Theory of Information Retrieval (ICTIR ’16). 59–68.
<p>[7] Leif Azzopardi and Guido Zuccon. 2016. Two Scrolls or One Click: A Cost Model for Browsing Search Results.
<p>[8] Leif Azzopardi and Guido Zuccon. 2018. Computational Interaction. Oxford University Press, Chapter Economics models
of interaction: a tutorial on modeling interaction using economics.
<p>[9] Eric L Charnov. 1976. Optimal foraging: attack strategy of a mantid. The American Naturalist 110, 971 (1976), 141–151.
<p>[10] Michael D. Cooper. 1972. A cost model for evaluating information retrieval systems. Journal of the American Society for Information Science (1972), 306–312.
<p>[11] Frederick S Hillier and Gerald J Lieberman. 2001. Introduction to operations research. NY, US (2001).
<p>[12] Katta G Murty. 2003. Optimization Models For Decision Making: Volume. University of Michigan, Ann Arbor (2003).
<p>[13] P. Pirolli and S.K. Card. 1999. Information foraging. Psychological Review 106 (1999), 643–675. Issue 4.
<p>[14] Howard L Resnikoff, HL Resenikoff, and HL Resnikoff. 1989. The illusion of reality. Springer-Verlag New York.
<p>[15] Tuukka Ruotsalo, Kumaripaba Athukorala, Dorota Glowacka, Ksenia Konyushkova, Antti Oulasvirta, Samuli Kaipiainen,
Samuel Kaski, and Giulio Jacucci. 2013. Supporting Exploratory Search Tasks with Interactive User Modeling. In Proceedings
of the 76th ASIS&T Annual Meeting (ASIST ’13). Article 39, 10 pages.
<p>[16] Daniel M. Russell, Mark J. Stefik, Peter Pirolli, and Stuart K. Card. 1993. The cost structure of sensemaking. In Proc. of
INTERACT/SIGCHI. 269–276.
<p>[17] Pamela Effrein Sandstrom. 1994. An optimal foraging approach to information seeking and use. The library quarterly
(1994), 414–449.
<p>[18] DW Stephens and JR Krebs. 1986. Foraging Theory. Princeton: Princeton University Press 1, 10 (1986), 100.
<p>[19] Amos Tversky and Daniel Kahneman. 1989. Rational Choice and the Framing of Decisions. In Multiple Criteria Decision
Making and Risk Analysis Using Microcomputers. 81–126.
<p>[20] Hal R Varian. 1997. How to build an economic model in your spare time. American Economist 41 (1997), 3–10.
