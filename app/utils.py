# A streamlit application class to use in the app
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StreamlitAPP:
    def __init__(self) -> None:
        self.parent_dir = os.getcwd()
        st.title("Telecom Data Analysis for TellCo.")
        logger.info("StreamlitApp instance initialized successfully")

    def load_dataframe(self, picke_path: str) -> pd.DataFrame:

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
            st.dataframe(df)
            logger.info("Successfully displayed dataframe into streamlit app.")
        except Exception as e:
            logger.error(f"Error displaying dataframe {df} to streamlit app. {str(e)}")

    def plot_bar_chart(self, 
                       df: pd.DataFrame,
                       title: str,
                       x_label: str,
                       y_label: str,
                       rotation: int = 0) -> None:
        
        try:
            # Plot a streamline barchart based on given parameters.
            df.plot(kind='bar', figsize=(10, 6))
            plt.title(title)
            plt.xticks(rotation=rotation)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            st.pyplot(plt)
            logger.info(f"Bar chart plotted successfully for {df}")
        
        except Exception as e:
            logger.error(f"Error plotting bar chart for {df}. {str(e)}")

    def plot_melted_bar_chart(self, 
                              df: pd.DataFrame,
                              title: str,
                              x_label: str,
                              y_label: str,
                              id_vars: str,
                              value_vars: list,
                              rotation: int = 0) -> None:
        
        try:
            # Melt the dataframe for bar plot
            melted_df = df.melt(id_vars=id_vars, value_vars=value_vars)
            logger.info(f'Dataframe {df} melted successfully.')

            # plot the bar chart
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=id_vars, y='value', hue='variable', data=melted_df, ax=ax)
            plt.title(title)
            plt.xticks(rotation=rotation)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            st.pyplot(fig)
            logger.info(f'Bar chart plotted successfully for {df}')
        
        except Exception as e:
            logger.error(f"Error plotting bar chart for {df}. {str(e)}")

    def show_correlation_with_heatmap(self,
                                      df: pd.DataFrame,
                                      columns: list,
                                      title: str) -> None:
        try:
            st.write(title)
        
            # Calculate correlations
            correlations = df[columns].corr()
            logger.info(f'Successfully calculated correlation between {columns} {df}')

            # Plot the heatmap
            fig, ax = plt.subplots()
            sns.heatmap(correlations, annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
            logger.info(f"Correlation heatmap between {columns} plotted successfully for {df}")
        
        except Exception as e:
            logger.error(f"Error plotting correlation heatmap between {columns} for {df}. {str(e)}")

        