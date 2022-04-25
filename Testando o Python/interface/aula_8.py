from tkinter import *


def bt_onclick():
    print((ed.get()))
    lb["text"] = ed.get()


window = Tk()

ed = Entry(window)
ed.place(x=100, y=100)

bt = Button(window, width=20, text="OK", command=bt_onclick)
bt.place(x=100, y=150)

lb = Label(window, text="Label")
lb.place(x=100, y=200)

window.geometry("400x300+200+200")
window.mainloop()
