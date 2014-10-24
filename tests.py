import cc
import lexicon
import map

tokens = lexicon.tokens

playertypes = input('>')
words = playertypes.split()


d_counter = 0
n_counter = 0
v_counter = 0

for word in words:
    if word.upper() in tokens[0][1]:
        print(word,' is a direction')
        d_counter += 1
    if word.upper() in tokens[1][1]:
        print(word,' is a verb')
        v_counter += 1
    if word.upper() in tokens[2][1]:
        print(word,' is a noun')
        n_counter += 1
print(d_counter,v_counter,n_counter)
