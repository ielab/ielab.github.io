---
name: Scalable Generative IR
image: /images/projects/sysrev.jpg
featured: true
people: [shuai-wang, shengyao-zhuang, shuyi-wang, guido-zuccon, bevan-koopman]
---

## About this project

The **Scalable Generative Information Retrieval (IR)** project investigates how generative models can be applied to information retrieval tasks in a scalable and efficient manner. Our goal is to develop retrieval systems that leverage large language models (LLMs) while remaining practical for real-world applications, such as domain-specific search and systematic reviews.

### Key Areas of Focus
- **Generative Representations:** We explore how encoder-decoder and decoder-only LLMs can generate representations for queries and documents, replacing traditional retrieval paradigms.

- **Elastic Modeling:** Our models support dynamic adjustment of transformer depth and embedding dimensionality, enabling flexible trade-offs between accuracy and speed.

- **Pretraining & Fine-tuning:** We introduce techniques such as **Structured Representation Learning (SRL)** and **Sparse Masked Autoencoding (SMAE)** to improve model robustness and generalization.

- **Cross-Domain Evaluation:** The models are tested across diverse benchmarks including web search, scientific literature, and biomedical datasets to validate their generalizability.

- **Scalable Inference:** We employ techniques like **2D Matryoshka pruning** to train compact, layer-adaptive retrievers, and explore **context compression strategies** to reduce memory and token usage in retrieval-augmented generation (RAG) systems.
