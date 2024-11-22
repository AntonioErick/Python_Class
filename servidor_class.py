from socket import *

class Servidor(object):
    def __init__(self):
        self.servidor = socket(AF_INET, SOCK_STREAM)
        self.servidor.bind(("localhost", 2222))
        self.servidor.listen()

    def aceitar(self):
        self.cliente, addr = self.servidor.accept()

    def __call__(self, *args, **kwargs):
        self.cliente.sendall("Bem Vindo".encode())
        while True:
            dados = self.cliente.recv(2048).decode()
            print(dados)

            dados = input("\n[+]")
            self.cliente.sendall(f"<Server> {dados}".encode())

srv = Servidor()
srv.aceitar()
srv()
