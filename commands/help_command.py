# commands/help_command.py

from commands.base_command import BaseCommand

class HelpCommand(BaseCommand):
    def __init__(self, shell):
        self.shell = shell
    
    def execute(self, arg):
        'Help command to list available commands'
        self.shell.print_topics(self.shell.doc_header, self.shell.get_names(), 15, 80)
