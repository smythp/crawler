import cc

##cc.Room("warehouse",{'n':'house','w':'pond'})
##cc.Room("pond",{'e':'warehouse'})
##cc.Room("house",{'s':'warehouse'})
##




import random

b_type = ('inn','house','lodge')
adj = ('ugly','old','run-down','red','green','yellow','modern')

def randomname():
    return ("%s %s" % (random.choice(adj),random.choice(b_type)))


lx = [x + 1 for x in range(0,10)]
ly = [y + 1 for y in range(0,10)]
lxy = []

for x in range(0,len(lx)):
    for y in range(0,len(ly)):
        lxy.append((lx[x],ly[y]))


for point in lxy:
    point = cc.Room('%s' % (randomname()),point)

##print(cc.Room.lookup)


