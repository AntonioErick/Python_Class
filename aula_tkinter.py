from tkinter import *
from tkinter import messagebox

def nova_janela():
    top = Toplevel()
    top.title("Novo arquivo")
    top.geometry("250x250")
    top.resizable(False, False)
    texto = Label(top, text="Whatsapp 2", font=("Arial Black", 20))
    texto.pack(pady=20)

def sair():
    window.destroy()
def envio():
    #messagebox.showinfo("questao1","Lindo, tesao, bonito e gostosao")
    #resultado = messagebox.askretrycancel("questao1", "Lindo, tesao, bonito e gostosao")
    resultado = messagebox.askyesno("questao1", "Lindo, tesao, bonito e gostosao")
    if resultado is True:
        dados = entrada.get()
        texto.insert(END, dados)

window = Tk()
window.title("Whatsapp 2")#titulo
window.geometry("500x500")#tamanho da janela
#window.iconbitmap("wpp2.ico")
window.resizable(False, False)#nao permite o usuario alterar o tamanho

#Imprimir mensagem de texto
msg = Label(window, text = "Nome", font=("Arial Black", 14))
msg.place(x=15, y=5)

#Espaço para o usuario digitar alguma informaçao
entrada = Entry(window, width= 55)
entrada.place(x=85, y=13)

#Botao
botao1 = Button(window, text="ENVIAR",font=("Arial Black", 10), command=envio)
botao1.place(x=425, y=8)

#Lista com opcoes
lb1 = Listbox(window, selectmode=MULTIPLE)
lb1.insert(1, "Dragon Ball Z")
lb1.insert(2, "One Piece")
lb1.insert(3, "Avatar")
lb1.insert(4, "Naruto")
lb1.insert(5, "Cowboy Bebop")
lb1.insert(6, "Vinland Saga")
lb1.insert(7, "Cyberpunk")
lb1.place(x=25, y=50)

#Espaço onde pode ser inserido textos
texto = Text(window, width=20)
texto.place(x=180, y=50)

#barra de tarefas
tasks = Menu(window)
new_item = Menu(tasks)
new_item.add_command(label="new", command=nova_janela)
new_item.add_separator()
new_item.add_command(label="edit")
new_item.add_separator()
new_item.add_command(label="exit", command=sair)

tasks.add_cascade(label="opçao", menu=new_item)
window.config(menu=tasks)
window.mainloop()