# Classes and methods for data processing and cleaning
import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class MissingValueHandler:
    """A class to inspect and handle missing values."""

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        logging.info("MissingValueHandler instance created")

    def missing_value_summary(self) -> pd.Series:
        """Returns the count of missing values in each column."""
        try:
            summary = self.df.isnull().sum()
            logging.info("Missing value summary computed successfully")
            return summary
        except Exception as e:
            logging.error(f"Error computing missing value summary: {str(e)}")
            return pd.Series()
    

    def missing_value_percentage(self) -> pd.Series:
        """Returns the percentage of missing values in each column."""
        try:
            percentage = (self.df.isnull().sum() / len(self.df)) * 100
            logging.info("Missing value percentage computed successfully")
            return percentage
        except Exception as e:
            logging.error(f"Error computing missing value percentage: {str(e)}")
            return pd.Series()
    
    def missing_values_heatmap(self) -> None:
        """Displays a heatmap of missing values."""
        try:
            sns.heatmap(self.df.isnull(), cbar=False)
            plt.show()
            logging.info("Missing values heatmap displayed successfully")
        except Exception as e:
            logging.error(f"Error displaying missing values heatmap: {str(e)}")

 
    def describe_numeric_columns(self) -> pd.DataFrame:
        """Returns summary statistics for numeric columns."""
        try:
            description = self.df.describe()
            logging.info("Numeric column descriptions computed successfully")
            return description
        except Exception as e:
            logging.error(f"Error describing numeric columns: {str(e)}")
            return pd.DataFrame()
    
    def value_counts_categorical(self, column_name: str) -> pd.Series:
        """Returns value counts for a specified categorical column."""
        try:
            counts = self.df[column_name].value_counts()
            logging.info(f"Value counts for column '{column_name}' computed successfully")
            return counts
        except Exception as e:
            logging.error(f"Error computing value counts for column '{column_name}': {str(e)}")
            return pd.Series()
        
    def correlation_matrix(self) -> pd.DataFrame:
        """Returns the correlation matrix of numerical columns."""
        try:
            corr_matrix = self.df.corr()
            logging.info("Correlation matrix computed successfully")
            return corr_matrix
        except Exception as e:
            logging.error(f"Error computing correlation matrix: {str(e)}")
            return pd.DataFrame()
    
    def inspect_outliers(self, columns=None) -> None:
        """
        Displays boxplots to inspect outliers for numeric columns.
        If specific columns are provided, inspects only those; otherwise inspects all numeric columns.
        """
        try:
            if columns is None:
                numeric_columns = self.df.select_dtypes(include='number').columns
            else:
                numeric_columns = columns

            for column in numeric_columns:
                plt.figure(figsize=(8, 4))
                sns.boxplot(x=self.df[column])
                plt.title(f'Boxplot of {column}')
                plt.show()
                logging.info(f"Boxplot for column '{column}' displayed successfully")
        except Exception as e:
            logging.error(f"Error displaying boxplots for outliers: {str(e)}")