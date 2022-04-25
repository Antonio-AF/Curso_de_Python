from tkinter import *


def bt_click():
    print('bt_click')

    lb["text"] = "Funcionou!!"


window = Tk()

bt = Button(window, width=20, text="OK", command=bt_click)
bt.place(x=100, y=100)

lb = Label(window, text="Teste")
lb.place(x=100, y=150)

window.geometry("400x300+250+250")
window.mainloop()
