# metodos de classe apontam para a classe em si e podem acessar variáveis de classe
# métodos estáticos não apontam para a classe nem para a instância e não podem acessar variáveis de classe ou de instância diretamente
# além disso, métodos estáticos são usados para funcionalidades que não dependem do estado da classe ou da instância e não podem mudar a classe ou a instância

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def multiplicar(a, b):
        return a * b
    
# Usando os métodos estáticos
resultado_soma = Matematica.somar(5, 3)
resultado_multiplicacao = Matematica.multiplicar(4, 6)
print(f"Soma: {resultado_soma}, Multiplicação: {resultado_multiplicacao}")


class Pessoa:
    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, {Pessoa.idade_maior_ou_menor(self.idade)}"

    @staticmethod
    def idade_maior_ou_menor(idade):
        if idade >= 18:
            return "Maior de idade"
        else:
            return "Menor de idade"
# Criando uma instância da classe Pessoa
# retorne informando que é maior ou menor de idade usando o método estático
pessoa1 = Pessoa("Carlos", 20)

print(pessoa1)  # Nome: Carlos, Idade: 20

#status_idade = Pessoa.idade_maior_ou_menor(pessoa1.idade)
#print(f"{pessoa1.nome} é {status_idade}")  # Carlos é Maior de idade

# if e else ali continua sendo um metódo estático, pois não depende do estado da classe ou da instância e somente usa o valor passado como argumento para determinar o resultado da condição imposta que é se a idade é maior ou menor de idade...