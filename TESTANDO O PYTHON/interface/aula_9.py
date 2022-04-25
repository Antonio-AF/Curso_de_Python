# Capturando e procesando valores

from tkinter import *

window = Tk()


def bt_click():
    print("bt_click")
    if not str(ed1.get()).isnumeric() or not str(ed2.get()).isnumeric():
        lb["text"] = "Valores informados inválidos."
    else:
        num1 = int(ed1.get())
        num2 = int(ed2.get())

        lb["text"] = num1 + num2


ed1 = Entry(window)
ed1.place(x=60, y=100)
ed2 = Entry(window)
ed2.place(x=200, y=100)

bt = Button(window, width=20, text="SOMA", command=bt_click)
bt.place(x=100, y=165)

lb = Label(window, text="Resultado", fg="red")
lb.place(x=100, y=200)

window.geometry("400x300+250+250")
window.mainloop()
