from functools import partial
from tkinter import *


def bt_click(botao):
    print(botao["text"])


window = Tk()

bt1 = Button(window, width=20, text="Botão 1")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100, y=100)
bt2 = Button(window, width=20, text="Botão 2")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=130)

window.geometry("400x300+200+200")
window.mainloop()
