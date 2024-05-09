from Historico import *
from buscar_cpf import *
from RegistroLog import *

class Conta:
    def __init__(self, id, cliente):
        self._saldo = 0
        self._id = id
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._historico

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def cliente(self):
        return self._cliente

    @property
    def id(self):
        return self._id

    def saldo_mostrar(self):
        return f"Cliente: {self._cliente} tem conta com id {self._id} com saldo {self._saldo}"

    @staticmethod
    def nova_conta(contas, clientes):
        cpf = input("Insira seu CPF: ")
        condicao, cliente = buscar_cpf(clientes, cpf)
        if condicao:
            id = novo_id(contas)
            nova_conta = Conta(id, cliente)
            contas.append(nova_conta)
            return f"Conta criada com sucesso! ID = {id}"
        else:
            return "Não existe cliente com esse cpf"

    @decorador_log
    def depositar(self, valor, contas):
        if valor <= 0:
            return "Valor do depósito tem que ser positivo"
        else:
            for conta in contas:
                if conta._id == self._id:
                    conta._saldo += valor
                    return "Depósito realizado com sucesso!", [self, valor]
            return "Conta não encontrada"

    def gerador_extrato(self, tipo):

        for acao in self._historico.transacoes:
            if tipo in acao:
                print(acao)



def novo_id(contas):
    return contas[-1].id + 1 if contas else 1
