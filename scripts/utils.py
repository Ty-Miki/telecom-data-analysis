# Small utility functions to be used in the analysis
import logging
from dotenv import dotenv_values
import psycopg2
from psycopg2.extensions import connection as Connection

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_environment_variables(parent_directory: str) -> dict | None:
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
    
def connect_to_database(db_parameters: dict) -> Connection | None:
    try:
        logger.info('Attempting to connect to the database')
        conn = psycopg2.connect(**db_parameters)
        logger.info('Connection successful')
        return conn
    
    except Exception as e:
        logger.error(f'Error connecting to database: {str(e)}')
        return None

    
