import io

import pandas as pd
import pytest
from data_analysis import load_data, basic_eda


# --------------------------------------------------
# load_data() tests
# --------------------------------------------------

def test_load_csv():
    file = io.BytesIO(
        b"name,age,salary\nAkash,21,50000\nRahul,22,60000"
    )
    file.name = "test.csv"

    df = load_data(file)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 3)
    assert list(df.columns) == ["name", "age", "salary"]


def test_load_xlsx(tmp_path):
    file_path = tmp_path / "test.xlsx"

    original_df = pd.DataFrame({
        "name": ["Akash", "Rahul"],
        "age": [21, 22],
        "salary": [50000, 60000],
    })

    original_df.to_excel(file_path, index=False)

    with open(file_path, "rb") as file:
        df = load_data(file)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 3)
    assert list(df.columns) == ["name", "age", "salary"]


def test_load_data_converts_missing_values():
    file = io.BytesIO(
        b"name,age,salary\nAkash,NA,50000\nRahul,22,N/A\nAman,missing,60000"
    )
    file.name = "test.csv"

    df = load_data(file)

    assert df["age"].isna().sum() == 2
    assert df["salary"].isna().sum() == 1


def test_load_data_invalid_file():
    file = io.BytesIO(b"some data")
    file.name = "test.txt"

    with pytest.raises(
        ValueError,
        match="Only CSV and XLSX files are supported."
    ):
        load_data(file)


# --------------------------------------------------
# basic_eda() tests
# --------------------------------------------------

def test_basic_eda_returns_correct_shape():
    df = pd.DataFrame({
        "name": ["Akash", "Rahul", "Aman"],
        "age": [21, 22, 23],
        "salary": [50000, 60000, 70000],
    })

    result = basic_eda(df)

    assert result["rows"] == 3
    assert result["columns"] == 3


def test_detect_numerical_columns():
    df = pd.DataFrame({
        "name": ["Akash", "Rahul"],
        "age": [21, 22],
        "salary": [50000, 60000],
    })

    result = basic_eda(df)

    assert result["numerical_columns"] == ["age", "salary"]


def test_detect_categorical_columns():
    df = pd.DataFrame({
        "name": ["Akash", "Rahul"],
        "age": [21, 22],
        "department": ["IT", "HR"],
    })

    result = basic_eda(df)

    assert result["categorical_columns"] == [
        "name",
        "department",
    ]


def test_missing_values():
    df = pd.DataFrame({
        "age": [21, None, 23],
        "salary": [50000, 60000, None],
    })

    result = basic_eda(df)

    assert result["missing_values"] == {
        "age": 1,
        "salary": 1,
    }


def test_missing_values_are_sorted_descending():
    df = pd.DataFrame({
        "age": [None, None, 23],
        "salary": [50000, None, None],
        "bonus": [1000, 2000, 3000],
    })

    result = basic_eda(df)

    assert list(result["missing_values"].keys()) == [
        "age",
        "salary",
    ]


def test_duplicate_rows():
    df = pd.DataFrame({
        "name": ["Akash", "Rahul", "Rahul", "Aman"],
        "age": [21, 22, 22, 23],
    })

    result = basic_eda(df)

    assert result["duplicate_rows"] == 1


def test_statistics():
    df = pd.DataFrame({
        "age": [10, 20, 30, 40, 50],
    })

    result = basic_eda(df)

    statistics = result["statistics"]

    assert statistics["age"]["count"] == 5.0
    assert statistics["age"]["mean"] == 30.0
    assert statistics["age"]["min"] == 10.0
    assert statistics["age"]["max"] == 50.0


def test_statistics_are_rounded_to_two_decimals():
    df = pd.DataFrame({
        "value": [1, 2, 4],
    })

    result = basic_eda(df)

    statistics = result["statistics"]

    assert statistics["value"]["mean"] == 2.33


def test_correlation():
    df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [2, 4, 6, 8, 10],
    })

    result = basic_eda(df)

    correlation = result["correlation"]

    assert correlation["x"]["y"] == 1.0
    assert correlation["y"]["x"] == 1.0


def test_no_correlation_with_one_numerical_column():
    df = pd.DataFrame({
        "name": ["A", "B", "C"],
        "age": [20, 25, 30],
    })

    result = basic_eda(df)

    assert result["correlation"] == {}


# --------------------------------------------------
# Edge cases
# --------------------------------------------------

def test_no_missing_values():
    df = pd.DataFrame({
        "age": [20, 25, 30],
        "salary": [30000, 40000, 50000],
    })

    result = basic_eda(df)

    assert result["missing_values"] == {}


def test_no_duplicate_rows():
    df = pd.DataFrame({
        "age": [20, 25, 30],
        "salary": [30000, 40000, 50000],
    })

    result = basic_eda(df)

    assert result["duplicate_rows"] == 0


def test_no_numerical_columns():
    df = pd.DataFrame({
        "name": ["Akash", "Rahul", "Aman"],
        "department": ["IT", "HR", "Finance"],
    })

    result = basic_eda(df)

    assert result["numerical_columns"] == []
    assert result["statistics"] == {}
    assert result["correlation"] == {}


def test_empty_dataframe():
    df = pd.DataFrame()

    result = basic_eda(df)

    assert result["rows"] == 0
    assert result["columns"] == 0
    assert result["numerical_columns"] == []
    assert result["categorical_columns"] == []
    assert result["missing_values"] == {}
    assert result["duplicate_rows"] == 0
    assert result["statistics"] == {}
    assert result["correlation"] == {}