import logging
from app.commands import Command
from data.history import HistoryManager

class ExitCommand(Command):

    def execute(self):
        logging.info("System Exit Raised.")
        raise SystemExit
