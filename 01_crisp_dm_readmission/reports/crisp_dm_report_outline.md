# CRISP-DM report outline

## Executive summary

State the readmission problem, dataset, best model, clinically relevant metrics, limitations, and intended operational use.

## 1. Business Understanding

- Stakeholders and decision point.
- Business objective and data-mining objective.
- Success criteria: useful recall/precision trade-off, calibrated risk, and acceptable subgroup performance.
- Constraints: historical data, class imbalance, privacy, no clinical deployment claim.
- Project risks and mitigation plan.

## 2. Data Understanding

- Source, population, time period, and licensing.
- Data dictionary.
- Row/column counts and data types.
- Missingness and placeholder values.
- Target distribution.
- EDA figures and observations.

## 3. Data Preparation

- Patient-grouped train/test split.
- Identifier and leakage review.
- Missing-value treatment.
- Categorical encoding and numeric scaling.
- Feature engineering decisions.
- Reproducibility and pipeline design.

## 4. Modeling

- Baseline definition.
- Logistic regression.
- Random forest.
- Hyperparameter choices.
- Cross-validation strategy.

## 5. Evaluation

- ROC-AUC and PR-AUC.
- Recall, precision, F1, and confusion matrix.
- Threshold analysis.
- Calibration.
- Subgroup analysis where sample sizes allow.
- Error analysis and business interpretation.

## 6. Deployment

- Proposed scoring workflow.
- Human review and intervention policy.
- Monitoring for drift, calibration, missingness, and subgroup performance.
- Retraining and rollback plan.
- Model card and limitations.

## Conclusion

Answer the original business question and state what additional data or validation would be required before real-world use.
