# XG4Repo: Explainable Graphs for Drug Repurposing

**Authors**: Zazo, S., et al.  
**Journal**: Nature Scientific Reports  
**Year**: 2024  
**DOI**: 10.1038/s41598-024-67163-x  
**URL**: https://www.nature.com/articles/s41598-024-67163-x

## Paper Analysis

### Problem
Drug repurposing using AI and knowledge graphs lacks explainability needed for clinical validation. While AI can process large amounts of data for repurposing predictions, the black-box nature of most approaches limits clinical adoption and validation.

### Prior Work Assumptions
- Prediction accuracy is the primary concern for drug repurposing systems
- Complex graph neural networks are necessary for superior performance
- Explainability can be addressed separately from prediction performance
- Generic knowledge graph completion methods work equally well for drug repurposing

### Key Insight
Explainable graph completion methods that automatically generate and optimize methapaths of different types and lengths can provide meaningful explanations for drug repurposing predictions through interpretable pathway connections.

### Technical Approach
- **XG4Repo Framework**: General architecture for explainable graph completion methods
- **Automatic Methapath Generation**: System automatically generates and optimizes pathways
- **Multi-Type Path Analysis**: Supports methapaths of different types and lengths
- **Biomedical Knowledge Graph Integration**: Leverages connectivity of biomedical knowledge graphs
- **Pathway-Based Explanations**: Paths include genes, pathways, side effects, anatomies
- **Target Mechanism Identification**: Provides information about targets and biomedical mechanisms

### Evaluation
- Case studies on Epirubicin, Paclitaxel, and Prednisolone repurposing
- Expert validation of predicted pathways and mechanisms
- Comparison with traditional drug repurposing approaches
- Analysis of pathway interpretability and clinical relevance

### Impact
- **Hypothesis Validation**: Strong support for H2 (actionability-first design) through explainable pathways
- **Clinical Adoption**: Addresses interpretability requirements for clinical validation
- **Mechanistic Understanding**: Provides biological rationale for repurposing predictions
- **Expert Integration**: Enables expert validation and further research guidance
- **Methodology Contribution**: Establishes framework for explainable knowledge graph completion

## Research Implications

This work directly addresses the clinical translation gap in AI drug repurposing by prioritizing explainability alongside prediction accuracy. The pathway-based explanations provide the mechanistic understanding required for clinical adoption, validating our core hypothesis about actionability-first design.

## Citation
Zazo, S., et al. (2024). Explainable drug repurposing via path based knowledge graph completion. Scientific Reports, 14, 16751.