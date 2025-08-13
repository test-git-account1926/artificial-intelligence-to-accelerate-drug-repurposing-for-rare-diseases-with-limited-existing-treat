# LLMs for Drug-Drug Interaction Prediction: A Comprehensive Comparison (2025)

**Authors**: De Vito et al.  
**ArXiv**: 2502.06890  
**Date**: February 2025  

## 6-Point Analysis Framework

### 1. Problem
The increasing volume of drug combinations in modern therapeutic regimens requires reliable methods for predicting drug-drug interactions (DDIs). While Large Language Models have shown promise across domains, their potential in pharmaceutical research, particularly DDI prediction, remains largely unexplored and undervalidated.

### 2. Prior Assumptions
- **Structured data requirement**: Prior work assumes DDI prediction requires specialized molecular representations and graph-based architectures
- **Domain-specific models**: Traditional approaches assume pharmaceutical applications need custom-trained models
- **Feature engineering**: Prior methods assume hand-crafted molecular features are necessary for accurate predictions

### 3. Insight
LLMs can effectively process molecular structures, target organisms, and gene interaction data as raw text input, eliminating the need for specialized molecular representations. The key insight is that fine-tuned LLMs can capture complex molecular interaction patterns through text-based processing of SMILES and biological data.

### 4. Technical Approach
- **Text-Based Input**: Processes SMILES, target organisms, and gene interaction data as raw text
- **Comprehensive Evaluation**: 18 different LLMs from proprietary (GPT-4, Claude, Gemini) to open-source (1.5B-72B parameters)
- **Zero-Shot Assessment**: Initial evaluation without task-specific training
- **Selective Fine-Tuning**: Optimized performance through targeted fine-tuning of select models
- **Multi-Scale Analysis**: From small (1.5B) to large (72B) parameter models
- **External Validation**: Testing across 13 external DDI datasets

### 5. Evaluation
- **Model Scale**: 18 LLMs ranging from 1.5B to 72B parameters
- **Comprehensive Comparison**: Against traditional L2-regularized logistic regression and state-of-the-art ML methods
- **Performance Metrics**: Phi-3.5 2.7B achieved 0.978 sensitivity and 0.919 accuracy on balanced datasets
- **Superiority**: Fine-tuned LLMs outperformed both zero-shot predictions and traditional machine learning approaches
- **Cross-Dataset**: Validation across 13 external DDI datasets demonstrates generalizability

### 6. Impact
- **Methodological**: Demonstrates LLMs' effectiveness in processing molecular data as text
- **Practical**: Provides ready-to-use framework for pharmaceutical DDI prediction
- **Clinical**: Enables more accessible DDI screening for clinical settings
- **Research**: Opens new directions for text-based molecular interaction modeling
- **Scalable**: Framework applicable to related pharmaceutical prediction tasks

## Relevance to Our Hypotheses

**Challenges H1 (Data Minimalism)**: Demonstrates that larger, more comprehensive models can outperform minimal approaches  
**Supports H2 (Actionability-First)**: Focus on practical DDI prediction for clinical applications  
**Supports H3 (Cross-Drug Patterns)**: LLMs identify shared interaction patterns across different drug pairs  
**Supports H5 (Human-AI Collaboration)**: Provides interpretable text-based reasoning for drug interactions

## Key Technical Contributions
1. First comprehensive comparison of LLMs for DDI prediction using text-based molecular representations
2. Demonstration that fine-tuned smaller LLMs can outperform larger zero-shot models
3. Framework for processing SMILES and biological data as natural language input
4. Extensive validation across multiple external datasets showing generalizability

## Clinical Translation Advantages
- **Interpretability**: Text-based processing provides more interpretable reasoning than graph neural networks
- **Accessibility**: Standard LLM fine-tuning is more accessible than specialized molecular modeling
- **Integration**: Easier integration with existing clinical text-processing workflows
- **Scalability**: Can leverage existing LLM infrastructure and expertise

## Performance Insights
- **Fine-tuning Critical**: Significant improvement from zero-shot to fine-tuned performance
- **Model Size Trade-offs**: Smaller fine-tuned models (2.7B) can outperform larger zero-shot models
- **Gene Target Importance**: Models effectively leverage gene interaction data for improved predictions
- **Balanced Dataset Performance**: Strong performance on both positive and negative DDI cases

## Limitations
- Limited to DDI prediction (doesn't address drug repurposing directly)
- Requires fine-tuning for optimal performance, increasing computational requirements
- May not capture all nuances of molecular structure compared to specialized graph-based methods
- Validation focused on existing datasets rather than prospective clinical studies