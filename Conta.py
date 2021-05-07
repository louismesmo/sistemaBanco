import datetime
from Extrato import Extrato
class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.clientes = []
        self.saldo = saldo
        self.abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):

        if self.saldo < valor:
            return False

        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True
    #Realiza a transferencia de saldo entre contas
    def pix(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Você não possui saldo suficiente.")

        else:
            self.saldo -= valor
            contaDestino += valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return ("Transação realizada com sucesso!")

    #Gera o saldo atual da conta
    def gerarsaldo(self):
        print(f'numero: {self.numero}\nsaldo: {self.saldo}')