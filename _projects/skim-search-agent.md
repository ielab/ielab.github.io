---
name: SkimSearchAgent
image: /images/projects/skim-search-agent.jpg
featured: true
people: [shuai-wang, haodong-chen, yu-yin, shengyao-zhuang, guido-zuccon, teerapong-leelanupab]
---

## About This Project

**SkimSearchAgent** is an open-source Python framework for building and evaluating deep-search agents over your own document collection. These agents answer complex questions through repeated searching, reading, and reasoning. The framework lets researchers change the retriever, search tools, language model, or search strategy while keeping the rest of the experiment fixed, making it easier to understand which components improve an agent's effectiveness and efficiency.

### Key Areas of Focus

- **Modular agentic search:** Combine lexical, dense, sparse, and hybrid retrieval with rerankers, document-reading tools, and different language models. Compare multi-step search strategies with one-shot retrieval-augmented generation (RAG) and retrieval-only baselines.
- **Selective reading and interaction-aware retrieval:** The framework supports [Sieve](https://ielab.io/skim-search-agent/sieve/), which uses Boolean filtering and structured result cards to help agents inspect documents before fetching selected sections, and [ITER](https://ielab.io/skim-search-agent/iter/), which trains retrievers from agent trajectories and conditions retrieval on the search history.
- **Reproducible evaluation:** Every run records its configuration, full agent trajectory, and metrics in a shared format. Common evaluation tools and a [BrowseComp-Plus leaderboard](https://ielab.io/skim-search-agent/leaderboard/) support comparisons across retrievers, rerankers, and agent models.

Explore the [project website](https://ielab.io/skim-search-agent/) for an overview and examples, or visit the [GitHub repository](https://github.com/ielab/skim-search-agent) for installation instructions, experiment configurations, and documentation.
