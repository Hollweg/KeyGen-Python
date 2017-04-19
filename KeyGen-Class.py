
# Python Key Generator 
# Developed by Guilherme Hollweg - Electrical Engineer

# Using PEP 8 -- Style Guide for Python Code
# https://www.python.org/dev/peps/pep-0008/
# Last Modified on 18/04/2017 (PEP 8 format)

import random
import Tkinter
from Tkconstants import *

# Vars initialization
listCrypt = []
listGen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
listKey = [0] * len(listGen)
listKeyFinal = ""


class KeyGeneration(object):    
    
    # Matrix generation algorithm
    def matrix_generation (self):
        global listGen
        listGen = [random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9), \
                   random.randint(0,9)]

        return listGen


    # Key generation algorithm
    def key_algorithm (self):
        global listKey

        for indList in range(0, len(listGen)):
            listKey[indList] = (listGen[indList] ^ 2) % 2
        
        return listKey


    # Cryptography generation
    # Int trunking and conversion to hex(base)
    def password_crypt(self):
        global listKey, listKeyFinal

        listKeyFinal = ""
        for indList in range(0, len(listKey)):
            listKeyFinal += str(listKey[indList])

        crypt = hex(int (listKeyFinal))
        crypt = crypt.replace ("0x", "")
        crypt = crypt.replace ("a", "A")
        crypt = crypt.replace ("b", "B")
        crypt = crypt.replace ("c", "C")
        crypt = crypt.replace ("d", "D")
        crypt = crypt.replace ("e", "E")
        crypt = crypt.replace ("f", "F")

        if len(crypt) < 10:
            return

        return crypt


    # Keys generation according with user input number
    def generate_keys (self, numKey):
        global crypt, listCrypt
        
        for i in range(0, int(numKey)):
            KeyGen = KeyGeneration()
            matrix = KeyGen.matrix_generation()
            algorithm = KeyGen.key_algorithm()
            crypt = KeyGen.password_crypt()

            while crypt == None:
                matrix = KeyGen.matrix_generation()
                algorithm = KeyGen.key_algorithm()
                crypt = KeyGen.password_crypt()
            
            listCrypt.append (crypt)
            print crypt

            f = open('Keys.txt', 'a+')
            f.write("Key #")
            f.write(str(i))
            f.write("  :  ")
            f.write(crypt)
            f.write('\n')
            f.close()


KeyGen = KeyGeneration()
print KeyGen.generate_keys(5)         
