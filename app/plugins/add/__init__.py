from app.commands import Command

class AddCommand(Command):

    def execute(self,x , y):
        result = x + y
        return result
