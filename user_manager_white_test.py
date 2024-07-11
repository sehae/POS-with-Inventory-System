import unittest
from unittest.mock import MagicMock, patch

from PyQt5.QtTest import QSignalSpy

from validator.user_manager import userManager


class TestUserManager(unittest.TestCase):

    @patch('modules.maintenance.user_logs.conn')
    def setUp(self, mock_conn):
        # Mock the database connection
        self.mock_conn = mock_conn
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

        # Initialize the userManager instance
        self.user_manager = userManager()

    def test_set_department_valid(self):
        spy = QSignalSpy(self.user_manager.user_type_updated)
        self.user_manager.set_department("Admin")
        self.assertEqual(self.user_manager.get_department(), "Admin")
        self.assertEqual(len(spy), 1)
        self.assertEqual(spy[0][0], "Admin")

    def test_set_department_invalid(self):
        self.user_manager.set_department("InvalidDepartment")
        self.assertIsNone(self.user_manager.get_department())

    def test_reset_user_data(self):
        self.user_manager.set_department("Admin")
        self.user_manager.set_current_username("test_user")
        self.user_manager.reset_user_data()
        self.assertIsNone(self.user_manager.get_department())
        self.assertIsNone(self.user_manager.get_current_username())

    def test_signals(self):
        # Using QSignalSpy to check if the signals are emitted correctly
        spy_fullname = QSignalSpy(self.user_manager.fullname_updated)
        self.user_manager.set_current_fullname("John Doe")
        self.assertEqual(len(spy_fullname), 1)
        self.assertEqual(spy_fullname[0][0], "John Doe")

        spy_firstname = QSignalSpy(self.user_manager.first_name_updated)
        self.user_manager.set_first_name("John")
        self.assertEqual(len(spy_firstname), 1)
        self.assertEqual(spy_firstname[0][0], "John")

if __name__ == '__main__':
    unittest.main()
