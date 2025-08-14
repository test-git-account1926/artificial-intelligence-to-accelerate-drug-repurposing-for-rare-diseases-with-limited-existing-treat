#!/usr/bin/env python3
"""
Data Quality Threshold Detection Experiment
Tests the assumption that minimal, high-quality data outperforms comprehensive, noisy data
for rare disease drug repurposing.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import roc_auc_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
import os

# Set random seeds for reproducibility
np.random.seed(42)

class QualityThresholdExperiment:
    def __init__(self, n_diseases=10, base_samples=1000):
        self.n_diseases = n_diseases
        self.base_samples = base_samples
        self.results = []
        
    def generate_synthetic_data(self, n_samples, n_relevant_features, n_noise_features, signal_strength):
        """Generate synthetic biomedical data with controlled quality parameters"""
        
        # Generate relevant features with biological signal
        X_relevant = np.random.randn(n_samples, n_relevant_features)
        
        # Create drug-disease outcome relationships with specified signal strength
        # Simulate biomarkers that correlate with drug effectiveness
        drug_effectiveness_weights = np.random.uniform(0.2, signal_strength, n_relevant_features)
        true_scores = np.dot(X_relevant, drug_effectiveness_weights)
        
        # Convert to binary outcomes (drug effective/not effective)
        threshold = np.percentile(true_scores, 70)  # 30% positive rate (realistic for drug repurposing)
        y = (true_scores > threshold).astype(int)
        
        # Add noise features (irrelevant biomedical measurements)
        X_noise = np.random.randn(n_samples, n_noise_features)
        
        # Combine relevant and noise features
        X = np.hstack([X_relevant, X_noise])
        
        return X, y, drug_effectiveness_weights
    
    def train_minimal_model(self, X, y, max_features=500):
        """Train minimal model with feature selection"""
        selector = SelectKBest(f_classif, k=min(max_features, X.shape[1]))
        X_selected = selector.fit_transform(X, y)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        
        # Use cross-validation for robust evaluation
        cv_scores = cross_val_score(model, X_selected, y, cv=StratifiedKFold(5), 
                                   scoring='roc_auc', n_jobs=-1)
        
        # Train on full data for detailed analysis
        model.fit(X_selected, y)
        y_pred_proba = model.predict_proba(X_selected)[:, 1]
        y_pred = model.predict(X_selected)
        
        return {
            'model_type': 'minimal',
            'cv_auc_mean': cv_scores.mean(),
            'cv_auc_std': cv_scores.std(),
            'train_auc': roc_auc_score(y, y_pred_proba),
            'train_precision': precision_score(y, y_pred),
            'train_recall': recall_score(y, y_pred),
            'n_features_used': X_selected.shape[1]
        }
    
    def train_comprehensive_model(self, X, y):
        """Train comprehensive model using all features"""
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        
        # Use cross-validation for robust evaluation
        cv_scores = cross_val_score(model, X, y, cv=StratifiedKFold(5), 
                                   scoring='roc_auc', n_jobs=-1)
        
        # Train on full data for detailed analysis
        model.fit(X, y)
        y_pred_proba = model.predict_proba(X)[:, 1]
        y_pred = model.predict(X)
        
        return {
            'model_type': 'comprehensive',
            'cv_auc_mean': cv_scores.mean(),
            'cv_auc_std': cv_scores.std(),
            'train_auc': roc_auc_score(y, y_pred_proba),
            'train_precision': precision_score(y, y_pred),
            'train_recall': recall_score(y, y_pred),
            'n_features_used': X.shape[1]
        }
    
    def calculate_quality_score(self, n_relevant, n_noise):
        """Calculate data quality score as percentage of relevant features"""
        return n_relevant / (n_relevant + n_noise)
    
    def run_experiment(self):
        """Run the complete quality threshold detection experiment"""
        print(f"Starting Quality Threshold Experiment at {datetime.now()}")
        
        # Define experimental conditions
        noise_levels = [0.1, 0.25, 0.5, 0.75, 0.9]  # Percentage of irrelevant features
        signal_strengths = [0.8, 0.6, 0.4]  # Correlation strength of relevant features
        n_relevant_base = 200  # Base number of relevant features
        
        experiment_id = 0
        
        for signal_strength in signal_strengths:
            for noise_level in noise_levels:
                # Calculate feature counts
                n_relevant = n_relevant_base
                n_noise = int(n_relevant * noise_level / (1 - noise_level))
                quality_score = self.calculate_quality_score(n_relevant, n_noise)
                
                print(f"Running condition: Signal={signal_strength:.1f}, Quality={quality_score:.2f} "
                      f"({n_relevant} relevant, {n_noise} noise features)")
                
                # Generate data for multiple disease scenarios
                for disease_id in range(self.n_diseases):
                    X, y, weights = self.generate_synthetic_data(
                        self.base_samples, n_relevant, n_noise, signal_strength
                    )
                    
                    # Train both models
                    minimal_results = self.train_minimal_model(X, y)
                    comprehensive_results = self.train_comprehensive_model(X, y)
                    
                    # Store results
                    base_info = {
                        'experiment_id': experiment_id,
                        'disease_id': disease_id,
                        'signal_strength': signal_strength,
                        'noise_level': noise_level,
                        'quality_score': quality_score,
                        'n_relevant_features': n_relevant,
                        'n_noise_features': n_noise,
                        'n_samples': self.base_samples
                    }
                    
                    self.results.append({**base_info, **minimal_results})
                    self.results.append({**base_info, **comprehensive_results})
                    
                experiment_id += 1
        
        print(f"Experiment completed at {datetime.now()}")
        return self.results
    
    def analyze_results(self):
        """Analyze results to identify quality thresholds"""
        df = pd.DataFrame(self.results)
        
        # Calculate average performance by condition and model type
        summary = df.groupby(['quality_score', 'model_type']).agg({
            'cv_auc_mean': ['mean', 'std'],
            'train_precision': ['mean', 'std'],
            'train_recall': ['mean', 'std']
        }).round(4)
        
        # Find crossover points where minimal outperforms comprehensive
        pivot = df.groupby(['quality_score', 'model_type'])['cv_auc_mean'].mean().unstack()
        
        # Identify quality thresholds
        quality_scores = pivot.index.values
        minimal_better = pivot['minimal'] > pivot['comprehensive']
        
        if any(minimal_better):
            threshold_candidates = quality_scores[minimal_better]
            optimal_threshold = threshold_candidates.min()
            print(f"\nQUALITY THRESHOLD IDENTIFIED: {optimal_threshold:.3f}")
            print(f"Minimal approach outperforms comprehensive when >{optimal_threshold*100:.1f}% of features are relevant")
        else:
            print("\nNo clear quality threshold identified - comprehensive model dominates")
            optimal_threshold = None
        
        return summary, pivot, optimal_threshold
    
    def create_visualizations(self, output_dir):
        """Create visualizations of the results"""
        df = pd.DataFrame(self.results)
        
        # Performance vs Quality plot
        plt.figure(figsize=(12, 8))
        
        for model_type in ['minimal', 'comprehensive']:
            model_data = df[df['model_type'] == model_type]
            avg_performance = model_data.groupby('quality_score')['cv_auc_mean'].mean()
            std_performance = model_data.groupby('quality_score')['cv_auc_mean'].std()
            
            plt.errorbar(avg_performance.index, avg_performance.values, 
                        yerr=std_performance.values, label=f'{model_type.title()} Model',
                        marker='o', capsize=5, capthick=2, linewidth=2)
        
        plt.xlabel('Data Quality Score (Fraction of Relevant Features)', fontsize=12)
        plt.ylabel('Cross-Validation AUC', fontsize=12)
        plt.title('Model Performance vs Data Quality\nRare Disease Drug Repurposing', fontsize=14)
        plt.legend(fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'quality_threshold_analysis.png'), dpi=300)
        plt.close()
        
        # Performance difference plot
        plt.figure(figsize=(10, 6))
        pivot = df.groupby(['quality_score', 'model_type'])['cv_auc_mean'].mean().unstack()
        difference = pivot['minimal'] - pivot['comprehensive']
        
        plt.plot(difference.index, difference.values, 'ro-', linewidth=2, markersize=8)
        plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
        plt.xlabel('Data Quality Score', fontsize=12)
        plt.ylabel('Performance Difference (Minimal - Comprehensive)', fontsize=12)
        plt.title('When Does Data Minimalism Win?', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'performance_difference.png'), dpi=300)
        plt.close()
    
    def save_results(self, output_dir):
        """Save detailed results to files"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Save raw results
        df = pd.DataFrame(self.results)
        df.to_csv(os.path.join(output_dir, 'raw_results.csv'), index=False)
        
        # Save summary statistics
        summary, pivot, threshold = self.analyze_results()
        summary.to_csv(os.path.join(output_dir, 'summary_statistics.csv'))
        pivot.to_csv(os.path.join(output_dir, 'performance_matrix.csv'))
        
        # Save threshold information
        threshold_info = {
            'optimal_threshold': float(threshold) if threshold is not None else None,
            'experiment_date': datetime.now().isoformat(),
            'n_diseases_tested': self.n_diseases,
            'base_samples': self.base_samples,
            'validation_method': 'stratified_5_fold_cv'
        }
        
        with open(os.path.join(output_dir, 'threshold_results.json'), 'w') as f:
            json.dump(threshold_info, f, indent=2)
        
        # Create visualizations
        self.create_visualizations(output_dir)
        
        return threshold_info

if __name__ == "__main__":
    # Run the experiment
    experiment = QualityThresholdExperiment(n_diseases=10, base_samples=1000)
    results = experiment.run_experiment()
    
    # Create output directory
    output_dir = "/home/runner/work/artificial-intelligence-to-accelerate-drug-repurposing-for-rare-diseases-with-limited-existing-treat/artificial-intelligence-to-accelerate-drug-repurposing-for-rare-diseases-with-limited-existing-treat/data/micro-exp-a-results"
    
    # Save and analyze results
    threshold_info = experiment.save_results(output_dir)
    
    print(f"\n{'='*60}")
    print("EXPERIMENT COMPLETED SUCCESSFULLY")
    print(f"{'='*60}")
    print(f"Results saved to: {output_dir}")
    if threshold_info['optimal_threshold']:
        print(f"Optimal Quality Threshold: {threshold_info['optimal_threshold']:.3f}")
        print(f"Data minimalism wins when >{threshold_info['optimal_threshold']*100:.1f}% features are relevant")
    else:
        print("No clear threshold identified - further investigation needed")
    print(f"{'='*60}")