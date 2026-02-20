"""Tests for hello_world_app.py"""
import sys
from io import StringIO
from unittest.mock import patch
import pytest  # pyright: ignore[reportMissingImports]


def test_main():
    """Test that main function prints Hello World message."""
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        from hello_world_app import main
        main()
    
    output = captured_output.getvalue()
    assert "Hello, World!" in output
    assert "Welcome to Python programming!" in output


def test_main_output(capsys):
    """Test main function output using pytest capsys."""
    from hello_world_app import main
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
    assert "Welcome to Python programming!" in captured.out
