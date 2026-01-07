linguagens = {'Python', 'Java', 'C#', 'Python'}
print(linguagens)  # Saída: {'Python', 'Java', 'C#'} essa saida já sai com set implícito
print(type(linguagens))  # Saída: <class 'set'>


# outra saida com set
carros = set(['Fiat', 'Ford', 'Chevrolet', 'Fiat'])
print(carros)  # Saída: {'Fiat', 'Ford', 'Chevrolet'}
print(type(carros))  # Saída: <class 'set'>

for carro in carros:
    print(carro)

enumerate_carros = enumerate(carros)
print(list(enumerate_carros))

"""carros1 = list(carros)# para indexar um conjunto, é necessário converter para lista ou tupla
print(carros1[0]) # Acessando o primeiro elemento da lista convertida"""