import pytest
from unittest.mock import patch, Mock
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scripts.data_processing import MissingValueHandler

def test_missing_value_summary():
    df = pd.DataFrame({'A': [1, None, 3], 'B': [None, None, 3]})
    handler = MissingValueHandler(df)
    result = handler.missing_value_summary()
    expected = pd.Series({'A': 1, 'B': 2})
    assert result.equals(expected)

def test_missing_value_percentage():
    df = pd.DataFrame({'A': [1, None, 3], 'B': [None, None, 3]})
    handler = MissingValueHandler(df)
    result = handler.missing_value_percentage()
    expected = pd.Series({'A': 1 / 3 * 100, 'B': 2 / 3 * 100})
    assert result.equals(expected)

@patch('scripts.data_processing.plt.show')
def test_missing_values_heatmap(mock_show):
    df = pd.DataFrame({'A': [1, None, 3], 'B': [None, None, 3]})
    handler = MissingValueHandler(df)
    handler.missing_values_heatmap()
    mock_show.assert_called_once()

def test_describe_numeric_columns():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    handler = MissingValueHandler(df)
    result = handler.describe_numeric_columns()
    expected = df.describe()
    assert result.equals(expected)

def test_value_counts_categorical():
    df = pd.DataFrame({'A': ['cat', 'dog', 'cat']})
    handler = MissingValueHandler(df)
    result = handler.value_counts_categorical('A')
    expected = pd.Series({'cat': 2, 'dog': 1})
    assert result.equals(expected)

def test_correlation_matrix():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    handler = MissingValueHandler(df)
    result = handler.correlation_matrix()
    expected = df.corr()
    assert result.equals(expected)

@patch('scripts.data_processing.plt.show')
def test_inspect_outliers(mock_show):
    df = pd.DataFrame({'A': [1, 2, 3, 100]})
    handler = MissingValueHandler(df)
    handler.inspect_outliers()
    mock_show.assert_called_once()
