#!/usr/bin/python3
'''
console.py
AirBnB command interpreter
- quit: Exits the cmd
- EOF: Exits (Ctrl+D)
- <empty line>: Does nothing
Usage:
./console.py
'''
import cmd
import re
from shlex import split

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
    def do_quit(self,arg):
        '''
        Exit cmd
        Usage: quit
        '''
        return True
    
if __name__ =='__main__':
    HBNBCommand().cmdloop()
