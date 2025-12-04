frutas = ["manzana", "banana", "cereza", "naranja"] #lista de frutas, pode ser feitas com valores ou vazia


letras = list("python") #cria uma lista a partir de uma string
numeros = list(range(1, 6)) #cria uma lista a partir de um range de números
print(frutas)
print(letras)
print(numeros)

frutas.append("kiwi") #adiciona um elemento no final da lista
print(frutas)
frutas.insert(1, "mango") #adiciona um elemento em uma posição específica
print(frutas)
frutas.remove("banana") #remove um elemento específico da lista
print(frutas)
ultima_fruta = frutas.pop() #remove o último elemento da lista e o retorna
print(ultima_fruta) 
print(frutas)
frutas.sort() #ordena a lista em ordem alfabética
print(frutas)
frutas.reverse() #inverte a ordem dos elementos na lista
print(frutas)  
print(len(frutas)) #retorna o número de elementos na lista
print(frutas[0]) #acessa o primeiro elemento da lista
print(frutas[-1]) #acessa o último elemento da lista

# para remover coisas específicas
del frutas[0]
print(frutas)

# para remover mais de um valor de minha escolha
del frutas[1:3]
print(frutas)

# para remover toda a lista 
frutas.clear()
print(frutas)

# tem como colocar steps na hora de fatiar a lista 
numeros = list(range(1, 11))
print(numeros[::2]) # imprime os números de 2 em 2
