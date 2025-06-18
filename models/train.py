# models/train.py
import xgboost as xgb

def train_model(X_train, y_train, X_test):
    from xgboost import DMatrix
    dtrain = DMatrix(X_train, label=y_train)
    dtest = DMatrix(X_test)
    params = {'objective': 'reg:squarederror', 'max_depth': 5, 'eta': 0.1, 'seed': 42}
    model = xgb.train(params, dtrain, num_boost_round=300,
                      evals=[(dtrain, 'train')],
                      early_stopping_rounds=20, verbose_eval=False)
    preds = model.predict(dtest)
    return model, dtest, preds
