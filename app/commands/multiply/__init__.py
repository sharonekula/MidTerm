
from app.commands import Command

class MultiplyCommand(Command):

    def execute(self, a, b):
        return a * b
        
