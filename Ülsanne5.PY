from tkinter import *


    
def arvuta():
    sis = float(sisestus.get())
    kaive = var.get()
    tehe = sis * kaive
    v1.config(text=tehe)
    tehe2 = sis + tehe
    v2.config(text=tehe2)
    
    




#akna seaded
aken = Tk()
aken.title('Kalkulaator')
aken.geometry("300x170")

#sildid
maksuta = Label(aken, text="Hind käibemaksuta:")
maksuta.grid(row=0,column=0)

#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=3)

#funktsioonid
def naita_valikut():
    print(var.get())
    
silt = Label(aken, text="Käibemaksumäär:")
silt.grid(row=2,column=0)

#valikukast
var = DoubleVar()
kaive9 = Radiobutton(aken,text="9%", variable=var, value=0.09)
kaive9.grid(row=3,column=3)
kaive20 = Radiobutton(aken,text="20%", variable=var, value=0.2)
kaive20.grid(row=2,column=3,)

silt = Label(aken, text="Käibemaksumäär:")
silt.grid(row=2,column=0)

#joon
silt = Label(aken, text="________________________________________________________")
silt.grid(row=4,column=0, columnspan=5)

silt = Label(aken, text="Käibemaks:")
silt.grid(row=5,column=0)

v1 = Label(aken, text="0.00€")
v1.grid(row=5,column=1)

silt = Label(aken, text="hind käibemaksuga:")
silt.grid(row=6,column=0)

v2 = Label(aken, text="0.00€")
v2.grid(row=6,column=1)

OK = Button(aken, text="OK", width=10, command=arvuta)
OK.grid(row=8, column=3)


aken.mainloop()