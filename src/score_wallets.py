import json
import pandas as pd
from feature_engineering import preprocess_transactions, aggregate_wallet_features
from scoring import train_model, score_wallets

with open("data/user-wallet-transactions.json", "r") as f:
    data = json.load(f)

df = preprocess_transactions(data)
features = aggregate_wallet_features(df)
model, scaler = train_model(features)
scores = score_wallets(model, scaler, features)
scores.to_csv("output/wallet_scores.csv", index=False)
print("Scoring complete. Output saved to output/wallet_scores.csv")
