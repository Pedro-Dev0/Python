from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV.")
        print("A TV está ligada.")

    def desligar(self):
        print("Desligando TV.")
        print("A TV está desligada.")

    @property
    def marca(self):
        return "Samsung"


class ControleArcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar Condicionado.")
        print("O Ar Condicionado está ligado.")

    def desligar(self):
        print("Desligando Ar Condicionado.")
        print("O Ar Condicionado está desligado.")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle_ar = ControleArcondicionado()

controle.ligar()
controle.desligar()
controle_ar.ligar()
controle_ar.desligar()

print(f"Marca da TV: {controle.marca}")
print(f"Marca do Ar Condicionado: {controle_ar.marca}")

#classe abstrata - interface
"""from abc import ABC, abstractmethod
class ControleRemoto(ABC):
    @abstractmethod


    classe abstrata obriga sua classe filha a implementar os métodos abstratos definidos na classe mãe.   

    já na herença simples, a classe filha pode ou não implementar os métodos da classe mãe.

    em classe abstrata só fazemos sentido em si dos contratos e é implementado em suas classes filhas as regras enquanto a classe mãe não tem implementação concreta e somente define os métodos abstratos que devem ser implementados.

"""

"""
property - decorador que transforma métodos em atributos 
serve para encapsulamento de atributos e controle de acesso a eles além de permitir a criação de atributos computados e derivados, explicando melhor isso seria um atributo que não é armazenado diretamente, mas é calculado com base em outros atributos ou estados do objeto.
"""