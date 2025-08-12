# K-Paths: Reasoning over Graph Paths for Drug Repurposing and Drug Interaction Prediction

**Citation**: Abdullahi, T., Gemou, I., Nayak, N.V., et al. (2025). K-Paths: Reasoning over Graph Paths for Drug Repurposing and Drug Interaction Prediction. arXiv:2502.13344.

## Analysis Framework

### Problem
- **What problem does it solve?** 
  - Extracting meaningful insights from large-scale biomedical knowledge graphs is challenging
  - Traditional subgraph methods only work with GNNs, not LLMs
  - Complex graph traversal limits practical applications

### Prior Assumptions
- **What did earlier work assume?**
  - Subgraph-based methods are optimal for knowledge graph analysis
  - Graph neural networks are the only viable approach for KG reasoning
  - Large language models cannot effectively process graph-structured data

### Insight
- **What's the novel contribution?**
  - K-Paths framework extracts structured, diverse, biologically meaningful paths from KGs
  - Enables both LLMs AND GNNs to predict drug interactions effectively
  - Bridges gap between knowledge graphs and large language models

### Technical Approach
- **How is it implemented?**
  - Diversity-aware adaptation of Yen's algorithm for K shortest loopless paths
  - Structured path format that LLMs can directly process
  - Reduces KG size by 90% while maintaining performance
  - Facilitates explainable reasoning through path visualization

### Evaluation
- **How was it validated?**
  - Llama 8.1B: +12.45 F1 points on drug repurposing, +13.42 on interaction severity
  - Llama 70B: +6.18 and +8.46 F1 point gains respectively
  - EmerGNN: Maintained performance with 90% KG size reduction
  - Provides explainable rationales for predictions

### Impact
- **What are the implications?**
  - Democratizes knowledge graph analysis for drug discovery
  - Enables explainable AI for drug repurposing decisions
  - Bridges traditional graph methods with modern LLM capabilities

## Technical Innovation
- **Path Extraction**: Novel approach to make KGs accessible to LLMs
- **Explainability**: Provides clear reasoning paths for predictions
- **Efficiency**: 90% size reduction while maintaining performance
- **Versatility**: Works with both GNNs and LLMs

## Relevance to Our Hypotheses
- **H1 (Data Minimalism)**: Achieves 90% data reduction with maintained performance
- **H2 (Actionability-First)**: Provides explainable reasoning paths for clinical decisions
- **H5 (Human-AI Collaboration)**: Explainable paths enable human verification and guidance
- **Technical Bridge**: Shows how to make complex biomedical data accessible to modern AI