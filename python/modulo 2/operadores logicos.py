saldo = 1000
saque = 200
limite = 100
conta_especial = True

saldo >= saque
print(saldo >= saque)  # True

saldo <= limite
print(saldo <= limite)  # False

saldo >= saque and saque <= limite
print(saldo >= saque and saque <= limite)  # False

saldo >= saque or saque <= limite
print(saldo >= saque or saque <= limite)  # True

not(saldo >= saque)
print(not(saldo >= saque))  # False

not(saldo <= limite)
print(not(saldo <= limite))  # True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print((saldo >= saque and saque >= limite) or (conta_especial and saldo >= saque))  # True
