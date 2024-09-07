import pytest
import pandas as pd
import numpy as np

from scripts.enagagement_utils import normalize_data
from scripts.enagagement_utils import cluster_data

def test_normalize_data_success():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })
    columns = ['A', 'B']
    
    result = normalize_data(df, columns)
    
    # Expect values to be scaled between 0 and 1
    expected = pd.DataFrame({
        'A': [0.0, 0.25, 0.5, 0.75, 1.0],
        'B': [0.0, 0.25, 0.5, 0.75, 1.0]
    })
    
    pd.testing.assert_frame_equal(result, expected)

def test_normalize_data_missing_column():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })
    columns = ['A', 'C']  # 'C' does not exist in df

    result = normalize_data(df, columns)
    
    # Expect an empty DataFrame with specified columns
    expected = pd.DataFrame(columns=columns)
    
    pd.testing.assert_frame_equal(result, expected)

def test_cluster_data_success():
    df = pd.DataFrame({
        'Metric1': [0.0, 0.25, 0.5, 0.75, 1.0],
        'Metric2': [0.0, 0.25, 0.5, 0.75, 1.0]
    })

    result = cluster_data(df)
    
    # Ensure the result is a NumPy array
    assert isinstance(result, np.ndarray)
    
    # Ensure the result has the same number of elements as rows in the DataFrame
    assert len(result) == len(df)
    
    # Ensure there are 3 unique clusters
    assert len(set(result)) == 3

def test_cluster_data_failure():
    df = pd.DataFrame({
        'Metric1': [0.0, 0.25, 0.5, 0.75, 1.0],
        'Metric2': [0.0, 0.25, 0.5, 0.75, 1.0]
    })

    # Simulate failure by passing an incorrect number of clusters (e.g., -1)
    result = cluster_data(df, n_clusters=-1)
    
    # Ensure the function returns None on failure
    assert result is None