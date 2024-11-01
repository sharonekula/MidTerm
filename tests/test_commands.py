"""
Unit Tests for Arithmetic Command Classes

This module provides unit tests for classes in `app.commands` handling arithmetic operations. 
It covers the addition, subtraction, multiplication, and division commands, 
verifying correct output and error handling (e.g., division by zero).
"""
from unittest.mock import patch
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_add_command(capsys):
    """Verify AddCommand correctly adds two numbers."""
    command = AddCommand()
    with patch("builtins.input", side_effect=["3", "5"]):
        command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 3 + 5 = 8"

def test_subtract_command(capsys):
    """Verify SubtractCommand correctly subtracts one number from another."""
    command = SubtractCommand()
    with patch("builtins.input", side_effect=["10", "4"]):
        command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 10 - 4 = 6"

def test_multiply_command(capsys):
    """Verify MultiplyCommand correctly multiplies two numbers."""
    command = MultiplyCommand()
    with patch("builtins.input", side_effect=["7", "6"]):
        command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 7 * 6 = 42"

def test_divide_command(capsys):
    """Verify DivideCommand correctly divides two numbers."""
    command = DivideCommand()
    with patch("builtins.input", side_effect=["8", "2"]):
        command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 8 / 2 = 4.0"

def test_divide_by_zero(capsys):
    """Ensure DivideCommand raises ValueError on division by zero."""
    command = DivideCommand()
    with patch("builtins.input", side_effect=["8", "0"]):
        command.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "DivisionByZero Exception"
