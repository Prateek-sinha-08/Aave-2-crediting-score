# Wallet Credit Score Analysis

In this section, we provides a simple summary of how wallets performed based on their credit scores and what the scores imply about their behavior.

## Score Distribution and Wallet Behavior

After running the scoring model, we found that most wallet scores ranged from 300 to 950 that is a large number of wallets had scores between 300 and 400. These wallets generally showed very limited or no repayments, few transactions, and short activity durations. They may be inactive wallets, test addresses, or bots with minimal interaction.

As scores increased toward 500 and 600, wallets started showing slightly more responsible behavior, such as occasional repayments and slightly longer activity periods. However, they still lacked consistent transaction history.

Wallets that scored between 600 and 800 demonstrated better habits. These wallets often had steady deposits, fair repayment ratios, and interactions with multiple assets or pools. They likely represent low-risk users who actively engage with the Aave protocol.

The highest scores (above 800) were assigned to wallets that consistently deposited, borrowed, and repaid over long periods. These wallets had excellent repayment-to-borrow ratios, used a variety of assets, and were active for many months. They are the most reliable and trustworthy users based on historical behavior.

A histogram was generated to visually show how wallet scores were distributed across these ranges. Most wallets clustered in the lower score ranges, while fewer reached the highest tiers.

This analysis confirms that the scoring model successfully captures wallet behavior and assigns scores that reflect financial responsibility in the DeFi ecosystem.

