from app.commands import CommandHandler, Command
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand

class App:
    def __init__(self):
        self.registry = CommandHandler()

        self.registry.register_command('add', AddCommand())
        self.registry.register_command('subtract', SubtractCommand())
        self.registry.register_command('multiply', MultiplyCommand())
        self.registry.register_command('divide', DivideCommand())
        self.registry.register_command('exit', ExitCommand())

    def start(self):
        print("Welcome to the my MID TERM PROJECT _ REPL CALCULATOR")
        while True:
            user_input = input("Enter Add, Subtract, Multiply, Divide or 'exit'\n").lower()

            if user_input in self.registry.commands and user_input!= 'exit':
                a, b = map(int, input("Enter two numbers separated by a space: ").split())
                result = self.registry.execute_command(user_input, a, b)
                print(f"Result : {result}")
            elif user_input == 'exit':
                self.registry.execute_command(user_input)
            else:
                print(f"Unknown Command: {user_input}")