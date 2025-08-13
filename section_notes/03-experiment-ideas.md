



# Experiment Ideas

## Overview

This experimental program tests five fundamental assumptions in AI drug repurposing for rare diseases. Following Computer Science research methodology, we design controlled experiments that directly validate assumption inversions through comparative analysis. Each experiment follows the structure: assumption identification → hypothesis formulation → experimental design → evaluation metrics → validation strategy.

Our core research thesis: **Strategically minimal, actionability-focused AI systems can outperform comprehensive, accuracy-optimized approaches for rare disease drug repurposing.**

## Planned Experiments

### Experiment 1: Data Minimalism vs. Data Maximalism
- **Research Hypothesis**: H1 - Minimal but highly curated datasets achieve superior actionable predictions compared to comprehensive multi-modal approaches
- **Assumption Challenged**: Prior work assumes more comprehensive datasets always improve repurposing predictions
- **Objective**: Compare prediction quality and clinical actionability between minimal curated datasets vs. comprehensive multi-modal datasets
- **Methodology**: 
  - **Minimal Dataset**: Curate high-confidence drug-disease associations from clinical sources (FDA approvals, clinical trials, expert annotations)
  - **Maximal Dataset**: Integrate multi-modal data (genomics, proteomics, chemical structures, literature mining, pathway databases)
  - **Controlled Variables**: Same ML architectures, evaluation protocols, and rare disease targets
  - **Independent Variables**: Dataset size, data modality count, curation level
  - **Dependent Variables**: Prediction accuracy, clinical actionability score, expert agreement, implementation feasibility
- **Experimental Tasks**:
  1. Build minimal dataset (n=500 high-confidence associations) vs. maximal dataset (n=50,000+ multi-modal features)
  2. Train identical ML models on both datasets for 10 rare diseases
  3. Evaluate predictions using both accuracy metrics and clinical actionability framework
  4. Conduct expert evaluation with rare disease clinicians
- **Expected Outcomes**: Minimal datasets will show comparable accuracy but superior actionability and expert acceptance
- **Success Metrics**: 
  - Clinical Actionability Score (interpretability + uncertainty quantification + decision support)
  - Expert Agreement Rate with AI predictions
  - Time-to-clinical-implementation feasibility
- **Validity Threats**: Selection bias in minimal dataset curation, domain expert availability
- **Mitigations**: Multiple curators, cross-validation across disease domains, blinded expert evaluation
- **Resources**: 3 months, access to clinical databases, 5 rare disease experts

### Experiment 2: Accuracy-First vs. Actionability-First AI Design
- **Research Hypothesis**: H2 - AI systems optimized for clinical actionability produce better real-world outcomes than accuracy-optimized models
- **Assumption Challenged**: Prior work assumes predictive accuracy is the primary success metric
- **Objective**: Compare real-world clinical utility between accuracy-optimized and actionability-optimized AI systems
- **Methodology**:
  - **Accuracy-First Model**: Traditional ML pipeline optimizing for AUC/F1 scores
  - **Actionability-First Model**: Pipeline optimizing for interpretability, uncertainty quantification, and clinical decision support
  - **Controlled Variables**: Same training data, evaluation diseases, clinical partners
  - **Independent Variables**: Optimization objective, model architecture (black-box vs. interpretable)
  - **Dependent Variables**: Prediction accuracy, clinical adoption rate, decision time, confidence in predictions
- **Experimental Tasks**:
  1. Design actionability-focused evaluation framework (SHAP scores, uncertainty bounds, clinical decision trees)
  2. Train both model types on same rare disease repurposing tasks
  3. Deploy both systems with clinical partners for real-world validation
  4. Measure adoption rates, usage patterns, and clinical outcomes
- **Expected Outcomes**: Actionability-first models will show higher clinical adoption despite potentially lower raw accuracy
- **Success Metrics**:
  - Clinical Adoption Rate (% of recommendations acted upon)
  - Decision Confidence Score (clinician self-reported)
  - Time from prediction to clinical action
- **Validity Threats**: Hawthorne effect, clinical partner bias, confounding variables
- **Mitigations**: Randomized deployment, multiple clinical sites, long-term longitudinal study
- **Resources**: 6 months, clinical partnerships, IRB approval

### Experiment 3: Cross-Disease Pattern Learning vs. Disease-Specific Modeling
- **Research Hypothesis**: H3 - Meta-learning approaches leveraging shared patterns across rare diseases outperform disease-specific models
- **Assumption Challenged**: Prior work assumes each rare disease requires custom computational approaches
- **Objective**: Test whether transfer learning and meta-learning can identify universal repurposing patterns across rare diseases
- **Methodology**:
  - **Disease-Specific Models**: Individual models trained for each rare disease
  - **Cross-Disease Models**: Meta-learning and transfer learning approaches trained across multiple rare diseases
  - **Controlled Variables**: Same base architectures, evaluation metrics, disease selection criteria
  - **Independent Variables**: Training strategy (individual vs. meta-learning), number of source diseases
  - **Dependent Variables**: Prediction performance on new diseases, sample efficiency, generalization capability
- **Experimental Tasks**:
  1. Select 20 rare diseases with varying pathophysiology and available data
  2. Implement Model-Agnostic Meta-Learning (MAML) for drug repurposing
  3. Compare few-shot learning performance: meta-learned vs. disease-specific models
  4. Analyze learned representations for shared mechanistic patterns
- **Expected Outcomes**: Meta-learning will enable effective repurposing for ultra-rare diseases with minimal data
- **Success Metrics**:
  - Few-shot learning performance (predictions with <10 examples)
  - Cross-disease generalization accuracy
  - Mechanistic interpretability of shared patterns
