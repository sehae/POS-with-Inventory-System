from unittest.mock import patch, MagicMock
import pytest
from modules.maintenance.user_logs import user_log

# Scenario 1: Attempted to Login
@patch('modules.maintenance.user_logs.conn')
def test_user_log_attempted_login(mock_conn):
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    user_log(user_id=1, user_action="attempted to login", username='test_user')
    mock_cursor.execute.assert_called()
    mock_conn.commit.assert_called()

# Scenario 2: Successfully Logged In
@patch('modules.maintenance.user_logs.conn')
def test_user_log_successful_login(mock_conn):
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    user_log(user_id=1, user_action="successfully logged in", username='test_user')
    mock_cursor.execute.assert_called()
    mock_conn.commit.assert_called()
