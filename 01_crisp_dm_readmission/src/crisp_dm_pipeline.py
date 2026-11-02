"""Reproducible CRISP-DM pipeline for diabetic 30-day readmission.

Place the downloaded UCI/Kaggle file at:
    data/raw/diabetic_data.csv

The script intentionally does not download data or commit patient-level records.
Run it from the project directory after installing the repository requirements.
"""

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    RocCurveDisplay,
)
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_DIR / "data" / "raw" / "diabetic_data.csv"
ARTIFACT_DIR = PROJECT_DIR / "artifacts"
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)


def load_and_prepare(path: Path) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    """Load the raw data and define a leakage-aware modeling table."""
    df = pd.read_csv(path, na_values=["?"])
    if "readmitted" not in df.columns:
        raise ValueError("Expected a readmitted column in the raw dataset")
    if "patient_nbr" not in df.columns:
        raise ValueError("Expected patient_nbr for grouped leakage prevention")

    y = (df["readmitted"].astype(str) == "<30").astype(int)
    groups = df["patient_nbr"].copy()

    # Identifiers and post-outcome fields are excluded from predictors.
    drop_columns = [
        "readmitted",
        "encounter_id",
        "patient_nbr",
        "weight",
        "payer_code",
        "medical_specialty",
    ]
    X = df.drop(columns=[c for c in drop_columns if c in df.columns]).copy()

    # Treat the age bands as ordered categories rather than arbitrary numbers.
    if "age" in X.columns:
        X["age"] = X["age"].astype("string")
    return X, y, groups


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    numeric = X.select_dtypes(include=["number"]).columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]

    numeric_pipe = Pipeline(
        [
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]
    )
    categorical_pipe = Pipeline(
        [
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    return ColumnTransformer(
        [
            ("numeric", numeric_pipe, numeric),
            ("categorical", categorical_pipe, categorical),
        ],
        remainder="drop",
    )


def evaluate(name: str, pipeline: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    probabilities = pipeline.predict_proba(X_test)[:, 1]
    predictions = (probabilities >= 0.5).astype(int)
    report = classification_report(y_test, predictions, output_dict=True)
    result = {
        "model": name,
        "roc_auc": roc_auc_score(y_test, probabilities),
        "average_precision": average_precision_score(y_test, probabilities),
        "positive_recall_at_0.5": report["1"]["recall"],
        "positive_precision_at_0.5": report["1"]["precision"],
    }
    pd.DataFrame(confusion_matrix(y_test, predictions)).to_csv(
        ARTIFACT_DIR / f"confusion_matrix_{name}.csv", index=False
    )
    return result


def main() -> None:
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            f"Download diabetic_data.csv and place it at {RAW_PATH}"
        )

    X, y, groups = load_and_prepare(RAW_PATH)
    split = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    train_idx, test_idx = next(split.split(X, y, groups=groups))
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    preprocessor = build_preprocessor(X_train)
    models = {
        "logistic_regression": LogisticRegression(
            max_iter=1000, class_weight="balanced", random_state=42
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=300,
            class_weight="balanced_subsample",
            min_samples_leaf=5,
            random_state=42,
            n_jobs=-1,
        ),
    }

    results = []
    fitted = {}
    for name, model in models.items():
        pipeline = Pipeline([("preprocess", preprocessor), ("model", model)])
        pipeline.fit(X_train, y_train)
        results.append(evaluate(name, pipeline, X_test, y_test))
        fitted[name] = pipeline

    results_df = pd.DataFrame(results).sort_values("average_precision", ascending=False)
    results_df.to_csv(ARTIFACT_DIR / "model_comparison.csv", index=False)

    best_name = results_df.iloc[0]["model"]
    joblib.dump(fitted[best_name], ARTIFACT_DIR / "best_readmission_pipeline.joblib")

    RocCurveDisplay.from_predictions(
        y_test,
        fitted[best_name].predict_proba(X_test)[:, 1],
        name=best_name,
    )
    plt.title("CRISP-DM readmission model: ROC curve")
    plt.tight_layout()
    plt.savefig(ARTIFACT_DIR / "roc_curve.png", dpi=180)
    plt.close()

    print(results_df.to_string(index=False))


if __name__ == "__main__":
    main()
