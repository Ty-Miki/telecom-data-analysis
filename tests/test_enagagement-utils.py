import pytest
import pandas as pd
import numpy as np

from scripts.enagagement_utils import normalize_data
from scripts.enagagement_utils import cluster_data
from scripts.enagagement_utils import convert_bytes_to_gigabytes
from scripts.enagagement_utils import convert_milliseconds_to_minutes
from scripts.enagagement_utils import calculate_total_data_per_app

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

def test_calculate_total_data_success():
    # Sample DataFrame with downlink (DL) and uplink (UL) data for multiple applications
    data = {
        'MSISDN/Number': ['12345', '67890', '12345'],
        'Social Media DL (Bytes)': [1000, 2000, 1500],
        'Social Media UL (Bytes)': [500, 1000, 800],
        'Google DL (Bytes)': [2000, 2500, 3000],
        'Google UL (Bytes)': [1000, 1200, 1400],
    }
    df = pd.DataFrame(data)
    
    applications = ['Social Media', 'Google']
    
    # Call the function
    result = calculate_total_data_per_app(df, applications)
    
    # Check that the result is a DataFrame
    assert isinstance(result, pd.DataFrame)
    
    # Check that the new columns exist
    assert 'Social Media Total Data (Bytes)' in result.columns
    assert 'Google Total Data (Bytes)' in result.columns
    
    # Check that the grouping and summing is correct
    expected_data = {
        'MSISDN/Number': ['12345', '67890'],
        'Social Media Total Data (Bytes)': [3800, 3000],  # 1000+500 + 1500+800 for '12345' and 2000+1000 for '67890'
        'Google Total Data (Bytes)': [7400, 3700],  # 2000+1000 + 3000+1400 for '12345' and 2500+1200 for '67890'
    }
    expected_df = pd.DataFrame(expected_data)
    
    pd.testing.assert_frame_equal(result, expected_df)

def test_calculate_total_data_missing_column():
    # Sample DataFrame missing some columns
    data = {
        'MSISDN/Number': ['12345', '67890'],
        'Social Media DL (Bytes)': [1000, 2000],
    }
    df = pd.DataFrame(data)
    
    applications = ['Social Media', 'Google']
    
    # Call the function and expect None because of missing columns
    result = calculate_total_data_per_app(df, applications)
    
    # Ensure the function returns None on failure
    assert result is None

def test_calculate_total_data_empty_dataframe():
    # Empty DataFrame
    df = pd.DataFrame()
    
    applications = ['Social Media', 'Google']
    
    # Call the function and expect None because the DataFrame is empty
    result = calculate_total_data_per_app(df, applications)
    
    # Ensure the function returns None on failure
    assert result is None