- **Validity Threats**: Disease selection bias, limited rare disease data, evaluation dataset overlap
- **Mitigations**: Stratified disease selection, careful train/test splits, external validation datasets
- **Resources**: 4 months, computational resources for meta-learning, rare disease datasets

### Experiment 4: Parallel vs. Sequential Validation Strategies
- **Research Hypothesis**: H4 - Parallel validation using real-world evidence accelerates repurposing without compromising safety
- **Assumption Challenged**: Prior work assumes drug validation must follow sequential preclinical → clinical stages
- **Objective**: Compare time-to-treatment and safety outcomes between parallel and sequential validation approaches
- **Methodology**:
  - **Sequential Validation**: Traditional preclinical → Phase I → Phase II pathway
  - **Parallel Validation**: Concurrent real-world evidence analysis, in silico validation, and accelerated clinical protocols
  - **Controlled Variables**: Same drug candidates, disease targets, safety monitoring
  - **Independent Variables**: Validation strategy, evidence types, timeline structure
  - **Dependent Variables**: Time to treatment availability, safety profile detection, regulatory acceptance
- **Experimental Tasks**:
  1. Design parallel validation framework using EHR data, claims databases, and patient registries
  2. Select matched drug-disease pairs for parallel vs. sequential validation
  3. Implement real-world evidence analysis pipeline
  4. Compare timelines and outcomes with regulatory partners
- **Expected Outcomes**: Parallel validation will reduce time-to-treatment by 40-60% while maintaining safety standards
- **Success Metrics**:
  - Time from hypothesis to treatment availability
  - Safety signal detection sensitivity
  - Regulatory acceptance rate
- **Validity Threats**: Regulatory resistance, real-world evidence quality, safety monitoring gaps
- **Mitigations**: Regulatory engagement, data quality standards, enhanced safety protocols
- **Resources**: 12 months, regulatory partnerships, access to real-world datasets

### Experiment 5: Human-AI Collaboration vs. Fully Automated Approaches
- **Research Hypothesis**: H5 - Hybrid human-AI systems outperform fully automated approaches for complex repurposing decisions
- **Assumption Challenged**: Prior work assumes AI should minimize human bias and replace expert judgment
- **Objective**: Compare decision quality and clinical outcomes between collaborative and automated AI systems
- **Methodology**:
  - **Fully Automated**: AI system makes repurposing recommendations without human input
  - **Human-AI Collaborative**: Interactive system that amplifies human expertise while providing AI insights
  - **Controlled Variables**: Same underlying AI models, evaluation datasets, clinical scenarios
  - **Independent Variables**: Human involvement level, interface design, decision-making workflow
  - **Dependent Variables**: Decision accuracy, time to decision, confidence scores, clinical adoption
- **Experimental Tasks**:
  1. Design collaborative interface for clinician-AI drug repurposing decisions
  2. Recruit rare disease experts for comparative evaluation study
  3. Present matched cases to automated vs. collaborative systems
  4. Analyze decision quality, process efficiency, and user satisfaction
- **Expected Outcomes**: Collaborative systems will achieve higher clinical adoption and better complex decision-making
- **Success Metrics**:
  - Decision Quality Score (expert panel evaluation)
  - Clinical Implementation Rate
  - User Satisfaction and Trust Scores
- **Validity Threats**: Expert availability, interface effects, learning curves
- **Mitigations**: Balanced study design, interface standardization, adequate training periods
- **Resources**: 4 months, rare disease expert panel, interface development

## Cross-Experiment Integration

### Meta-Analysis Framework
- **Objective**: Synthesize findings across all five experiments to validate core research thesis
- **Methodology**: Systematic comparison of effect sizes, confidence intervals, and practical significance
- **Success Criteria**: Demonstrate that assumption inversions lead to measurably better clinical outcomes

### Validation Pipeline
1. **Internal Validation**: Cross-validation within each experiment
2. **External Validation**: Testing on held-out rare diseases not used in training
3. **Clinical Validation**: Real-world deployment with clinical partners
4. **Regulatory Validation**: Engagement with FDA and EMA on new evaluation frameworks

## Timeline

### Phase 1: Foundation (Months 1-3)
- Experiment 1: Data Minimalism vs. Maximalism
- Establish evaluation frameworks and clinical partnerships
- IRB approvals and regulatory engagement

### Phase 2: Core Testing (Months 4-8)
- Experiment 2: Actionability-First AI Design
- Experiment 3: Cross-Disease Pattern Learning
- Experiment 5: Human-AI Collaboration

### Phase 3: Advanced Validation (Months 9-12)
- Experiment 4: Parallel Validation Strategies
- Meta-analysis and integration
- Regulatory validation and clinical deployment

### Phase 4: Impact Assessment (Months 13-15)
- Long-term outcome tracking
- Field impact evaluation
- Publication and dissemination

## Resource Requirements

### Computational
- GPU cluster for meta-learning experiments
- Cloud infrastructure for real-world evidence analysis
- Secure environments for clinical data processing

### Data Access
- Clinical databases (EHR, claims, registries)
- Regulatory databases (FDA, EMA approval data)
- Rare disease patient registries

### Human Resources
- 5 rare disease clinical experts
- 2 regulatory affairs specialists
- 3 ML/AI researchers
- 1 biostatistician

### Partnerships
- Academic medical centers
- Regulatory agencies (FDA, EMA)
- Rare disease patient organizations
- Pharmaceutical industry collaborators



