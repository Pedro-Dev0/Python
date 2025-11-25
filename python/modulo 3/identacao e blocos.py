saldo_banco = 1000  # Exemplo de saldo inicial

def saque_bancario(valor):
    global saldo_banco  # Indica que estamos usando a variável global saldo_banco

    if saldo_banco >= valor:
        saldo_banco -= valor
        print("Saque realizado com sucesso!")
        print(f"Saldo restante: {saldo_banco}")
    else:
        print("Saldo insuficiente para realizar o saque.")
        print(f"Saldo restante: {saldo_banco}")

# Exemplo de uso da função
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso mas resta 0 de saldo!
saque_bancario(200) #saldo insuficiente!

# como gravar o valor para sempre mostrar o saldo atualizado após cada saque?
# Para manter o saldo atualizado após cada saque, você pode usar uma variável global ou encapsular o saldo em uma classe. Aqui está um exemplo usando uma variável global: