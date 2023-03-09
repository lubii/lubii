from cgitb import text
from contextlib import AsyncExitStack
from distutils import text_file
import tkinter
from tkinter import *
root=None




class Buts:
    def __init__(self,a,b,c,d,e=10):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
    def make_buts(self):
        bbts = Button(root,width=self.e,height=1,text= self.c,command=self.d)
        bbts.place(x=self.a,y=self.b)




            