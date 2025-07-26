import sys
from unittest.mock import patch
from main import main


@patch('main.file_input', side_effect = FileNotFoundError)
@patch('builtins.input', side_effect = ["2", "textfile.txt"])
@patch('builtins.print')
def test_file_not_found(mock_print, mock_input, mock_file_input):
    sys.argv = ["main.py"]
    main()
    printed = [args[0] for args, kwargs in mock_print.call_args_list]
    assert any("not found" in line for line in printed)



@patch('main.file_input', return_value = [])
@patch('builtins.input', side_effect = ["2", "textfile.txt"])
@patch('builtins.print')
def test_empty_file(mock_print, mock_input, mock_file_input):
    sys.argv = ["main.py"]
    main()
    printed = [args[0] for args, kwargs in mock_print.call_args_list if args]
    assert any("No data found" in line for line in printed)