from tkinter import *
from tkinter import messagebox

def b1_func():
    entrada.insert(END, '1')

def b2_func():
    entrada.insert(END, '4')

def b3_func():
    entrada.insert(END, '7')

def b4_func():
    if True:
        conteudo = entrada.get('1.0', END)
        conteudo = conteudo[:-2]
        entrada.delete('1.0', END)
        entrada.insert('1.0', conteudo)

def b5_func():
    entrada.insert(END, '2')

def b6_func():
    entrada.insert(END, '3')

def b7_func():
    entrada.insert(END, "+")

def b8_func():
    entrada.insert(END, '5')

def b9_func():
    entrada.insert(END, '6')

def b10_func():
    entrada.insert(END, "-")

def b11_func():
    entrada.insert(END, '8')

def b12_func():
    entrada.insert(END, '9')

def b13_func():
    entrada.insert(END, "*")

def b14_func():
    entrada.insert(END, '0')

def b15_func():
    #entrada.insert(END, "=")
    conteudo = entrada.get('1.0', END).strip()
    resultado = eval(conteudo)
    caixa.delete('1.0', END)
    caixa.insert(END, resultado)

def b16_func():
    entrada.insert(END, "/")

window = Tk()
window.title("Calculadora")
window.geometry("300x300")
window.resizable(False, False)

entrada = Text(window, width=23, height=1)
entrada.place(x=5, y=5)

caixa = Text(window, width=11, height=1)
caixa.place(x=200, y=5)

b1 = Button(window, width=7, height=3, text = "1", command= b1_func)
b1.place(x=5, y=27)

b2 = Button(window, width=7, height=3, text = "4", command= b2_func)
b2.place(x=5, y=94)

b3 = Button(window, width=7, height=3, text = "7", command= b3_func)
b3.place(x=5, y=160)

b4 = Button(window, width=7, height=3, text = "Clear", command= b4_func)
b4.place(x=5, y=227)

b5 = Button(window, width=7, height=3, text = "2", command= b5_func)
b5.place(x=80, y=27)

b6 = Button(window, width=7, height=3, text = "3", command= b6_func)
b6.place(x=155, y=27)

b7 = Button(window, width=7, height=3, text = "+", command= b7_func)
b7.place(x=230, y=27)

b8 = Button(window, width=7, height=3, text = "5", command= b8_func)
b8.place(x=80, y=94)

b9 = Button(window, width=7, height=3, text = "6", command= b9_func)
b9.place(x=155, y=94)

b10 = Button(window, width=7, height=3, text = "-", command= b10_func)
b10.place(x=230, y=94)

b11 = Button(window, width=7, height=3, text = "8", command= b11_func)
b11.place(x=80, y=160)

b12 = Button(window, width=7, height=3, text = "9", command= b12_func)
b12.place(x=155, y=160)

b13 = Button(window, width=7, height=3, text = "*", command= b13_func)
b13.place(x=230, y=160)

b14 = Button(window, width=7, height=3, text = "0", command= b14_func)
b14.place(x=80, y=227)

b15 = Button(window, width=7, height=3, text = "=", command= b15_func)
b15.place(x=155, y=227)

b16 = Button(window, width=7, height=3, text = "/", command= b16_func)
b16.place(x=230, y=227)

window.mainloop()