import os
import pkgutil
import importlib
import sys
from data.history import HistoryManager
from data.csv import CsvCommand
from app.commands import CommandHandler, Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            print(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    print(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                print(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        self.load_plugins()
        print("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    history = self.history_manager.get_history()
                    if len(history) > 0:
                        option = input("Do you want to save the history? Y or N :\n")
                        if option == "Y":
                            csv_run = CsvCommand(history)
                            csv_run.execute()
                            print("Exiting the calculator After Saving to csv.")
                        elif option == "N":
                            print("Exiting the calculator Without Saving.")

                    self.command_handler.execute_command(cmd_input)
                try:
                    num1, num2 = map(float, input("Enter two numbers space-separated: ").split())
                    result = self.command_handler.execute_command(cmd_input, num1, num2, self.history_manager)
                    print(f"Result of {cmd_input} operation between {num1} and {num2} is: {result}")
                except KeyError:
                    print(f"Unknown command: {cmd_input}")
                    sys.exit(1)
        except KeyboardInterrupt:
            print("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            print("Application shutdown.")
