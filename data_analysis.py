import pandas as pd
import numpy as np


def load_data(file):
    """Load CSV or Excel file."""

    if file.name.endswith(".csv"):
        df = pd.read_csv(
            file,
            na_values=["NA", "N/A", "missing"]
        )

    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(
            file,
            na_values=["NA", "N/A", "missing"]
        )

    else:
        raise ValueError("Only CSV and XLSX files are supported.")

    return df


def basic_eda(df):
    """Generate basic EDA information."""

    # Separate columns
    numerical = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    categorical = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    # Missing values
    missing = df.isnull().sum()

    missing = missing[missing > 0].sort_values(
        ascending=False
    )

    # Duplicates
    duplicates = int(df.duplicated().sum())

    # Statistics
    statistics = df[numerical].describe().round(2)

    # Correlation
    correlation = pd.DataFrame()

    if len(numerical) > 1:
        correlation = df[numerical].corr().round(2)

    # Basic summary
    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numerical_columns": numerical,
        "categorical_columns": categorical,
        "missing_values": missing.to_dict(),
        "duplicate_rows": duplicates,
        "statistics": statistics.to_dict(),
        "correlation": correlation.to_dict(),
    }

    return summary