from datetime import datetime
from abc import ABC, abstractmethod
#começando com criação da base do banco o cliente 


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas=[]

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Transacao(ABC): #estou aqui=============
    @property
    @abstractmethod
    def valor(self):
        # Isso obriga o Saque e o Depósito a terem um .valor
        pass

    @abstractmethod
    def registrar(self, conta):
        # Isso obriga o Saque e o Depósito a terem uma função .registrar
        pass
        

class Historico:
    def __init__(self):
        # Criamos uma lista vazia para começar a anotar as transações
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Este método será chamado toda vez que um saque ou depósito der certo
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S") # Vamos ver como pegar a data real logo mais
            }
        )

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @property
    def agencia(self):
        return self._agencia
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False


        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False

    @classmethod
    def nova_conta(cls, cliente, numero):
    # Aqui ele apenas executa o 'molde' (cls) e devolve a conta
        return cls(numero, cliente)
    



            

        


        






    









