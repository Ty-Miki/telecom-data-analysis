import pandas as pd
import logging
from typing import Tuple

# Load parent directory to sys.path
import sys, os
parent_dir = os.getcwd()
sys.path.insert(0, parent_dir)
from scripts.satisfaction_utils import train_linear_regression_model


# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Model:
    def __init__(self, 
                 satisfaction_data: pd.DataFrame,
                 feature_column: list[str],
                 target_column: str,
                 test_size: float = 0.2) -> None:
        self.data = satisfaction_data
        self.feature_column = feature_column
        self.target_column = target_column
        self.test_size = test_size
        logger.info("A model instance created successfully.")

    def train_model(self) -> Tuple[pd.Series, pd.Series] | None:
        try:
            test, prediction = train_linear_regression_model(df=self.data,
                                                             feature_columns=self.feature_column,
                                                             target_column=self.target_column,
                                                             test_size=self.test_size)
            if test is not None and prediction is not None:
                logger.info("Model run successfully, outputs are ready for evaluation.")
                return test, prediction
            else:
                logger.warning("Model did not successfully no test or predicted data avaliable")
                return None
        except Exception as e:
                logger.error(f"Error running model. {str(e)}")
                return None
        
if __name__ == '__main__':
    satisfaction_data = pd.read_pickle('./model/satisfaction_data.pkl')
    model = Model(satisfaction_data=satisfaction_data,
                  feature_column=['Engagement Score', 'Experience Score'],
                  target_column='Satisfaction Score',
                  test_size= 0.2)
    test, prediction = model.train_model()