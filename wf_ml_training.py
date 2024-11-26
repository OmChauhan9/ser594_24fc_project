import os
import joblib
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.neighbors import KNeighborsRegressor

base_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(base_dir, 'models')

def train_models(X_train, y_train, model_dir=model_path):
    """Train multiple models and save them to a specified directory."""
    
    # Create the model directory if it doesn't exist
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        print(f"Created directory: {model_dir}")
    
    # Define a dictionary of models to train
    models = {
        'linear_regression': LinearRegression(),
    }

    # Loop through the models, train them, and save them
    for name, model in models.items():
        print(f"Training model: {name}")
        model.fit(X_train, y_train)  # Train the model
        
        # Define the path where the model will be saved
        model_save_path = os.path.join(model_dir, f'{name}.joblib')
        
        # Save the trained model using joblib
        joblib.dump(model, model_save_path)

        # Print a confirmation message
        print(f"{name} model saved to {model_save_path}")

    print("All models have been trained and saved successfully!")


    
   




    
    
    