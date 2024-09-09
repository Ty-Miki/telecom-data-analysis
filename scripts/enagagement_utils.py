# Utility functions used in the engaement analysis
import logging
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

def normalize_data(df: pd.DataFrame) -> np.ndarray | None:
    try:
        
        # Normalize the data
        scaler = MinMaxScaler()
        normalized_data = scaler.fit_transform(df)
        return normalized_data

    except Exception as e:
        logging.error(f"Error normalizing data: {str(e)}")
        return None
    
def cluster_data(normalized_data: np.ndarray, n_clusters: int = 3) -> np.ndarray | None:
    try:
        # Run K-Means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        clusters = kmeans.fit_predict(normalized_data)
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

def convert_bytes_to_megabytes(df: pd.DataFrame, bytes_column: str, gb_column: str) -> pd.DataFrame | None:
    
    try:
        # Convert bytes to megabytes
        df[gb_column] = df[bytes_column] / (1024 * 1024)

        # Drop the original bytes column
        df.drop(columns=[bytes_column], inplace=True)
        logging.info(f"Conversion of '{bytes_column}' to megaytes in column '{gb_column}' successful")
        return df

    except KeyError as e:
        logging.error(f"Column '{bytes_column}' not found in DataFrame: {str(e)}")
        return None

    except Exception as e:
        logging.error(f"Error converting '{bytes_column}' to megabytes: {str(e)}")
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


def calculate_total_data_per_app(df: pd.DataFrame, applications: list) -> pd.DataFrame | None:
    try:
        # Calculate total data for each application
        for application in applications:
            df[f'{application} Total Data (Bytes)'] = df[f'{application} DL (Bytes)'] + df[f'{application} UL (Bytes)']
        
        # Group by 'MSISDN/Number' and sum the total data for each application
        relevant_df = df.groupby('MSISDN/Number')[[f'{application} Total Data (Bytes)' for application in applications]].sum().reset_index()
        
        logging.info("Total data calculation and grouping successful")
        return relevant_df
    
    except KeyError as e:
        logging.error(f"One or more columns not found in DataFrame: {str(e)}")
        return None

    except Exception as e:
        logging.error(f"Error in calculating total data: {str(e)}")
        return None

def elbow_method(normalized_data: np.ndarray, max_k: int = 10) -> None:
    
    try:
        if len(normalized_data) == 0:
            raise ValueError("Input data is empty.")

        inertia = []
        k_values = range(1, max_k + 1)

        for k in k_values:
            kmeans = KMeans(n_clusters=k, random_state=0)
            kmeans.fit(normalized_data)
            inertia.append(kmeans.inertia_)

        # Plot the inertia for each k value
        plt.figure(figsize=(10, 6))
        plt.plot(k_values, inertia, marker='o')
        plt.title('Elbow Method for Optimal k')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Inertia')
        plt.show()
        logging.info("Elbow method executed successfully.")
        
    except ValueError as e:
        logging.error(f"Value error: {str(e)}")

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")