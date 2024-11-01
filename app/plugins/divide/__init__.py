from app.commands import Command

class DivideCommand(Command):

    def execute(self):
        a = int(input("First number:"))
        b = int(input("Second number:"))
        if (b != 0):
            print(f'The result of {a} / {b} = {a / b}')
        else:
            print("DivisionByZero Exception")