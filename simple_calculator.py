from operator import length_hint
from tkinter import *
from tkinter.tix import COLUMN
from turtle import color

root = Tk()
root.title("Viva L'edilizia!")


e = Entry(root,width=28,borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#per passare un numero alla funzione dobbiamo passare il parametro "number" tra le parentesi della funzione
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))   #incrementa il valore da destra verso sinistra

def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num                            #salva il valore attuale al di fuori della funzione con "global"
    global operando            
    f_num = int(first_number)
    operando = "addition"                   #definisci un attributo per questa variabile
    e.delete(0, END)
    
def button_subtract():
    first_number = e.get()
    global f_num 
    global operando
    f_num = int(first_number)
    operando = "subtraction"
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global operando
    f_num = int(first_number)
    operando = "multiply"
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num 
    global operando
    f_num = int(first_number)
    operando = "divide"
    e.delete(0, END)

def button_equal():
    second_number = e.get()                                 #acquisisce il secondo valore
    e.delete(0, END)

    if operando == "addition":                              #in base all'attributo fa un determinato calcolo
        e.insert(0, int(f_num) + int(second_number))        #prende il primo valore globale, esegue l'operazione con il valore attuale dal campo di input, e riscrive all'interno del campo di input

    if operando == "subtraction":
        e.insert(0, int(f_num) - int(second_number))
    
    if operando == "multiply":
        e.insert(0, int(f_num) * int(second_number))
    
    if operando == "divide":
        e.insert(0, int(f_num) / int(second_number))


#definisci e mostra i bottoni
mybutton1 = Button(root, text="1",width=8, height=2 ,command=lambda: button_click(1)).grid(row=3, column=0) #il parametro passato alla funzione è il valore fra () nel comando
mybutton2 = Button(root, text="2",width=8, height=2 ,command=lambda: button_click(2)).grid(row=3, column=1)
mybutton3 = Button(root, text="3",width=8, height=2 ,command=lambda: button_click(3)).grid(row=3, column=2)

mybutton4 = Button(root, text="4",width=8, height=2 ,command=lambda: button_click(4)).grid(row=2, column=0)
mybutton5 = Button(root, text="5",width=8, height=2 ,command=lambda: button_click(5)).grid(row=2, column=1)
mybutton6 = Button(root, text="6",width=8, height=2 ,command=lambda: button_click(6)).grid(row=2, column=2)

mybutton7 = Button(root, text="7",width=8, height=2 ,command=lambda: button_click(7)).grid(row=1, column=0)
mybutton8 = Button(root, text="8",width=8, height=2 ,command=lambda: button_click(8)).grid(row=1, column=1)
mybutton9 = Button(root, text="9",width=8, height=2 ,command=lambda: button_click(9)).grid(row=1, column=2)

mybutton0 = Button(root, text="0",width=8, height=2 ,command=lambda: button_click(0)).grid(row=4, column=1)

mybutton_add = Button(root, text="+",width=8, height=2 ,command=button_add).grid(row=1, column=4)
mybutton_equal = Button(root, text="=",width=8, height=2 ,command=button_equal).grid(row=4, column=2)
mybutton_clear = Button(root, text="CLEAR",width=8, height=2 ,command=button_clear).grid(row=4, column=0)

mybutton_subtract = Button(root, text="-",width=8, height=2 ,command=button_subtract).grid(row=2, column=4)
mybutton_multiply = Button(root, text="*",width=8, height=2 ,command=button_multiply).grid(row=3, column=4)
mybutton_divide = Button(root, text="/",width=8, height=2 ,command=button_divide).grid(row=4, column=4)

root.mainloop()