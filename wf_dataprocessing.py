import pandas as pd
import numpy as np
from pathlib import Path
import logging
from datetime import datetime

def create_directory_structure():
    """Create necessary directories if they don't exist."""
    directories = ['data_original', 'data_processed', 'visuals']
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        logging.info(f"Created/verified directory: {directory}")

def load_data(data_path):
    """Load the MLB dataset with error handling."""
    try:
        df = pd.read_csv(data_path)
        logging.info(f"Successfully loaded data from {data_path}")
        logging.info(f"Initial data shape: {df.shape}")
        return df
    except FileNotFoundError:
        error_msg = f"Please place the MLB stats CSV file at: {data_path}"
        logging.error(error_msg)
        raise FileNotFoundError(error_msg)
    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        raise

def remove_html_content(df):
    """Remove HTML content from the dataframe."""
    try:
        # Make a copy to avoid modifying the original
        df = df.copy()
        
        # Remove rows that are completely HTML
        html_rows = df.astype(str).apply(lambda x: x.str.contains('<.*?>').all(), axis=1)
        if html_rows.any():
            df = df[~html_rows]
            logging.info(f"Removed {html_rows.sum()} rows containing HTML content")
        
        # Check columns for HTML content
        for col in df.columns:
            if df[col].astype(str).str.contains('<|>').any():
                logging.info(f"Dropping column with HTML content: {col}")
                df = df.drop(columns=[col])
                continue

            # try:
            #     df[col] = pd.to_numeric(df[col], errors='raise')
            # except (ValueError, TypeError):
            #     logging.info(f"Dropping non-numeric column: {col}")
            #     df = df.drop(columns=[col])
        
        return df
    except Exception as e:
        logging.error(f"Error removing HTML content: {str(e)}")
        raise

def clean_mlb_data(df):
    """Clean and preprocess MLB-specific data."""
    try:
        # Split the data if it's in the combined format
        if '--- When using SR data, please cite us and provide a link and/or a mention.' in df.columns:
            df = df['--- When using SR data, please cite us and provide a link and/or a mention.'].str.split(',', expand=True)
            df.columns = df.iloc[0]
            df = df.drop(0).reset_index(drop=True)
            logging.info("Processed combined format data")

        # Define column categories
        quantitative_columns = ['WAR', 'PA', 'AB', 'H', 'HR', 'RBI', 'OBP', 'SLG', 'OPS']
        counting_stats = ['PA', 'AB', 'H', 'HR', 'RBI']
        rate_stats = ['OBP', 'SLG', 'OPS']
        
        # Convert quantitative columns to numeric
        for col in quantitative_columns:
            if col in df.columns:
                original_nulls = df[col].isnull().sum()
                df[col] = pd.to_numeric(df[col], errors='coerce')
                new_nulls = df[col].isnull().sum()
                if new_nulls > original_nulls:
                    logging.info(f"Converting {col} to numeric created {new_nulls - original_nulls} new null values")

        # Handle missing values
        initial_rows = len(df)
        
        # 1. Fill counting stats with 0
        for col in counting_stats:
            if col in df.columns:
                null_count = df[col].isnull().sum()
                df[col] = df[col].fillna(0)
                if null_count > 0:
                    logging.info(f"Filled {null_count} missing values with 0 in {col}")

        # 2. Fill rate stats with league average
        for stat in rate_stats:
            if stat in df.columns:
                null_count = df[stat].isnull().sum()
                league_avg = df[stat].mean()
                df[stat] = df[stat].fillna(league_avg)
                if null_count > 0:
                    logging.info(f"Filled {null_count} missing values with league average ({league_avg:.3f}) in {stat}")

        # 3. Fill WAR with 0
        if 'WAR' in df.columns:
            null_count = df['WAR'].isnull().sum()
            df['WAR'] = df['WAR'].fillna(0)
            if null_count > 0:
                logging.info(f"Filled {null_count} missing WAR values with 0")

        # Data validation
        if len(df) < initial_rows:
            logging.warning(f"Lost {initial_rows - len(df)} rows during cleaning")

        # Verify data quality
        remaining_nulls = df[quantitative_columns].isnull().sum()
        if remaining_nulls.any():
            logging.warning("Remaining null values after cleaning:")
            for col, null_count in remaining_nulls.items():
                if null_count > 0:
                    logging.warning(f"{col}: {null_count} null values")

        return df
    except Exception as e:
        logging.error(f"Error in MLB data cleaning: {str(e)}")
        raise

def clean_data(df):
    """Master cleaning function that combines all cleaning steps."""
    try:
        # Remove HTML content
        df = remove_html_content(df)
        
        # Clean MLB-specific data
        df = clean_mlb_data(df)
        
        # Final validation
        if len(df) < 100:
            raise ValueError(f"After cleaning, only {len(df)} rows remain. This might not be enough for reliable analysis.")
        
        logging.info(f"Final dataframe shape after cleaning: {df.shape}")
        logging.info(f"Final columns: {', '.join(df.columns)}")
        
        return df
    except Exception as e:
        logging.error(f"Error in master cleaning function: {str(e)}")
        raise

def main():
    """Main data processing workflow."""
    try:
        # Create directory structure
        create_directory_structure()
        
        # Define paths
        script_dir = Path(__file__).parent
        input_file = script_dir / 'data_original' / 'mlb_stats.csv'
        
        # Create timestamped output file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = script_dir / 'data_processed' / f'cleaned_mlb_stats.csv'
        
        # Load data
        logging.info("Loading data...")
        raw_data = load_data(input_file)
        logging.info(f"Initial columns: {', '.join(raw_data.columns)}")
        
        # Clean data
        logging.info("Starting data cleaning process...")
        cleaned_data = clean_data(raw_data)
        
        # Save processed data
        logging.info(f"Saving processed data to {output_file}")
        cleaned_data.to_csv(output_file, index=False)
        
        logging.info("Data processing completed successfully.")
        return cleaned_data
        
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        if 'raw_data' in locals():
            logging.error(f"Data shape: {raw_data.shape}")
            logging.error(f"Data columns: {raw_data.columns.tolist()}")
        raise

if __name__ == "__main__":
    main()