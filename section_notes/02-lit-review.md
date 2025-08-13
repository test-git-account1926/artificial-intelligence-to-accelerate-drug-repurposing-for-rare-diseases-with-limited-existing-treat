





# Literature Review

## Summary

Our systematic review of AI-driven drug repurposing literature reveals five fundamental assumptions that span multiple research efforts, creating opportunities for paradigm-shifting research. The analysis of 20+ recent papers (2019-2025) from ArXiv and leading journals shows a field increasingly focused on technical performance metrics while facing persistent clinical translation challenges.

**Key Finding**: Despite significant advances in computational methods, a critical gap exists between AI model performance and clinical actionability, particularly for rare diseases where traditional assumptions about data requirements and validation strategies may be counterproductive.

## Literature-Level Assumptions Identified

Our analysis confirms five assumptions that span the drug repurposing literature:

1. **Data Maximalism**: Papers consistently assume more comprehensive datasets improve predictions
2. **Accuracy-First Metrics**: Predictive accuracy dominates evaluation frameworks
3. **Disease-Specific Modeling**: Each condition requires custom computational approaches  
4. **Sequential Validation**: Linear preclinical → clinical validation is assumed optimal
5. **AI Supremacy**: Human expertise is viewed as bias to be minimized

## Key Papers Analysis

### Multi-Agent and Explainable Systems

#### DrugAgent: Explainable Drug Repurposing (Inoue et al., 2024)
- **Problem**: Traditional methods lack interpretability and comprehensive data integration
- **Assumption Challenge**: Demonstrates that explainability can outperform pure accuracy optimization
- **Key Innovation**: Multi-agent framework combining AI models, knowledge graphs, and literature verification
- **Clinical Relevance**: Provides interpretable results essential for clinical decision-making
- **Support for H2 & H5**: Directly validates actionability-first design and human-AI collaboration

#### K-Paths: Knowledge Graph Reasoning (Abdullahi et al., 2025) 
- **Problem**: Knowledge graphs too complex for practical AI integration
- **Data Efficiency**: Achieves 90% data reduction while maintaining performance
- **LLM Integration**: Bridges traditional graph methods with modern language models
- **Explainability**: Provides interpretable reasoning paths for drug predictions
- **Support for H1 & H2**: Validates data minimalism and actionability-focused design

### Rare Disease Applications

#### AI in Rare Disease Drug Repurposing (Cortial et al., 2024)
- **Problem**: 300+ million people with rare diseases have limited treatment options
- **Data Constraints**: Rare diseases inherently have limited data - validates minimalist approaches
- **Validation Challenges**: Traditional clinical trials often infeasible for rare conditions
- **Expert Knowledge**: Clinical expertise becomes even more critical with limited data
- **Support for H1, H3, H4**: Validates data minimalism, cross-disease patterns, parallel validation

#### Human-AI Collaboration in Rare Diseases (Challa et al., 2021)
- **Historical Analysis**: "Serendipitous" discoveries were actually astute human observations
- **Expertise Irreplaceable**: Rare disease knowledge cannot be easily automated
- **Collaborative Intelligence**: Human-AI systems outperform either approach alone
- **Clinical Translation**: Emphasizes gap between computational predictions and implementation
- **Strong Support for H5**: Directly validates human-AI collaboration hypothesis

### Technical Innovation and Validation

#### Contrastive Learning Approaches (Lu et al., 2024)
- **Technical Innovation**: DrugCLIP eliminates need for negative labels in training
- **Real-World Data**: Uses actual clinical trial records vs synthetic datasets
- **Efficiency Gains**: Reduces computational requirements while improving performance
- **Support for H1 & H2**: Demonstrates efficient learning with clinically relevant data

#### Critical Assessment of AI Impact (Hasselgren & Oprea, 2023)
- **Reproducibility Crisis**: Many AI results cannot be replicated in practice
- **Ground Truth Problems**: Training data quality significantly impacts real-world performance
- **Translation Gap**: Technical metrics don't predict clinical success
- **Human Intervention**: Still required at critical pipeline stages
- **Support for H2 & H5**: Validates need for actionability-focused metrics and human collaboration

### Emerging Paradigms

#### Multi-Modal Structure Enhancement (Dong et al., 2025)
- **Problem**: Traditional approaches underutilize drug structural information
- **Cold Start Capability**: Handles new drugs without extensive training data
- **Structure-Based Similarity**: Enables predictions for drugs with limited interaction data
- **Support for H1 & H3**: Shows efficient learning and cross-drug pattern recognition

#### Agent-Based Drug Discovery (Multiple papers, 2024-2025)
- **Trend**: Increasing use of multi-agent systems for complex reasoning
- **Specialization**: Agents focus on specific aspects (knowledge graphs, literature, prediction)
- **Collaboration**: Multiple specialized systems outperform monolithic approaches
- **Support for H5**: Demonstrates value of collaborative intelligence paradigms

## Cross-Paper Patterns

### Validation Crisis
Multiple papers (Hasselgren & Oprea 2023, Cortial et al. 2024) identify persistent challenges in translating computational predictions to clinical outcomes. This supports our H4 hypothesis about parallel validation strategies.

### Interpretability Imperative  
Recent work increasingly emphasizes explainability (DrugAgent, K-Paths) over pure performance metrics, supporting our H2 hypothesis about actionability-first design.

### Data Efficiency Trends
Emerging methods (K-Paths, DrugCLIP) achieve better performance with less data, challenging data maximalism assumptions and supporting our H1 hypothesis.

### Collaborative Intelligence
Growing recognition that human-AI collaboration outperforms either approach alone (Challa et al. 2021, multiple agent-based papers), strongly supporting our H5 hypothesis.

## Research Gaps Our Work Addresses

### 1. Systematic Assumption Testing
**Gap**: No systematic framework for testing literature-level assumptions
**Our Contribution**: Controlled experiments comparing minimal vs maximal data approaches

### 2. Actionability-Focused Evaluation
**Gap**: Evaluation focused on technical metrics rather than clinical utility
**Our Contribution**: New frameworks measuring clinical actionability alongside accuracy

### 3. Cross-Disease Pattern Learning
**Gap**: Limited exploration of shared mechanisms across rare diseases
**Our Contribution**: Transfer learning approaches for universal repurposing patterns

### 4. Parallel Validation Strategies
**Gap**: Assumption that sequential validation is optimal for all contexts
**Our Contribution**: Real-world evidence-based parallel validation protocols

### 5. Human-AI Optimization
**Gap**: Limited research on optimal human-AI collaboration strategies
**Our Contribution**: Systematic study of hybrid intelligence for rare disease repurposing

## Literature Synthesis

The literature reveals a field in transition. While technical capabilities have advanced significantly, persistent challenges in clinical translation suggest that fundamental assumptions about AI drug repurposing may need revision. Our research directly addresses this gap by:

1. **Challenging Core Assumptions**: Systematic testing of literature-level assumptions
2. **Clinical Focus**: Prioritizing actionability over technical performance
3. **Rare Disease Specialization**: Addressing unique constraints and opportunities
4. **Collaborative Intelligence**: Optimizing human-AI partnerships
5. **Alternative Validation**: Developing parallel validation strategies

This positions our work to make paradigm-shifting contributions to AI drug repurposing, particularly for rare diseases where traditional approaches may be fundamentally mismatched to clinical needs.





