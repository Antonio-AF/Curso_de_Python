from tkinter import  *

window = Tk()

lb1 = Label(window, text="Label 1", bg="green")
lb2 = Label(window, text="Label 2", bg="red")
lb3 = Label(window, text="Label 3", bg="blue")
lb4 = Label(window, text="Label 4", bg="yellow")

lb1.pack()
lb2.pack()
lb3.pack(side=LEFT)
lb4.pack(side=BOTTOM)

window.geometry("400x400+200+200")
window.mainloop()
