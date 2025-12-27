#.count para contar o que tem dentro da tupla  sss

# Exemplo:
tupla = (1, 2, 2, 3, 2, 4)
print(tupla.count(2))  # Output: 3

# existe também o index em tuplas
tupla = (1, 2, 2, 3, 2, 4)
print(tupla.index(2))  # Output: 1 (primeiro índice onde 2 aparece)
# como ver o segundo indice de dois
print(tupla.index(2, 2))  # Output: 2 (procura a partir do índice 2)
# e o len
tupla = (1, 2, 2, 3, 2, 4)
print(len(tupla))  # Output: 6 (número de elementos na tupla)