import os
import pytest
import pandas as pd
import logging
from unittest.mock import patch, MagicMock
from data.csv import CsvCommand

@pytest.fixture
def csv_command():
    mock_history_manager = [{'operation': 'add', 'result': 10}, {'operation': 'subtract', 'result': 5}]
    return CsvCommand(mock_history_manager)

def test_invalid_history_format():
    invalid_history_manager = "Invalid history format"
    csv_command = CsvCommand(invalid_history_manager)
    with patch('logging.error') as log_error_mock:
        csv_command.execute()
        log_error_mock.assert_called_once_with("Invalid data format in history manager. Expected a list of dictionaries.")

def test_csv_export(csv_command, tmpdir):
    data_dir = os.path.join(tmpdir, 'data')
    csv_command.filename = os.path.join(data_dir, 'test.csv')
    os.makedirs(data_dir, exist_ok=True)
    csv_command.execute()
    assert os.path.isfile(csv_command.filename)
    df = pd.read_csv(csv_command.filename)
    assert df.to_dict('records') == csv_command.history_manager
    csv_command.execute()
    df_appended = pd.read_csv(csv_command.filename)
    assert len(df_appended) == 2 * len(csv_command.history_manager)

@pytest.fixture(autouse=True)
def caplog(caplog):
    caplog.set_level(logging.ERROR)

