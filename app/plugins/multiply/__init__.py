import logging
from app.commands import Command
from data.history import HistoryManager

history_manager = HistoryManager()
class MultiplyCommand(Command):

    def execute(self,x , y, history_manager):
        logging.info(f"Performing Multiplication between {x} and {y}")
        result = x * y
        logging.info(f"Adding to history: Multiplication, {x}, {y}, {result}")
        history_manager.add_to_history("Multiplication", x, y, result)
        return result

