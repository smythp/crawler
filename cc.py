## crawlerclasses
import functions

class Room(object):
    lookup = {}
    def __init__(self,name,point):
        self.name = name
        self.point = point
        Room.lookup[point] = (name,self)
    i = []

class Mob(object):
    def __init__(self,name,c):
        self.name = name
        self.c = c
    def check_move(self,direction):
        u = functions.update_direction(direction,self.c)
        if u in Room.lookup.keys():
            return True
        else:
            return False
    def move(self,direction):
        u = functions.update_direction(direction,self.c)
        if u in Room.lookup.keys():
            self.c = u
        else:
            print('no go')
            return False

    i = []

class Player(Mob):
    def __init__(self,name,c):
        self.name = name
        self.c = c

########################
## Instantiate mobs ####
########################

p = Player('Patrick',(5,5))
















##    def currentexits(self):
##        return currentloc.exits
    
##    def go():
##        
##
##    moves = {
##        'n': gonorth(),
##        's': gosouth(),
##        'e': goeast(),
##        'w': gowest(),
##    }
