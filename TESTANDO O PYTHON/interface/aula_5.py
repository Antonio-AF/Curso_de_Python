from tkinter import *


window = Tk()

lb = Label(window, text="Fala galera!!") # Criando uma Label
lb.place(x=100, y=100) # Determinando o Layout a ser usado.


window.geometry("300x300+200+200")
window.mainloop()