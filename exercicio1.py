#questao3
n1 = int(input("informe um numero: "))
n2 = int(input("infrome outro numero: "))
soma = n1 + n2
print(soma)
n3 = int(input("insira um valor que seja menor que a soma dos valores anterior: "))
if n3 > soma:
    print("erro")
else:
    print("certo")

#questao2
texto = input("Informe sua linguagem de programaçao favorita: ")

if texto != "python":
    print("erro")
else:
    print("certo")

#questao1
n1 = int(input("informe um numero: "))
n2 = int(input("infrome outro numero: "))

if n1 > n2:
    print("o maior numero é: ", n1)

elif n1 == n2:
    print("os dois valores sao iguais")

else:
    print("o maior numero é: ", n2)

