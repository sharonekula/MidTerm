"""
Unit Tests for Arithmetic Command Classes

This module provides unit tests for classes in `app.commands` handling arithmetic operations. 
It covers the addition, subtraction, multiplication, and division commands, 
verifying correct output and error handling (e.g., division by zero).
"""
import pytest
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_add_command():
    """Verify AddCommand correctly adds two numbers."""
    command = AddCommand()
    result = command.execute(7, 3)
    assert result == 10, f"Expected 10, got {result}"

def test_subtract_command():
    """Verify SubtractCommand correctly subtracts one number from another."""
    command = SubtractCommand()
    result = command.execute(15, 8)
    assert result == 7, f"Expected 7, got {result}"

def test_multiply_command():
    """Verify MultiplyCommand correctly multiplies two numbers."""
    command = MultiplyCommand()
    result = command.execute(6, 4)
    assert result == 24, f"Expected 24, got {result}"

def test_divide_command():
    """Verify DivideCommand correctly divides two numbers."""
    command = DivideCommand()
    result = command.execute(20, 4)
    assert result == 5, f"Expected 5, got {result}"

def test_divide_by_zero():
    """Ensure DivideCommand raises ValueError on division by zero."""
    with pytest.raises(ValueError):
        command = DivideCommand()
        command.execute(10, 0)
