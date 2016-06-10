import cmd

from room import get_room

import textwrap

import shutil

import inspect

import tempfile

wrapper = textwrap.TextWrapper()
wrapper.replace_whitespace=False
wrapper.width=250

class Game(cmd.Cmd):
    
    def __init__(self):
        cmd.Cmd.__init__(self)
			
        self.dbfile = tempfile.mktemp()
        shutil.copyfile("game.db", self.dbfile) 
        hello_message=""" 
        
        You have woken up in a dark, dirty and horrible cell. The only escape is to navigate through the labyrinth of rooms.
        
        Each room has a question that if answered correclly will bring you to the next room.
        
        If all the questions are answered correctly you have completed the game succesfully. 
        
        You are then free from your underground prison and are free forever. 
        
        In order to navigate through the rooms you must select one of the displayed directions.

        The right answer to the question is the correct direction of travel to reach the end.
        
        There are six directions:
        
          North = n
          South = s
          East  = e 
          West  = w
          Up    = up 
          Down  = down
          
        Each question will only have four possible directions.
        
        One of the wrong answers will bring you back to the previous question for you to rinse and repeat.
                
        
        Would you like to start?
        
        """        
        print(hello_message)
        self.name = input()
        
        print("""
        
        %s, we shall start.
        
        """ % (self.name))
          
      
      
        self.loc = get_room(1, self.dbfile)
        
        self.look()
    
    def move(self, dir):
        ##print(self.loc) 
        inspect.getmembers(self.loc)
        newroom = self.loc._neighbor(dir)
        #print ("abcd")
        if newroom is None:
            print("You can't go that way")
        else:
            self.loc = get_room(newroom, self.dbfile)
            self.look()
            
        if newroom==29:
            print("""
            
            Thank you for playing, you have succesfully completed the game 
            
            """)
            
            exit()
          
    def use(self, args):
        print(self.loc) 
        print("Code a use function")
          
    def look(self):
        print(self.loc.name)
        print("")
        for line in wrapper.wrap(self.loc.description):
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
  