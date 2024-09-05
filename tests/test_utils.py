import pytest
import psycopg2
import pandas as pd
from unittest.mock import patch, mock_open, Mock

from scripts.utils import load_environment_variables
from scripts.utils import connect_to_database
from scripts.utils import load_data_from_db
from scripts.utils import close_database_connection

# Mock the dotenv_values function to simulate different scenarios
@patch('scripts.utils.dotenv_values')
def test_load_environment_variables_success(mock_dotenv_values):
    mock_dotenv_values.return_value = {'KEY': 'value'}
    
    result = load_environment_variables('/path/to/directory')
    
    assert result == {'KEY': 'value'}
    assert 'KEY' in result

@patch('scripts.utils.dotenv_values')
def test_load_environment_variables_empty_file(mock_dotenv_values):
    mock_dotenv_values.return_value = {}
    
    result = load_environment_variables('/path/to/directory')
    
    assert result == {}
    assert len(result) == 0

@patch('scripts.utils.dotenv_values')
def test_load_environment_variables_exception(mock_dotenv_values):
    mock_dotenv_values.side_effect = Exception("Some error")
    
    result = load_environment_variables('/path/to/directory')
    
    assert result is None

# Mock the psycopg2.connect method
@patch('scripts.utils.psycopg2.connect')
def test_connect_to_database_success(mock_connect):
    mock_connection = Mock()
    mock_connect.return_value = mock_connection
    
    db_parameters = {'dbname': 'test_db', 'user': 'test_user', 'password': 'test_pass'}
    result = connect_to_database(db_parameters)
    
    assert result == mock_connection
    mock_connect.assert_called_once_with(**db_parameters)

@patch('scripts.utils.psycopg2.connect')
def test_connect_to_database_failure(mock_connect):
    mock_connect.side_effect = Exception("Connection error")
    
    db_parameters = {'dbname': 'test_db', 'user': 'test_user', 'password': 'test_pass'}
    result = connect_to_database(db_parameters)
    
    assert result is None
    mock_connect.assert_called_once_with(**db_parameters)

# Mock the pandas read_sql_query method
@patch('scripts.utils.pd.read_sql_query')
def test_load_data_from_db_success(mock_read_sql_query):
    mock_df = pd.DataFrame({'column1': [1, 2], 'column2': ['A', 'B']})
    mock_read_sql_query.return_value = mock_df
    
    mock_conn = Mock()
    table_name = 'test_table'
    result = load_data_from_db(mock_conn, table_name)
    
    assert isinstance(result, pd.DataFrame)
    assert result.equals(mock_df)
    mock_read_sql_query.assert_called_once_with(f"SELECT * FROM {table_name}", mock_conn)

@patch('scripts.utils.pd.read_sql_query')
def test_load_data_from_db_failure(mock_read_sql_query):
    mock_read_sql_query.side_effect = Exception("SQL error")
    
    mock_conn = Mock()
    table_name = 'test_table'
    result = load_data_from_db(mock_conn, table_name)
    
    assert result is None
    mock_read_sql_query.assert_called_once_with(f"SELECT * FROM {table_name}", mock_conn)

def test_close_database_connection_success():
    mock_conn = Mock()
    
    close_database_connection(mock_conn)
    
    mock_conn.close.assert_called_once()
    # Since close() is void, we just need to ensure it was called

@patch('scripts.utils.logging.error')
def test_close_database_connection_failure(mock_logging_error):
    mock_conn = Mock()
    mock_conn.close.side_effect = Exception("Close error")
    
    close_database_connection(mock_conn)
    
    mock_conn.close.assert_called_once()
    mock_logging_error.assert_called_once_with("Error closing database connection: Close error")