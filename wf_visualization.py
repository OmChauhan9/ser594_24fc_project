import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from itertools import combinations

# Load the cleaned data
input_file = 'mlb_player_performance/data_processed/cleaned_mlb_stats.csv'
mlb_data_cleaned = pd.read_csv(input_file)

# 3. Summary Statistics
quantitative_columns = ['WAR', 'PA', 'AB', 'OBP', 'SLG']

# Compute min, max, median for quantitative features
summary_stats = mlb_data_cleaned[quantitative_columns].agg(['min', 'max', 'median'])

# Save the summary statistics to a file
os.makedirs('data_processed', exist_ok=True)
summary_stats.to_csv('mlb_player_performance/data_processed/summary.txt')

# 4. Correlation Matrix
correlation_matrix = mlb_data_cleaned[quantitative_columns].corr()
correlation_matrix.to_csv('mlb_player_performance/data_processed/correlations.txt')

# Optional: Visualize the correlation matrix as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title('Correlation Matrix')
plt.savefig('mlb_player_performance/visuals/correlation_matrix.png')
plt.show()

for (col1, col2) in combinations(quantitative_columns, 2):
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=col1, y=col2, data=mlb_data_cleaned)
    plt.title(f'Scatter Plot: {col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.grid(True)
    plt.savefig(f'mlb_player_performance/visuals/scatter_plot_{col1}_vs_{col2}.png')
    plt.close()  # Close the figure after saving

plt.figure(figsize=(12, 8))
sns.histplot(mlb_data_cleaned['OBP'], bins=20, color='blue', label='OBP', kde=True, stat='density', alpha=0.5)
sns.histplot(mlb_data_cleaned['SLG'], bins=20, color='orange', label='SLG', kde=True, stat='density', alpha=0.5)

plt.title('Distribution of On-Base Percentage (OBP) and Slugging Percentage (SLG)')
plt.xlabel('Percentage')
plt.ylabel('Density')
plt.legend()
plt.savefig('mlb_player_performance/visuals/histogram_obp_slg.png')
plt.close()  # Close the figure after saving

def main():
    # Your visualization logic here
    print("Visualization executed.")

if __name__ == "__main__":
    main()  # Allows running this file standalone
