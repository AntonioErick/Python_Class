"""
Foram anotadas as idades e alturas de x alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem
altura inferior à média de altura desses alunos.
"""

alunos = int(input("Informe a quantidade de alunos: "))
idades = []
alturas = []
altura_media = 0
abaixo_da_media = 0

for i in range(alunos):
    idade = int(input(f"Informe a idade do alunos {i + 1}: "))
    idades.append(idade)
    altura = int(input(f"Informe a altura do alunos {i + 1}: "))
    alturas.append(altura)
    altura_media += altura

altura_media /= alunos

for i in range(alunos):
    if idades[i] > 13:
        if alturas[i] < altura_media:
            abaixo_da_media += 1

print(f"{abaixo_da_media} alunos com mais de 13 anos tem altura abaixo da media")