from contextlib import AsyncExitStack
import tkinter
from tkinter import *
root=None




class Buts:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def make_buts(self):
        bbts = Button(root,width=10,height=1,text= self.c,command=self.d)
        bbts.place(x=self.a,y=self.b)

class Entr:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def make_entr(self) :
        enttr = Entry(root,width=20) 
        enttr.place(x=self.a,y=self.b)  

            