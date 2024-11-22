import random

class Jogo(object):
    def __init__(self):
        self.pc = 0
        self.user = 0

    def jogo(self, user_choice):
        op = random.choice(["pedra", "papel", "tesoura"])

        print(f"[User:{user_choice}][PC:{op}]")

        if op == "pedra" and user_choice == "tesoura":
            self.pc += 1
            print(f"[User {self.user}][PC {self.pc}]")
        elif op == "tesoura" and user_choice == "papel":
            self.pc += 1
            print(f"[User {self.user}][PC {self.pc}]")
        elif op == "papel" and user_choice == "pedra":
            self.pc += 1
            print(f"[User {self.user}][PC {self.pc}]")
        elif user_choice == "pedra" and op == "tesoura":
            self.user += 1
            print(f"[User {self.user}][PC {self.pc}]")
        elif user_choice == "tesoura" and op == "papel":
            self.user += 1
            print(f"[User {self.user}][PC {self.pc}]")
        elif user_choice == "papel" and op == "pedra":
            self.user += 1
            print(f"[User {self.user}][PC {self.pc}]")
        else:
            print("Empate!")

    def termino(self):
        if self.pc == 5 or self.user == 5:
            return True
        else:
            return False

    def __del__(self):
        print("__________________________________\n"
              "          FIM DE JOGO           \n")

ppt = Jogo()
while not ppt.termino():
    user_choice = input("Your turn: ")
    ppt.jogo(user_choice)

