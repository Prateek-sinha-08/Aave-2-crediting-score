# DeFi Credit Scoring using Aave V2 Data

## Solution

Here, We developed a Machine Learning wallet credit scoring system using historical transaction-level data from the Aave V2 protocol. The goal was to assign a credit score (300–950) that reflects a wallet's financial responsibility and reliability based on its behavioral patterns.

## Scoring Logic

As no labeled data (i.e., defaults, real credit scores) were available, we derived a *synthetic target score* using behavior-driven heuristics. These heuristics reflect what would be considered trustworthy actions in a DeFi ecosystem:

* *Repayment Ratio*: Total repaid / total borrowed — measures responsibility.
* *Deposit-to-Borrow Ratio*: Higher values indicate lower dependency on borrowed capital.
* *Activity Duration*: Wallets active over longer periods show more stability.
* *Transaction Frequency*: More frequent interaction implies engaged users.
* *Total Deposits in USD*: Reflects the economic footprint of a wallet.

These factors were combined and scaled to produce a pseudo-score, which was then applied on the `RandomForestRegressor`. This model learns non-linear relationships between features and the synthetic score, and using that generates the final wallet scores.

## Model Highlights

* *Algorithm*: Random Forest Regressor
* *Score Range*: 300 to 950
* *Features Used*: Repayment, deposit behavior, frequency, diversity, and longevity
* *Validation*: Correlation heatmap, score distribution, and case audits were conducted to ensure logical output.

This modular approach supports future improvements:

* Incorporate real labels (e.g., liquidations)
* Extend to other DeFi protocols
* Replace with more advanced models (e.g., XGBoost)

The full scoring pipeline is implemented in [score_wallets.py] and the model validation can be done via [validate_model.py].
