saldo = 500

print(f'Saldo inicial: {saldo}')

saldo = saldo + 200 # atribuição comum
print(f'Saldo após depósito: {saldo}')

saldo += 200  # atribuição com operador de adição
print(f'Saldo após segundo depósito: {saldo}')

saldo -= 100  # atribuição com operador de subtração
print(f'Saldo após saque: {saldo}')

saldo *= 2  # atribuição com operador de multiplicação
print(f'Saldo após investimento dobrado: {saldo}')

saldo //= 2  # atribuição com operador de divisão inteira
print(f'Saldo após retirada inteira do investimento: {saldo}')

saldo /= 2  # atribuição com operador de divisão
print(f'Saldo após retirada do investimento: {saldo}')

saldo %= 300  # atribuição com operador de módulo
print(f'Saldo após cálculo de módulo: {saldo}')

saldo **= 2  # atribuição com operador de exponenciação
print(f'Saldo após exponenciação: {saldo}')

saldo = int(saldo)  # convertendo saldo para inteiro
print(f'Saldo convertido para inteiro: {saldo}')
