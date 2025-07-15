import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from feature_engineering import preprocess_transactions, aggregate_wallet_features

# making sure output directory exists
os.makedirs("output", exist_ok=True)

scores = pd.read_csv("output/wallet_scores.csv")
with open("data/user-wallet-transactions.json", "r") as f:
    data = json.load(f)

features = aggregate_wallet_features(preprocess_transactions(data))
merged = pd.merge(features, scores, left_on="userWallet", right_on="wallet")

print("Score Range:", scores['score'].min(), "-", scores['score'].max())
print("Score Std Dev:", scores['score'].std())

#Correlation Matrix - Heatmap
corr = merged.drop(columns=["userWallet", "wallet"]).corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr[['score']].sort_values('score', ascending=False), annot=True, cmap="coolwarm")
plt.title("Feature Correlation with Credit Score")
plt.tight_layout()
plt.savefig("output/feature_score_correlation.png")
plt.close()

# Score Distribution Plot
plt.figure(figsize=(8, 4))
sns.histplot(scores['score'], bins=20, kde=True, color='skyblue')
sns.kdeplot(scores['score'], color='red')
plt.title("Wallet Credit Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/score_distribution.png")
plt.close()

# Top & Bottom Wallets
print("Lowest Score Wallets:\n", scores.sort_values('score').head(5))
print("\nHighest Score Wallets:\n", scores.sort_values('score', ascending=False).head(5))
