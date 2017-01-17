#imports
import collections

import string

#Basic caesar cipher
def caesar(text,shift):
    alp = string.ascii_lowercase
    alphabet = collections.deque(alp)
    #key
    alphabet.rotate(-shift)
    alphabet = "".join(list(alphabet))
    #map every letter to the alphabet variable
    return text.translate(str.maketrans(alp, alphabet))

def vigenere(sent, key):
    try: #to avoid error confusion...
        #list comprehension
        sent = [x for x in sent]
        #list comprehension to encrypt th text based on the shift and key
        encrypt = [caesar(sent[x], key[x]) for x in range(len(sent))]
        #turn the encrypted list into a string
        joinit = ''.join(encrypt)
        #display prettty
        disp = "Your Vigenere Cipher: %s" % (joinit)
        print("")
        return disp
    except IndexError:
        raise IndexError("Your Key is shorter or longer than the message...:/")

print(vigenere("Python", [19,22,4,6,9,20]))




        

