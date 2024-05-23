# commands/eof_command.py

from commands.base_command import BaseCommand

class EOFCommand(BaseCommand):
    def execute(self, arg):
        'EOF command to exit the program'
        print()
        return True
