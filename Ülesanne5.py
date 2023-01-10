from tkinter import *

def arvuta():
    sis = sisestus.get()
    kaive = KM.get()
    print(hind)

#akna seaded
aken = Tk()
aken.title('Kalkulaator')
aken.geometry("300x300")

#funktsioonid
...

#sildid
silt = Label(aken, text="Nimi:")
silt.grid(row=0,column=0)

valjund = Label(aken, text="Siia tuleb tervitus")
valjund.grid(row=2,columnspan=3)

#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#nupud
nupp1 = Button(aken, text="Tervita", width=10, command=tervita)
nupp1.grid(row=1, column=1)

#funktsioonid
def tervita():
    nimi = sisestus.get()
    print("Tere " +nimi)
    valjund.config(text="Tere "+nimi)

KM = IntVar()

valikukast = Radiobutton(aken,text="Valik 1", variable=KM, value=0.09)
valikukast.grid(row=1, column=1,sticky="w")
valikukast = Radiobutton(aken,text="Valik 1", variable=KM, value=0.2)
valikukast.grid(row=2, column=1,switcky="w")

joon = Label(aken,
             text"e",
             font="tahoma 12",
             padx=2,
             pady=2)
joon.grid(row=3, column=9, columnspan=2)

tekst = Label(aken,
             text="0.00€",
             font="tahoma 12",
             padx=2,
             pady=2)
hind.grid(row=5  column=1, sticky="w")

ok = Button(aken, text="7", width=4, font = "Tahoma 12 ")
ok.grid(row=6, column=0,padx=2,pady=2)



aken.mainloop()
