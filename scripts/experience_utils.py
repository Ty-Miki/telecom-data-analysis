# Small utility functions used in the experience analysis
import logging
import pandas as pd

def tukeys_fence(df: pd.DataFrame, columns: list) -> pd.DataFrame | None:
    try:
        # Check if specified columns exist in the DataFrame
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Columns not found in DataFrame: {missing_columns}")

        # Calculate Q1, Q3, and IQR
        Q1 = df[columns].quantile(0.25)
        Q3 = df[columns].quantile(0.75)
        IQR = Q3 - Q1
        logging.info("Q1, Q3, and IQR calculated successfully")

        # Calculate lower and upper bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        logging.info("Lower bound and upper bound calculated successfully")

        # Apply Tukey's Fence to filter outliers
        for index, column in enumerate(columns):
            column_median = df[column].median()
            df[column] = df[column].apply(
                lambda x: column_median if x > upper_bound.iloc[index] or x < lower_bound.iloc[index] else x
            )

        logging.info("Tukey's Fence applied successfully")
        return df

    except ValueError as e:
        logging.error(f"Value error: {str(e)}")
        return None

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return None