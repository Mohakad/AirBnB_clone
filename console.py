#!/usr/bin/python3

"""
Module console

Contain class Console
"""

import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file_path = "file.json"
    all_classes = {"BaseModel": BaseModel}

    def do_EOF(self, args):
        """EXIT command to exit the program"""
        return True
    
    def do_help(self, args):
        """Show help message"""
        if args == 'quit':
            print("Quit command to exit the program\n")
        elif args == 'EOF':
            print("EXIT command to exit the program\n")
        elif args == 'help':
            print("Show help message\n")
        else:
            super().do_help(args)

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        elif args not in self.all_classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.all_classes[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Print the string representation of an instance"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            all_instances = self.load_instances()
            if key in all_instances:
                print(all_instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            all_instances = self.load_instances()
            if key in all_instances:
                del all_instances[key]
                self.save_instances(all_instances)
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Print all string representations of instances"""
        args_list = args.split()
        all_instances = self.load_instances()
        if not args_list:
            print([str(obj) for obj in all_instances.values()])
        elif args_list[0] not in self.all_classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_instances.items() if args_list[0] in key])

    def do_update(self, args):
        """Update an instance based on the class name and id"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            all_instances = self.load_instances()
            if key in all_instances:
                obj = all_instances[key]
                attribute_name = args_list[2]
                attribute_value = args_list[3]
                setattr(obj, attribute_name, attribute_value)
                obj.save()
            else:
                print("** no instance found **")

    def load_instances(self):
        """Load instances from the JSON file"""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_instances(self, all_instances):
        """Save instances to the JSON file"""
        with open(self.file_path, 'w') as file:
            json.dump(all_instances, file)

if __name__ == '__main__':
    HBNBCommand().cmdloop()    
