#!/usr/bin/env python3
"""
Experiment execution script for Transfer Learning Similarity Mapping
Ensures reproducible execution with proper logging and error handling
"""

import sys
import os
import json
import traceback
from datetime import datetime
from pathlib import Path

# Add the experiment directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def setup_data_directory():
    """Create data directory for experiment results"""
    data_dir = Path("../../data/micro-exp-c-results")
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir

def log_experiment_start():
    """Log experiment start time and configuration"""
    start_info = {
        'experiment_id': 'micro-exp-c-transfer-similarity',
        'start_time': datetime.now().isoformat(),
        'python_version': sys.version,
        'working_directory': os.getcwd()
    }
    
    print("=" * 60)
    print("TRANSFER LEARNING SIMILARITY MAPPING EXPERIMENT")
    print("=" * 60)
    print(f"Start time: {start_info['start_time']}")
    print(f"Python version: {start_info['python_version']}")
    print(f"Working directory: {start_info['working_directory']}")
    print("=" * 60)
    
    return start_info

def run_experiment():
    """Execute the main experiment with error handling"""
    try:
        # Import the experiment module
        from transfer_similarity_experiment import main as run_experiment_main
        
        # Execute the experiment
        print("Starting experiment execution...")
        run_experiment_main()
        
        return True, None
        
    except Exception as e:
        error_info = {
            'error_type': type(e).__name__,
            'error_message': str(e),
            'traceback': traceback.format_exc()
        }
        print(f"ERROR: {error_info['error_message']}")
        print("Full traceback:")
        print(error_info['traceback'])
        
        return False, error_info

def log_experiment_end(start_info, success, error_info=None):
    """Log experiment completion status"""
    end_time = datetime.now()
    start_time = datetime.fromisoformat(start_info['start_time'])
    duration = end_time - start_time
    
    completion_info = {
        'end_time': end_time.isoformat(),
        'duration_seconds': duration.total_seconds(),
        'success': success,
        'error_info': error_info
    }
    
    print("=" * 60)
    print("EXPERIMENT COMPLETION")
    print("=" * 60)
    print(f"End time: {completion_info['end_time']}")
    print(f"Duration: {duration}")
    print(f"Success: {completion_info['success']}")
    
    if not success and error_info:
        print(f"Error: {error_info['error_message']}")
    
    print("=" * 60)
    
    return completion_info

def main():
    """Main execution wrapper with logging and error handling"""
    # Setup
    setup_data_directory()
    start_info = log_experiment_start()
    
    # Run experiment
    success, error_info = run_experiment()
    
    # Cleanup and logging
    completion_info = log_experiment_end(start_info, success, error_info)
    
    # Save execution log
    execution_log = {
        'start_info': start_info,
        'completion_info': completion_info
    }
    
    log_path = Path("../../data/micro-exp-c-results/execution_log.json")
    with open(log_path, 'w') as f:
        json.dump(execution_log, f, indent=2)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()