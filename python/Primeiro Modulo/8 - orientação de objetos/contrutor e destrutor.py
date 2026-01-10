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
del p1

p2 = Pessoa("Bruno", 25)    
print(p2.saudacao())
del p2


#explique tudo nesse código 
# Neste código, estamos definindo uma classe chamada Pessoa que representa uma pessoa com atributos nome e idade.
# A classe possui um construtor (__init__) que é chamado automaticamente quando um novo objeto da classe é criado.
# O construtor inicializa os atributos nome e idade com os valores fornecidos como argumentos e imprime uma mensagem indicando que a pessoa foi registrada no sistema.
# A classe também possui um método chamado saudacao que retorna uma saudação personalizada com o nome e a idade da pessoa.
# Além disso, a classe possui um destrutor (__del__) que é chamado automaticamente quando o objeto é removido da memória.
# O destrutor imprime uma mensagem indicando que a pessoa foi removida do sistema.# No final do código, criamos dois objetos da classe Pessoa (p1 e p2) com nomes e idades diferentes.
# Em seguida, chamamos o método saudacao para cada objeto e imprimimos as saudações.
# Finalmente, usamos a instrução del para remover os objetos p1 e p2 da memória, o que aciona a chamada do destrutor e imprime as mensagens de remoção. 
