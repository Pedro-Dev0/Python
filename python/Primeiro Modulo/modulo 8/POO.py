class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        return "Biiiiiiiii"
    
    def parar(self):
        return "A bicicleta parou"
    
    def correr(self):
        return "A bicicleta está correndo"
    
b2 = bicicleta("vermelha", "mountain bike", 2020, 1500)
print(b2.buzinar())
print(b2.parar())
print(b2.correr())

b2.buzinar()