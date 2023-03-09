import tkinter
from msilib.schema import Class
from re import T
from tkinter import *
from turtle import width
#from tkinter import Button, Entry, Tk,Text
#from turtle import width
#from typing import Text
from cls import Buts
root = Tk()
xy =["500x400","500x450","500x500","500x550","500x600"]

f=0

root.geometry(xy[f])
w=40;h=20
global au

tt=Text(root,width=w,height=h,background="light blue")
tt.place(x=150,y=50)


def tt_get():
     with open("FileFolder/data_files.txt","a") as file:

        au= tt.get(1.0, tkinter.END)
        file.write(au)

def tlac():
    
    with open("FileFolder/data_files.txt","w") as file:
        au = tt.get(1.0,tkinter.END)
        file.write("")

def big():
    global f,h,w
    if f<4:
        f+=1
        w=40;h=h+3
    root.geometry(xy[f])
    
    tt.config(width=w,height=h)
    

def min():
    global f,h,w
    if f>0:
        f-=1
        w=40;h=h-3
    root.geometry(xy[f])
    
    tt.config(width=w,height=h)
    



b1= Buts(30,50,"Zapíš",tlac)
b1.make_buts()
b2= Buts(30,80,"Pridaj",tt_get)
b2.make_buts()
b3= Buts(30,350,"Koniec",root.quit)
b3.make_buts()




b4= Buts(150,12,"+",big,3)
b4.make_buts()
    
b5= Buts(180,12,"-",min,3)
b5.make_buts()







root.mainloop()