from app.commands import Command

class ExitCommand:

    def execute(self):
        print("Exiting.....")
        raise SystemExit