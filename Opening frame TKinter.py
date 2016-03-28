from Tkinter import *
import time
import datetime


#root=Tk()
#flag=True
#c=0
f=Frame(height=600, width=900,cursor="target")
f.pack(padx=15,pady=15)
'''
#Creacion del logo
logoimg= PhotoImage(file="logohiway.gif")
etiquetalogo=Label(f,image =logoimg)
etiquetalogo.pack(side=TOP,padx=10, pady=10)
'''

#Creacion del titulo
titulo= Label(f,text = "Realtime Monitoring", font=("Arial",15))
titulo.pack(padx=0, pady=0)

lista=Listbox(f)
lista.pack(side=BOTTOM, padx=10, pady=10)

a=raw_input()