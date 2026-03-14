from datetime import datetime

# dados da conta
saldo = 0
LIMITE_DE_TRANSACOES = 10
transacoes_realizadas = 0

# historico de transações
extrato = []


def data_hora_atual():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def depositar(valor):
    global saldo, transacoes_realizadas  # precisamos modificar variáveis fora da função

    # Verifique se transacoes_realizadas < LIMITE_TRANSACOES
    if transacoes_realizadas < LIMITE_DE_TRANSACOES:
        # Atualize o saldo
        saldo += valor

        # Registre no histórico (append com dicionário)
        extrato.append(
            {
                "tipo": "DEPÓSITO",
                "valor": valor,
                "data": data_hora_atual(),
                "saldo_apos": saldo,
            }
        )

        # Aumente o contador
        transacoes_realizadas += 1

        print(f"✅ Depósito de R$ {valor:.2f} realizado em {data_hora_atual()}")
    else:
        print("❌ LIMITE DE TRANSAÇÕES EXCEDIDO!")


def sacar(valor):
    global saldo, transacoes_realizadas

    # Complete aqui seguindo a lógica do depósito
    if transacoes_realizadas < LIMITE_DE_TRANSACOES and saldo >= valor:
        # Atualize o saldo
        saldo -= valor

        # Registre no histórico (append com dicionário)
        extrato.append(
            {
                "tipo": "SAQUE",
                "valor": valor,
                "data": data_hora_atual(),
                "saldo_apos": saldo,
            }
        )

        # Aumente o contador
        transacoes_realizadas += 1

        print(f"✅ Saque de R$ {valor:.2f} realizado em {data_hora_atual()}")
    # Mas adicione uma verificação extra: saldo >= valor
    elif saldo < valor:
        print("❌ SALDO INSUFICIENTE!")
    else:
        print("❌ LIMITE DE TRANSAÇÕES EXCEDIDO!")


def mostrar_extrato():
    print("\n=== EXTRATO BANCÁRIO ===")
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        for transacao in extrato:
            print(
                f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f} | Saldo após: R$ {transacao['saldo_apos']:.2f}"
            )
    print("========================\n")


def menu():
    while True:
        print("=== MENU ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar Extrato")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            valor = float(input("Digite o valor para depósito: "))
            depositar(valor)
        elif escolha == "2":
            valor = float(input("Digite o valor para saque: "))
            sacar(valor)
        elif escolha == "3":
            mostrar_extrato()
        elif escolha == "4":
            print("Saindo do sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
