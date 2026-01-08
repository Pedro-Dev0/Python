# [].count para contar quantos elementos tem repetido na lista
lista_1 = ["azul", "rosa", "amarelo", "rosa"]

print(lista_1)
print(lista_1.count("azul"))
print(lista_1.count("rosa"))

#[].extend passa mais valores do que append que é um em um

lista_1.extend(["roxo", "Lilas"])
print(lista_1)

# index passa a posição do objeto informado, mas só da primeira vez que ele aparece
print(lista_1.index("azul"))
print(lista_1.index("amarelo"))

# pop para tirar o último elemento da lista mas pode ser colocado cordenada para remover em especifíco
lista_1.pop()
print(lista_1)

# remove você passa oque deseja remover, remove só primeira ocorrencia 
lista_1.remove("rosa")
print(lista_1)

# reverse só espelha ao contrario
lista_1.reverse()
print(lista_1)

# sort ordena alfabeticamente
lista_1.sort() #(reverse=True ai fica ao contrario), podendo colocar (key=lambda x: len(x), reverse=True)
print(lista_1)

print(len(lista_1))

lista_1.sorted()
print(lista_1)