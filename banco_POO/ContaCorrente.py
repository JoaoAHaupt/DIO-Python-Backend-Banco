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

    def sacar(self, valor, contas):
        for conta in contas:
            if conta._id == self._id:
                if conta.limite_saques <= conta.quantidade_limite_saques:
                    if conta._saldo < valor:
                        return "Valor do saque maior que saldo"
                    elif conta._saldo > 0:
                        conta._saldo -= valor
                        return "Saque realizado"
                    else:
                        return "Valor de saque inválido"
                else:
                    return "Quantidade de saques excedido"
        return "Conta não encontrada"

    def __str__(self):
        return f"ContaCorrente(id={self.id}, cliente={self.cliente}, saldo={self.saldo}, limite={self._limite}, historico={self._historico})"
