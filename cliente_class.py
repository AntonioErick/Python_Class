from socket import *
from threading import *

def main():
    client = socket(AF_INET, SOCK_STREAM)

    try:
        client.connect(("localhost",2222))
    except:
        print("\nImpossivel conectar-se ao servidor!\n")

    username = input("Usuario> ")
    print("\nUsuario conectado!")

    t1 = Thread(target=receber_mensagem, args=[client])
    t2 = Thread(target=enviar_mensagem, args=[client, username])

    t1.start()
    t2.start()

def receber_mensagem(client):
    while True:
        try:
            msg = client.recv(2048).decode()
            print(msg+"\n")
        except:
            print("\nErro! Cliente nao conectado.")
            print("\nDigite [ENTER] para continuar...")

def enviar_mensagem(client, username):
    try:
        msg = input("\n")
        client.send(f"<{username}> {msg}".encode())
    except:
        return

main()
