#!/usr/bin/env python

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a newline for the EOF
        return True

    def do_help(self, arg):
        """Help command"""
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    if sys.stdin.isatty():
        # Interactive mode
        HBNBCommand().cmdloop()
    else:
        # Non-interactive mode
        cmd_line = sys.stdin.read()
        if cmd_line:
            HBNBCommand().onecmd(cmd_line.strip())