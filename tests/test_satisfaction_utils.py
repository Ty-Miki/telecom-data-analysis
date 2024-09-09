import pytest
import pandas as pd
import numpy as np

from scripts.satisfaction_utils import calculate_centroids
from scripts.satisfaction_utils import euclidean_distance

def test_calculate_centroids_success():
    # Sample DataFrame
    data = {
        'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    centroids = calculate_centroids(df, k=2)
    
    # Check that the function returns a numpy array
    assert isinstance(centroids, np.ndarray)
    
    # Ensure the shape of the centroids array is correct (k clusters, n features)
    assert centroids.shape == (2, df.shape[1])

def test_calculate_centroids_failure():
    # Pass an empty DataFrame to check failure scenario
    df = pd.DataFrame()
    
    # Call the function
    centroids = calculate_centroids(df, k=2)
    
    # Check that the function returns None on failure
    assert centroids is None

def test_euclidean_distance_success():
    # Sample data
    data = np.array([1.0, 2.0, 3.0])
    centroid = np.array([4.0, 5.0, 6.0])
    
    # Call the function
    distance = euclidean_distance(data, centroid)
    
    # Check that the function returns a float
    assert isinstance(distance, float)
    
    # Calculate expected distance manually
    expected_distance = np.sqrt(np.sum((data - centroid) ** 2))
    
    # Ensure the calculated distance matches the expected distance
    assert np.isclose(distance, expected_distance)

def test_euclidean_distance_shape_mismatch():
    # Sample data with mismatched shapes
    data = np.array([1.0, 2.0])
    centroid = np.array([1.0, 2.0, 3.0])
    
    # Call the function
    distance = euclidean_distance(data, centroid)
    
    # Check that the function returns None due to shape mismatch
    assert distance is None

def test_euclidean_distance_failure():
    # Pass non-numeric data to check failure scenario
    data = "invalid_data"
    centroid = np.array([1.0, 2.0, 3.0])
    
    # Call the function
    distance = euclidean_distance(data, centroid)
    
    # Check that the function returns None on failure
    assert distance is None