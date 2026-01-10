# construtores e destrutores em Python com POO(Programação Orientada a Objetos)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"{self.nome} foi registrada em sistema...")

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    def __del__(self):
        print(f"{self.nome} foi removida do sistema...")

p1 = Pessoa("Ana", 30)
p2 = Pessoa("Bruno", 25)    
print(p1.saudacao())
print(p2.saudacao())

del p1
del p2