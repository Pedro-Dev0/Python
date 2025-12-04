# [].count para contar quantos elementos tem repetido na lista
lista_1 = ["azul", "rosa", "amarelo", "rosa"]

print(lista_1)
print(lista_1.count("azul"))
print(lista_1.count("rosa"))

#[].extend passa mais valores do que append que é um em um

lista_1.extend(["Roxo", "Lilas"])
print(lista_1)