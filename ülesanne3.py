from tkinter import *




aken = Tk()
aken.resizable(0,0)
aken.title('Kalkulaator')
tekst = Label(aken,
              text="Nimi: Karin eegrid\nRühm: e420\n2016",
              font = "Tahoma 16 bolt italic",
              fg="red",
              padx=2,
              pady=2)
tekst.grid(row=0, column=0, columnspan=4)



aken.mainloop()
