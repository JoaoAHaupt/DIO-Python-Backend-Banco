from PessoaFisica import *
from ContaCorrente import *
from Conta import *


def main():
    clientes = []
    contas = []
    while True:

        opc = input().upper()

        if opc == "NU":
            print(PessoaFisica.novo_usuario(clientes))

        elif opc == "NC":
            print(ContaCorrente.nova_conta(contas, clientes))
        elif opc == "D":
            print(ContaCorrente.depositar(contas))
        elif opc == "S":
            print(ContaCorrente.sacar(contas))
        elif opc == "MC":
            for conta in contas:
                print(conta)
        elif opc == "MU":
            pass
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
