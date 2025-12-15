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