## crawlerclasses


class Room(object):
    lookup = {}
    def __init__(self,name,exits):
        self.name = name
        self.exits = exits
        Room.lookup[name] = self
    i = []

class Mob(object):
    def __init__(self,name,c):
        self.name = name
        self.c = c
    def move(self,direction):
        if direction in Room.lookup[self.c].exits:
            self.c = Room.lookup[self.c].exits[direction]

    i = []

class Player(Mob):
    def __init__(self,name,c):
        self.name = name
        self.c = c
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
