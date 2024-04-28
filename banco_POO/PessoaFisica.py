from Cliente import Cliente
from buscar_cpf import buscar_cpf
import re



class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_de_nascimento, cep):
        super().__init__(cep)
        self._cpf = cpf
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return f"PessoaFisica(nome={self.nome}, cpf={self.cpf})"


    @staticmethod
    def novo_usuario(clientes):
        nome = input("Insira seu nome: ")
        cpf = input("Insira seu cpf: ")
        data_de_nascimento = input("Insira sua data de nascimento: ")
        cep = input("Insira seu cep: ")

        if not buscar_cpf(clientes, cpf):
            if validar_cpf(cpf):
                novo = PessoaFisica(cpf, nome, data_de_nascimento, cep)
                clientes.append(novo)
                return f"Usuario: {novo.nome} acabou de ser cadastrado!"
            else:
                return "CPF inválido"
        else:
            return "Usuário já cadastrado"


def validar_cpf(cpf):
    cpf = re.sub('[!-.:-@]', '', cpf)
    cpf_sem_2 = cpf[:-2]
    if len(cpf_sem_2) == 9:
        num = [10, 11]
        restos = [0, 0]
        for i in range(2):

            valor = 0
            for digito in cpf_sem_2:
                valor = valor + (num[i] * int(digito))
                num[i] -= 1

            if valor % 11 >= 2:
                restos[i] = 11 - (valor % 11)
            else:
                restos[i] = 0

            cpf_sem_2 = cpf_sem_2 + str(restos[0])
        if restos[1] == int(cpf[len(cpf) - 1]):
            return True
        return False





