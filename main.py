import _tkinter
from msilib.schema import Class
from tkinter import Button, Tk
from cls import Buts,Entr
root = Tk()
root.geometry("600x600")




def tlac():
    print("ahoj")        


b1= Buts(20,20,"aaa",tlac)
b1.make_buts()
b2= Buts(20,50,"bbb",tlac)
b2.make_buts()

ent1 = Entr(150,50)
ent1.make_entr()







root.mainloop()