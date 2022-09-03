#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    '''class entry point of command interpreter'''

    def __init__(self):
        '''Instantiantion'''
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "
        
    def emptyline(self):
        '''Do nothing when an emptyline is entered as input'''
        pass
    
    def do_help(self, arg: str):
        '''Built-in help function which prints documentation of each command to STDOUT'''
        return super().do_help(arg)
    
    def do_quit(self, arg):
        '''Quit command to exit the program'''
        sys.exit(1)
        
    def do_EOF(self, line):
        '''EOF condition to exit the program'''
        return True
    
    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id'''
        if arg:
            if arg in classes:
                new_instance = eval("{}()".format(classes[0]))
                new_instance.save()
            else:
                print("** class doesn't exist")
        else:
            print("** class name missing **")
    
    def do_show(self, arg):  #YET TO IMPLEMENT
        '''Prints the string representation of an instance based on the class name and id'''
        pass
    
    def do_destroy(self, arg):   #YET TO IMPLEMENT
        '''Deletes an instance based on the class name and id (save the change into the JSON file)'''
        pass

    def do_all(self, arg):   #YET TO IMPLEMENT
        ''' Prints all string representation of all instances based or not on the class name'''
        pass
    
    def do_update(self, arg):  #YET TO IMPLEMENT
        '''Updates an instance based on the class name and id by adding or updating attribute'''
        pass

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
        
