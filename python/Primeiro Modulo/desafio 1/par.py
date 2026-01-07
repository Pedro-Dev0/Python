'''numero = int(input())

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"Par")
    else:
        print(f"Ímpar")

par_ou_impar(numero)'''


"""def verificador_ano_bissexto():
    ano = int(input())
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto")
    else:
        print(f"{ano} não é um ano bissexto")

verificador_ano_bissexto()"""

def conta_vogais(texto):
    # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = set("aeiouAEIOU")

    # TODO: Inicialize um contador para contar as vogais:
    contador = 0

    # Iteramos pelos caracteres da string
    for char in texto:
        # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in vogais:
            contador += 1
    return contador

# Solicitamos ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")