class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("O motor foi ligado.")
        
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas):
        super().__init__(cor, placa, numero_rodas)
        # Você pode adicionar atributos ou métodos específicos para caminhão aqui
    def carregar_carga(self, carregando):
        if carregando:
            print("O caminhão está carregando carga.")
        else:
            print("O caminhão não está carregando carga.")


moto = Motocicleta("Vermelha", "XYZ-1234", 2)
carro = Carro("Azul", "ABC-5678", 4)
caminhao = Caminhao("Branco", "DEF-9012", 6)

moto.ligar_motor()
carro.ligar_motor()
caminhao.ligar_motor()
caminhao.carregar_carga(True)

print(f"Motocicleta: Cor={moto.cor}, Placa={moto.placa}, Rodas={moto.numero_rodas}")
print(f"Carro: Cor={carro.cor}, Placa={carro.placa}, Rodas={carro.numero_rodas}")
print(f"Caminhão: Cor={caminhao.cor}, Placa={caminhao.placa}, Rodas={caminhao.numero_rodas}")

