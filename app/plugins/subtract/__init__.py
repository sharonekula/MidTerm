from app.commands import Command

class SubtractCommand(Command):

    def execute(self):
        a = int(input("First number:"))
        b = int(input("Second number:"))
        print(f'The result of {a} - {b} = {a - b}')