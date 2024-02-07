import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()    
