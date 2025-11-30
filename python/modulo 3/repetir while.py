opcao = -1

while opcao != 0:
    opcao = int(input("1, sacar\n2, depositar\n0, sair\nEscolha uma opção: "))

    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Depósito realizado com sucesso!")
    elif opcao == 0:
        print("Saindo...")