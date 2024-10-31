"""
Unit Tests for Command Registration and Execution

This module contains unit tests for the `CommandHandler` class, specifically 
testing the ability to register and execute commands. The tests focus on:
1. Ensuring commands can be registered successfully.
2. Verifying that registered commands execute correctly and return expected results.

A mock `MockCommand` class is used for testing purposes, simulating a simple 
command that sums its arguments.
"""
import pytest
from app.commands import Command, CommandHandler

# Mock command class for testing
class MockCommand(Command):
    """
    Manages command registration and execution.
    Allows commands to be registered with a name and executed later by that name. 
    Commands must implement the `Command` interface with an `execute` method.
    """
    def execute(self, *args):
        return sum(args)  # Example implementation: returns the sum of all args

@pytest.fixture
def command_handler():
    """Fixture to create a CommandHandler instance."""
    return CommandHandler()

def test_register_command(command_handler):
    """Test that a command can be registered successfully."""
    command = MockCommand()
    command_handler.register_command("add", command)
    assert "add" in command_handler.commands, "Command 'add' was not registered."

def test_execute_command(command_handler):
    """Test that an executed command returns the correct result."""
    command = MockCommand()
    command_handler.register_command("add", command)
    result = command_handler.execute_command("add", 1, 2, 3)
    assert result == 6, f"Expected 6, got {result}"

def test_register_duplicate_command(command_handler):
    """Test that registering a command with a duplicate name raises a ValueError."""
    command = MockCommand()
    command_handler.register_command("add", command)
    with pytest.raises(ValueError, match="Command 'add' is already registered."):
        command_handler.register_command("add", command)

def test_execute_unregistered_command(command_handler):
    """Test that executing an unregistered command raises a ValueError."""
    with pytest.raises(ValueError, match="Command 'subtract' not found."):
        command_handler.execute_command("subtract", 10, 5)
