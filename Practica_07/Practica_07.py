import os
import tkinter as tk
from bitarray import bitarray
from tkinter import Tk, Label, Button,filedialog,Entry,E,W,N,S,Checkbutton,Label, Radiobutton,messagebox

SHIFT = [1, 2, 4, 6, 8, 10, 12, 14, 15, 17, 19, 21, 23, 25, 27, 28]

PC1 = [ 57,49,41,33,25,17, 9, 1,
        58,50,42,34,26,18,10, 2,
        59,51,43,35,27,19,11, 3,
        60,52,44,36,63,55,47,39,
        31,23,15, 7,62,54,46,38,
        30,22,14, 6,61,53,45,37,
        29,21,13, 5,28,20,12, 4]

PC2 = [ 14,17,11,24, 1, 5, 3,28,
        15, 6,21,10,23,19,12, 4,
        26, 8,16, 7,27,20,13, 2,
        41,52,31,37,47,55,30,40,
        51,45,33,48,44,49,39,56,
        34,53,46,42,50,36,29,32]


class CalculatorGUI:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Practica de Nidia <3")
        self.lbl_key = Label(master, text="Key", width=10)
        self.lbl_key.grid(sticky="ew")
        self.lbl_Num = Label(master, text="#Key", width=10)
        self.lbl_Num.grid(sticky="ew")
        self.ent_key = Entry(master,width = 10, text = '12341234')
        self.ent_key.grid(row=0, column=1, sticky="ew")
        self.ent_iv = Entry(master, width=10)
        self.ent_iv.grid(row=1, column=1, sticky="ew")
        self.bttn_back = Button(master,text = 'Calcular',width =10, command = self.initialPerm)
        self.bttn_back.grid(row = 2, column=1,  sticky="ew")
        self.lbl_res = Label(master, text="Subkey")
        self.lbl_res.grid(row = 3, column = 1, columnspan = 2 , sticky="ew")

    def initialPerm(self):
        if(len(self.ent_key.get()) != 8):
            messagebox.showwarning('Error!','The key most be 8 char long')
            return
        if(int(self.ent_iv.get()) > 16 and int(self.ent_iv.get()) < 1):
            messagebox.showwarning('Error!','Sub key must be between 1 and 16')
            return
        self.key = bitarray()
        self.key.frombytes(self.ent_key.get().encode('utf-8'))
        Lpart = [self.key[i-1] for i in PC1][:28]
        Rpart = [self.key[i-1] for i in PC1][28:]
        print(bitarray(Lpart))
        print(bitarray(Rpart),end='\n\n')
        for i in range(SHIFT[int(self.ent_iv.get())-1]):
            Rpart = Rpart[1:]+[Rpart[0]]
            Lpart = Lpart[1:]+[Lpart[0]]
            print(bitarray(Lpart))
            print(bitarray(Rpart),end='\n\n')
        Rpart = Lpart + Rpart
        Lpart = [Rpart[i-1] for i in PC2]
        Lpart = ['1' if x else '0' for x in Lpart]
        self.key = []


        for i in range(0,len(Lpart),8):
            self.key.append( Lpart[i:i+8])



        self.lbl_res.config( text = ' '.join(['{:02x}'.format(int(''.join(i),2)) for i in self.key]))

        

    
print(len(SHIFT))        
root = Tk()
root.geometry('400x300')
my_gui = CalculatorGUI(root)
root.mainloop()
