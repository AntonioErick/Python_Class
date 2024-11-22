import random

try:
    retomar = int(input("Deseja retomar o progresso anterior? |1-SIM|2-NAO|\n"))
except:
    print("Informe um número!")

if retomar == 1:
    save = open("memorycard.txt", "r")
    dados = save.read()
    dados = dados.split("|")
    rand = int(dados[0])
    contador = int(dados[1])
    save.close()
else:
    rand = random.randint(1,1000)
    contador = 0

#sites = open("sites.txt", "r+")
#urls = []
#print(rand)

print("Digite 'S' caso queira salvar seu progresso.")

while True:
    palpite = (input("Informe o numero sorteado:"))

    if palpite == "S":
        save = open("memorycard.txt", "w")
        save.write(f"{rand}|{contador}")
        save.close()
        exit(0)

    palpite = int(palpite)

    if palpite == rand:
        print("Acertou!")
        break
    elif palpite > rand:
        print("O numero informado é maior que o sorteado\n")
        contador += 1
    else:
        print("O numero informado é menor que o sorteado\n")
        contador += 1

print("O numero de tentativas foi:", contador+1)

""""
for linha in sites.readlines():
    if "http" in linha:
        url = linha[linha.find("http"): -1]
        urls.append(url)
print(urls)"""