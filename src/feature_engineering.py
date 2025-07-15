import pandas as pd
import numpy as np

def preprocess_transactions(transactions):
    df = pd.json_normalize(transactions)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['amount_usd'] = df['actionData.amount'].astype(float) * df['actionData.assetPriceUSD'].astype(float)
    return df

def aggregate_wallet_features(df):
    grouped = df.groupby('userWallet')

    features = pd.DataFrame()
    features['num_transactions'] = grouped.size()
    features['num_deposits'] = grouped.apply(lambda g: (g['action'] == 'deposit').sum())
    features['num_borrows'] = grouped.apply(lambda g: (g['action'] == 'borrow').sum())
    features['num_repays'] = grouped.apply(lambda g: (g['action'] == 'repay').sum())
    features['num_redeems'] = grouped.apply(lambda g: (g['action'] == 'redeemUnderlying').sum())

    features['total_deposit_usd'] = grouped.apply(lambda g: g[g['action'] == 'deposit']['amount_usd'].sum())
    features['total_borrow_usd'] = grouped.apply(lambda g: g[g['action'] == 'borrow']['amount_usd'].sum())
    features['total_repay_usd'] = grouped.apply(lambda g: g[g['action'] == 'repay']['amount_usd'].sum())

    features['deposit_to_borrow_ratio'] = features['total_deposit_usd'] / (features['total_borrow_usd'] + 1e-9)
    features['repay_ratio'] = features['total_repay_usd'] / (features['total_borrow_usd'] + 1e-9)

    features['activity_span_days'] = grouped['timestamp'].apply(lambda x: (x.max() - x.min()).days + 1)
    features['tx_frequency'] = features['num_transactions'] / (features['activity_span_days'] + 1)

    features['unique_assets'] = grouped['actionData.assetSymbol'].nunique()

    features = features.fillna(0)
    return features.reset_index()