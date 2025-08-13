







# Experiment Ideas

## Overview

Our experimental approach follows Computer Science-inspired research methodology to test fundamental assumptions in AI-driven drug repurposing for rare diseases. We design controlled experiments that challenge five literature-level assumptions through systematic comparison of traditional vs. assumption-flipped approaches. Each experiment is structured with clear hypotheses, measurable outcomes, and validity controls to ensure rigorous scientific evaluation.

**Experimental Strategy**: We employ a two-phase approach - (1) assumption validation experiments that test whether traditional assumptions hold, and (2) hypothesis validation experiments that demonstrate superior performance of our flipped approaches. This allows us to both invalidate existing assumptions and validate our novel hypotheses.

## Planned Experiments

### Experiment 1: Data Minimalism vs. Data Maximalism
- **Thesis**: Strategically minimal, high-signal datasets can outperform comprehensive multi-modal approaches for rare disease drug repurposing
- **Assumption Being Tested**: Data Maximalism Assumption - more comprehensive multi-modal datasets always improve repurposing predictions
- **Hypothesis**: H1: Minimal but highly curated datasets achieve superior actionable predictions compared to comprehensive multi-modal approaches
- **Independent Variables**: 
  - Dataset size (minimal curated vs. comprehensive multi-modal)
  - Data quality (high-signal vs. mixed-quality)
  - Feature selection strategy (expert-curated vs. automated)
- **Dependent Variables**:
  - Actionable prediction accuracy (predictions that lead to successful clinical outcomes)
  - Clinical translation rate (percentage of predictions that advance to trials)
  - Time-to-actionable-insight
  - Prediction confidence calibration
- **Experimental Design**:
  - **Control Group**: Traditional comprehensive multi-modal approach using DrugBank, ChEMBL, OMIM, GTEx, and literature data
  - **Treatment Group**: Minimal dataset approach using only high-signal clinical trial data, FDA adverse events, and expert-curated drug-target interactions
  - **Test Set**: 50 rare diseases with known successful repurposing cases as ground truth
- **Validity Threats & Mitigations**:
  - Selection bias → Use stratified sampling across disease categories
  - Confounding by disease complexity → Match diseases by patient population size and genetic complexity
  - Evaluation bias → Use blinded clinical expert evaluation of predictions
- **Success Metrics**:
  - Actionable accuracy > 15% improvement over control
  - Clinical translation rate > 25% improvement
  - Time-to-insight < 50% of control time
- **Timeline**: 12 weeks (4 weeks data curation, 6 weeks experimentation, 2 weeks analysis)

### Experiment 2: Actionability-First vs. Accuracy-First AI Design
- **Thesis**: AI systems optimized for clinical actionability produce better real-world outcomes than accuracy-optimized models
- **Assumption Being Tested**: Accuracy-First Assumption - predictive accuracy is the primary success metric for AI systems
- **Hypothesis**: H2: Models designed for clinical actionability (interpretability, uncertainty quantification, decision support) outperform accuracy-optimized models in clinical outcomes
- **Independent Variables**:
  - Model optimization objective (actionability vs. accuracy)
  - Interpretability features (present vs. absent)
  - Uncertainty quantification (calibrated vs. uncalibrated)
- **Dependent Variables**:
  - Clinical adoption rate by physicians
  - Real-world patient outcomes
  - Physician confidence in predictions
  - Time spent on prediction evaluation
- **Experimental Design**:
  - **Control Group**: Traditional accuracy-optimized models (high AUC, low interpretability)
  - **Treatment Group**: Actionability-optimized models with built-in interpretability, uncertainty bounds, and clinical decision support
  - **Setting**: Retrospective analysis of clinical decision-making with 100 rare disease cases
- **Validity Threats & Mitigations**:
  - Hawthorne effect → Use historical data analysis
  - Physician preference bias → Randomize physician-model assignments
  - Case complexity confounding → Stratify by disease severity
- **Success Metrics**:
  - Clinical adoption rate > 40% higher than control
  - Patient outcome improvement > 20%
  - Physician confidence scores > 30% higher
- **Timeline**: 16 weeks (8 weeks model development, 6 weeks clinical evaluation, 2 weeks analysis)

### Experiment 3: Cross-Disease Transfer Learning vs. Disease-Specific Models
- **Thesis**: Meta-learning approaches can identify universal repurposing patterns that generalize across rare diseases
- **Assumption Being Tested**: Disease-Specific Modeling Assumption - each rare disease requires custom computational approaches
- **Hypothesis**: H3: Transfer learning models leveraging shared mechanistic patterns outperform disease-specific models, especially for ultra-rare conditions with limited data
- **Independent Variables**:
  - Model architecture (transfer learning vs. disease-specific)
  - Training data composition (cross-disease vs. single-disease)
  - Target disease data availability (ultra-rare vs. rare)
- **Dependent Variables**:
  - Prediction accuracy for low-data diseases
  - Model generalization across disease families
  - Required training data size for acceptable performance
- **Experimental Design**:
  - **Control Group**: Disease-specific models trained individually for each rare disease
  - **Treatment Group**: Meta-learning models trained on mechanistic patterns across multiple diseases, then fine-tuned for specific diseases
  - **Test Scenarios**: 
    - High-data scenario (>1000 patients per disease)
    - Low-data scenario (100-999 patients per disease)  
    - Ultra-rare scenario (<100 patients per disease)
