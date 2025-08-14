#!/usr/bin/env python3
"""
Simplified Transfer Learning Similarity Mapping Experiment
Uses only Python standard library for maximum compatibility
"""

import json
import random
import math
from datetime import datetime

def jaccard_similarity(set1, set2):
    """Calculate Jaccard similarity for binary lists"""
    intersection = sum(a and b for a, b in zip(set1, set2))
    union = sum(a or b for a, b in zip(set1, set2))
    return intersection / union if union > 0 else 0.0

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(a * a for a in vec2))
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    return dot_product / (norm1 * norm2)

def correlation(vec1, vec2):
    """Calculate Pearson correlation coefficient"""
    n = len(vec1)
    if n == 0:
        return 0.0
    
    mean1 = sum(vec1) / n
    mean2 = sum(vec2) / n
    
    numerator = sum((a - mean1) * (b - mean2) for a, b in zip(vec1, vec2))
    
    sum_sq1 = sum((a - mean1) ** 2 for a in vec1)
    sum_sq2 = sum((b - mean2) ** 2 for b in vec2)
    
    denominator = math.sqrt(sum_sq1 * sum_sq2)
    
    if denominator == 0:
        return 0.0
    
    return numerator / denominator

def generate_synthetic_diseases(n_diseases=50):
    """Generate synthetic disease profiles"""
    print("Generating synthetic disease profiles...")
    
    diseases = []
    for i in range(n_diseases):
        # Generate binary genetic profile (15% involvement)
        genetic_profile = [random.random() < 0.15 for _ in range(100)]
        
        # Generate phenotypic profile (exponential distribution approximation)
        phenotypic_profile = [-math.log(random.random()) * 0.3 for _ in range(50)]
        
        # Generate binary pathway profile (8% involvement)  
        pathway_profile = [random.random() < 0.08 for _ in range(50)]
        
        # Generate clinical profile (gamma distribution approximation)
        clinical_profile = [random.gammavariate(2, 0.5) for _ in range(25)]
        
        disease = {
            'id': f'disease_{i:03d}',
            'genetic_profile': genetic_profile,
            'phenotypic_profile': phenotypic_profile,
            'pathway_profile': pathway_profile,
            'clinical_profile': clinical_profile,
            'complexity': random.uniform(0.1, 1.0),
            'data_availability': random.expovariate(1.25)  # 1/0.8
        }
        diseases.append(disease)
    
    print(f"Generated {len(diseases)} synthetic diseases")
    return diseases

def calculate_similarities_and_outcomes(diseases, n_pairs=50):
    """Calculate disease similarities and simulate transfer outcomes"""
    print("Calculating similarities and simulating transfer outcomes...")
    
    similarity_data = []
    
    # Generate random disease pairs
    for _ in range(n_pairs):
        source_idx = random.randint(0, len(diseases) - 1)
        target_idx = random.randint(0, len(diseases) - 1)
        while target_idx == source_idx:
            target_idx = random.randint(0, len(diseases) - 1)
        
        source = diseases[source_idx]
        target = diseases[target_idx]
        
        # Calculate similarities
        genetic_sim = jaccard_similarity(source['genetic_profile'], target['genetic_profile'])
        phenotypic_sim = cosine_similarity(source['phenotypic_profile'], target['phenotypic_profile'])
        pathway_sim = jaccard_similarity(source['pathway_profile'], target['pathway_profile'])
        clinical_sim = abs(correlation(source['clinical_profile'], target['clinical_profile']))
        
        # Complexity adjustment
        complexity_adj = 1.0 - abs(source['complexity'] - target['complexity'])
        
        # Data availability factor
        data_factor = min(source['data_availability'], target['data_availability']) / 2.0
        
        # Simulate transfer learning success probability
        success_prob = (
            0.3 * genetic_sim +
            0.25 * phenotypic_sim +
            0.2 * pathway_sim +
            0.15 * clinical_sim +
            0.1 * min(data_factor, 1.0)
        )
        
        # Add noise and bound
        success_prob += random.gauss(0, 0.1)
        success_prob = max(0.0, min(1.0, success_prob))
        
        # Binary success outcome
        transfer_success = 1 if success_prob > 0.5 else 0
        
        # Performance improvement
        performance_improvement = success_prob * 0.4 + random.gauss(0, 0.05)
        performance_improvement = max(0.0, performance_improvement)
        
        similarity_data.append({
            'source_disease': source['id'],
            'target_disease': target['id'],
            'genetic_similarity': genetic_sim,
            'phenotypic_similarity': phenotypic_sim,
            'pathway_similarity': pathway_sim,
            'clinical_similarity': clinical_sim,
            'complexity_adjusted_similarity': complexity_adj,
            'data_availability_factor': min(data_factor, 1.0),
            'transfer_success': transfer_success,
            'performance_improvement': performance_improvement,
            'success_probability': success_prob
        })
    
    print(f"Calculated similarities for {len(similarity_data)} disease pairs")
    return similarity_data

def analyze_correlations(similarity_data):
    """Analyze correlations between similarity metrics and transfer success"""
    print("Analyzing correlations...")
    
    similarity_metrics = [
        'genetic_similarity',
        'phenotypic_similarity', 
        'pathway_similarity',
        'clinical_similarity',
        'complexity_adjusted_similarity',
        'data_availability_factor'
    ]
    
    correlations = {}
    
    for metric in similarity_metrics:
        # Extract metric values and success outcomes
        metric_values = [d[metric] for d in similarity_data]
        success_values = [d['transfer_success'] for d in similarity_data]
        performance_values = [d['performance_improvement'] for d in similarity_data]
        
        # Calculate correlations
        success_corr = correlation(metric_values, success_values)
        performance_corr = correlation(metric_values, performance_values)
        
        correlations[metric] = {
            'success_correlation': success_corr,
            'performance_correlation': performance_corr,
            'mean_value': sum(metric_values) / len(metric_values),
            'max_value': max(metric_values),
            'min_value': min(metric_values)
        }
        
        print(f"{metric}: success_r={success_corr:.3f}, performance_r={performance_corr:.3f}")
    
    return correlations

