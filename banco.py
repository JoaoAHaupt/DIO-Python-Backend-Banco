saldo = 0.0
limite = 500
extrato = []
numero_de_saques = 0
LIMITE_SAQUES = 3

menu = f'''
===============BANCO===============
           SALDO: {saldo}
             [S]aque
            [D]eposito
            [E]xtrato
              [Q]uit
===================================

'''

while True:
    print(menu)
    opcao = input().lower()

    if opcao == "d":
        deposito = float(input("Adicione o valor de deposito: R$"))
        if deposito > 0:
            saldo += deposito
            extrato.append(f"Deposito de R${deposito}. Total na conta {saldo}\n")
            print(f"Valor de {deposito} adicionado \n")
        else:
            print("DEPOSITO INVÁLIDO")
    elif opcao == "s":
        if numero_de_saques < LIMITE_SAQUES:
            saque = float(input("Adicione o valor de saque: R$"))
            if 0 < saque <= limite and saque <= saldo:
                saldo = saldo - saque
                numero_de_saques = 1 + numero_de_saques
                extrato.append(f"Saque de R${saque}. Total na conta {saldo}\n")
                print(f"Valor de {saque} sacado\n")
            else:
                print("SAQUE INVÁLIDO")
        else:
            print("NÚMERO DE SAQUES EXCEDIDOS")
    elif opcao == "e":
        if len(extrato) == 0:
            print("NENHUMA AÇÃO CONSTA")
        else:
            for acao in extrato:
                print(acao)
    elif opcao == "q":
        print("SAINDO DO BANCO")
        break
    else:
        print("COMANDO NÃO IDENTIFICADO\n")
