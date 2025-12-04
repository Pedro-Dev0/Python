mesas = list(range(30))
print(mesas)

pares = []

for numero in mesas:
    if numero % 2 == 0:
        pares.append(numero)

print(pares) # primeiro filtro para se usar uma lista antiga e criar uma nova lista com base nessa antiga mas tirando as partes que não interessa ou não quer

# usando list comprehension para fazer o mesmo que o código acima
pares_comp = [numero for numero in mesas if numero % 2 == 0]
print(pares_comp)

cadeiras = list(range(40))
print(cadeiras)

cadeirinhas = []

for numero in cadeiras:
    if numero % 2 ==0:
        cadeirinhas.append(numero)

print(cadeirinhas)

cadeirinhas_par = [string for string in cadeiras if string % 2 == 0] # transformada a lista em string e divida em numeros pares

print(cadeirinhas_par)