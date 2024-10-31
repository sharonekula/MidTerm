from app.commands import Command
import pytest

class DivideCommand(Command):

    def execute(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("The DivideByZero Exception Occured")
        