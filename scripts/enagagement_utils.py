# Utility functions used in the engaement analysis
import logging
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import numpy as np

def normalize_data(df: pd.DataFrame) -> np.ndarray | None:
    try:
        
        # Normalize the data
        scaler = MinMaxScaler()
        normalized_data = scaler.fit_transform(df)
        return normalized_data

    except Exception as e:
        logging.error(f"Error normalizing data: {str(e)}")
        return None
    
def cluster_data(normalized_df: pd.DataFrame, n_clusters: int = 3) -> np.ndarray | None:
    try:
        # Run K-Means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        clusters = kmeans.fit_predict(normalized_df)
        logging.info("K-Means clustering successful, customers classified into three groups")
        
        return clusters
    except Exception as e:
        logging.error(f"Error clustering customers by engagement: {str(e)}")
        return None

def convert_bytes_to_gigabytes(df: pd.DataFrame, bytes_column: str, gb_column: str) -> pd.DataFrame | None:
    
    try:
        # Convert bytes to gigabytes
        df[gb_column] = df[bytes_column] / (1024 * 1024 * 1024)

        # Drop the original bytes column
        df.drop(columns=[bytes_column], inplace=True)
        logging.info(f"Conversion of '{bytes_column}' to gigabytes in column '{gb_column}' successful")
        return df

    except KeyError as e:
        logging.error(f"Column '{bytes_column}' not found in DataFrame: {str(e)}")
        return None

    except Exception as e:
        logging.error(f"Error converting '{bytes_column}' to gigabytes: {str(e)}")
        return None
    
def convert_milliseconds_to_minutes(df: pd.DataFrame, ms_column: str, min_column: str) -> pd.DataFrame | None:
    try:
        # Convert seconds to hours
        df[min_column] = df[ms_column] / (1000 * 60)
        
        # Drop the original seconds column
        df.drop(columns=[ms_column], inplace=True)
        logging.info(f"Conversion of '{ms_column}' to minutes in column '{min_column}' successful")
        return df

    except KeyError as e:
        logging.error(f"Column '{ms_column}' not found in DataFrame: {str(e)}")
        return None

    except Exception as e:
        logging.error(f"Error converting '{ms_column}' to minutes: {str(e)}")
        return None