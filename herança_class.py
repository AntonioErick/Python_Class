class Funcionario(object):
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.nome = cargo
        self.salario = salario

    def mostrar_salario(self):
        print(self.salario)

class Chefe(Funcionario):
    def mostrar_salario(self):
        print("Informaçao confidencial")

    def mostrar_chefe(self):
        print("I'm the boss")

emp = Chefe("Erick", "CEO", 100000)
emp2 = Funcionario("Erick", "CEO", 100000)
emp.mostrar_salario()
emp2.mostrar_salario()