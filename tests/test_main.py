import sys
from unittest.mock import patch
from main import main


@patch('main.file_input', side_effect = FileNotFoundError)   #imitation of FileNotFoundError in file_input
@patch('builtins.input', side_effect = ["2", "textfile.txt"])   #imitation of user input in menu
@patch('builtins.print')   #capturing outputs
def test_file_not_found(mock_print, mock_input, mock_file_input):
    sys.argv = ["main.py"]
    main()
    printed = [args[0] for args, kwargs in mock_print.call_args_list]   #collect and check printed lines (errors) after running the program
    assert any("not found" in line for line in printed)



@patch('main.file_input', return_value = [])   #imitation of empty file
@patch('builtins.input', side_effect = ["2", "textfile.txt"])   #imitation of user input in menu
@patch('builtins.print')   #capturing outputs
def test_empty_file(mock_print, mock_input, mock_file_input):
    sys.argv = ["main.py"]
    main()
    printed = [args[0] for args, kwargs in mock_print.call_args_list if args]   #collect and check printed lines (errors) after running the program
    assert any("No data found" in line for line in printed)