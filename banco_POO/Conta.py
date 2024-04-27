import Historico
from buscar_cpf import *


class Conta:
    def __init__(self, id, cliente):
        self._saldo = 0
        self._id = id
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = "lepo"

    def depositar(self, valor):
        self._saldo += valor
        return "Depósito realizado"

    def saldo_mostrar(self):
        return f"Cliente: {self._cliente} tem conta com id {self._id} com saldo {self._saldo}"

    @property
    def saldo(self):
        return self._saldo

    @property
    def cliente(self):
        return self._cliente

    @property
    def id(self):
        return self._id


def novo_id(contas):
    return contas[-1]._id + 1 if contas else 1


def nova_conta(contas, clientes):
    cpf = input("Insira seu CPF: ")
    condicao, cliente = buscar_cpf(clientes, cpf)
    print(condicao)
    print(cliente)
    if  condicao:
        id = novo_id(contas)
        nova_conta = Conta(id, cliente)
        contas.append(nova_conta)
        return "Conta criada com sucesso!"
    else:
        return "Não existe cliente com esse cpf"

