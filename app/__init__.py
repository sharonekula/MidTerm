import pkgutil
import importlib
import os
import logging
import logging.config
from dotenv import load_dotenv
from data.history import HistoryManager
from data.csv import CsvCommand
from app.commands import CommandHandler, Command

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.info, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.info(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.ERROR(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        self.load_plugins()
        logging.info("Application started. REPL Calculator")
        print("Enter command to perform operation Add Subtract Multiply Divide or 'exit' to Exit")
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
                            message = "Exiting the calculator After Saving to csv."
                            logging.info(message)
                            print(message)
                        elif option == "N":
                            message = "Exiting the calculator Without Saving."
                            logging.info(message)
                            print(message)

                    self.command_handler.execute_command(cmd_input)
                try:
                    num1, num2 = map(float, input("Enter two numbers space-separated: ").split())
                    result = self.command_handler.execute_command(cmd_input, num1, num2, self.history_manager)
                    print(f"Result of {cmd_input} operation between {num1} and {num2} is: {result}")
                except KeyError:
                    logging.ERROR(f"Unknown command: {cmd_input}")
                    print("Command Not Found")
                    sys.exit(1)
        except KeyboardInterrupt:
            logging.info("Application interrupted")
            sys.exit(0)
        finally:
            print("Application shutdown.")
