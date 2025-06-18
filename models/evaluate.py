# models/evaluate.py
from sklearn.metrics import mean_squared_error
from math import sqrt

def evaluate_model(y_test, preds):
    rmse = sqrt(mean_squared_error(y_test, preds))
    print(f"Test RMSE: {rmse:.2f}")
