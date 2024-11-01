from app.commands import CommandRegistry, Command
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand
from app.commands import CommandRegistry

class App:
    
    def __init__(self):

        self.registry = CommandRegistry()
        self.registry.register_command('add', AddCommand())
        self.registry.register_command('subtract', SubtractCommand())
        self.registry.register_command('multiply', MultiplyCommand())
        self.registry.register_command('divide', DivideCommand())
        self.registry.register_command('exit', ExitCommand())

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue
    
    def execute(self, command, *args):
        if command != 'exit' and command in self.registry.commands:
            return self.registry.commands[command].execute(*args)
        elif command == 'exit':
            return self.registry.commands[command].execute(*args)
        else:
            raise ValueError(f"Command '{command}' not found.")
    
    def start(self):
        history = []
        app = App()
        print("Welcome to the my MID TERM PROJECT _ REPL CALCULATOR")
        while True:
            command = input("Enter Command to Perform Operation - Add , Subtract , Multiply , Divide\n").lower()
            if command != 'exit' and command in self.registry.commands:
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    result = app.execute(command, a, b)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Error: {e}")
            elif command == "exit":
                 app.execute(command)
            else:
                print("Command Not Found!")
