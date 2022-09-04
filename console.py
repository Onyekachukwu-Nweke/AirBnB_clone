#!/usr/bin/python3
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    '''class entry point of command interpreter'''

    def __init__(self):
        '''Instantiantion'''
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    classes = ["BaseModel", "User", "Place", "State",
               "City", "Amenity", "Review"]

    def emptyline(self):
        '''Do nothing when an emptyline is entered as input'''
        pass

    def do_help(self, arg: str):
        '''
        Built-in help function which prints
        documentation of each command to STDOUT
        '''
        return super().do_help(arg)

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        sys.exit(1)

    def do_EOF(self, line):
        '''EOF condition to exit the program'''
        return True

    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        '''
        if arg:
            args = arg.split()
            if args[0] in HBNBCommand.classes:
                new_instance = eval("{}()".format(args[0]))
                print(new_instance.id)
                new_instance.save()
            else:
                print("** class doesn't exist")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        '''
        Prints the string representation of an instance
        based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            if args[0] in classes:
                objects = models.storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key not in objects.keys():
                    print("** no instance found **")
                else:
                    print(objects[key])
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            if args[0] in classes:
                objects = models.storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key not in objects.keys():
                    print("** no instance found **")
                else:
                    del objects[key]
                    models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        '''
        Prints all string representation of all
        instances based or not on the class name
        '''
        args = arg.split()
        objects = models.storage.all()
        to_print = []
        if len(args) == 0:
            for v in objects.values():
                to_print.append(str(v))
        elif args[0] in classes:
            for k, v in objects.items():
                if args[0] in k:
                    to_print.append(str(v))
        else:
            print("** class doesn't exist **")
        print(to_print)

    def do_update(self, arg):
        '''
        Updates an instance based on the class name
        and id by adding or updating attribute
        '''
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            # Type checking
            if isinstance(eval(args[3]), int):
                args[3] = int(args[3])
            elif isinstance(eval(args[3]), float):
                args[3] = float(args[3])
        except NameError:
            args[3] = args[3]

        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
