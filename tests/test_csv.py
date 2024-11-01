"""
Unit tests for the CsvCommand class from data.csv module.

This module uses pytest to test various functionalities of CsvCommand, including:
1. Handling invalid history format.
2. Exporting history to a CSV file and appending on subsequent executions.
3. Ensuring the 'data' directory exists and that the CSV file is properly written.

Fixtures:
    csv_command: Creates a CsvCommand instance with mock data for testing.
    caplog: Captures log messages for validating logging output.

Tests:
    - test_invalid_history_format: Checks if invalid history data type triggers a logging error.
    - test_csv_export: Verifies the CSV export functionality and checks for data consistency.
"""

import logging
from unittest.mock import patch
import os
import pytest
import pandas as pd
from data.csv import CsvCommand

@pytest.fixture
def csv_command():
    """
    Fixture to create a CsvCommand instance with mock history data for testing.

    Returns:
        CsvCommand: A CsvCommand instance with sample history data.
    """
    mock_history_manager = [{'operation': 'add', 'result': 10}, {'operation': 'subtract', 'result': 5}]
    return CsvCommand(mock_history_manager)

def test_invalid_history_format():
    """
    Test that CsvCommand logs an error if the history data format is invalid.

    This function passes a non-list, invalid history format to CsvCommand and checks that
    an appropriate error message is logged.
    """
    invalid_history_manager = "Invalid history format"
    csv_command = CsvCommand(invalid_history_manager)
    with patch('logging.error') as log_error_mock:
        csv_command.execute()
        log_error_mock.assert_called_once_with("Invalid data format in history manager. Expected a list of dictionaries.")

def test_csv_export(csv_command, tmpdir):
    """
    Test that CsvCommand correctly exports history to a CSV file.

    The test checks:
        - If a CSV file is created in the specified data directory.
        - That the contents of the file match the history data.
        - The CSV file is appended to on subsequent executions.

    Args:
        csv_command (CsvCommand): The CsvCommand instance provided by the fixture.
        tmpdir (py.path.local): A temporary directory provided by pytest.
    """
    data_dir = os.path.join(tmpdir, 'data')
    csv_command.filename = os.path.join(data_dir, 'test.csv')
    os.makedirs(data_dir, exist_ok=True)

    # Execute the CSV export and verify file creation
    csv_command.execute()
    assert os.path.isfile(csv_command.filename)

    # Check that the data in the CSV file matches the mock history data
    df = pd.read_csv(csv_command.filename)
    assert df.to_dict('records') == csv_command.history_manager

    # Execute again to test appending to the CSV
    csv_command.execute()
    df_appended = pd.read_csv(csv_command.filename)
    assert len(df_appended) == 2 * len(csv_command.history_manager)

@pytest.fixture(autouse=True)
def caplog(caplog):
    """
    Fixture to capture log messages at the ERROR level.

    This fixture is automatically used in all tests to check for logged error messages.
    """
    caplog.set_level(logging.ERROR)
