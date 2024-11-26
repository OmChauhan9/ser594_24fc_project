import logging
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
import joblib
import os
import wf_ml_training
import wf_ml_prediction


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_folder = os.path.join(BASE_DIR, 'data_processed')
model_path = os.path.join(BASE_DIR, 'models')
evaluation_path = os.path.join(BASE_DIR, 'evaluation')
summary_file = os.path.join(BASE_DIR, 'evaluation', 'summary.txt')
visualization_folder = os.path.join(evaluation_path, 'prediction')

def load_and_merge_data():
    """Load and merge all processed datasets"""
    data = pd.read_csv('data_processed/cleaned_mlb_stats.csv')
    
    # Perform any necessary preprocessing here (e.g., drop non-numeric columns, handle missing values)
    data = data.dropna()  # Example: drop rows with missing values
    
    # You can inspect the columns and types to ensure they are as expected
    print(data.dtypes)  # To see the data types of each column
    
    return data

def prepare_features(df):
    """Prepare features for ML model"""
    # Drop non-numeric columns like player names or any string-based columns
    df = df.select_dtypes(include=[np.number])  # Only keep numeric columns
    
    # Select features and target variable
    X = df.drop(columns=['WAR', 'OPS', 'SLG'])  # Features (predictors)
    y = df[['WAR', 'OPS', 'SLG']]  # Target variable (to predict WAR, OPS, and SLG)

    return X,y

def split():
    
    # Create models directory if it doesn't exist
    if not os.path.exists(model_path,):
        os.makedirs(model_path)
    
    # Load and prepare data
    data = load_and_merge_data()
    X, y = prepare_features(data)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    if len(y_test) < 30:
        raise ValueError(f"Test set too small: {len(y_test)} samples (minimum 30 required)")

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test= scaler.transform(X_test)
    
    # Save scaled data
    pd.DataFrame(X_train).to_csv(os.path.join(model_folder, 'X_train.csv'), index=False)
    pd.DataFrame(X_test).to_csv(os.path.join(model_folder, 'X_test.csv'), index=False)
    pd.DataFrame(y_train).to_csv(os.path.join(model_folder, 'y_train.csv'), index=False)
    pd.DataFrame(y_test).to_csv(os.path.join(model_folder, 'y_test.csv'), index=False)
    
    # Save scaler
    joblib.dump(scaler, os.path.join(model_path, 'scaler.joblib'))

    return X_train, y_train

def load_data():
    """Load training and test data"""
    X_train = pd.read_csv(os.path.join(model_folder, 'X_train.csv')).values 
    X_test = pd.read_csv(os.path.join(model_folder, 'X_test.csv')).values  
    y_train = pd.read_csv(os.path.join(model_folder, 'y_train.csv')).values 
    y_test = pd.read_csv(os.path.join(model_folder, 'y_test.csv')).values  
    
    return X_train, X_test, y_train, y_test

def construct_alternative_models(X_train, y_train):
    """Construct alternative models with different configurations"""
    
    # Alternative 1: Linear Regression
    ridge_model = Ridge(alpha=0.1)
    # Alternative 2: Ridge Regression (with alpha tuning)
    lasso_model = Lasso(alpha=0.1)
    # Alternative 4: KNN Regressor (different values of k)
    knn_model_1 = KNeighborsRegressor(n_neighbors=3)
    knn_model_2 = KNeighborsRegressor(n_neighbors=10)
    
    # Fit models
    ridge_model.fit(X_train, y_train)
    lasso_model.fit(X_train, y_train)
    knn_model_1.fit(X_train, y_train)
    knn_model_2.fit(X_train, y_train)
    
    models = {
        'Ridge Regression (alpha = 0.1)': ridge_model,
        'Lasso Regression': lasso_model,
        'KNN (k=3)': knn_model_1,
        'KNN (k=10)': knn_model_2
    }

    for name, model in models.items():
        print(f"Training model: {name}")
        model.fit(X_train, y_train)  # Train the model
        
        # Define the path where the model will be saved
        model_save_path = os.path.join(model_path, f'{name}.joblib')
        
        # Save the trained model using joblib
        joblib.dump(model, model_save_path)
    
    return models

def evaluate_models():

    if not os.path.exists(evaluation_path):
        os.makedirs(evaluation_path)
    """Evaluate multiple models and save the results"""
    # Load data
    X_train, X_test, y_train, y_test = load_data()
    
    # Construct alternative models
    models = construct_alternative_models(X_train, y_train)
    
    # Prepare a list to store results
    results = []
    
    # Evaluate each model
    for name, model in models.items():
        y_pred = model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        
        # Store results in a dictionary
        results.append({
            'model_name': name,
            'mean_squared_error': mse,
            'root_mean_squared_error': rmse,
            'r_squared': r2,
            'mean_absolute_error': mae,
        })
    
    if not results:
        logging.error("No results to evaluate. Check if models were loaded and evaluated correctly.")
        return
    
    # Write results to a file
    with open(summary_file, 'w') as f:
        f.write(f"Model Evaluation Summary\n")
        f.write("=" * 80 + "\n\n")
        
        # Create header, including 'model_name'
        metrics = list(results[0].keys())  # Include 'model_name' in the header
        header = "| " + " | ".join(f"{m:^25}" for m in metrics) + " |"
        separator = "|" + "|".join("-" * 27 for _ in metrics) + "|"
        
        f.write(header + "\n")
        f.write(separator + "\n")
        
        # Write results, ensuring model name is first
        for result in results:
            row = "| " + " | ".join(
                f"{str(result[m]):^25}" if m == 'model_name' else f"{result[m]:^25.4f}"
                for m in metrics
            ) + " |"
            f.write(row + "\n")
        
    logging.info(f"Evaluation results saved to {summary_file}")

def main():
    X_train,y_train = split()
    print("\nStarting training...")
    wf_ml_training.train_models(X_train, y_train)
    print("Model training and saving completed.")
    wf_ml_prediction.main()
    evaluate_models()

if __name__ == '__main__':
    main()