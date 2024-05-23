# HBNB Command Shell
The HBNB Command Shell is a command-line interface (CLI) application designed to handle various commands interactively and non-interactively. It is built using Python's cmd module and is structured in a modular, tree-like format, ensuring clear separation of functionality and easy maintainability.

## Directory Structure

hbnb_console/
├── console.py
├── commands/
│   ├── __init__.py
│   ├── base_command.py
│   ├── eof_command.py
│   ├── help_command.py
│   └── quit_command.py
## Description of Files
console.py:

Purpose: The main entry point of the shell application.
Functionality: Initializes the shell, integrates command classes, and handles both interactive and non-interactive modes.
commands/init.py:

Purpose: Marks the commands directory as a Python package.
Functionality: Typically empty but necessary for package recognition.
commands/base_command.py:

Purpose: Defines a base class for all command classes.
Functionality: Provides an abstract execute method that must be implemented by all subclasses.
commands/quit_command.py:

Purpose: Implements the quit command.
Functionality: Exits the shell when the quit command is issued.
commands/eof_command.py:

Purpose: Implements the EOF command.
Functionality: Exits the shell upon receiving an EOF signal (e.g., Ctrl-D).
commands/help_command.py:

Purpose: Implements the help command.
Functionality: Displays a list of available commands and their descriptions.
## Usage
Interactive Mode: Start the shell and manually input commands.


$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) quit
$
Non-Interactive Mode: Pass commands via standard input.


$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
This modular and structured approach ensures that the shell is extendable and easy to manage, allowing for the addition of new commands with minimal changes to the existing codebase.