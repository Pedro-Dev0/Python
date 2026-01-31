class Estudante:
    escola = "DIO"  # Variável de classe

    def __init__(self, nome, matricula):
        self.nome = nome          # Variável de instância
        self.matricula = matricula  # Variável de instância
    
    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Escola: {Estudante.escola}"

# Criando instâncias da classe Estudante
estudante1 = Estudante("Alice", "12345")
estudante2 = Estudante("Bob", "67890")

# Acessando variáveis de instância
print(estudante1)  # Nome: Alice, Matrícula: 12345, Escola: DIO
print(estudante2)  # Nome: Bob, Matrícula: 67890, Escola: DIO