import os
import tkinter as tk
from PIL import Image, ImageTk
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from tkinter import Tk, Label, Button,filedialog,Entry,E,W,N,S,Checkbutton,Label, Radiobutton,messagebox

class CipherGUI:
    def __init__(self, master):
        self.encMode = None
        self.algorithm = None
        self.keyVal = None
        self.inVect = None
        self.master = master
        self.master.title("Practica de Nidia <3")
        self.lbl_key = Label(master, text="Key", width=10)
        self.lbl_key.grid(sticky="ew")
        self.lbl_iv = Label(master, text="IV", width=10)
        self.lbl_iv.grid(sticky="ew")
        self.ent_key = Entry(master,width = 10)
        self.ent_key.grid(row=0, column=1, sticky="ew")
        self.ent_iv = Entry(master, width=10)
        self.ent_iv.grid(row=1, column=1, sticky="ew")

        self.bttn_ECB = Button(master, text="ECB",
                                command=self.encryptECB)
        self.bttn_ECB.grid(row=3, column=0, sticky="nsew")
        self.bttn_CBC = Button(master, text="CBC",
                               command=self.changeCBC)
        self.bttn_CBC.grid(row=3, column=1, sticky="nsew")
        self.bttn_OFB = Button(master, text="OFB",
                               command=self.changeOFB)
        self.bttn_OFB.grid(row=4, column=0, sticky="nsew")
        self.bttn_CFB= Button(master, text="CFB",
                                command=self.changeCFB)
        self.bttn_CFB.grid(row=4, column=1, sticky="nsew")
        self.encrypting =True 
        self.bttn_Mode = Button(master, text="Encrypting",
                               command=self.changeMode)
        self.bttn_Mode.grid(row=5, column=0, columnspan=2)

        self.bttn_Open = Button(master, text="Open Image", command=self.openFilePath)
        self.bttn_Open.grid(row=5, column=2, sticky="nsew")
        self.bttn_Save = Button(master, text="Save", command=self.saveFilePath)
        self.bttn_Save.grid(row=5, column=3, sticky="nsew")
        self.label_image = Label(root)
        self.setImagePath('./japan.bmp')
        self.label_image.grid(row=0, column=2, columnspan=2, rowspan=5,
               sticky=W+E+N+S, padx=5, pady=5)

    def updateImage(self,p):
        self.thumbnail = Image.open(p)
        self.thumbnail = self.thumbnail.resize(
            (self.thumbnail.size[0], self.thumbnail.size[1]))
        self.tki = ImageTk.PhotoImage(self.thumbnail)
        self.label_image.configure(image = self.tki)
    
    def setImage(self,img):
        self.tki = ImageTk.PhotoImage(img)
        self.label_image.configure(image = self.tki)

    def setImagePath(self,p):
        self.thumbnail = Image.open(p)
        self.tki = ImageTk.PhotoImage(self.thumbnail)
        self.label_image.configure(image = self.tki)

    def openFilePath(self):
        filename = filedialog.askopenfilename(initialdir="./", title="Select file")
        if filename == None:
            return
        self.updateImage(filename)            
            
    def saveFilePath(self):
        filename = filedialog.asksaveasfilename(defaultextension=".bmp")
        if filename == None:
            return
        self.thumbnail.save(filename,format = 'BMP')

    def getkey(self):
        if len(self.ent_key.get())!=8:
            messagebox.showwarning('','Key value must be 8 characters long ♥')
            return None
        else:
            return bytes(self.ent_key.get(),'utf-8')

    def getiv(self):
        if len(self.ent_iv.get()) != 8:
            messagebox.showwarning('', 'I Vector value must be 8 characters long ♥')
            return None 
        else:
            return bytes(self.ent_key.get(), 'utf-8')

    def changeMode(self):
        if self.encrypting:
            self.bttn_Mode.configure(text = 'Decrypting')
        else:
            self.bttn_Mode.configure(text = 'Encrypting')
        self.encrypting = not self.encrypting

    def encryptECB(self):
        key = self.getkey()
        if key == None:
            return
        cipher = Cipher(algorithms.TripleDES(key),
                        modes.ECB(), backend=default_backend())
        if self.encrypting:
            enc = cipher.encryptor()
            ct = enc.update(self.thumbnail.tobytes()) + enc.finalize()
        else:
            dec = cipher.decryptor()
            ct = dec.update(self.thumbnail.tobytes()
                                  ) + dec.finalize()
        self.thumbnail = Image.frombytes(data = ct,
            mode=self.thumbnail.mode, size=self.thumbnail.size)
        self.setImage(self.thumbnail)
        
    
    def changeCBC(self):
        key = self.getkey()
        if key == None:
            return
        iv = self.getiv()
        if iv == None:
            return
        cipher = Cipher(algorithms.TripleDES(key),
                        modes.CBC(iv), backend=default_backend())
        if self.encrypting:
            enc = cipher.encryptor()
            ct = enc.update(self.thumbnail.tobytes()) + enc.finalize()
        else:
            dec = cipher.decryptor()
            ct = dec.update(self.thumbnail.tobytes()
                            ) + dec.finalize()
        self.thumbnail = Image.frombytes(data=ct,
                                         mode=self.thumbnail.mode, size=self.thumbnail.size)
        self.setImage(self.thumbnail)
    
    def changeOFB(self):
        key = self.getkey()
        if key == None:
            return
        iv = self.getiv()
        if iv == None:
            return
        cipher = Cipher(algorithms.TripleDES(key),
                        modes.OFB(iv), backend=default_backend())
        if self.encrypting:
            enc = cipher.encryptor()
            ct = enc.update(self.thumbnail.tobytes()) + enc.finalize()
        else:
            dec = cipher.decryptor()
            ct = dec.update(self.thumbnail.tobytes()
                                  ) + dec.finalize()
        self.thumbnail = Image.frombytes(data=ct,
                                         mode=self.thumbnail.mode, size=self.thumbnail.size)
        self.setImage(self.thumbnail)

    def changeCFB(self):
        key = self.getkey()
        if key == None:
            return
        iv = self.getiv()
        if iv == None:
            return
        cipher = Cipher(algorithms.TripleDES(key),
                        modes.OFB(iv), backend=default_backend())
        if self.encrypting:
            enc = cipher.encryptor()
            ct = enc.update(self.thumbnail.tobytes()) + enc.finalize()
        else:
            dec = cipher.decryptor()
            ct = dec.update(self.thumbnail.tobytes()
                            ) + dec.finalize()
        self.thumbnail = Image.frombytes(data=ct,
                                         mode=self.thumbnail.mode, size=self.thumbnail.size)
        self.setImage(self.thumbnail)
        
root = Tk()
my_gui = CipherGUI(root)
root.mainloop()
