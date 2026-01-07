# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:

'''
def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
'''


"""Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

Detalhamento:

Função elementos_comuns:
1. Crie a função que converte cada elemento das listas lista1 e lista2 para inteiro usando map(int, lista) antes de convertê-los em conjuntos (set) e encontrar a interseção entre eles. Isso garante que tratemos os elementos corretamente como números inteiros e não como strings."""

def elementos_comuns(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)  
    return list(set1.intersection(set2))

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")

    