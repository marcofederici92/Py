from tkinter import *
from turtle import color

root = Tk()


def myclick():
    mylabel = Label(root, text="Viva L'edilizia!").grid(row=1, column=1)


mybutton = Button(root, text="click me!",fg="blue",bg="red" ,command=myclick).grid(row=0, column=0)

root.mainloop()