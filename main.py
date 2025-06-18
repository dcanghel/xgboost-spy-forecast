# main.py
from data.load_data import load_tiingo_data
from features.engineer import create_features
from models.train import train_model
from models.evaluate import evaluate_model
from visualization.plots import plot_forecast, plot_feature_importance

# === Load Data ===
df = load_tiingo_data()

# === Feature Engineering ===
df = create_features(df)

# === Train/Test Split ===
train = df[:'2024']
test = df['2025':]

X_train = train.drop(columns=['adj_close'])
y_train = train['adj_close']
X_test = test.drop(columns=['adj_close'])
y_test = test['adj_close']

# === Train Model ===
model, dtest, preds = train_model(X_train, y_train, X_test)

# === Evaluate ===
evaluate_model(y_test, preds)

# === Plotting ===
plot_forecast(y_test, preds)
plot_feature_importance(model)
