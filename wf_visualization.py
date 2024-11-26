# wf_visualization.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from itertools import combinations

def load_processed_data(file_path):
    """Load the processed MLB data."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Processed data file not found at: {file_path}")

def generate_summary_statistics(data, quantitative_columns, output_dir):
    """Generate and save summary statistics."""
    # Compute summary statistics (min, max, median)
    summary_stats = data[quantitative_columns].agg(['min', 'max', 'median'])
    
    # Add mean and standard deviation
    summary_stats.loc['mean'] = data[quantitative_columns].mean()
    summary_stats.loc['std'] = data[quantitative_columns].std()
    
    # Save summary statistics
    summary_stats.to_csv(output_dir / 'summary.txt')
    print("Summary statistics saved successfully.")
    return summary_stats

def create_correlation_matrix(data, quantitative_columns, output_dir, visuals_dir):
    """Create and save correlation matrix."""
    correlation_matrix = data[quantitative_columns].corr()
    
    # Save correlation data
    correlation_matrix.to_csv(output_dir / 'correlations.txt')
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt='.2f')
    plt.title('MLB Statistics Correlation Matrix')
    plt.tight_layout()
    plt.savefig(visuals_dir / 'correlation_matrix.png')
    plt.close()
    
    print("Correlation matrix saved successfully.")
    return correlation_matrix

def create_scatter_plots(data, quantitative_columns, output_dir):
    """Create scatter plots for pairs of variables."""
    for (col1, col2) in combinations(quantitative_columns, 2):
        plt.figure(figsize=(12, 8))
        sns.scatterplot(x=col1, y=col2, data=data)
        plt.title(f'Scatter Plot: {col1} vs {col2}')
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.grid(True)
        plt.savefig(output_dir / f'scatter_{col1}_{col2}.png')
        plt.close()

def create_distribution_plots(data, output_dir):
    """Create distribution plots for key statistics."""
    plt.figure(figsize=(12, 8))
    sns.histplot(data['OBP'], bins=20, color='blue', label='OBP', kde=True, stat='density', alpha=0.5)
    sns.histplot(data['SLG'], bins=20, color='orange', label='SLG', kde=True, stat='density', alpha=0.5)

    plt.title('Distribution of On-Base Percentage (OBP) and Slugging Percentage (SLG)')
    plt.xlabel('Percentage')
    plt.ylabel('Density')
    plt.legend()
    plt.savefig(output_dir / 'histogram_obp_slg.png')
    plt.close() 

def main():
    """Main visualization workflow."""
    try:
        # Setup paths
        script_dir = Path(__file__).parent
        input_file = script_dir / 'data_processed' / 'cleaned_mlb_stats.csv'
        output_dir = script_dir / 'data_processed'
        visuals_dir = script_dir / 'visuals'
        
        # Create output directories if they don't exist
        output_dir.mkdir(exist_ok=True)
        visuals_dir.mkdir(exist_ok=True)
        
        # Load data
        print("Loading processed data...")
        data = load_processed_data(input_file)
        
        # Define columns for analysis
        quantitative_columns = ['WAR', 'PA', 'AB', 'OBP', 'SLG']
        
        # Generate and save summary statistics
        print("Generating summary statistics...")
        summary_stats = generate_summary_statistics(data, quantitative_columns, output_dir)
        print("\nSummary Statistics:")
        print(summary_stats)
        
        # Create and save correlation matrix
        print("\nGenerating correlation matrix...")
        correlation_matrix = create_correlation_matrix(data, quantitative_columns, output_dir, visuals_dir)
        print("\nCorrelation Matrix:")
        print(correlation_matrix)
        
        # Create visualizations
        print("\nCreating scatter plots...")
        create_scatter_plots(data, quantitative_columns, visuals_dir)
        
        print("Creating distribution plots...")
        create_distribution_plots(data, visuals_dir)
        
        print("Visualization completed successfully.")
        
    except Exception as e:
        print(f"Error in visualization: {str(e)}")
        raise

if __name__ == "__main__":
    main()