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


'''Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

Detalhamento:

Função elementos_comuns:
1. Crie a função que converte cada elemento das listas lista1 e lista2 para inteiro usando map(int, lista) antes de convertê-los em conjuntos (set) e encontrar a interseção entre eles. Isso garante que tratemos os elementos corretamente como números inteiros e não como strings.'''

'''
# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:

def elementos_comuns(lista1, lista2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    comuns = set1.intersection(set2)
    return list(comuns)

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
'''

'''O desafio consiste em adicionar à função contar_caracteres um dicionário vazio chamado contador para armazenar as contagens de caracteres. Vamos iterar através de cada caractere na string string. Para cada caractere, verifique se ele já está presente no dicionário contador. Se estiver, incremente o valor associado a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. Neste dicionário, as chaves são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.'''


def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
#TODO: Itere através de cada caractere na string string.
    for char in string:
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1

    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
    