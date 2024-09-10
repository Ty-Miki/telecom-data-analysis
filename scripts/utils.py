# Small utility functions to be used in the analysis
import logging
from dotenv import dotenv_values
import psycopg2
from psycopg2.extensions import connection as Connection
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine as AlchemyConnection

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

def load_data_from_db(conn: Connection, table_name: str) -> pd.DataFrame | None:

    query = f"SELECT * FROM {table_name}"

    try:
        logging.info(f"Executing query: {query}")
        df = pd.read_sql_query(query, conn)
        logger.info("Data loaded into DataFrame successfully")
        return df
    
    except Exception as e:
        logger.error(f"Error loading data from table '{table_name}': {str(e)}")
        return None

def close_database_connection(conn: Connection) -> None:
    try:
        conn.close()
        logging.info("Database connection closed successfully")
    except Exception as e:
        logging.error(f"Error closing database connection: {str(e)}")

def create_alchemy_connection(credentials: dict) -> AlchemyConnection | None:
    try:
        username = credentials.get('USER')
        host = credentials.get('host')
        port = credentials.get('port')
        db = credentials.get('DB_NAME')

        engine = create_engine(f'postgresql://{username}:@{host}:{port}/{db}')
        logging.info(f"Created SQLAlchemy connection")
        return engine

    except Exception as e:
        logging.error(f"Error creating SQLAlchemy connection: {str(e)}")
        return None

def export_df_to_db(df: pd.DataFrame, 
                    table_name: str,
                    conn: AlchemyConnection,
                    if_exists: str = 'fail' # Options are 'fail', 'replace', 'append'
                    ) -> bool | None:
    try:
        # Check if table exists in the database
        table_exists = conn.dialect.has_table(conn.connect(), table_name)
        
        if table_exists and if_exists == 'fail':
            raise ValueError(f"Table '{table_name}' already exists and 'if_exists' is set to 'fail'. Operation aborted.")
        
        # Export df to sql
        df.to_sql(table_name, con=conn, if_exists=if_exists, index=False)
        logging.info(f"DataFrame exported to table '{table_name}' successfully.")
        return True
    
    except ValueError as e:
        logging.error(f'{e}')
        return None
    except Exception as e:
        logging.error(f"Error exporting DataFrame to table '{table_name}': {str(e)}")
        return None