#### SER594: Machine Learning Evaluation
#### Precision Play: Innovating MLB Performance Analysis Through Data Integration
#### Om Rajesh Chauhan
#### November 25, 2024

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error (MSE)

**Choice Justification:** The most commonly used metric for regression problems is the Mean Squared Error (MSE), 
which calculates the average of squared differences between predicted and actual values. By squaring the errors, MSE 
gives heavy penalties to larger errors, hence being sensitive to outliers. This property is useful in our case because 
we want to minimize significant discrepancies between the model's predictions and the actual performance of the MLB 
players. The smaller MSE means that the estimated values of this model are closer to the true values.

**Interpretation:** A lower MSE is a better model performance since the error between the predicted and actual values is 
small. However, MSE squares the errors, so it gives disproportionately larger weights to bigger errors; hence, it is 
very useful when large deviations are undesirable.

### Metric 2
**Name:** R-squared (R²)

**Choice Justification:** R-squared, or the coefficient of determination, describes the proportion of variance in the 
dependent variable (target, such as WAR, OPS, or SLG) that is predictable from the independent variables 
(predictor features such as hits, home runs, etc.). R² is a conventional metric to assess the goodness of fit for any 
regression model. The larger the value of R² is, the better the model is at describing the variation in the target 
variable using the predictors.

**Interpretation:** R² ranges from 0 to 1. A value toward 1 indicates that most of the variance in the target variable
is explained by the model, while a value toward 0 indicates that the model is not useful for prediction. Sometimes, 
R² can be misleading, especially in cases when there are non-linear relationships between predictors and the target.
So, R² should be considered with some other metrics such as MSE and RMSE for further details.

### Metric 3

**Name:** Root Mean Squared Error (RMSE)

**Choice Justification:** RMSE is the square root of MSE. The measure here gives a similar measure of average error in 
the model's prediction. RMSE is more interpretable than MSE because it's in the same units as the target variable. 
For instance, assuming that the target variable is WAR, which in itself is a continuous variable, the RMSE will also 
be in the WAR units. This can be used to meaningfully understand how far off the forecasts are, in practical terms.

**Interpretation:** The lower the value of RMSE, the better the performance. The main advantage of RMSE is that it 
tells us something about the size of the typical prediction error in the context of the target variable. Because it 
is measured in the same unit as the target variable, the interpretation of its meaning as an average prediction error 
is more intuitive.

### Metric 4

**Name:** Mean Absolute Error (MAE)

**Choice Justification:** MAE is another common metric for regression tasks. It computes the average of the absolute 
differences between the predicted and actual values. Unlike MSE and RMSE, MAE does not square the errors, meaning it 
treats all errors equally, regardless of their size. This makes MAE less sensitive to large deviations and outliers 
compared to MSE and RMSE.

**Interpretation:** The result is that a lower MAE specifies the model's providing more average accurate predictions. 
MAE is generally used when one wants a more robust measure of prediction error, which does not give excessive penalty 
to large errors, thus being ideal in cases when outliers should not unduly affect evaluation.



## Alternative Models
### Alternative 1
**Construction:** Ridge Regression (alpha = 0.1)

**Evaluation:** Ridge regression is a kind of regularized linear regression where L2 regularization is used on the 
coefficients. This model works to avoid multicollinearity, not allowing overfitting by penalizing large coefficients. 
In this model, the choice of alpha used was 0.1, which somehow creates a balance between model regularization and 
accuracy.

* MSE:  0.1060,
* R²: 0.9411,
* RMSE: 0.3255,
* MAE:  0.1457,

### Alternative 2
**Construction:** Lasso Regression (alpha = 0.1)

**Evaluation:** Lasso regression does apply L1 regularization and, hence, can shrink some of the coefficients to zero; 
therefore, feature selection is performed in the process. The reason Lasso was chosen here is to reduce model 
complexity by eliminating less relevant features. With an alpha value of 0.1, this model allows regularization to be 
controlled while still offering a good fit to the data.

* MSE:  0.1862,
* R²: 0.3714,
* RMSE: 0.4315,
* MAE:  0.2193,

### Alternative 3
**Construction:** K-Nearest Neighbors (K = 3)

**Evaluation:** K-Nearest Neighbors is a non-parametric, lazy learning algorithm that predicts the output by finding the K-nearest data points in the feature space. Here, K equals 3, so it makes a prediction based on the 3 nearest data points. While it can be very powerful for capturing complex relationships, K-Nearest Neighbors usually performs poorly with high-dimensional data and may have a hard time dealing with big datasets because of its high computational complexity.

* MSE:  0.2005
* R²: 0.8700
* RMSE: 0.4478  
* MAE:  0.1903

### Alternative 3
**Construction:** K-Nearest Neighbors (K = 10)

**Evaluation:** K-Nearest Neighbors is a non-parametric, lazy learning algorithm that predicts the output by finding the K-nearest data points in the feature space. Here, K equals 10, so it makes a prediction based on the 10 nearest data points. While it can be very powerful for capturing complex relationships, K-Nearest Neighbors usually performs poorly with high-dimensional data and may have a hard time dealing with big datasets because of its high computational complexity.

* MSE:  0.1656
* R²: 0.8804
* RMSE: 0.4069
* MAE:  0.1784


## Best Model

**Model:** Ridge Regression (alpha = 0.1)

**Reason** According to the results obtained from evaluation, Ridge Regression with alpha = 0.1 turned out to be the best model, since it showed a very balanced performance regarding all metrics. It minimized overfitting through regularization while still maintaining good predictive accuracy across MSE, R², RMSE, and MAE. This model provided the most robust predictions for offensive and defensive performance in the MLB dataset.`



