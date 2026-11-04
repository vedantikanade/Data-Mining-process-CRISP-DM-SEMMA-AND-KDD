# Complete Google Colab execution guide

Run the three projects separately. Do not upload raw CSV files to GitHub.

## Before starting

1. Open the repository on GitHub.
2. Open the required notebook.
3. Click **Open in Colab**. If that button is not shown, open [Google Colab](https://colab.research.google.com/), choose **GitHub**, enter the repository name, and select the notebook.
4. In Colab, choose **Runtime → Run all** only after uploading the correct CSV.

If package installation is needed, run this once at the top of the notebook:

```python
!pip install -q pandas numpy scikit-learn matplotlib seaborn joblib
```

## Project 1 — CRISP-DM

### Notebook

```text
01_CRISP_DM_Diabetes_Readmission/notebooks/01_crisp_dm_diabetes_readmission.ipynb
```

### CSV required

```text
diabetic_data.csv
```

Download it from the [Kaggle Diabetes 130-US Hospitals dataset](https://www.kaggle.com/brandao/diabetes/code) or the [official UCI source](https://archive.ics.uci.edu/dataset/296/diabetes+130+us+hospitals+for+years+1999+2008).

### Execution steps

1. Open the CRISP-DM notebook in Colab.
2. Click the folder icon on the left.
3. Click the upload icon.
4. Upload `diabetic_data.csv`.
5. Confirm that the file appears at `/content/diabetic_data.csv`.
6. Select **Runtime → Run all**.
7. Confirm that the notebook displays the dataset profile, target distribution, model comparison, ROC/precision-recall curves, classification report, confusion matrix, and threshold table.
8. The notebook also creates model and chart artifacts in `/content/artifacts/`.

## Project 2 — SEMMA

### Notebook

```text
02_semma_heart_disease/notebooks/02_semma_heart_disease.ipynb
```

### CSV required

Use one of these names:

```text
heart.csv
heart_disease.csv
```

Download the [Kaggle Heart Disease Classification dataset](https://www.kaggle.com/c/heart-disease-uci) or the [official UCI Heart Disease dataset](https://uci-ics-mlr-prod.aws.uci.edu/dataset/45/heart%2Bdisease).

### Execution steps

1. Open the SEMMA notebook in Colab.
2. Upload `heart.csv` or `heart_disease.csv` using the folder pane.
3. Confirm the file appears under `/content/`.
4. Select **Runtime → Run all**.
5. Confirm that Sample outputs the stratified train/test split.
6. Confirm that Explore outputs missingness, target distribution, and correlation analysis.
7. Confirm that Modify creates the preprocessing pipeline.
8. Confirm that Model/Assess outputs comparisons for logistic regression, decision tree, random forest, and SVM.
9. Confirm that the confusion matrix and serialized best pipeline are created under `/content/artifacts/`.

## Project 3 — KDD

### Notebook

```text
03_kdd_chronic_kidney_disease/notebooks/03_kdd_chronic_kidney_disease.ipynb
```

### CSV required

Use one of these names:

```text
kidney_disease.csv
chronic_kidney_disease.csv
```

Download the [Kaggle Chronic Kidney Disease dataset](https://www.kaggle.com/mansoordaku/ckdisease/tasks).

### Execution steps

1. Open the KDD notebook in Colab.
2. Upload `kidney_disease.csv` or `chronic_kidney_disease.csv` using the folder pane.
3. Confirm the file appears under `/content/`.
4. Select **Runtime → Run all**.
5. Confirm that Selection identifies the target and removes the ID field.
6. Confirm that Preprocessing displays missingness and performs type cleanup.
7. Confirm that Transformation creates the encoded/scaled feature matrix and two-dimensional projection.
8. Confirm that Data Mining outputs classifier metrics and K-means clusters.
9. Confirm that the confusion matrix, projection charts, clustering chart, and serialized best pipeline are created under `/content/artifacts/`.

## How to verify successful execution

Every code cell should finish without a red error message. The notebook should visibly contain:

- tables;
- charts;
- model metrics;
- confusion matrices;
- methodology-specific analysis;
- responsible-use notes.

If a cell fails, read the error message before continuing. The most common cause is an incorrect CSV filename or a dataset with different column names.

## Download the executed notebooks

After a notebook finishes:

1. Choose **File → Download → Download .ipynb**.
2. Rename the downloaded file to the project notebook name if necessary.
3. Replace the matching notebook in the repository.
4. Confirm that the downloaded notebook contains visible cell outputs.

The outputs are embedded inside the `.ipynb` file and will be visible in Colab and when GitHub renders the notebook.

## Upload executed notebooks later

After downloading the executed notebooks, copy them into:

```text
01_CRISP_DM_Diabetes_Readmission/notebooks/
02_semma_heart_disease/notebooks/
03_kdd_chronic_kidney_disease/notebooks/
```

Then commit and push them. Do not upload the raw CSV files.
