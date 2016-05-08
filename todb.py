import sys
import sqlite3
import os
import os.path

def main(dnmae):
    con = sqlite3/connect(dbname)
    
    con.execute("CREATE TABLE IF NOT EXISTS rooms(id INTEGER PRIMARY KEY, json TEXT NOT NULL)")
    con.commit()
     
    for filname in os.listdir():
        base, extension = os.path. splitext(filename)
        if extension == '.json':
            with open(filename, 'r') as f:
                json = f.read()
                
                print("Inserting room{0}".format(int(base)))
                
                con. execute("INSERT OR REPLACE INTO rooms(id, json) VALUES(?, ?);",
                                                                                (int(base), json))
                con.commit()
                
    con.close()
    

  if __name__ == "__main__":
      if len(sys.argv) != 2:
          print('Usage: {0} <databasename>' .format(sys.argv[0]))
      else:
          main(sys.argv[1])