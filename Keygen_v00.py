''' 
Python Key Generator
desenvolvido por: Guilherme Hollweg
Data: 04/06/2015
Ultima modificacao: 10/08/2015
'''    

import random
#import Tkinter
#from Tkconstants import *

#inicializacao de variaveis
list_crypt = []
list_gen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_key = [0] * len(list_gen)
list_key_final = ""

class KeyGeneration(object):    
    
    # algoritmo de geracao de matriz
    def geraMatriz (self):
        global list_gen
        list_gen = [random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                    random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                    random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                    random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                    random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                    random.randint(0,9)]
        return list_gen

    # algoritmo de geracao de senha
    def algoritmoSenha (self):
        global list_key
        for indice_lista in range(0, len(list_gen)):
            list_key[indice_lista] = (list_gen[indice_lista]^2) %2
        return list_key

    # Geracao da Cripto
    # Truncagem dos valores em int e conversao de base para hex
    def criptoSenha(self):
        global list_key
        global list_key_final

        list_key_final = ""
        for indice_lista in range(0, len(list_key)):
            list_key_final += str(list_key[indice_lista])
        crypt = hex(int (list_key_final))
        crypt = crypt.replace ("0x", "")
        crypt = crypt.replace ("a", "A")
        crypt = crypt.replace ("b", "B")
        crypt = crypt.replace ("c", "C")
        crypt = crypt.replace ("d", "D")
        crypt = crypt.replace ("e", "E")
        crypt = crypt.replace ("f", "F")

        if len(crypt) <10:
            return
        return crypt

    # Geracao de Keys de acordo com o numero
    # de entrada fornecido pelo usuario
    def geraKeys (self, numKey):
        global crypt
        global list_crypt
        i = 0
        
        for i in range(0, int(numKey)):
            KeyGen = KeyGeneration()
            matriz = KeyGen.geraMatriz()
            algoritmo = KeyGen.algoritmoSenha()
            crypt = KeyGen.criptoSenha()

            while crypt == None:
                matriz = KeyGen.geraMatriz()
                algoritmo = KeyGen.algoritmoSenha()
                crypt = KeyGen.criptoSenha()
            
            list_crypt.append (crypt)
            print crypt
            #f = open('Keys.txt', 'a+')
            #f.write("Key #")
            #f.write(str(i))
            #f.write("  :  ")
            #f.write(crypt)
            #f.write('\n')
            #f.close()

KeyGen = KeyGeneration()
print KeyGen.geraKeys(5)         
