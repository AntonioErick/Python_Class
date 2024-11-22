import random

class Dados(object):
    def __init__(self):
        self.rand = random.randint(1,1000)
        self.contador = 1

    def jogo_advinha(self):
        print("Digite [-1] para encerrar o jogo.")
        while True:
            try:
                palpite = int(input("[+]Informe um numero > "))
                if palpite == -1:
                    break

            except:
                print("Erro! Valido apenas números.")

            if palpite == self.rand:
                print("__________________________________\n"
                      "     Parabéns, voce acertou!")
                break

            elif palpite < self.rand:
                print("Mais...")

            else:
                print("Menos...")

            self.contador += 1

    def __str__(self):
        return (f"__________________________________\n"
                f"       Número sorteado: {self.rand}\n"
                f"     Total de tentativas: {self.contador}")

    def __del__(self):
        print("__________________________________\n"
              "          FIM DE JOGO           \n")

resultado = Dados()
resultado.jogo_advinha()
print(resultado)