from PessoaFisica import *
from ContaCorrente import *




def main():
    clientes = []
    contas = []
    while True:
        opc = input().upper()

        if opc == "NU":
            print(novo_usuario(clientes))

        elif opc == "NC":
            print(nova_conta(contas, clientes))
        elif opc == "S":
            print(sacar(contas))
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
