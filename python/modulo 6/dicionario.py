# criando dicionarios

meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# acessando valores
print(meu_dicionario["nome"])  # Output: João
print(meu_dicionario.get("idade"))  # Output: 25
print(meu_dicionario.get("cidade"))  # Output: São Paulo

# adicionando ou atualizando valores
meu_dicionario["profissão"] = "Engenheiro"
meu_dicionario["idade"] = 26  # atualizando idade

print(meu_dicionario)

# removendo valores
del meu_dicionario["cidade"]
idade_removida = meu_dicionario.pop("idade") 

# novos jeitos de criar dicionarios

novo_dicionario = dict(nome="Maria", idade=30, cidade="Rio de Janeiro")
print(novo_dicionario)

novo_dicionario["Telefone"] = "1234-5678" # adicionando novo par chave-valor
print(novo_dicionario)

# aninhamento de dicionarios    
dicionario_aninhado = {
    "pessoa1": {
        "nome": "Ana",
        "idade": 28
    },
    "pessoa2": {
        "nome": "Carlos",
        "idade": 32
    }
}

print(dicionario_aninhado["pessoa1"]["nome"])  # Output: Ana
print(dicionario_aninhado["pessoa2"]["nome"])  # Output: Carlos

dicionario_aninhado["pessoa1"]["nome"] = "Rebecca"  # atualizando nome
print(dicionario_aninhado["pessoa1"]["nome"])  # Output: Rebecca

print(dicionario_aninhado["pessoa1"]["nome"])  # Output: Rebecca
print(dicionario_aninhado["pessoa2"]["nome"])  # Output: Carlos

for chave, valor in dicionario_aninhado.items(): # melhor forma de iterar
    print(f"{chave}: {valor}") # imprime cada par chave-valor no dicionário aninhado


for chave in dicionario_aninhado: # outra forma de iterar
    print(f"{chave}: {dicionario_aninhado[chave]}") # imprime cada par chave-valor no dicionário aninhado
