import unittest
from unittest.mock import patch

from sysadmin_utils.system import automation


class TestSystemAutomation(unittest.TestCase):
    @patch("sysadmin_utils.system.automation.pyautogui.position")
    def test_mock_mouse_position(self, mock_position):
        """Test getting mouse position with a mock to avoid real GUI interactions."""
        mock_position.return_value = (100, 200)
        pos = automation.get_mouse_position()
        self.assertEqual(pos, (100, 200))
        mock_position.assert_called_once()


if __name__ == "__main__":
    unittest.main()
