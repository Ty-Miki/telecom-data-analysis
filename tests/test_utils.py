import pytest
from unittest.mock import patch, mock_open

from scripts.utils import load_environment_variables

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
