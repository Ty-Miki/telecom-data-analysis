import pytest
import pandas as pd
from scripts.experience_utils import tukeys_fence

def test_tukeys_fence_success():
    # Sample DataFrame with numerical data
    data = {
        'A': [1, 2, 3, 4, 100],
        'B': [5, 6, 7, 8, 200],
    }
    df = pd.DataFrame(data)
    
    columns = ['A', 'B']
    
    # Call the function
    result = tukeys_fence(df.copy(), columns)
    
    # Check that the function returns a DataFrame
    assert isinstance(result, pd.DataFrame)

    # Check that outliers have been replaced with the median
    expected_data = {
        'A': [1.0, 2.0, 3.0, 4.0, 3.0],  # 100 should be replaced by the median 3
        'B': [5.0, 6.0, 7.0, 8.0, 7.0],  # 200 should be replaced by the median 7
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result, expected_df)

def test_tukeys_fence_missing_column():
    # Sample DataFrame missing one of the specified columns
    data = {
        'A': [1, 2, 3, 4, 100],
    }
    df = pd.DataFrame(data)
    
    columns = ['A', 'B']
    
    # Call the function and expect None due to missing column
    result = tukeys_fence(df, columns)
    
    assert result is None

def test_tukeys_fence_empty_dataframe():
    # Empty DataFrame
    df = pd.DataFrame()
    
    columns = ['A', 'B']
    
    # Call the function and expect None due to empty DataFrame
    result = tukeys_fence(df, columns)
    
    assert result is None

def test_tukeys_fence_no_outliers():
    # DataFrame with no outliers
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
    }
    df = pd.DataFrame(data)
    
    columns = ['A', 'B']
    
    # Call the function
    result = tukeys_fence(df.copy(), columns)
    
    # Check that the function returns a DataFrame and no changes were made
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(result, df)
