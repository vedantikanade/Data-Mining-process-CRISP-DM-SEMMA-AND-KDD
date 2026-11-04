# Healthcare Data Mining: CRISP-DM, SEMMA, and KDD

This repository contains three separate healthcare data-mining projects. Each project uses a different methodology and a different dataset.

## Projects and exact CSV files

| Project folder | Methodology | Colab notebook | CSV file to upload | Objective |
|---|---|---|---|---|
| `01_CRISP_DM_Diabetes_Readmission` | CRISP-DM | `01_crisp_dm_diabetes_readmission.ipynb` | `diabetic_data.csv` | Predict 30-day diabetic hospital readmission |
| `02_semma_heart_disease` | SEMMA | `02_semma_heart_disease.ipynb` | `heart.csv` or `heart_disease.csv` | Predict presence of heart disease |
| `03_kdd_chronic_kidney_disease` | KDD | `03_kdd_chronic_kidney_disease.ipynb` | `kidney_disease.csv` or `chronic_kidney_disease.csv` | Classify CKD and discover clusters |

## Required links

### CRISP-DM: Diabetes readmission

- Dataset: [Kaggle Diabetes 130-US Hospitals](https://www.kaggle.com/brandao/diabetes/code)
- Official documentation: [UCI Diabetes 130-US Hospitals](https://archive.ics.uci.edu/dataset/296/diabetes+130+us+hospitals+for+years+1999+2008)
- Notebook: `01_CRISP_DM_Diabetes_Readmission/notebooks/01_crisp_dm_diabetes_readmission.ipynb`

### SEMMA: Heart disease

- Dataset: [Kaggle Heart Disease Classification](https://www.kaggle.com/c/heart-disease-uci)
- Official documentation: [UCI Heart Disease](https://uci-ics-mlr-prod.aws.uci.edu/dataset/45/heart%2Bdisease)
- Notebook: `02_semma_heart_disease/notebooks/02_semma_heart_disease.ipynb`

### KDD: Chronic kidney disease

- Dataset: [Kaggle Chronic Kidney Disease](https://www.kaggle.com/mansoordaku/ckdisease/tasks)
- Notebook: `03_kdd_chronic_kidney_disease/notebooks/03_kdd_chronic_kidney_disease.ipynb`

## Execution instructions

Follow [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md) for the complete Colab procedure, including which CSV to upload, how to run all cells, how to download the executed notebook, and how to upload it to GitHub.

## Submission links

Add the final published links here after completing the articles and videos:

- CRISP-DM Medium article: `[Add Medium article URL here]`
- CRISP-DM YouTube walkthrough: `[Add YouTube URL here]`
- SEMMA Medium article: `[Add Medium article URL here]`
- SEMMA YouTube walkthrough: `[Add YouTube URL here]`
- KDD Medium article: `[Add Medium article URL here]`
- KDD YouTube walkthrough: `[Add YouTube URL here]`

## Responsible-use note

These datasets are historical and educational. The resulting models are not medical devices and must not be used for diagnosis or treatment decisions.

Raw datasets are intentionally excluded from GitHub. Only notebooks, code, documentation, and generated non-sensitive artifacts should be committed.
