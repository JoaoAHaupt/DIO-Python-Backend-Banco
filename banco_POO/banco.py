from PessoaFisica import *
from ContaCorrente import *
from Conta import *
from Deposito import *
from Saque import *
from Historico import *


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

    def mostrar_historico():
        id = int(input("Coloque o id da conta: "))
        for conta in contas:
            if conta.id == id:
                print(f"Conta={conta.cliente}")
                for acao in conta.historico.transacoes:
                    print(acao)

    def mostrar_contas():
        for conta in contas:
            print(conta)

    def mostrar_clientes():
        for cliente in clientes:
            print(cliente)

    while True:

        opc = input().upper()

        if opc == "NU":
            print(PessoaFisica.novo_usuario(clientes))

        elif opc == "NC":
            print(ContaCorrente.nova_conta(contas, clientes))
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


def procurar_conta(id, contas):
    for conta in contas:
        if conta.id == id:
            return conta
    return False


if __name__ == "__main__":
    main()
