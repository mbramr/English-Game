import cmd

from room import get_room

import textwrap

import shutil

import inspect

import tempfile

class Game(cmd.Cmd):
    
    def __init__(self):
        cmd.Cmd.__init__(self)
			
        self.dbfile = tempfile.mktemp()
        shutil.copyfile("game.db", self.dbfile) 
        
        print("Hello weary traveller. My name is Zork. What is your name?")
        self.name = input()
        
        print("Nice to meet you %s" % (self.name))
          
      
      
        self.loc = get_room(1, self.dbfile)
        
        self.look()
    
    def move(self, dir):
        print(self.loc) 
        inspect.getmembers(self.loc)
        newroom = self.loc._neighbor(dir)
        #print ("abcd")
        if newroom is None:
            print("You can't go that way")
        else:
            self.loc = get_room(newroom, self.dbfile)
            self.look()
            
        if newroom==13:
            exit()
          
    def use(self, args):
        print(self.loc) 
        print("Code a use function")
          
    def look(self):
        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)
    
    def do_up(self, args):
        """Go up"""
        self.move('up')
        
    def do_down(self, args):
        """Go down"""
        self.move('down')
    
    
    
    
    def do_n(self, args):
        """Go north"""
        self.move('n')

    def do_s(self, args):
        """Go south"""
        self.move('s')

    def do_e(self, args):
        """Go east"""
        self.move('e')

    def do_w(self, args):
        """Go west"""
        self.move('w')     
    
    def do_save(self, args):
        """Save the game"""
        shutil.copyfile(self.dbfile, args)
        print("The game was saved to {O}".format(args))
      
    def do_quit(self, args):
        """Leaves the game"""
        print("Thank you for playing")
        return True	
    def do_xyssy(self, args):
        print('''A hollow voice says, "This isnt Frotran..."''')
        
    def do_use(self, args):
        """Specify a tool from your backpack"""
        self.use(args)
        
if __name__ == "__main__":
 
  g = Game()
  g.cmdloop()
  