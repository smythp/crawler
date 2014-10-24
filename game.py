import cc
import map
import lexicon
import functions
import mobs

p = mobs.p

tokens = lexicon.tokens


##print("%s is in %s." % (p.name,p.c))
##p.move('n')

while 1:
    playertypes = input('>')
    words = playertypes.split()
    sen = functions.parse(words)
    s = functions.sanitize_sentence(sen)
    functions.check_commands(s)








# debug inputs
##    if len(s) == 0:
##        print('no input')
##    else:
##        yzz = ""
##        for zzz in range(0,len(s)):
##            yzz = yzz + s[zzz] + ' '
##        print(yzz)




##
##sentence = ['xxx','xxx','xxx']
##
##
##d_counter,n_counter,v_counter = 0,0,0
##
##
##functions.sanitize_sentence(sentence)
##
##print(sentence)
##
##print('''
##
##''')
##
##print(d_counter,v_counter,n_counter)
