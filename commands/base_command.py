# commands/base_command.py

class BaseCommand:
    def execute(self, arg):
        raise NotImplementedError("You should implement this method")
