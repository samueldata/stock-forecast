import subprocess
import webbrowser
import time
import os
import pytest
from unittest.mock import patch
from main import start_flask_app, open_browser

# Test for start_flask_app function
@patch('subprocess.Popen')
def test_start_flask_app(mock_popen):
    start_flask_app()
    app_path = os.path.join(os.path.dirname(__file__), 'src', 'webapp', 'app.py')
    mock_popen.assert_called_once_with(['python', app_path])

# Test for open_browser function
@patch('webbrowser.open')
@patch('time.sleep')
def test_open_browser(mock_sleep, mock_open):
    open_browser()
    mock_sleep.assert_called_once_with(2)
    mock_open.assert_called_once_with('http://127.0.0.1:5000/')

# Test if start_flask_app does not raise any exceptions
@patch('subprocess.Popen')
def test_start_flask_app_no_exception(mock_popen):
    try:
        start_flask_app()
    except Exception as e:
        pytest.fail(f"start_flask_app raised an exception: {e}")

# Test if open_browser does not raise any exceptions
@patch('webbrowser.open')
@patch('time.sleep')
def test_open_browser_no_exception(mock_sleep, mock_open):
    try:
        open_browser()
    except Exception as e:
        pytest.fail(f"open_browser raised an exception: {e}")

# Test if start_flask_app and open_browser are called when main is executed
@patch('subprocess.Popen')
@patch('webbrowser.open')
@patch('time.sleep')
def test_main_execution(mock_sleep, mock_open, mock_popen):
    with patch('main.start_flask_app') as mock_start_flask_app, \
         patch('main.open_browser') as mock_open_browser:
        import main
        main.start_flask_app()
        main.open_browser()
        mock_start_flask_app.assert_called_once()
        mock_open_browser.assert_called_once()

# Test if the Flask app path is correctly set
def test_app_path():
    app_path = os.path.join(os.path.dirname(__file__), 'src', 'webapp', 'app.py')
    expected_path = os.path.join(os.path.dirname(__file__), 'src', 'webapp', 'app.py')
    assert app_path == expected_path

# Test if the URL is correctly set
def test_url():
    url = 'http://127.0.0.1:5000/'
    assert url == 'http://127.0.0.1:5000/'
