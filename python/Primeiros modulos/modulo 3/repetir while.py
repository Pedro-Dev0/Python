opcao = -1

while opcao != 0:
    opcao = int(input("1, sacar\n2, depositar\n0, sair\nEscolha uma opção: "))

    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Depósito realizado com sucesso!")
    elif opcao == 0:
        print("Saindo...")

# Estrutura de repetição com for é bom para quando sabe quantas vezes vai repetir caso contrário while é melhor para ser usado quando não sabe quantas vezes vai repetir até que a condição seja satisfeita.

#loop infinito
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando.lower() == "sair":
        break
    print("Você digitou:", comando)


for numero in range(1000000):
    if numero == 50000:        
        break
    print(numero, end=" ")

    # break para quebar o loop ou continue para pular para a próxima iteração informada