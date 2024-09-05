# Small utility functions to be used in the analysis
import logging
from dotenv import dotenv_values

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_environment_variables(parent_directory):
    # Load environment variables for a .env file
    try:
        env_file_path = f'{str(parent_directory)}/.env'
        logger.info(f'Trying to load environment variables from {env_file_path}')

        CREDENTIALS = dotenv_values(env_file_path)

        if CREDENTIALS:
            logger.info("Credentials loaded successfully")
        else:
            logger.warning("Credentials not loaded. Possibly an empty .env file")
        
        return CREDENTIALS
    
    except Exception as e:
        logger.error(f'Error loading credentials: {str(e)}')
        return None