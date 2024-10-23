import pandas as pd
import os

# Load the original MLB dataset
input_file = 'mlb_player_performance/data_original/mlb_stats.csv'
output_file = 'mlb_player_performance/data_processed/cleaned_mlb_stats.csv'

# Load data
mlb_data = pd.read_csv(input_file)

# Data cleaning (splitting columns based on the format, handle missing values)
mlb_data_cleaned = mlb_data['--- When using SR data, please cite us and provide a link and/or a mention.'].str.split(',', expand=True)

# Set the first row as headers and drop the original first row
mlb_data_cleaned.columns = mlb_data_cleaned.iloc[0]
mlb_data_cleaned = mlb_data_cleaned.drop(0).reset_index(drop=True)

# Convert relevant columns to numeric
quantitative_columns = ['WAR', 'PA', 'AB', 'H', 'HR', 'RBI', 'OBP', 'SLG', 'OPS']
mlb_data_cleaned[quantitative_columns] = mlb_data_cleaned[quantitative_columns].apply(pd.to_numeric, errors='coerce')

# Save processed data
os.makedirs('data_processed', exist_ok=True)
mlb_data_cleaned.to_csv(output_file, index=False)

def main():
    # Your data processing logic here
    print("Data processing executed.")

if __name__ == "__main__":
    main()  # Allows running this file standalone
