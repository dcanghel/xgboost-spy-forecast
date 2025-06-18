# visualization/plots.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_forecast(y_test, preds):
    plt.figure(figsize=(12,5))
    plt.plot(y_test.index, y_test, label='Actual', linewidth=2)
    plt.plot(y_test.index, preds, label='Forecast', linestyle='--')
    plt.title('SPY Forecast (XGBoost)')
    plt.legend()
    plt.grid()
    plt.show()

def plot_feature_importance(model):
    importance = model.get_score(importance_type='weight')
    imp_df = pd.DataFrame.from_dict(importance, orient='index', columns=['importance'])
    imp_df.sort_values(by='importance', ascending=True).plot(kind='barh', figsize=(10,5), legend=False)
    plt.title("XGBoost Feature Importance")
    plt.grid()
    plt.show()
