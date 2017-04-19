
# Python Key Generator - Tk Inter
# Developed by Guilherme Hollweg - Electrical Engineer

# Using PEP 8 -- Style Guide for Python Code
# https://www.python.org/dev/peps/pep-0008/
# Last Modified on 18/04/2017 (PEP 8 format)

__author__ = 'Guilherme'

import random
import Tkinter
from Tkconstants import *

# Vars initialization
inp = 0
listCrypt = []
listGen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
listKey = [0] * len(listGen)
listKeyFinal = ""

f = open('Keys.txt', 'a+')
f.write("\n")
f.write("             Key Generation Algorithm - v.1 \n")
f.write("                  Developed by Hollweg      \n")
f.write("              Last Modified on 18/04/2017   \n")
f.write('\n')
f.write('\n')
f.close()


# Matrix generation algorithm
def matrix_generation ():
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
def key_algorithm ():
    global listKey

    for indList in range(0, len(listGen)):
        listKey[indList] = (listGen[indList] ^ 2) % 2

    return listKey


# Cryptography generation
# Int trunking and conversion to hex(base)
def password_crypt():
    global listKey, listKeyFinal, inp
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
def generate_keys ():
    global inp, crypt, listCrypt

    for i in range(0, int(inp)):
        matrix = matrix_generation()
        algorithm = key_algorithm()
        crypt = password_crypt()

        while crypt == None:
            matrix = matrix_generation()
            algorithm = key_algorithm()
            crypt = password_crypt()

        listCrypt.append (crypt)
        f = open('Keys.txt', 'a+')
        f.write("Key #")
        f.write(str(i))
        f.write("  :  ")
        f.write(crypt)
        f.write('\n')
        f.close()


# Generate Matryx button manipulator
def print_matrix():
    global listGen

    matrix_generation()
    print listGen


# Generate Algorithm button manipulator
def print_algorithm():
    key_algorithm()
    print listKey


# Generate Crypt button manipulator
def print_crypt():
    crypt = password_crypt()
    print crypt


# Generate Keys button manipulator
def create_keys ():
    generate_keys()


# Reset button manipulator
def reset_keys ():
    listCrypt = []
    pass


def select_val():
    global firstEntry, inp

    inp = firstEntry.get()


def frame_init(master):
    global frame

    frame = Tkinter.Frame(master, relief = RIDGE, borderwidth = 2)
    frame.pack(fill = BOTH, expand = 1)
    tk.title ("Test")


class Buttons:
    def __init__(self):
        global frame

        self.button_matrix_generation = Tkinter.Button(frame, text = "Select Value", fg = "red", command = select_val)
        self.button_matrix_generation.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_matrix_generation.place (x = 10, y = 40)

        self.button_matrix_generation = Tkinter.Button(frame, text = "Generate Matrix", fg = "red", command = print_matrix)
        self.button_matrix_generation.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_matrix_generation.place (x = 10, y = 40)

        self.button_geraCript = Tkinter.Button(frame, text = "Generate Crypt",fg = "red",command = print_algorithm)
        self.button_geraCript.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_geraCript.place (x = 10, y = 70)

        self.button_geraAlg = Tkinter.Button(frame, text = "Generate Algorithm",fg = "red", command = print_crypt)
        self.button_geraAlg.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_geraAlg.place (x = 10, y = 100)

        self.button_generate_keys = Tkinter.Button(frame, text = "Generate Keys",fg = "red",command = create_keys)
        self.button_generate_keys.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_generate_keys.place (x = 10, y = 130)

        self.button_Reset = Tkinter.Button(frame, text = "Reset",fg = "red",command = tk.destroy)
        self.button_Reset.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_Reset.place (x = 10, y = 160)

        self.button_exit = Tkinter.Button(frame, text = "Exit",fg = "red",command = tk.destroy)
        self.button_exit.pack(padx = 5, pady = 6, ipadx = 6, ipady = 6, side = LEFT)
        #self.button_exit.place (x = 10, y = 190)


class Entries:
    def __init__ (self):
        global frame, firstEntry

        firstLabel = Tkinter.Label(frame, text = "Keys Number:")
        firstLabel.grid (row = 0)
        firstLabel.pack(side = LEFT)

        firstEntry = Tkinter.Entry(frame)
        firstEntry.insert (0, "example: 10")
        firstEntry.grid (row = 0, column = 1)
        firstEntry.pack (side = LEFT)


tk = Tkinter.Tk()
frame_init(tk)
Entries()
Buttons()

tk.mainloop()