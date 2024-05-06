from PessoaFisica import *
from ContaCorrente import *
from Conta import *
from Deposito import *
from Saque import *
from DecoradorDataHora import *


def main():
    clientes = []
    contas = []
    print('''
    ================BANCO PY================
    [NU] Novo Usuário
    [NC] Nova Conta
    [D]  Depositar
    [S]  Sacar
    [MC] Mostrar Contas
    [MU] Mostrar Usuários
    [H]  Histórico
    [Q]  Sair
    
    
    ''')

    @decorador_data_hora
    def sacar():
        id_conta = int(input("Coloque o id da sua conta: "))
        conta = procurar_conta(id_conta, contas)
        if conta:
            cliente = ContaCorrente(conta.id, conta.cliente)
            valor = float(input("Coloque o valor do saque: "))

            if cliente.sacar(valor, contas):
                Saque(valor).registrar(conta)
                print("Depósito registrado com sucesso!")
            else:
                print("Falha ao efetuar o saque. Verifique o valor e tente novamente.")
        else:
            print("Conta não encontrada")

    @decorador_data_hora
    def depositar():
        id_conta = int(input("Coloque o id da sua conta: "))
        conta = procurar_conta(id_conta, contas)
        if conta:
            cliente = ContaCorrente(conta.id, conta.cliente)
            valor = float(input("Coloque o valor do depósito: "))

            if cliente.depositar(valor, contas):
                Deposito(valor).registrar(conta)
                print("Depósito registrado com sucesso!")
            else:
                print("Falha ao efetuar o depósito. Verifique o valor e tente novamente.")
        else:
            print("Conta não encontrada")

    @decorador_data_hora
    def mostrar_contas():
        for conta in contas:
            print(conta)

    @decorador_data_hora
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

    @decorador_data_hora
    def nova_conta(contas, clientes):
        cpf = input("Insira seu CPF: ")
        condicao, cliente = buscar_cpf(clientes, cpf)

        if condicao:
            id = novo_id(contas)
            nova_conta = ContaCorrente(id, cliente)
            contas.append(nova_conta)
            return f"Conta criada com sucesso! ID = {id}"
        else:
            return "Não existe cliente com esse cpf"

    def mostrar_clientes():
        for cliente in clientes:
            print(cliente)

    def mostrar_historico():
        id = int(input("Coloque o id da conta: "))
        for conta in contas:
            if conta.id == id:
                print(f"Conta={conta.cliente}")
                for acao in conta.historico.transacoes:
                    print(acao)

    def procurar_conta(id, contas):
        baixo = 0
        alto = len(contas) - 1

        while baixo <= alto:
            meio = (alto + baixo) // 2
            chute = contas[meio].id

            if chute == id:
                return contas[meio]
            if chute > id:
                alto = meio - 1
            else:
                baixo = meio + 1
        return None

    while True:

        opc = input().upper()

        if opc == "NU":
            novo_usuario(clientes)
        elif opc == "NC":
            nova_conta(contas, clientes)
        elif opc == "D":
            depositar()
        elif opc == "S":
            sacar()
        elif opc == "MC":
            mostrar_contas()
        elif opc == "MU":
            mostrar_clientes()
        elif opc == "H":
            mostrar_historico()

        elif opc == "Q":
            input("Saindo do banco")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
