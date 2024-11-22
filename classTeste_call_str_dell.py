class Pessoa(object):
    #Distribui as variáveis pelo codigo
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

    #Facilita na hora de chamar, pois pode ser chamado diretamente com um 'print'
    def __str__(self):
        return (f"Meu nome é {self.nome} e tenho {self.idade} anos.")

    #Chama a variável diretamente com os parentes 'p1()', sem a necessidade de usar 'print(p1)'
    def __call__(self, *args, **kwargs):
        print("ISSO É IMPORTANTE!")

    #Sempre será executado no final do programa
    def __del__(self):
        print("__________________________________\n"
              "       Isso é tudo pessoal.       \n"
              "__________________________________")

p1 = Pessoa("ERICK", 20)
#p1.mostrar_dados()
print(p1)
p1()