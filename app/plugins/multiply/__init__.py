from app.commands import Command
class MultiplyCommand(Command):

    def execute(self,x , y):
        result = x * y
        return result

