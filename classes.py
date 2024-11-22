class Funcionario(object):
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def mostrar_salario(self):
        print(f"Seu salario é {self.salario}")

    def atualizar_salario(self, salario):
        self.salario = salario

    def mostrar_funcionario(self):
        return (f"{self.nome} trabalha em {self.cargo} e ganha {self.salario}")

funcionario1 = Funcionario("erick", "estudante", 240)
funcionario1_dados = funcionario1.mostrar_funcionario()
funcionario1.mostrar_salario()
funcionario1.atualizar_salario(2500)
funcionario1.mostrar_salario()

print(funcionario1_dados)