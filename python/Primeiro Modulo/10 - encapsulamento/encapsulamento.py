class Conta:
    def __init__(self, saldo=0, nro_agencia="0001", titular="Pedro"):
        self._saldo = saldo  # Atributo privado
        self._nro_agencia = nro_agencia  # Atributo protegido
        self.titular = titular  # Atributo público

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

    def ver_saldo(self):
        return self._saldo
    

conta = Conta(100)
print(conta.ver_saldo())  # Acessa      ndo o saldo via método público

