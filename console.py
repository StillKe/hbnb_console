import cmd
import sys
from commands.quit_command import QuitCommand
from commands.eof_command import EOFCommand
from commands.help_command import HelpCommand

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def __init__(self):
        super().__init__()
        self.commands = {
            'quit': QuitCommand(),
            'EOF': EOFCommand(),
            'help': HelpCommand(self)
        }
    
    def default(self, line):
        cmd, arg, line = self.parseline(line)
        if cmd in self.commands:
            result = self.commands[cmd].execute(arg)
            if result:
                return result
        else:
            print(f"*** Unknown syntax: {line}")

    def emptyline(self):
        'Do nothing on empty input line'
        pass

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        print()
        return True

if __name__ == '__main__':
    hbnb_cmd = HBNBCommand()
    if sys.stdin.isatty():
        # Interactive mode
        hbnb_cmd.cmdloop()
    else:
        # Non-interactive mode
        hbnb_cmd.cmdloop(stdin=sys.stdin)