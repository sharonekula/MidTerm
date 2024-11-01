import pytest
from data.history import HistoryManager

@pytest.fixture
def history_manager():
    # Fixture to create a new HistoryManager instance before each test
    return HistoryManager()

def test_add_to_history(history_manager):
    # Test adding an entry to history
    history_manager.add_to_history("add", 5, 3, 8)
    assert len(history_manager.history) == 1
    assert history_manager.history[0] == {
        "Operation": "add",
        "Operand1": 5,
        "Operand2": 3,
        "Result": 8
    }

def test_get_history(history_manager):
    # Test retrieving history entries
    history_manager.add_to_history("subtract", 10, 4, 6)
    history_manager.add_to_history("multiply", 3, 3, 9)
    history = history_manager.get_history()
    assert len(history) == 2
    assert history == [
        {"Operation": "subtract", "Operand1": 10, "Operand2": 4, "Result": 6},
        {"Operation": "multiply", "Operand1": 3, "Operand2": 3, "Result": 9}
    ]

def test_clear_history(history_manager):
    # Test clearing the history
    history_manager.add_to_history("divide", 20, 5, 4)
    assert len(history_manager.history) == 1  # Verify that history has entries
    history_manager.clear_history()
    assert len(history_manager.history) == 0  # Ensure history is cleared
