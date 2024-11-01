from app.commands import Command

class SubtractCommand(Command):

    def execute(self,x , y):
        result = x - y
        return result

