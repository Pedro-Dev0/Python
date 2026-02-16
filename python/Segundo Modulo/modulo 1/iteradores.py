# iteradores ajudam a percorrer coleções de dados de forma eficiente
# iteradores são objetos que implementam o protocolo de iteração, ou seja, possuem os métodos __iter__() e __next__() 
# iteráveis são objetos que podem ser iterados, ou seja, podem retornar um iterador, como listas, tuplas, dicionários e conjuntos
# um iterador mantém o estado da iteração, permitindo que você percorra os elementos um por um, sem precisar carregar todos os elementos na memória de uma vez

# exemplo de iterador personalizado

class Iterador:
    def __init__(self, numeros):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:  
            raise StopIteration

for numero in Iterador([1, 2, 3, 4, 5]):
    print(numero)