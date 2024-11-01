"""
Unit Tests for Arithmetic Command Classes

This module provides unit tests for classes in `app.commands` handling arithmetic operations. 
It covers the addition, subtraction, multiplication, and division commands, 
verifying correct output and error handling (e.g., division by zero).
"""
import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from data.history import HistoryManager

history_manager = HistoryManager()
def test_add_command():
    add_command = AddCommand()
    result = add_command.execute(3, 4, history_manager)
    assert result == 7, "The addition result should match the expected value."
    
def test_subtract_command():
    """Verify SubtractCommand correctly subtracts one number from another."""
    command = SubtractCommand()
    result = command.execute(15, 8, history_manager)
    assert result == 7, f"Expected 7, got {result}"

def test_multiply_command():
    """Verify MultiplyCommand correctly multiplies two numbers."""
    command = MultiplyCommand()
    result = command.execute(6, 4, history_manager)
    assert result == 24, f"Expected 24, got {result}"

def test_divide_command():
    """Verify DivideCommand correctly divides two numbers."""
    command = DivideCommand()
    result = command.execute(20, 4, history_manager)
    assert result == 5, f"Expected 5, got {result}"

def test_divide_by_zero():
    """Ensure DivideCommand raises ValueError on division by zero."""
    with pytest.raises(ValueError):
        command = DivideCommand()
        command.execute(10, 0, history_manager)
