import pytest
import psycopg2
from unittest.mock import patch, mock_open, Mock

from scripts.utils import load_environment_variables
from scripts.utils import connect_to_database

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