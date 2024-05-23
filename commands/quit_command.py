# commands/quit_command.py

from commands.base_command import BaseCommand

class QuitCommand(BaseCommand):
    def execute(self, arg):
        'Quit command to exit the program'
        return True
