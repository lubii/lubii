import tkinter
from msilib.schema import Class
from re import T
from tkinter import *
#from tkinter import Button, Entry, Tk,Text
#from turtle import width
#from typing import Text
from cls import Buts
root = Tk()
root.geometry("500x400")

global au

tt=Text(root,width=40,height=20,background="light blue")
tt.place(x=150,y=50)


def tt_get():
     with open("FileFolder/data_files.txt","a") as file:

        au= tt.get(1.0, tkinter.END)
        file.write(au)

def tlac():
    
    with open("FileFolder/data_files.txt","w") as file:
        au = tt.get(1.0,tkinter.END)
        file.write(au)





b1= Buts(30,50,"Zapíš",tlac)
b1.make_buts()
b2= Buts(30,80,"Pridaj",tt_get)
b2.make_buts()
b3= Buts(30,350,"Koniec",root.quit)
b3.make_buts()









root.mainloop()