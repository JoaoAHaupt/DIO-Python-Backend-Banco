import Historico
from buscar_cpf import *


class Conta:
    def __init__(self, id, cliente):
        self._saldo = 0
        self._id = id
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = "lepo"

    @property
    def saldo(self):
        return self._saldo

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

    @staticmethod
    def depositar(contas):
        id_conta = int(input("Coloque o id da sua conta: "))
        for conta in contas:
            if conta.id == id_conta:
                valor = float(input("Coloque o valor do depósito: "))

                if valor < 0:
                    return "Valor do depósito tem que ser positivo"
                else:
                    conta._saldo += valor
                    return "Depósito realizado com sucesso!"
        return f"Conta com id {id_conta} não encontrada"


def novo_id(contas):
    return contas[-1]._id + 1 if contas else 1






