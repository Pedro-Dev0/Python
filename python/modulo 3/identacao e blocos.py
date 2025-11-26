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

    print("Obrigado por usar nosso banco! e feliz natal!")

# Exemplo de uso da função
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso mas resta 0 de saldo!
saque_bancario(200) #saldo insuficiente!

def deposito_bancario(valor):
    global saldo_banco  # Indica que estamos usando a variável global saldo_banco

    if saldo_banco <= 0:
        saldo_banco += valor
        print("Depósito realizado com sucesso!")
        print(f"Saldo atualizado: {saldo_banco}")
    
    print("Obrigado por usar nosso banco! e feliz natal!")

deposito_bancario(1000)
saque_bancario(200)
# Exercício: Crie uma função para saque bancário que verifique se há saldo suficiente antes de permitir o saque.

# como gravar o valor para sempre mostrar o saldo atualizado após cada saque?
# Para manter o saldo atualizado após cada saque, você pode usar uma variável global ou encapsular o saldo em uma classe. Aqui está um exemplo usando uma variável global:

"""def saque_bancario(saldo, valor):
    if saldo >= valor:
        saldo -= valor
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")
    
    print(f"Saldo restante: {saldo}")
    return saldo  # devolve o saldo atualizado

# Exemplo de uso:
saldo_banco = 1000  # saldo inicial
saldo_banco = saque_bancario(saldo_banco, 200)
saldo_banco = saque_bancario(saldo_banco, 200)
saldo_banco = saque_bancario(saldo_banco, 200)
saldo_banco = saque_bancario(saldo_banco, 200)
saldo_banco = saque_bancario(saldo_banco, 200)
saldo_banco = saque_bancario(saldo_banco, 200)

Forma complicada, mas funciona e mais profissional para não mexer muito com variáveis globais, pois é perigoso em programas maiores.
"""