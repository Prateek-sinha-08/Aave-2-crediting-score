from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

def train_model(features):
    X = features.drop(columns=['userWallet'])
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Improved synthetic score
    y = (
        X['repay_ratio'].clip(0, 1) * 300 +
        np.log1p(X['total_deposit_usd']) * 100 +
        np.log1p(X['tx_frequency']) * 100 +
        X['deposit_to_borrow_ratio'].clip(0, 3) * 100 +
        np.log1p(X['activity_span_days']) * 50
    )

    if y.max() != y.min():
        y_scaled = MinMaxScaler(feature_range=(300, 950)).fit_transform(y.values.reshape(-1, 1)).flatten()
    else:
        y_scaled = np.full_like(y, 300)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_scaled, y_scaled)
    return model, scaler

def score_wallets(model, scaler, features):
    X = features.drop(columns=['userWallet'])
    X_scaled = scaler.transform(X)
    scores = model.predict(X_scaled)
    return pd.DataFrame({
        'wallet': features['userWallet'],
        'score': scores.astype(int)
    })