MAIOR_IDADE = 18
idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, por isso é responsável pelos seus atos.")
elif idade > 15 and idade < MAIOR_IDADE:
    print("É menor de idade, mas já começou a entrar na adolescência.")
else: #idade <= 15
    print("Você é uma criança, aproveite sua infância!")


saldo = 500
saque = 600
#  ternario funciona como um if simplificado
status = "Sucesso!" if saldo >= saque else "Falha!"

print(f"{status} ao realizar o saque!")