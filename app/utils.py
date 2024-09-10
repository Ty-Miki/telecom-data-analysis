# A streamlit application class to use in the app
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StreamlitAPP:
    def __init__(self) -> None:
        self.parent_dir = os.getcwd()
        st.title("Telecom Data Analysis for TellCo.")
        st.write("Analyzing ")
        logger.info("StreamlitApp instance initialized successfully")

    def load_dataframe(self, picke_path: str) -> pd.DataFrame:
        # The picke path should be relatice to the project parent directory
        # Ex: '/notebooks/user_satisfaction_analysis/satisfaction_data.pkl

        try:
            data = pd.read_pickle(picke_path)
            logger.info(f"DataFrame loaded from {picke_path}")
            return data
        except Exception as e:
            logger.error(f"Error loading data from {picke_path}. {str(e)}")
            return None

    def display_dataframe(self, df: pd.DataFrame, title: str) -> None:
        # Display the dataframe

        try:
            st.write(title)
            st.dataframe(df.head())
            logger.info("Successfully displayed dataframe into streamlit app.")
        except Exception as e:
            logger.error(f"Error displaying dataframe {df} to streamlit app. {str(e)}")

    def plot_bar_chart(self, 
                       df: pd.DataFrame,
                       title: str,
                       x_label: str,
                       y_label: str) -> None:
        # Plot a streamline barchart based on given parameters.
        df.plot(kind='bar', figsize=(10, 6))
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        st.pyplot(plt)