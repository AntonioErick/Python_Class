from threading import *
from socket import *

clients = []

def main():
    server = socket(AF_INET, SOCK_STREAM)
    try:
        server.bind(("localhost", 2222))
        server.listen(5)
    except:
        return print("\nNao foi possível iniciar o servidor!\n")

    while True:
        client, addr = server.accept()
        clients.append(client)

    thread = Thread(target=message_treatment, args=[client])
    thread.start()

def message_treatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            delete_client(client)
            break

def broadcast(msg, client):
    for client_item in clients:
        if client_item != client:
            try:
                client_item.send(msg)
            except:
                delete_client(client_item)

def delete_client(client):
    clients.remove(client)




main()