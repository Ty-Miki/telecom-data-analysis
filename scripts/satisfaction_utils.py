# Small utility functions used in the satisfaction analysis
import logging
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from typing import Tuple

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

def train_linear_regression_model(
    df: pd.DataFrame,
    feature_columns: list[str],
    target_column: str,
    test_size: float = 0.2,
    random_state: int = 42
) -> Tuple[pd.Series, pd.Series] | None:
    
    try:
        # Extract features and target from the DataFrame
        X = df[feature_columns]
        y = df[target_column]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        logging.info("Data split into training and testing sets successfully")

        # Initialize and train the Linear Regression model
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        logging.info("Linear Regression model trained successfully")

        # Predict the target values for the test set
        y_pred = regressor.predict(X_test)
        logging.info("Prediction using the trained model completed successfully")

        return y_test, pd.Series(y_pred, index=X_test.index)

    except KeyError as e:
        logging.error(f"Column not found in DataFrame: {str(e)}")
        return None

    except Exception as e:
        logging.error(f"Error training Linear Regression model: {str(e)}")
        return None
