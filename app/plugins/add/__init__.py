import logging
from app.commands import Command
from data.history import HistoryManager

history_manager = HistoryManager()
class AddCommand(Command):

    def execute(self,x , y, history_manager):
        logging.info(f"Performing addition for {x} and {y}")
        result = x + y
        logging.info(f"Adding to history : Addition,{x},{y},{result}")
        history_manager.add_to_history("Addition", x, y, result)
        return result