from socket import *

servidor = socket(AF_INET, SOCK_DGRAM)
servidor.bind(("localhost", 3333))

while True:
    print("Esperando conexao")
    dados, cliente = servidor.recvfrom(2048)
    print(dados.decode())

    if dados.decode() == "sair":
        servidor.close()
        break
    dados = input("Servidor: ")
    servidor.sendto(dados.encode(), cliente)