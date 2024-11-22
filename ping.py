import os
from threading import *

clientes = []
threads = []
lock = Lock()

def get_ip():
    ip = os.popen("ipconfig")
    for linha in ip.readlines():
        if "IPv4" in linha:
            inicio = linha.find(":")
            saida = (linha[inicio + 2:-1])
    return saida

def scanner(endereco_ip, clientes, lock):
    resultado = os.popen("ping {0} -n 1".format(endereco_ip)).read()
    if "TTL" in resultado:
        with lock:
            clientes.append(endereco_ip)
            print(endereco_ip)

meu_ip = get_ip()
rede = meu_ip[:meu_ip.rfind(".")+1]

for item in range(1,255):
    teste = rede + str(item)
    thread = Thread(target=scanner,args=[teste, clientes, lock])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(clientes)

