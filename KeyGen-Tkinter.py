__author__ = 'Guilherme'

import random
import Tkinter
from Tkconstants import *

# Inicializacao de variaveis
inp = 0
list_crypt = []
list_gen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_key = [0] * len(list_gen)
list_key_final = ""

f = open('Keys.txt', 'a+')
f.write("\n")
f.write("           Algoritmo de Geracao de Keys - v.1 \n")
f.write("                Desenvolvido por Hollweg      \n")
f.write("                Ultimo update em 10/2016      \n")
f.write('\n')
f.write('\n')
f.close()

# algoritmo de geracao de matriz
def geraMatriz ():
    global list_gen
    list_gen = [random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                random.randint(0,9), random.randint(0,9), random.randint(0,9), \
                random.randint(0,9)]
    return list_gen

# algoritmo de geracao de senha
def algoritmoSenha ():
    global list_key
    for indice_lista in range(0, len(list_gen)):
        list_key[indice_lista] = (list_gen[indice_lista]^2) %2
    return list_key

# Geracao da Cripto
# Truncagem dos valores em int e conversao de base para hex
def criptoSenha():
    global list_key
    global list_key_final
    global inp

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
def geraKeys ():
    global inp
    global crypt
    global list_crypt

    i = 0
    for i in range(0, int(inp)):
        matriz = geraMatriz()
        algoritmo = algoritmoSenha()
        crypt = criptoSenha()

        while crypt == None:
            matriz = geraMatriz()
            algoritmo = algoritmoSenha()
            crypt = criptoSenha()

        list_crypt.append (crypt)
        f = open('Keys.txt', 'a+')
        f.write("Key #")
        f.write(str(i))
        f.write("  :  ")
        f.write(crypt)
        f.write('\n')
        f.close()

# Manipulador para o botao Gera Matriz
def printaMatriz():
    global list_gen
    geraMatriz()
    print list_gen

# Manipulador para o botao Gerar Algoritmo
def printaAlgoritmo():
    algoritmoSenha()
    print list_key

# Manipulador para o botao Gerar Cripto
def printaCripto():
    crypt = criptoSenha()
    print crypt

# Manipulador o botao GeraKeys
def createKeys ():
    geraKeys()

# Manipulador do botao Reset
def resetKeys ():
    list_crypt = []
    pass

def selecvalor():
    global entry_1
    global inp
    inp = entry_1.get()

def InitFrame(master):
    global frame

    frame = Tkinter.Frame(master, relief = RIDGE, borderwidth = 2)
    frame.pack(fill = BOTH, expand = 1)
    tk.title ("Teste")

class Buttons:
    def __init__(self):
        global frame

        self.button_geraMatriz = Tkinter.Button(frame, text = "Seleciona Valor", fg = "red", command = selecvalor)
        self.button_geraMatriz.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_geraMatriz.place (x = 10, y = 40)

        self.button_geraMatriz = Tkinter.Button(frame, text = "Gerar Matriz", fg = "red", command = printaMatriz)
        self.button_geraMatriz.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_geraMatriz.place (x = 10, y = 40)

        self.button_geraCript = Tkinter.Button(frame, text = "Gerar Cripto",fg = "red",command = printaAlgoritmo)
        self.button_geraCript.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_geraCript.place (x = 10, y = 70)

        self.button_geraAlg = Tkinter.Button(frame, text = "Gerar Algoritmo",fg = "red", command = printaCripto)
        self.button_geraAlg.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_geraAlg.place (x = 10, y = 100)

        self.button_geraKeys = Tkinter.Button(frame, text = "Gerar Keys",fg = "red",command = createKeys)
        self.button_geraKeys.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_geraKeys.place (x = 10, y = 130)

        self.button_Reset = Tkinter.Button(frame, text = "Reset",fg = "red",command = tk.destroy)
        self.button_Reset.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_Reset.place (x = 10, y = 160)

        self.button_exit = Tkinter.Button(frame, text = "Exit",fg = "red",command = tk.destroy)
        self.button_exit.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_exit.place (x = 10, y = 190)

class Entries:
    def __init__ (self):
        global frame
        global entry_1

        label_1 = Tkinter.Label(frame, text = "Numero de Keys:")
        label_1.grid (row = 0)
        label_1.pack(side = LEFT)

        entry_1 = Tkinter.Entry(frame)
        entry_1.insert (0, "por exemplo: 10")
        entry_1.grid (row = 0, column = 1)
        entry_1.pack (side = LEFT)


tk = Tkinter.Tk()
InitFrame(tk)
Entries()
Buttons()

tk.mainloop()