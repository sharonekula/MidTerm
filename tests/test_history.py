"""
Unit tests for the HistoryManager class from data.history module.

This module tests the functionality of the HistoryManager class, including:
1. Adding entries to the history.
2. Retrieving the current history.
3. Clearing all entries from the history.

Fixtures:
    history_manager: Provides a new instance of HistoryManager for each test.

Tests:
    - test_add_to_history: Validates adding a single entry to the history.
    - test_get_history: Checks that history entries can be retrieved as expected.
    - test_clear_history: Confirms that the history is cleared correctly.
"""

import pytest
from data.history import HistoryManager

@pytest.fixture
def history_manager():
    """
    Fixture to create a new HistoryManager instance before each test.

    Returns:
        HistoryManager: A fresh instance of HistoryManager.
    """
    return HistoryManager()

def test_add_to_history(history_manager):
    """
    Test that an entry can be added to the history.

    This test checks:
        - The entry is added to the history list.
        - The entry matches the expected format and values.
    """
    history_manager.add_to_history("add", 5, 3, 8)
    assert len(history_manager.history) == 1
    assert history_manager.history[0] == {
        "Operation": "add",
        "Operand1": 5,
        "Operand2": 3,
        "Result": 8
    }

def test_get_history(history_manager):
    """
    Test retrieving entries from the history.

    This test verifies:
        - Multiple entries can be added to history.
        - The get_history method returns the correct entries in the expected order.
    """
    history_manager.add_to_history("subtract", 10, 4, 6)
    history_manager.add_to_history("multiply", 3, 3, 9)
    history = history_manager.get_history()
    assert len(history) == 2
    assert history == [
        {"Operation": "subtract", "Operand1": 10, "Operand2": 4, "Result": 6},
        {"Operation": "multiply", "Operand1": 3, "Operand2": 3, "Result": 9}
    ]

def test_clear_history(history_manager):
    """
    Test that all entries can be cleared from the history.

    This test confirms:
        - The clear_history method removes all entries from the history.
        - The history list is empty after calling clear_history.
    """
    history_manager.add_to_history("divide", 20, 5, 4)
    assert len(history_manager.history) == 1  # Verify history contains entries
    history_manager.clear_history()
    assert len(history_manager.history) == 0  # Confirm history is cleared
