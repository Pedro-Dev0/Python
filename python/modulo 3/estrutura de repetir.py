texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # Para pular uma linha após a impressão das vogais


# built-in functions: range
for numero in range(1, 12, 2):
    print(numero, end="...")

for numero in range(11):
    print(numero, end=" ")

tabuada = int(input("\nDigite um número para ver a tabuada: "))
for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")

# \n é o caractere de nova linha, usado para pular linhas