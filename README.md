# Healthcare Data Mining: CRISP-DM, SEMMA, and KDD

This repository contains three separate healthcare data-mining projects. Each project uses a different methodology and dataset.

## Projects

| Project | Methodology | Dataset | Objective |
|---|---|---|---|
| `01_crisp_dm_readmission` | CRISP-DM | Diabetes 130-US Hospitals | Predict 30-day hospital readmission |
| `02_semma_heart_disease` | SEMMA | Cleveland Heart Disease | Predict presence of heart disease |
| `03_kdd_chronic_kidney_disease` | KDD | Chronic Kidney Disease | Discover and classify kidney-disease patterns |

## Repository map

```text
01_crisp_dm_readmission/
  README.md
  notebooks/
  reports/
  artifacts/
02_semma_heart_disease/
  README.md
  notebooks/
  reports/
  artifacts/
03_kdd_chronic_kidney_disease/
  README.md
  notebooks/
  reports/
  artifacts/
shared/
  data_dictionary_template.md
  model_card_template.md
  responsible_ai_checklist.md
medium-articles/
walkthrough-scripts/
```

The raw datasets are intentionally not committed. Each project README documents the source, download procedure, license, and expected filename.

## Responsible-use note

These datasets are historical and educational. The resulting models are not medical devices and must not be used for diagnosis or treatment decisions.
