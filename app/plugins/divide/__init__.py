import logging
from app.commands import Command
from data.history import HistoryManager

history_manager = HistoryManager()
class DivideCommand(Command):

    def execute(self,x , y, history_manager):
        if y == 0:
            logging.error("DivideByzero exception")
            raise ValueError("Cannot divide by zero!")
        logging.info(f"Performing Division for {x} and {y}")
        result = x / y
        logging.info(f"Adding to history Division, {x}, {y}, {result}")
        history_manager.add_to_history("Division", x, y, result)
        return result