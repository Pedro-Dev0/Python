saldo_banco = 1000  # Exemplo de saldo inicial

def saque_bancario(valor):
    global saldo_banco  # Indica que estamos usando a variável global saldo_banco
    #valor = float(input("Digite o valor que deseja sacar: "))

    if saldo_banco >= valor: #pode fazer para ter limite máximo de saque também
        saldo_banco -= valor
        print("Saque realizado com sucesso!")
        print(f"Saldo restante: {saldo_banco}")
    else:
        print("Saldo insuficiente para realizar o saque.")
        print(f"Saldo restante: {saldo_banco}")

    print("Obrigado por usar nosso banco! e feliz natal!")

# Exemplo de uso da função
"""saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso
saque_bancario(200) #sucesso mas resta 0 de saldo!
saque_bancario(200) #saldo insuficiente!"""

def deposito_bancario(valor):
    global saldo_banco  # Indica que estamos usando a variável global saldo_banco
    #valor = float(input("Digite o valor que deseja depositar: ")) #simulando input

    if saldo_banco <= 0: #pode fazer para ter limite máximo de depósito também
        saldo_banco += valor
        print("Depósito realizado com sucesso!")
        print(f"Saldo atualizado: {saldo_banco}")
    
    print("Obrigado por usar nosso banco! e feliz natal!")

"""deposito_bancario(1000)
saque_bancario(200) """
# Exercício: Crie uma função para saque bancário que verifique se há saldo suficiente antes de permitir o saque.

opcao = int(input(f"Digite 1 para sacar ou 2 depositar: "))

if opcao == 1:
    valor = float(input("Digite o valor que deseja sacar: "))
    saque_bancario(valor)
elif opcao == 2:
    valor = float(input("Digite o valor que deseja depositar: "))
    deposito_bancario(valor)
else:
    print("Opção inválida!")