from socket import *

cliente = socket(AF_INET, SOCK_DGRAM)

while True:
    dados =  input("Cliente: ")

    if dados == "sair":
        cliente.sendto(dados.encode(), ("localhost", 3333))
        cliente.close()
        break

    cliente.sendto(dados.encode(), ("localhost", 3333))
    dados, servidor = cliente.recvfrom(2048)
    print(dados.decode())