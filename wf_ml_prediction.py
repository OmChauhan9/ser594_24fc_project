import pandas as pd
import numpy as np
import joblib
import os
import sys

def load_models():
    """Load all trained models"""
    models = {}
    try:
        scaler = joblib.load('models/scaler.joblib')
        
        for model_file in os.listdir('models'):
            if model_file.endswith('.joblib') and model_file != 'scaler.joblib':
                model_name = model_file.replace('.joblib', '')
                models[model_name] = joblib.load(f'models/{model_file}')
        
        return models, scaler
    except FileNotFoundError as e:
        print(f"Error loading models: {e}")
        sys.exit(1)

def load_test_data():
    """Load the saved test data for predictions"""
    try:
        X_test_scaled = pd.read_csv('data_processed/X_test.csv').values
        y_test = pd.read_csv('data_processed/y_test.csv').values.flatten()
        return X_test_scaled, y_test
    except FileNotFoundError as e:
        print(f"Error loading test data: {e}")
        sys.exit(1)

def predict_changes():
    """Make predictions using all models"""
    # Load models and scaler
    models, _ = load_models()
    
    # Load test data
    X_test, y_test = load_test_data()
    
    # Make predictions with each model
    predictions = {}
    for name, model in models.items():
        model_predictions = model.predict(X_test)
        predictions[name] = {
            'predictions': model_predictions,
            'sample_predictions': {
                'first_5_actual': y_test[:5],
                'first_5_predicted': model_predictions[:5]
            }
        }
    
    return predictions

def save_predictions(predictions):
    """Save predictions to CSV files"""
    # Ensure predictions directory exists
    if not os.path.exists('predictions'):
        os.makedirs('predictions')
    
    for model_name, pred_data in predictions.items():
        # Separate each target prediction into its own column
        pred_df = pd.DataFrame({
            'Actual': pred_data['sample_predictions']['first_5_actual'],
        })
        
        # If there are multiple predictions per model, handle each one separately
        num_predictions = pred_data['sample_predictions']['first_5_predicted'].shape[1]
        for i in range(num_predictions):
            pred_df[f'Predicted_Target_{i+1}'] = pred_data['sample_predictions']['first_5_predicted'][:, i]
        
        pred_df.to_csv(f'predictions/{model_name}_sample_predictions.csv', index=False)

def main():
    """Main prediction workflow"""
    print("Starting Model Predictions...")
    predictions = predict_changes()
    # Print sample predictions
    for model_name, pred_data in predictions.items():
        print(f"\nModel: {model_name}")
        print("First 5 Actual Values:", pred_data['sample_predictions']['first_5_actual'])
        print("First 5 Predicted Values:\n", pred_data['sample_predictions']['first_5_predicted'])
    
    # # Save predictions
    # save_predictions(predictions)
    # print("Finished Model Predictions...")
    # # print("\nPrediction results saved in 'predictions' directory.")

if __name__ == '__main__':
    main()
