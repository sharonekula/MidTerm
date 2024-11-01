import logging
from app.commands import Command
from data.history import HistoryManager

history_manager = HistoryManager()
class SubtractCommand(Command):

    def execute(self,x , y, history_manager):
        logging.info(f"Peforming Subtaction between {x} and {y}")
        result = x - y
        logging.info(f"Adding to history: Subtraction, {x}, {y}, {result}")
        history_manager.add_to_history("Subtraction", x, y, result)
        return result