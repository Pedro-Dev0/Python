from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV.")
        print("A TV está ligada.")

    def desligar(self):
        print("Desligando TV.")
        print("A TV está desligada.")


class ControleArcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar Condicionado.")
        print("O Ar Condicionado está ligado.")

    def desligar(self):
        print("Desligando Ar Condicionado.")
        print("O Ar Condicionado está desligado.")



controle = ControleTV()
controle_ar = ControleArcondicionado()

controle.ligar()
controle.desligar()
controle_ar.ligar()
controle_ar.desligar()


#classe abstrata - interface
"""from abc import ABC, abstractmethod
class ControleRemoto(ABC):
    @abstractmethod
"""