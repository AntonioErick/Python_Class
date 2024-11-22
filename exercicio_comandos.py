import os


#from funçoes import get_ip
#print(get_ip())

ip = os.popen("ipconfig")
for linha in ip.readlines():
    if "IPv4 Address" in linha:
        inicio = linha.find(":")
        print = linha[inicio+2:-1]
        break

comandos = []

for i in range(5):
    comando = input("Informe um comando (digite \"sair\" para sair):")
    if comando == "sair":
        break
    comandos.append(comando)

print("[*] Executando os comandos...")

for comando in comandos:
    if os.system(comando) == 0:
        print(f"[+] Comando {comando} executado com sucesso.")
    else:
        print(f"[-] Comando {comando} falhou.")
