#!/usr/bin/python3
'''HolbertonBnB command interpreter'''
import cmd
import re
from datetime import datetime
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def parse(self, arg):
        curly_braces = re.search(r"\{(.*?)\}", arg)
        brackets = re.search(r"\[(.*?)\]", arg)
        if curly_braces is None:
            if brackets is None:
                return [i.strip(",") for i in arg.split()]
            else:
                lexer = (arg[:brackets.span()[0]]).split()
                retl = [i.strip(",") for i in lexer]
                retl.append(brackets.group())
                return retl
        else:
            lexer = (arg[:curly_braces.span()[0]]).split()
            retl = [i.strip(",") for i in lexer]
            retl.append(curly_braces.group())
            return retl

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = self.parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(argl[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Usage: show <class> <id>
        Display the string representation of a class instance of a given id.
        """
        argl = self.parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        else:
            obj = storage.get(argl[0], argl[1])
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        argl = self.parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        else:
            obj = storage.get(argl[0], argl[1])
            if obj is None:
                print("** no instance found **")
            else:
                storage.delete(obj)
                storage.save()

    def do_all(self, arg):
        """Usage: all [class]
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        if len(arg) > 0 and arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = storage.all(arg)
            print([str(obj) for obj in obj_list])

    def do_count(self, arg):
        """Usage: count <class>
        Retrieve the number of instances of a given class."""
        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = storage.all(arg)
            print(len(obj_list))

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair."""
        argl = self.parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        else:
            obj = storage.get(argl[0], argl[1])
            if obj is None:
                print("** no instance found **")
                return
            if len(argl) == 2:
                print("** attribute name missing **")
            elif len(argl) == 3:
                print("** value missing **")
            else:
                setattr(obj, argl[2], argl[3])
                storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

