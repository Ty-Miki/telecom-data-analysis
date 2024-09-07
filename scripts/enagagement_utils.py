# Utility functions used in the engaement analysis
import logging
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import numpy as np

def normalize_data(df: pd.DataFrame, columns: list) -> tuple | pd.DataFrame:
    try:
        # Ensure that the specified columns exist in the DataFrame
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Columns not found in DataFrame: {missing_columns}")
        
        # Normalize the data
        scaler = MinMaxScaler()
        normalized_data = scaler.fit_transform(df[columns])
        
        # Convert the normalized data back to a DataFrame
        normalized_df = pd.DataFrame(normalized_data, columns=columns)
        logging.info("Data normalization successful")

        return normalized_df
    
    except Exception as e:
        logging.error(f"Error normalizing data: {str(e)}")
        return pd.DataFrame(columns=columns)
    
def cluster_data(normalized_df: pd.DataFrame, n_clusters: int = 3) -> np.ndarray | None:
    try:
        # Run K-Means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(normalized_df)
        logging.info("K-Means clustering successful, customers classified into three groups")
        
        return clusters
    except Exception as e:
        logging.error(f"Error clustering customers by engagement: {str(e)}")
        return None