import map
import lexicon
import functions
import synonyms
import cc

tokens = lexicon.tokens

## Main loop
while 1:
    playertypes = input('>')
    words = playertypes.split()
    print(words)
    sen = functions.parse(words)
    print(sen)
    s = functions.sanitize_sentence(sen)
    print(s)
    s = functions.synonymize(s)
    print("synonyms: ",s)
    functions.check_commands(s)








