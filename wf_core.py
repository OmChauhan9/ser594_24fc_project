import os
import wf_dataprocessing
import wf_visualization
import wf_ml_evaluation

def check_environment():
    """Check if required directories exist."""
    required_dirs = ['data_original', 'data_processed', 'visuals']
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory
    
    for dir_name in required_dirs:
        dir_path = os.path.join(base_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {dir_path}")

def main():
    """Main workflow execution."""
    try:
        print("Checking environment...")
        check_environment()
        
        print("\nStarting data processing...")
        wf_dataprocessing.main()
        
        print("\nStarting visualization...")
        wf_visualization.main()

        print("\nStaring Evaluation...")
        wf_ml_evaluation.main()
        
        print("\nWorkflow completed successfully!")
        
    except Exception as e:
        print(f"\nError in workflow execution: {str(e)}")
        print("\nPlease ensure:")
        print("1. The raw data file 'mlb_stats.csv' is placed in the 'data_original' directory")
        print("2. All required Python packages are installed (pandas, seaborn, matplotlib)")
        raise

if __name__ == "__main__":
    main()