- **Validity Threats & Mitigations**:
  - Domain shift → Validate on held-out disease families
  - Data leakage → Ensure no shared patients across diseases
  - Evaluation inconsistency → Use standardized evaluation protocols
- **Success Metrics**:
  - Ultra-rare disease accuracy improvement > 35%
  - Generalization score across disease families > 0.75
  - Training data efficiency > 50% reduction
- **Timeline**: 20 weeks (12 weeks model development, 6 weeks evaluation, 2 weeks analysis)

### Experiment 4: Parallel vs. Sequential Validation Strategies
- **Thesis**: Parallel validation approaches can accelerate repurposing timelines without compromising safety
- **Assumption Being Tested**: Sequential Validation Assumption - drug validation must follow linear preclinical → clinical stages
- **Hypothesis**: H4: Parallel multi-stage validation using real-world evidence achieves equivalent safety validation in significantly less time
- **Independent Variables**:
  - Validation strategy (parallel vs. sequential)
  - Evidence sources (RWE + preclinical vs. preclinical only)
  - Risk tolerance levels (conservative vs. adaptive)
- **Dependent Variables**:
  - Time-to-clinical-decision
  - Safety signal detection rate
  - False positive/negative rates
  - Resource utilization efficiency
- **Experimental Design**:
  - **Control Group**: Traditional sequential validation (preclinical → Phase I → Phase II)
  - **Treatment Group**: Parallel validation combining real-world evidence, computational modeling, and accelerated preclinical testing
  - **Dataset**: Historical drug repurposing cases with known safety profiles
- **Validity Threats & Mitigations**:
  - Hindsight bias → Use contemporaneous data only
  - Regulatory acceptance → Partner with regulatory scientists
  - Safety standard differences → Match safety thresholds
- **Success Metrics**:
  - Time reduction > 60% while maintaining safety
  - Safety signal detection ≥ 95% of sequential method
  - Resource efficiency > 40% improvement
- **Timeline**: 24 weeks (16 weeks protocol development, 6 weeks retrospective analysis, 2 weeks reporting)

### Experiment 5: Human-AI Collaboration vs. Fully Automated Systems
- **Thesis**: Hybrid human-AI systems that amplify clinical expertise outperform fully automated approaches
- **Assumption Being Tested**: AI Supremacy Assumption - AI should minimize human bias and replace expert judgment
- **Hypothesis**: H5: Collaborative human-AI systems leveraging irreplaceable rare disease expertise outperform fully automated approaches for complex repurposing decisions
- **Independent Variables**:
  - System design (collaborative vs. fully automated)
  - Expert involvement level (high vs. minimal)
  - Decision complexity (simple vs. complex cases)
- **Dependent Variables**:
  - Decision quality scores
  - Clinical expert satisfaction
  - System learning rate improvement
  - Error detection and correction rates
- **Experimental Design**:
  - **Control Group**: Fully automated AI system making repurposing recommendations
  - **Treatment Group**: Human-AI collaborative system where experts guide feature selection, interpret predictions, and provide domain knowledge
  - **Participants**: 20 rare disease clinical experts
  - **Cases**: 200 drug repurposing decisions across complexity levels
- **Validity Threats & Mitigations**:
  - Expert variability → Use multiple experts per case
  - Learning effects → Counterbalance system exposure
  - Case selection bias → Randomize case assignments
- **Success Metrics**:
  - Decision quality > 30% improvement over automated
  - Expert satisfaction scores > 4.0/5.0
  - System improvement rate > 25% per month
- **Timeline**: 18 weeks (4 weeks system development, 12 weeks user studies, 2 weeks analysis)

## Comprehensive Evaluation Framework

### Cross-Experiment Validation
- **Integrated Testing**: Combine successful elements from individual experiments into a unified system
- **Real-World Validation**: Partner with rare disease clinics for prospective validation
- **Longitudinal Analysis**: Track long-term clinical outcomes and system adoption

### Statistical Analysis Plan
- **Power Analysis**: Ensure adequate sample sizes for detecting meaningful differences
- **Multiple Comparisons**: Use Bonferroni correction for multiple hypothesis testing
- **Effect Size Reporting**: Report Cohen's d and confidence intervals for all findings
- **Bayesian Updates**: Use Bayesian statistics for evidence accumulation across experiments

### Resource Requirements
- **Computational**: Cloud computing resources for large-scale model training
- **Data**: Access to clinical databases, drug repositories, and patient registries  
- **Human**: Collaboration with clinical experts and regulatory scientists
- **Regulatory**: IRB approval for human subjects research components

## Timeline

**Phase 1 (Months 1-3): Foundation Building**
- Literature review completion
- Data acquisition and preprocessing
- Baseline model development
- IRB approvals and partnerships

**Phase 2 (Months 4-9): Core Experiments**
- Execute Experiments 1-3 in parallel
- Iterative refinement based on initial results
- Preliminary validation with clinical experts

**Phase 3 (Months 10-15): Advanced Validation**
- Execute Experiments 4-5
- Integrated system development
- Comprehensive evaluation and analysis

**Phase 4 (Months 16-18): Translation and Dissemination**
- Real-world pilot studies
- Regulatory pathway development
- Publication and patent preparation

**Milestone Checkpoints**:
- Month 6: Complete assumption validation experiments
- Month 12: Complete hypothesis validation experiments  
- Month 15: Complete integrated system evaluation
- Month 18: Complete clinical translation validation

This experimental plan systematically tests each literature assumption while providing rigorous validation of our novel hypotheses, following Computer Science research standards with clear evaluation metrics and validity controls.







