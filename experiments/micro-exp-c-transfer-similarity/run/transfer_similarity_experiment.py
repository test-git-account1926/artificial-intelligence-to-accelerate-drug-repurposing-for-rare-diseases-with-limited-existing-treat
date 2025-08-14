#!/usr/bin/env python3
"""
Transfer Learning Similarity Mapping Experiment
Tests which disease similarity metrics best predict transfer learning success
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity, jaccard_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import r2_score, classification_report, confusion_matrix
from scipy.stats import pearsonr, spearmanr
import json
import random
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class TransferSimilarityExperiment:
    def __init__(self, n_diseases=50, n_pairs=50, random_seed=42):
        """Initialize transfer learning similarity mapping experiment"""
        self.n_diseases = n_diseases
        self.n_pairs = n_pairs
        self.random_seed = random_seed
        random.seed(random_seed)
        np.random.seed(random_seed)
        
        self.disease_data = None
        self.similarity_data = []
        self.results = {}
        
    def generate_synthetic_diseases(self):
        """Generate synthetic disease profiles with genetic, phenotypic, and molecular features"""
        print("Generating synthetic disease profiles...")
        
        diseases = []
        for i in range(self.n_diseases):
            disease = {
                'id': f'disease_{i:03d}',
                'name': f'Synthetic Rare Disease {i}',
                # Genetic features (gene involvement patterns)
                'genetic_profile': np.random.binomial(1, 0.15, 1000),  # 15% gene involvement
                # Phenotypic features (symptom patterns)
                'phenotypic_profile': np.random.exponential(0.3, 200),  # symptom severity
                # Molecular pathway involvement
                'pathway_profile': np.random.binomial(1, 0.08, 500),   # 8% pathway involvement
                # Clinical presentation (symptom categories)
                'clinical_profile': np.random.gamma(2, 0.5, 100),      # clinical manifestations
                # Disease complexity and data availability
                'complexity': np.random.uniform(0.1, 1.0),
                'data_availability': np.random.exponential(0.8)
            }
            diseases.append(disease)
        
        self.disease_data = diseases
        print(f"Generated {len(diseases)} synthetic diseases")
        return diseases
    
    def calculate_similarity_metrics(self):
        """Calculate various disease similarity metrics"""
        print("Calculating disease similarity metrics...")
        
        similarity_metrics = []
        
        # Generate disease pairs for analysis
        disease_pairs = []
        for _ in range(self.n_pairs):
            source_idx = random.randint(0, self.n_diseases - 1)
            target_idx = random.randint(0, self.n_diseases - 1)
            while target_idx == source_idx:  # Ensure different diseases
                target_idx = random.randint(0, self.n_diseases - 1)
            disease_pairs.append((source_idx, target_idx))
        
        for source_idx, target_idx in disease_pairs:
            source = self.disease_data[source_idx]
            target = self.disease_data[target_idx]
            
            # Genetic similarity (Jaccard index on binary genetic profiles)
            genetic_sim = self._jaccard_similarity(source['genetic_profile'], target['genetic_profile'])
            
            # Phenotypic similarity (cosine similarity on symptom patterns)
            phenotypic_sim = cosine_similarity(
                source['phenotypic_profile'].reshape(1, -1),
                target['phenotypic_profile'].reshape(1, -1)
            )[0, 0]
            
            # Molecular pathway similarity (Jaccard on pathway involvement)
            pathway_sim = self._jaccard_similarity(source['pathway_profile'], target['pathway_profile'])
            
            # Clinical presentation similarity (correlation between clinical profiles)
            clinical_sim = np.corrcoef(source['clinical_profile'], target['clinical_profile'])[0, 1]
            if np.isnan(clinical_sim):
                clinical_sim = 0.0
            
            # Combined complexity-adjusted similarity
            complexity_diff = abs(source['complexity'] - target['complexity'])
            complexity_adj = 1.0 - complexity_diff
            
            # Data availability factor (affects transfer learning feasibility)
            data_factor = min(source['data_availability'], target['data_availability']) / 2.0
            
            similarity_metrics.append({
                'source_disease': source['id'],
                'target_disease': target['id'],
                'genetic_similarity': genetic_sim,
                'phenotypic_similarity': phenotypic_sim,
                'pathway_similarity': pathway_sim,
                'clinical_similarity': clinical_sim,
                'complexity_adjusted_similarity': complexity_adj,
                'data_availability_factor': data_factor,
                'source_complexity': source['complexity'],
                'target_complexity': target['complexity'],
                'source_data_availability': source['data_availability'],
                'target_data_availability': target['data_availability']
            })
        
        self.similarity_data = similarity_metrics
        print(f"Calculated similarity metrics for {len(similarity_metrics)} disease pairs")
        return similarity_metrics
    
    def _jaccard_similarity(self, set1, set2):
        """Calculate Jaccard similarity for binary vectors"""
        intersection = np.sum(set1 & set2)
        union = np.sum(set1 | set2)
        return intersection / union if union > 0 else 0.0
    
    def simulate_transfer_learning_success(self):
        """Simulate transfer learning success based on realistic patterns"""
        print("Simulating transfer learning outcomes...")
        
        transfer_outcomes = []
        
        for metrics in self.similarity_data:
            # Realistic success probability based on multiple factors
            success_probability = (
                0.3 * metrics['genetic_similarity'] +          # Genetic similarity is important
                0.25 * metrics['phenotypic_similarity'] +      # Clinical similarity matters
                0.2 * metrics['pathway_similarity'] +          # Molecular pathways contribute
                0.15 * metrics['complexity_adjusted_similarity'] +  # Complexity matching helps
                0.1 * min(metrics['data_availability_factor'], 1.0)  # Data availability enables transfer
            )
            
            # Add realistic noise and constraints
            success_probability += np.random.normal(0, 0.1)  # Noise in real-world outcomes
            success_probability = max(0.0, min(1.0, success_probability))  # Bound between 0-1
            
            # Binary success outcome
            transfer_success = int(success_probability > 0.5)
            
            # Continuous performance metric (e.g., accuracy improvement)
            performance_improvement = success_probability * 0.4 + np.random.normal(0, 0.05)
            performance_improvement = max(0.0, performance_improvement)  # No negative improvements
            
            transfer_outcomes.append({
                'success_probability': success_probability,
                'transfer_success': transfer_success,
                'performance_improvement': performance_improvement,
                **metrics
            })
        
        # Update similarity data with transfer outcomes
        self.similarity_data = transfer_outcomes
        print(f"Simulated transfer learning for {len(transfer_outcomes)} pairs")
        
        # Print success rate
        success_rate = np.mean([x['transfer_success'] for x in transfer_outcomes])
        print(f"Overall transfer learning success rate: {success_rate:.2%}")
        
        return transfer_outcomes
    
    def analyze_similarity_correlations(self):
        """Analyze correlations between similarity metrics and transfer success"""
        print("Analyzing similarity-success correlations...")
        
        df = pd.DataFrame(self.similarity_data)
        
        # Similarity metrics to analyze
        similarity_cols = [
            'genetic_similarity',
            'phenotypic_similarity', 
            'pathway_similarity',
            'clinical_similarity',
            'complexity_adjusted_similarity',
            'data_availability_factor'
        ]
        
        # Correlation analysis
        correlations = {}
        for col in similarity_cols:
            # Correlation with binary success
            corr_success, p_val_success = pearsonr(df[col], df['transfer_success'])
            
            # Correlation with continuous performance improvement
            corr_performance, p_val_performance = pearsonr(df[col], df['performance_improvement'])
            
            correlations[col] = {
                'success_correlation': corr_success,
                'success_p_value': p_val_success,
                'performance_correlation': corr_performance, 
                'performance_p_value': p_val_performance,
                'mean_value': df[col].mean(),
                'std_value': df[col].std()
            }
            
            print(f"{col}:")
            print(f"  Success correlation: r={corr_success:.3f}, p={p_val_success:.4f}")
            print(f"  Performance correlation: r={corr_performance:.3f}, p={p_val_performance:.4f}")
        
        self.results['correlations'] = correlations
        return correlations
    
    def build_prediction_models(self):
        """Build models to predict transfer learning success from similarity metrics"""
        print("Building transfer success prediction models...")
        
        df = pd.DataFrame(self.similarity_data)
        
        # Feature matrix
        feature_cols = [
            'genetic_similarity',
            'phenotypic_similarity',
            'pathway_similarity', 
            'clinical_similarity',
            'complexity_adjusted_similarity',
            'data_availability_factor'
        ]
        X = df[feature_cols].values
        
        # Binary classification model (success/failure)
        y_binary = df['transfer_success'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.3, random_state=self.random_seed)
        
        # Logistic regression for binary prediction
        log_reg = LogisticRegression(random_state=self.random_seed)
        log_reg.fit(X_train, y_train)
        
        binary_accuracy = log_reg.score(X_test, y_test)
        binary_cv_scores = cross_val_score(log_reg, X, y_binary, cv=5)
        
        print(f"Binary classification accuracy: {binary_accuracy:.3f}")
        print(f"Cross-validation accuracy: {binary_cv_scores.mean():.3f} ± {binary_cv_scores.std():.3f}")
        
        # Regression model for performance improvement
        y_continuous = df['performance_improvement'].values
        
        lin_reg = LinearRegression()
        lin_reg.fit(X_train, y_continuous[:len(X_train)])
        
        continuous_r2 = r2_score(y_continuous[len(X_train):], lin_reg.predict(X_test))
        continuous_cv_scores = cross_val_score(lin_reg, X, y_continuous, cv=5, scoring='r2')
        
        print(f"Continuous prediction R²: {continuous_r2:.3f}")
        print(f"Cross-validation R²: {continuous_cv_scores.mean():.3f} ± {continuous_cv_scores.std():.3f}")
        
        # Feature importance analysis
        feature_importance = pd.DataFrame({
            'feature': feature_cols,
            'binary_coef': log_reg.coef_[0],
            'continuous_coef': lin_reg.coef_,
            'abs_binary_coef': np.abs(log_reg.coef_[0]),
            'abs_continuous_coef': np.abs(lin_reg.coef_)
        }).sort_values('abs_binary_coef', ascending=False)
        
        print("\nFeature Importance (Binary Classification):")
        for _, row in feature_importance.iterrows():
            print(f"  {row['feature']}: {row['binary_coef']:.3f}")
        
        self.results['models'] = {
            'binary_accuracy': binary_accuracy,
            'binary_cv_mean': binary_cv_scores.mean(),
            'binary_cv_std': binary_cv_scores.std(),
            'continuous_r2': continuous_r2,
            'continuous_cv_mean': continuous_cv_scores.mean(),
            'continuous_cv_std': continuous_cv_scores.std(),
            'feature_importance': feature_importance.to_dict('records')
        }
        
        return log_reg, lin_reg, feature_importance
    
    def identify_similarity_thresholds(self):
        """Identify optimal similarity thresholds for transfer learning viability"""
        print("Identifying similarity thresholds...")
        
        df = pd.DataFrame(self.similarity_data)
        
        similarity_cols = [
            'genetic_similarity',
            'phenotypic_similarity',
            'pathway_similarity',
            'clinical_similarity'
        ]
        
        thresholds = {}
        
        for col in similarity_cols:
            # Find threshold that maximizes classification accuracy
            best_threshold = 0.5
            best_accuracy = 0.0
            
            for threshold in np.linspace(0.1, 0.9, 17):  # Test thresholds from 0.1 to 0.9
                predicted = (df[col] >= threshold).astype(int)
                accuracy = (predicted == df['transfer_success']).mean()
                
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_threshold = threshold
            
            # Calculate sensitivity and specificity at best threshold
            predicted = (df[col] >= best_threshold).astype(int)
            true_pos = ((predicted == 1) & (df['transfer_success'] == 1)).sum()
            false_pos = ((predicted == 1) & (df['transfer_success'] == 0)).sum()
            true_neg = ((predicted == 0) & (df['transfer_success'] == 0)).sum()
            false_neg = ((predicted == 0) & (df['transfer_success'] == 1)).sum()
            
            sensitivity = true_pos / (true_pos + false_neg) if (true_pos + false_neg) > 0 else 0
            specificity = true_neg / (true_neg + false_pos) if (true_neg + false_pos) > 0 else 0
            
            thresholds[col] = {
                'optimal_threshold': best_threshold,
                'accuracy': best_accuracy,
                'sensitivity': sensitivity,
                'specificity': specificity
            }
            
            print(f"{col}: threshold={best_threshold:.2f}, accuracy={best_accuracy:.3f}")
        
        self.results['thresholds'] = thresholds
        return thresholds
    
    def generate_results_summary(self):
        """Generate comprehensive results summary"""
        print("Generating results summary...")
        
        # Overall experiment summary
        df = pd.DataFrame(self.similarity_data)
        
        summary = {
            'experiment_id': 'micro-exp-c-transfer-similarity',
            'experiment_date': datetime.now().isoformat(),
            'total_disease_pairs': len(self.similarity_data),
            'success_rate': df['transfer_success'].mean(),
            'mean_performance_improvement': df['performance_improvement'].mean(),
            'std_performance_improvement': df['performance_improvement'].std()
        }
        
        # Key findings
        correlations = self.results.get('correlations', {})
        strongest_predictors = sorted(
            [(k, v['success_correlation']) for k, v in correlations.items()],
            key=lambda x: abs(x[1]),
            reverse=True
        )[:3]
        
        findings = {
            'strongest_predictors': [
                f"{predictor}: r={correlation:.3f}" 
                for predictor, correlation in strongest_predictors
            ],
            'model_performance': {
                'binary_accuracy': self.results.get('models', {}).get('binary_accuracy', 0),
                'continuous_r2': self.results.get('models', {}).get('continuous_r2', 0)
            },
            'success_criteria_met': {
                'strong_correlations_found': any(
                    abs(v['success_correlation']) > 0.8 
                    for v in correlations.values()
                ),
                'prediction_accuracy_threshold': (
                    self.results.get('models', {}).get('binary_accuracy', 0) > 0.75
                ),
                'moderate_success_achieved': any(
                    abs(v['success_correlation']) > 0.6 
                    for v in correlations.values()
                )
            }
        }
        
        self.results.update({
            'summary': summary,
            'findings': findings
        })
        
        return summary, findings
    
    def save_results(self, filepath):
        """Save experiment results to JSON file"""
        print(f"Saving results to {filepath}")
        
        with open(filepath, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print("Results saved successfully")

def main():
    """Run the transfer learning similarity mapping experiment"""
    print("=== Transfer Learning Similarity Mapping Experiment ===")
    print("Testing which disease similarity metrics predict transfer learning success")
    
    # Initialize experiment
    experiment = TransferSimilarityExperiment(n_diseases=50, n_pairs=50)
    
    # Run experiment pipeline
    experiment.generate_synthetic_diseases()
    experiment.calculate_similarity_metrics()
    experiment.simulate_transfer_learning_success()
    experiment.analyze_similarity_correlations()
    experiment.build_prediction_models()
    experiment.identify_similarity_thresholds()
    experiment.generate_results_summary()
    
    # Save results
    experiment.save_results('../../data/micro-exp-c-results/transfer_similarity_results.json')
    
    # Print final summary
    print("\n=== EXPERIMENT COMPLETE ===")
    summary, findings = experiment.results['summary'], experiment.results['findings']
    
    print(f"Total pairs analyzed: {summary['total_disease_pairs']}")
    print(f"Transfer success rate: {summary['success_rate']:.2%}")
    print(f"Mean performance improvement: {summary['mean_performance_improvement']:.3f}")
    
    print("\nStrongest predictive metrics:")
    for predictor in findings['strongest_predictors']:
        print(f"  {predictor}")
    
    print(f"\nModel performance:")
    print(f"  Binary accuracy: {findings['model_performance']['binary_accuracy']:.3f}")
    print(f"  Continuous R²: {findings['model_performance']['continuous_r2']:.3f}")
    
    # Success criteria evaluation
    criteria = findings['success_criteria_met']
    if criteria['strong_correlations_found']:
        print("\n✅ STRONG SUCCESS: Found correlations > 0.8")
    elif criteria['moderate_success_achieved']:
        print("\n✅ MODERATE SUCCESS: Found correlations > 0.6") 
    else:
        print("\n📝 LEARNING OUTCOME: No strong correlations, but identified boundary conditions")
    
    if criteria['prediction_accuracy_threshold']:
        print("✅ Prediction model exceeds 75% accuracy threshold")
    else:
        print("📊 Prediction model below 75% accuracy - opportunities for improvement")

if __name__ == "__main__":
    main()