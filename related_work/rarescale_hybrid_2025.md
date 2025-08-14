# RareScale: Rare Disease Differential Diagnosis with Large Language Models at Scale (2025)

## Citation
Schumacher, E., Naik, D., & Kannan, A. (2025). Rare Disease Differential Diagnosis with Large Language Models at Scale: From Abdominal Actinomycosis to Wilson's Disease. arXiv:2502.15069.

## Summary

**Problem**: LLMs have demonstrated impressive capabilities in disease diagnosis but their effectiveness in identifying rare diseases remains limited. Clinical decision support systems for rare diseases lack knowledge of common disorders and are difficult to use.

**Assumption in Prior Work**: LLMs can be used directly for rare disease diagnosis without specialized architectures or expert system integration.

**Insight**: RareScale combines LLM knowledge with expert systems through a hybrid approach - using expert systems + LLMs to generate training data for a rare disease candidate predictor, then feeding candidates to black-box LLMs for final differential diagnosis.

**Technical Overview**: 
- Joint expert system and LLM simulation of rare disease chats
- Rare disease candidate predictor model training 
- Two-stage architecture: candidate generation → final diagnosis
- Evaluation on 575+ rare diseases from Abdominal Actinomycosis to Wilson's Disease

**Proof**: 17% improvement in Top-5 accuracy over baseline black-box LLMs; 88.8% candidate generation performance on GPT-4o generated chats.

**Impact**: Demonstrates that hybrid human-AI systems can effectively balance rare and common diagnoses, addressing a critical gap in clinical decision support for rare diseases.

## Relevance to Our Research

**Directly Validates Multiple Hypotheses**:
- **H5 (Human-AI Collaboration)**: Explicit hybrid architecture combining expert knowledge with LLM capabilities
- **H2 (Actionability-First)**: Focus on clinical decision support rather than pure prediction accuracy
- **H1 (Data Minimalism)**: Strategic use of expert systems to generate high-quality training data rather than massive datasets
- **H15 (Rare Disease-Specific Methods)**: Specialized architecture optimized for rare disease constraints

**Key Insights**:
1. **Expert-LLM Synergy**: Shows that combining expert systems with LLMs outperforms either approach alone
2. **Clinical Translation Focus**: Explicitly designed for primary care physician workflow integration
3. **Scalability**: Covers 575+ rare diseases, demonstrating approach scales to comprehensive rare disease coverage
4. **Performance Gains**: Significant improvement over baseline LLMs validates our hypothesis about specialized approaches

**Connection to Literature-Level Assumptions**:
- Challenges assumption that general-purpose LLMs sufficient for rare disease diagnosis
- Validates our assumption flip that specialized hybrid systems outperform monolithic approaches
- Shows implementation-focused design achieving superior real-world utility

## Notes
- First large-scale systematic approach to LLM-based rare disease diagnosis
- Novel two-stage architecture could inform other rare disease AI applications
- Strong validation of our core thesis about human-AI collaborative intelligence
- Demonstrates practical clinical utility with measurable performance improvements