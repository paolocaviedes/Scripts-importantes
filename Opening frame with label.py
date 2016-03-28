from Tkinter import *
import time

f=Frame(height=600, width=900, cursor="target")

f.pack(padx=15,pady=15)

#logoimg= PhotoImage(file="logohiway.gif")
#etiquetalogo=Label(f,image =logoimg)
#etiquetalogo.pack(side=TOP,padx=10, pady=10)

titulo= Label(f,text = "Harnes -- Hiway", font=("Arial",15))

titulo.pack(side=TOP, padx=10, pady=10)

lista=Listbox(f)
lista.pack(side=BOTTOM, padx=10, pady=10)

time.sleep(3)
f.mainloop()