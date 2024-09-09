# Small utility functions used in the satisfaction analysis
import logging
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_centroids(df: pd.DataFrame, k: int=3) -> np.ndarray | None:
    try:
        # Normalize data
        scaler = StandardScaler()
        normalized_data = scaler.fit_transform(df)
        logger.info("Data normalization successful")

        # Apply KMeans
        kmeans = KMeans(n_clusters=k, random_state=0)
        kmeans.fit(normalized_data)
        logger.info("KMeans clustering successful")

        # Get the centroids
        centroids = kmeans.cluster_centers_
        logger.info(f"Centroids calculated for {k} clusters")

        return centroids

    except Exception as e:
        logger.error(f"Error calculating centroids: {str(e)}")
        return None

def euclidean_distance(data: np.ndarray, centroid: np.ndarray) -> float | None:
    try:
        # Ensure both inputs are numpy arrays and have the same shape
        if data.shape != centroid.shape:
            raise ValueError("Input data and centroid must have the same shape")
        
        # Calculate the Euclidean distance
        distance = np.sqrt(np.sum((data - centroid) ** 2))
        
        return distance

    except ValueError as e:
        logging.error(f"Value error: {str(e)}")
        return None

    except Exception as e:
        logging.error(f"Error calculating Euclidean distance: {str(e)}")
        return None