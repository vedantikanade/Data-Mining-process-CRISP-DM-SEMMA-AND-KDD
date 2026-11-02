# CRISP-DM: Predicting 30-Day Diabetic Hospital Readmission

## Business understanding

Hospitals want to identify encounters with elevated risk of readmission within 30 days so care-management teams can prioritize discharge planning and follow-up resources.

The model is a decision-support prototype, not a clinical diagnostic system. The analysis will emphasize recall, calibration, subgroup performance, leakage prevention, and operational usefulness rather than accuracy alone.

## Dataset

**Diabetes 130-US Hospitals for Years 1999–2008**

- Official source: UCI Machine Learning Repository, dataset 296.
- Kaggle mirror: Diabetes 130 US hospitals for years 1999–2008.
- Expected raw file: `diabetic_data.csv`.
- Target: `readmitted`, converted to a binary target where `<30` means readmitted within 30 days.

Download the data manually or with Kaggle credentials and place the file at `data/raw/diabetic_data.csv`. Do not commit the raw data.

## CRISP-DM deliverables

1. Business Understanding: stakeholders, objectives, constraints, risks, and success criteria.
2. Data Understanding: schema, data dictionary, quality profile, missingness, target balance, and EDA.
3. Data Preparation: leakage-safe split, missing-value policy, encoding, feature engineering, and reproducible preprocessing pipeline.
4. Modeling: baseline, logistic regression, tree ensemble, and calibrated probability model.
5. Evaluation: ROC-AUC, PR-AUC, recall, precision, calibration, confusion matrix, subgroup checks, and threshold analysis.
6. Deployment: scoring workflow, monitoring plan, model card, limitations, and a prototype dashboard/API design.

## Planned artifacts

- Executed Colab notebook.
- Cleaned-data schema and data dictionary.
- EDA figures and model comparison table.
- Final model and preprocessing pipeline.
- Model card and deployment/monitoring plan.
- Medium article and walkthrough video script.
