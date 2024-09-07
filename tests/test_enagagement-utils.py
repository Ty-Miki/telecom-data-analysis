import pytest
import pandas as pd
import numpy as np

from scripts.enagagement_utils import normalize_data
from scripts.enagagement_utils import cluster_data
from scripts.enagagement_utils import convert_bytes_to_gigabytes
from scripts.enagagement_utils import convert_milliseconds_to_minutes

def test_normalize_data_success():
    df = pd.DataFrame({
        'Metric1': [10, 20, 30, 40, 50],
        'Metric2': [100, 200, 300, 400, 500]
    })

    result = normalize_data(df)
    
    # Ensure the result is a NumPy array
    assert isinstance(result, np.ndarray)
    
    # Ensure the result has the same number of elements as rows in the DataFrame
    assert result.shape == df.shape
    
    # Ensure the values are scaled between 0 and 1
    assert result.min() >= 0.0 and result.max() <= 1.0

def test_normalize_data_failure():
    # Creating an invalid DataFrame (e.g., with non-numeric data) to simulate failure
    df = pd.DataFrame({
        'Metric1': [10, 20, 30, 'a', 50],  # 'a' is non-numeric
        'Metric2': [100, 200, 300, 400, 500]
    })

    result = normalize_data(df)
    
    # Ensure the function returns None on failure
    assert result is None

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

def test_convert_bytes_to_gigabytes_success():
    df = pd.DataFrame({
        'SizeInBytes': [1073741824, 2147483648, 3221225472],  # 1GB, 2GB, 3GB in bytes
    })

    result = convert_bytes_to_gigabytes(df, 'SizeInBytes', 'SizeInGB')
    
    # Ensure the function returns a DataFrame
    assert isinstance(result, pd.DataFrame)
    
    # Check if the new column exists and the old one is removed
    assert 'SizeInGB' in result.columns
    assert 'SizeInBytes' not in result.columns
    
    # Ensure the conversion is correct
    assert result['SizeInGB'].tolist() == [1.0, 2.0, 3.0]

def test_convert_bytes_to_gigabytes_column_not_found():
    df = pd.DataFrame({
        'SizeInBytes': [1073741824, 2147483648, 3221225472],  # 1GB, 2GB, 3GB in bytes
    })

    # Test with a non-existing column name
    result = convert_bytes_to_gigabytes(df, 'NonExistingColumn', 'SizeInGB')
    
    # Ensure the function returns None on failure
    assert result is None

def test_convert_bytes_to_gigabytes_failure():
    # Create a DataFrame with non-numeric data
    df = pd.DataFrame({
        'SizeInBytes': ['1GB', '2GB', '3GB'],
    })

    result = convert_bytes_to_gigabytes(df, 'SizeInBytes', 'SizeInGB')
    
    # Ensure the function returns None on failure
    assert result is None


def test_convert_milliseconds_to_minutes_success():
    df = pd.DataFrame({
        'TimeInMilliSeconds': [3600000, 7200000, 10800000],  # 60 mins, 120 mins , 180 mins in milliseconds
    })

    result = convert_milliseconds_to_minutes(df, 'TimeInMilliSeconds', 'TimeInMinutes')
    
    # Ensure the function returns a DataFrame
    assert isinstance(result, pd.DataFrame)
    
    # Check if the new column exists and the old one is removed
    assert 'TimeInMinutes' in result.columns
    assert 'TimeInMilliSeconds' not in result.columns
    
    # Ensure the conversion is correct
    assert result['TimeInMinutes'].tolist() == [60.0, 120.0, 180.0]

def test_convert_milliseconds_to_minutes_column_not_found():
    df = pd.DataFrame({
        'TimeInMilliSeconds': [36000, 72000, 108000],  # 60 mins, 120 mins , 180 mins in milliseconds
    })

    # Test with a non-existing column name
    result = convert_milliseconds_to_minutes(df, 'NonExistingColumn', 'TimeInMilliSeconds')
    
    # Ensure the function returns None on failure
    assert result is None

def test_convert_milliseconds_to_minutes_failure():
    # Create a DataFrame with non-numeric data
    df = pd.DataFrame({
        'TimeInMilliSeconds': ['1 min', '2 min', '3 min'],
    })

    result = convert_milliseconds_to_minutes(df, 'TimeInMilliSeconds', 'TimeInHours')
    
    # Ensure the function returns None on failure
    assert result is None