class Carros(object):
    def __init__(self, marca, km, ano):
        self.marca = marca
        self.km = km
        self.ano = ano

    def alterar_km(self, km):
        self.km = km
        return self.km

    def informacoes(self):
        print(f"____________________\n"
              f"|Marca: {self.marca}\n"
              f"|Km rodados: {self.km}\n"
              f"|Ano: {self.ano}\n"
              f"____________________\n")

carro1 = Carros("Palio", 3000, 1999 )
carro1.informacoes()
novo_km = carro1.alterar_km(12000)
print("Atualizando informaçoes...")
carro1.informacoes()