def find_optimal_thresholds(similarity_data):
    """Find optimal similarity thresholds for transfer success prediction"""
    print("Finding optimal thresholds...")
    
    similarity_metrics = [
        'genetic_similarity',
        'phenotypic_similarity',
        'pathway_similarity', 
        'clinical_similarity'
    ]
    
    thresholds = {}
    
    for metric in similarity_metrics:
        metric_values = [d[metric] for d in similarity_data]
        success_values = [d['transfer_success'] for d in similarity_data]
        
        best_threshold = 0.5
        best_accuracy = 0.0
        
        # Test thresholds from 0.1 to 0.9
        for threshold in [i * 0.05 for i in range(2, 19)]:  # 0.1 to 0.9 in steps of 0.05
            predictions = [1 if val >= threshold else 0 for val in metric_values]
            correct = sum(1 for p, s in zip(predictions, success_values) if p == s)
            accuracy = correct / len(success_values)
            
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_threshold = threshold
        
        # Calculate additional metrics at best threshold
        predictions = [1 if val >= best_threshold else 0 for val in metric_values]
        
        # True positives, false positives, etc.
        tp = sum(1 for p, s in zip(predictions, success_values) if p == 1 and s == 1)
        fp = sum(1 for p, s in zip(predictions, success_values) if p == 1 and s == 0)
        tn = sum(1 for p, s in zip(predictions, success_values) if p == 0 and s == 0)
        fn = sum(1 for p, s in zip(predictions, success_values) if p == 0 and s == 1)
        
        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0
        
        thresholds[metric] = {
            'optimal_threshold': best_threshold,
            'accuracy': best_accuracy,
            'sensitivity': sensitivity,
            'specificity': specificity
        }
        
        print(f"{metric}: threshold={best_threshold:.2f}, accuracy={best_accuracy:.3f}")
    
    return thresholds

def evaluate_success_criteria(correlations, similarity_data):
    """Evaluate experiment success criteria"""
    print("Evaluating success criteria...")
    
    # Find strongest correlations
    max_success_corr = max(abs(v['success_correlation']) for v in correlations.values())
    max_performance_corr = max(abs(v['performance_correlation']) for v in correlations.values())
    
    # Calculate overall success rate
    success_rate = sum(d['transfer_success'] for d in similarity_data) / len(similarity_data)
    
    # Determine success level
    success_criteria = {
        'strong_success': max_success_corr > 0.8,
        'moderate_success': max_success_corr > 0.6, 
        'learning_outcome': True,
        'max_correlation': max_success_corr,
        'success_rate': success_rate
    }
    
    if success_criteria['strong_success']:
        success_level = "STRONG SUCCESS"
        print("✅ STRONG SUCCESS: Found correlations > 0.8")
    elif success_criteria['moderate_success']:
        success_level = "MODERATE SUCCESS" 
        print("✅ MODERATE SUCCESS: Found correlations > 0.6")
    else:
        success_level = "LEARNING OUTCOME"
        print("📝 LEARNING OUTCOME: Identified boundary conditions and patterns")
    
    success_criteria['success_level'] = success_level
    return success_criteria

def main():
    """Run the complete experiment"""
    print("=== Transfer Learning Similarity Mapping Experiment ===")
    print("Testing which disease similarity metrics predict transfer learning success")
    print()
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Run experiment pipeline
    diseases = generate_synthetic_diseases(n_diseases=50)
    similarity_data = calculate_similarities_and_outcomes(diseases, n_pairs=50)
    correlations = analyze_correlations(similarity_data)
    thresholds = find_optimal_thresholds(similarity_data)
    success_criteria = evaluate_success_criteria(correlations, similarity_data)
    
    # Compile results
    results = {
        'experiment_id': 'micro-exp-c-transfer-similarity',
        'experiment_date': datetime.now().isoformat(),
        'metadata': {
            'n_diseases': len(diseases),
            'n_pairs': len(similarity_data),
            'success_rate': success_criteria['success_rate'],
            'max_correlation': success_criteria['max_correlation']
        },
        'correlations': correlations,
        'thresholds': thresholds,
        'success_criteria': success_criteria,
        'raw_data': similarity_data[:5]  # Sample of raw data for verification
    }
    
    # Create results directory
    import os
    os.makedirs('../../../data/micro-exp-c-results', exist_ok=True)
    
    # Save results
    with open('../../../data/micro-exp-c-results/transfer_similarity_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print()
    print("=== EXPERIMENT COMPLETE ===")
    print(f"Success Level: {success_criteria['success_level']}")
    print(f"Total pairs analyzed: {len(similarity_data)}")
    print(f"Transfer success rate: {success_criteria['success_rate']:.2%}")
    print(f"Strongest correlation: {success_criteria['max_correlation']:.3f}")
    
    # Identify top predictive metrics
    sorted_metrics = sorted(
        [(k, abs(v['success_correlation'])) for k, v in correlations.items()],
        key=lambda x: x[1],
        reverse=True
    )
    
    print("\nTop 3 predictive metrics:")
    for i, (metric, corr) in enumerate(sorted_metrics[:3], 1):
        print(f"  {i}. {metric}: r={corr:.3f}")
    
    print(f"\nResults saved to: data/micro-exp-c-results/transfer_similarity_results.json")

if __name__ == "__main__":
    main()