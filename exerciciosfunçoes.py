"""#import funçoes
#funçoes.ola()
from funçoes import ola, soma, test_args, test_kwargs
#ola()
#soma(2,8,10)
resultado = test_kwargs(acao="soma",num1=28, num2=32)
print(f"Funciona: {resultado}")"""

from funçoes import calculadora, soma, subtracao, divisao, multiplicacao

while True:
    n1 = int(input("Digite um numero:"))
    n2 = int(input("Digite outro numero:"))
    calculadora(n1, n2)
    continuar = input("deseja continuar(S/N)?")
    if continuar == 'N':
        print("Encerradno...")
        break