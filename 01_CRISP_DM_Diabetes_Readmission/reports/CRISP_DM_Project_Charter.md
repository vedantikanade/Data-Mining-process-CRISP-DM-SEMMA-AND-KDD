# CRISP-DM Project Charter

## Project title

Predicting 30-Day Diabetic Hospital Readmission

## Problem statement

Hospital readmissions are an important operational and patient-care concern. This project studies whether historical encounter-level information can identify diabetic encounters associated with readmission within 30 days.

## Business objective

Support prioritization of post-discharge follow-up and care-management resources.

## Data-mining objective

Build and evaluate a probability-based binary classifier for the `<30` readmission outcome.

## Success criteria

- Compare at least two modeling approaches.
- Report PR-AUC, ROC-AUC, precision, recall, F1-score, and calibration-related observations.
- Use a patient-grouped split to reduce leakage risk.
- Explain threshold trade-offs and operational implications.
- Document limitations, responsible-use constraints, and a monitoring plan.

## Scope exclusions

- No diagnosis or treatment recommendation.
- No claim of clinical validity.
- No use of raw patient-level data in Git history.
- No causal interpretation of predictive associations.

## Initial risks

- Severe class imbalance.
- Missing values may reflect workflow or access patterns.
- Multiple encounters may belong to the same patient.
- Historical data may not represent current clinical practice.
- A high-performing model may still be poorly calibrated or operationally impractical.
