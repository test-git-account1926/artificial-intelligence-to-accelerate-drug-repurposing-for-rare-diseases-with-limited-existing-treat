









# Literature Review

## Summary

Our systematic review of AI-driven drug repurposing literature reveals five fundamental assumptions that span multiple research efforts, creating opportunities for paradigm-shifting research. The analysis of 30+ recent papers (2019-2025) from ArXiv and leading journals shows a field in rapid evolution, with emerging paradigms challenging traditional assumptions about AI drug repurposing.

**Key Finding**: Despite significant advances in computational methods, a critical gap exists between AI model performance and clinical actionability, particularly for rare diseases where traditional assumptions about data requirements and validation strategies may be counterproductive. Recent 2025 research shows strong movement toward actionability-first designs, human-AI collaboration, and novel approaches to data efficiency.

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

### Breakthrough 2025 Research

#### DrugMCTS: Multi-Agent + Monte Carlo Tree Search (Yang et al., 2025)
- **Problem**: LLMs limited in drug repositioning when reasoning extends beyond pretraining knowledge
- **Innovation**: Combines multi-agent collaboration with Monte Carlo Tree Search for structured reasoning
- **Key Achievement**: Substantially higher recall and robustness compared to traditional approaches
- **Technical Breakthrough**: Five specialized agents with iterative reasoning and MCTS guidance
- **Support for H2 & H5**: Provides interpretable reasoning chains and collaborative intelligence

#### Decoding Rarity: LLMs in Rare Disease Diagnosis (Carbonari et al., 2025)
- **Problem**: Rare diseases lack diagnostic expertise accessibility
- **Innovation**: LLMs as intelligent conversational agents democratizing rare disease knowledge
- **Clinical Impact**: Makes specialized knowledge available to general practitioners
- **Future Vision**: Multimodal integration framework for comprehensive rare disease platforms
- **Strong Support for H5**: LLMs designed as collaborative diagnostic partners, not replacements

#### Madrigal: Multimodal AI for Clinical Outcomes (Huang et al., 2025)
- **Problem**: Gap between preclinical predictions and clinical outcomes
- **Innovation**: Transformer bottleneck unifying structural, pathway, cell viability, and transcriptomic data
- **Clinical Validation**: Successfully predicts FDA-approved MASH drug among top safety profiles
- **Missing Data Robustness**: Maintains performance with incomplete multimodal information
- **Challenges H1, Supports H2**: Demonstrates multimodal superiority but emphasizes clinical actionability

#### LLMs for Drug-Drug Interactions (De Vito et al., 2025)
- **Problem**: Need for reliable DDI prediction in complex therapeutic regimens
- **Innovation**: Text-based processing of SMILES and biological data using LLMs
- **Performance**: Phi-3.5 2.7B achieved 0.978 sensitivity, 0.919 accuracy
- **Key Finding**: Fine-tuned smaller models can outperform larger zero-shot models
- **Support for H2 & H3**: Text-based interpretability and cross-drug pattern recognition

#### Biomedical Knowledge Graphs: Unified Framework (Lu et al., 2025)
- **Problem**: Traditional databases inadequate for complex biomedical relationships
- **Innovation**: Comprehensive framework analyzing BKGs from domains, tasks, applications
- **Integration**: Molecular interactions, pharmacological data, clinical records
- **Real-World Impact**: Precision medicine and drug discovery applications
- **Challenges H1, Supports H2**: Comprehensive integration valuable, but emphasizes actionable applications

## Cross-Paper Patterns

### Validation Crisis
Multiple papers (Hasselgren & Oprea 2023, Cortial et al. 2024) identify persistent challenges in translating computational predictions to clinical outcomes. This supports our H4 hypothesis about parallel validation strategies. Madrigal (2025) demonstrates how real-world evidence can bridge preclinical-clinical gaps.

### Interpretability Imperative  
Strong 2025 trend toward explainability: DrugAgent, K-Paths, DrugMCTS all emphasize interpretable reasoning chains over pure performance. Carbonari et al. (2025) highlight clinical utility over accuracy. This strongly supports our H2 hypothesis about actionability-first design.

### Data Efficiency Revolution
Mixed but evolving evidence: K-Paths (2025) shows 90% data reduction with maintained performance; DrugCLIP (2024) efficient learning without negative sampling; Carbonari et al. (2025) focused textual data effectiveness. However, Madrigal (2025) and BioKG Survey (2025) demonstrate multimodal integration advantages. This creates nuanced support for H1 - context and application matter.

### Collaborative Intelligence Explosion
Strongest trend in 2025 literature: DrugMCTS multi-agent collaboration, Carbonari et al. LLMs as diagnostic partners, Madrigal LLM integration, BioKG interpretable representations. Combined with established evidence (Challa et al. 2021), this provides overwhelming support for H5 hypothesis.

### LLM Integration Revolution
New 2025 pattern: Multiple papers (DrugMCTS, Carbonari et al., De Vito et al., Madrigal) demonstrate LLM integration in drug discovery. This represents paradigm shift toward natural language interfaces and human-AI collaboration in biomedical research.

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

The literature reveals a field undergoing rapid paradigm transformation. The 2025 research landscape shows decisive movement away from traditional assumptions toward actionability-first, collaborative AI approaches. While technical capabilities continue advancing, the field has recognized that clinical translation requires fundamental rethinking of core assumptions about AI drug repurposing.

**Key Evolution Patterns:**
- **2019-2022**: Focus on technical performance and accuracy optimization
- **2023-2024**: Recognition of clinical translation challenges and interpretability needs  
- **2025**: Breakthrough toward actionability-first designs, human-AI collaboration, and context-sensitive data strategies

**Hypothesis Validation Status:**
- **H1 (Data Minimalism)**: Mixed evidence - context and application determine optimal data strategy
- **H2 (Actionability-First)**: Strongly supported across multiple 2025 breakthrough papers
- **H3 (Cross-Disease Patterns)**: Literature-supported through LLM and knowledge graph approaches
- **H4 (Parallel Validation)**: Literature-supported, with real-world evidence integration emerging
- **H5 (Human-AI Collaboration)**: Strongly validated - overwhelming trend toward collaborative intelligence

**Research Positioning:**
Our research is well-positioned at the forefront of this paradigm shift. The literature validates our core insight that fundamental assumptions need challenging, particularly:

1. **Assumption Testing Framework**: 2025 literature shows field ready for systematic assumption evaluation
2. **Actionability Focus**: Strong momentum toward clinical utility over technical metrics
3. **Rare Disease Context**: Unique constraints create opportunities for novel approaches
4. **Collaborative Intelligence**: Overwhelming evidence for human-AI partnership optimization
5. **Context-Sensitive Design**: Evidence suggests optimal approaches depend on specific application contexts

**Research Gap Positioning:**
While 2025 research shows strong movement in our hypothesized directions, critical gaps remain:
- No systematic framework for testing literature-level assumptions across the field
- Limited rare disease-specific research despite unique constraints and opportunities
- Insufficient integration of parallel validation strategies with AI prediction systems
- Need for comprehensive human-AI collaboration optimization frameworks

This positions our work to make paradigm-defining contributions to AI drug repurposing, particularly for rare diseases where traditional approaches are demonstrably mismatched to clinical realities.









