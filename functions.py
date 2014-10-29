import lexicon
import mobs

tokens = lexicon.tokens


def check_commands(s):
    try:
        print(s[0])
        if s[0] == 'GO' and s[1] in tokens['DIRECTIONS']:
            mobs.p.move((s[1]).lower())
            print('walking ',s[1].lower())
        elif s[0] == 'LOOK' and 'L':
            print("You're at the ",mobs.p.c)
        else:
            print("Can't do that!")
    except IndexError:
        print("Index Error")




def sanitize_sentence(sentence):
    try:
        while 1:
            if 'xxx' in sentence:
                sentence.remove('xxx')
            else:
                break
        return sentence
    except ValueError:
        return sentence

def parse(words):
    sentence = ['xxx','xxx','xxx']
    for word in words:
        if word.upper() in tokens['DIRECTIONS']:
            if sentence[1] == 'xxx':
                sentence[1] = word.upper()
        if word.upper() in tokens['VERBS']:
            if sentence[0] == 'xxx':
                sentence[0] = word.upper()
        if word.upper() in tokens['NOUNS']:
            if sentence[2] == 'xxx':
                sentence[2] = word.upper()
    return(sentence)



def debug_parse(words):
    sentence = ['xxx','xxx','xxx']
    for word in words:
        if word.upper() in tokens[0][1]:
            print(word,' is a direction')
            print('putting it in the sentence')
            if sentence[1] == 'xxx':
                sentence[1] = word.upper()
                print(sentence)
        if word.upper() in tokens[1][1]:
            print(word,' is a verb')
            print('putting it in the sentence')
            if sentence[0] == 'xxx':
                sentence[0] = word.upper()
                print(sentence)
        if word.upper() in tokens[2][1]:
            print(word,' is a noun')
            print('putting it in the sentence')
            if sentence[2] == 'xxx':
                sentence[2] = word.upper()
                print(sentence)
    return(sentence)
