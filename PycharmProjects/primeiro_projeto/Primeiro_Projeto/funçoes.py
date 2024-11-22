import os


"""
def ola():
    nome = input("Informe seu nome:")
    print(f"Olá, {nome}")

def soma(n1, n2, n3):
    resultado = n1 + n2 + n3
    print("O resultado é ", resultado)

def test_args(args_len, *args):
    if args is not None:
        print("O numero de argumentos é {0}".format(args_len))
        for arg in args:
             print(arg)

def test_kwargs(**kwargs):
    if "acao" in kwargs.keys():
        if kwargs["acao"] == "soma":
            num1 = kwargs["num1"]
            num2 = kwargs["num2"]
            return num1 + num2
"""
def get_ip():
    ip = os.popen("ipconfig")
    for linha in ip.readlines():
        if "IPv4" in linha:
            inicio = linha.find(":")
            saida = (linha[inicio + 2:-1])
    return saida


def soma(n1, n2):
    resultado = n1 + n2
    print ("O resultado é ", resultado)

def subtracao(n1, n2):
    resultado = n1 - n2
    print ("O resultado é ", resultado)

def multiplicacao(n1, n2):
    resultado = n1 * n2
    print ("O resultado é ", resultado)

def divisao(n1, n2):
    resultado = n1 / n2
    print ("O resultado é ", resultado)

def calculadora(n1, n2):
    print("1-Adiçao |"
          "2-Subtracao |"
          "3-Multiplicacao |"
          "4-Divisao |"
          "00 para encerrar")

    operacao = int(input("Informe qual o tipo de operaçao deseja realizar:"))
    while operacao != 00:
        if operacao == 1:

            soma(n1,n2)
            break

        elif operacao == 2:

            subtracao(n1, n2)
            break

        elif operacao == 3:

            multiplicacao(n1, n2)
            break

        elif operacao == 4:

            if n1 == 0 or n2 == 0:
                print("Opcao invalida")
                break
            else:
                divisao(n1, n2)
                break

        else:
            print("opcao invalida")
            break
