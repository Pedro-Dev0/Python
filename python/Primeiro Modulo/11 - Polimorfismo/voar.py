class Passaro:
    def voar(self):
        print("O pássaro está voando.")
    
class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("A avestruz não pode voar.")

class Aviao(Passaro):
    def voar(self):
        print("O avião está decolando.")

# como fazer o uso do polimorfismo no avestruz? 
def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Avestruz())  # Output: A avestruz não pode voar.
plano_de_voo(Pardal())  # Output: O pássaro está voando
plano_de_voo(Aviao())   # Output: O avião está decolando.

    

# polimorfismo é a capacidade de diferentes classes responderem ao mesmo método de maneiras distintas.
