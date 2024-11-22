from tkinter import *
import os
from tkinter import messagebox

def comandos():
    comando = messagebox.askyesno("Executar comando", "Deseja executar esse comando?")
    if comando is True:
        dados = entrada.get()
        resultado = os.popen(dados).read()
        caixa.delete('1.0', 'end')
        caixa.insert(END, resultado)


window = Tk()
window.title("Execute Command")
window.geometry("400x400")
window.resizable(False, False)

msg = Label(window, text = "Command", font= ("Arial", 14))
msg.place(x=5,y=9)

entrada = Entry(window, width=35)
entrada.place(x=100,y=16)

botao1 = Button(window, text="Send", font=("Arial", 14), command=comandos)
botao1.place(x=320,y=8)

caixa = Text(window, width=45)
caixa.pack(pady=70)

window.mainloop()