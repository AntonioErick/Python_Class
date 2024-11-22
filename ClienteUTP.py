from threading import *
from socket import *

def main():

    client = socket(AF_INET, SOCK_STREAM)

    try:
        client.connect(("localhost", 2222))
    except:
        print("\nimpossivel conectar-se ao servidor!\n")

    username = input("Usuario: ")
    print("\nConcetado\n")

    thread1 = Thread(target=receber_mensagem, args=[client])
    thread2 = Thread(target=enviar_mensagem, args=[client, username])
    thread1.start()
    thread2.start()

def receber_mensagem(client):
    while True:
        try:
            msg = client.recv(2048).decode()
            print(msg+'\n')
        except:
            print("\nNao foi possivel permanecer conectado ao servidor!\n")
            print("Pressione <Enter> para continuar...")
            client.close()
            break

def enviar_mensagem(client, username):
    while True:
        try:
            msg = input("\n")
            client.send(f"<{username}> {msg}".encode())
        except:
            return


main()