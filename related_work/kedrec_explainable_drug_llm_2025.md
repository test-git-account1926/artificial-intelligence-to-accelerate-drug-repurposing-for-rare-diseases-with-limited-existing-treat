# KEDRec-LM: Knowledge-distilled Explainable Drug Recommendation LLM

**Authors**: Zhang, K., Zhu, R., Ma, S., Xiong, J., Kim, Y., Murai, F., Liu, X.  
**Journal**: arXiv  
**Year**: 2025  
**DOI**: 2502.20350  
**URL**: https://arxiv.org/abs/2502.20350

## Paper Analysis

### Problem
Drug discovery requires explainable recommendations that can provide clinical rationale, yet current approaches focus on prediction accuracy without interpretable justification. LLMs show promise but lack domain-specific knowledge integration for drug recommendation tasks.

### Prior Work Assumptions
- Prediction accuracy is sufficient for drug recommendation systems
- LLMs can operate effectively without extensive domain-specific knowledge integration
- Single-modal approaches are adequate for complex biomedical decision-making
- Explainability can be addressed post-hoc rather than designed into the system

### Key Insight
Knowledge-distilled LLMs that integrate comprehensive medical knowledge from multiple sources (knowledge graphs, clinical trials, literature) can provide both accurate drug recommendations and meaningful clinical rationales through instruction tuning.

### Technical Approach
- **Comprehensive Dataset Construction**: Utilizes drug knowledge graphs, clinical trial data, and PubMed publications
- **expRxRec Dataset**: First comprehensive dataset for explainable drug discovery tasks
- **KEDRec-LM Framework**: Instruction-tuned LLM architecture
- **Knowledge Distillation**: Distills knowledge from rich medical knowledge corpus
- **Dual Output Generation**: Produces both drug recommendations and explanatory rationales
- **Multi-Source Integration**: Combines structured knowledge graphs with unstructured literature

### Evaluation
- Evaluation on drug recommendation accuracy and rationale quality
- Human evaluation of generated explanations for clinical relevance
- Comparison with baseline LLMs and traditional drug recommendation systems
- Assessment of knowledge integration effectiveness through ablation studies

### Impact
- **Hypothesis Validation**: Directly validates H2 (actionability-first design) and H5 (human-AI collaboration)
- **Clinical Translation**: Addresses the explainability gap in AI-driven drug discovery
- **Methodological Innovation**: First knowledge-distilled explainable drug recommendation LLM
- **Dataset Contribution**: Provides expRxRec as a benchmark for explainable drug discovery
- **Real-World Applications**: Enables clinically interpretable drug recommendation systems

## Research Implications

This work represents a significant advancement in explainable AI for drug discovery, directly addressing the clinical need for interpretable recommendations. The emphasis on knowledge distillation and multi-source integration validates our hypotheses about actionability-first design and human-AI collaboration in medical AI systems.

## Citation
Zhang, K., Zhu, R., Ma, S., Xiong, J., Kim, Y., Murai, F., & Liu, X. (2025). KEDRec-LM: A Knowledge-distilled Explainable Drug Recommendation Large Language Model. arXiv:2502.20350.