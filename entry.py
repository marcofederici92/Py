from operator import length_hint
from tkinter import *
from tkinter.tix import COLUMN
from turtle import color

root = Tk()


#campo di input, non posso fare .pack (da capire perche)
e = Entry(root,width=30,bg="white",fg="black",borderwidth=5)
e.grid(row=0, column=0)
e.insert(0, "enter your name")       #inserisce il valore di default


#definisco una funzione che si chiama myclick,  all'interno dico che hello è l'insieme di "hello"+ "e" che sarebbe l'input entry
def myclick():
    hello = "Hello " + e.get()
    #definisco una label che mi visualizza il contenuto di "hello"
        #nota in text per richiamare una variabile inserirla senza "" altrimenti scrive quello che è fra le ""
    mylabel = Label(root, text = hello).grid(row=2, column=0)

#definisco un bottone che al click richiama la funzione "myclick"    
mybutton = Button(root, text="scrivi il tuo nome",fg="blue",bg="white" ,command=myclick).grid(row=1, column=0)


root.mainloop()