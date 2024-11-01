from app.commands import Command
from data.history import HistoryManager

class ExitCommand(Command):

    def execute(self):
        raise SystemExit