from Conta import *
from buscar_cpf import *


class ContaCorrente(Conta):
    def __init__(self, id, cliente):
        super().__init__(id, cliente)
        self._limite = 500
        self._limite_saques = 0
        self.quantidade_limite_saques = 3

    @property
    def limite_saques(self):
        return self._limite_saques

    @limite_saques.setter
    def limite_saques(self, novo_limite_saques):
        self._limite_saques = novo_limite_saques


def sacar(contas):
    id_conta = int(input("Coloque o id da sua conta: "))
    for conta in contas:
        if conta.id == id_conta:
            valor = input("Coloque o valor do saque: ")
            saldo = conta.saldo

            if saldo > valor:
                return "Valor do saque maior que saldo"
            elif saldo > 0:
                conta.saldo -= valor
                return "Saque realizado"
            else:
                return "Valor de saque inválido"

        return f"Conta com id {id} não encontrada"


def nova_conta(contas, clientes):
    cpf = input("Insira seu CPF: ")
    condicao, cliente = buscar_cpf(clientes, cpf)

    if condicao:
        id = novo_id(contas)
        nova_conta = ContaCorrente(id, cliente)
        contas.append(nova_conta)
        return "Conta criada com sucesso!"
    else:
        return "Não existe cliente com esse cpf"
