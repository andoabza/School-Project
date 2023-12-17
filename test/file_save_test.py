import unittest
import pandas as pd
from sqlalchemy import create_engine
from unittest.mock import patch, MagicMock
from save.file_save import save_to_excel

class TestSaveToExcel(unittest.TestCase):
    @patch('pandas.read_sql')
    @patch('pandas.DataFrame.to_excel')
    def test_save_to_excel(self, mock_to_excel, mock_read_sql):
        mock_read_sql.return_value = pd.DataFrame()
        save_to_excel()
        mock_read_sql.assert_called_once()
        mock_to_excel.assert_called_once_with('students.xlsx', index=False)

if __name__ == '__main__':
    unittest.main()