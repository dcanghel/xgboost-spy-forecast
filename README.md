# SPY Time Series Forecasting with XGBoost

This modular project uses **XGBoost** to forecast the **adjusted closing price of SPY** (S&P 500 ETF) using **Tiingo daily data (2023–2025)**.

## 🧠 Features
- Time series lag features
- Rolling mean and standard deviation
- Supervised ML regression via XGBoost
- Early stopping
- Feature importance analysis

## 📁 Project Structure
```
main.py
├── data/
│   └── load_data.py
├── features/
│   └── engineer.py
├── models/
│   ├── train.py
│   └── evaluate.py
├── visualization/
    └── plots.py
```

## 🔧 Requirements
```bash
pip install pandas requests xgboost matplotlib scikit-learn
```

## 🚀 How to Run
1. Replace `YOUR_TIINGO_API_KEY_HERE` in `data/load_data.py`.
2. Run `main.py`.

## 📊 Output
- Forecast plot
- RMSE evaluation
- Feature importance chart
