extrato = []


def criar_usuario(*, nome, cpf, logadouro, usuarios_lista):
    for usuario in usuarios_lista:
        if usuario["cpf"] == cpf or usuario["nome"] == nome.lower():
            return "Conta já existente."
    novo_usuario = {"nome": nome.lower(), "cpf": cpf, "logadouro": logadouro}
    usuarios_lista.append(novo_usuario)
    return f"Usuário criado com sucesso. {novo_usuario}"


def criar_conta_corrente(*, cliente, saldo, contas_lista, usuarios_lista):
    for usuario in usuarios_lista:
        if usuario["nome"] == cliente:
            if len(usuarios_lista) <= 1:
                novo_id = 0
            else:
                ultima_conta = contas_lista[-1]
                novo_id = ultima_conta["id"] + 1
            nova_conta = {"cliente": cliente, "agencia": "0001", "id": novo_id, "saldo": saldo, "numero_de_saques": 0}
            contas_lista.append(nova_conta)
            return nova_conta
        else:
            return "Usuário não cadastrado"


def deposito(*, cliente, conta_id, contas_lista, valor):
    if valor > 0:
        for conta in contas_lista:
            if conta["cliente"] == cliente and conta["id"] == int(conta_id):
                conta["saldo"] = float(conta["saldo"]) + valor
                extrato_fum(conta_id=conta_id,acao="deposito",saldo=conta["saldo"],valor=valor, extrato_lista=extrato, cliente=cliente)
                return conta

        return "Conta não encontrada"
    else:
        return "Valor inválido"


def sacar(*, cliente, conta_id, contas_lista, valor):
    for conta in contas_lista:
        if conta["cliente"] == cliente and conta["id"] == int(conta_id):
            if 0 < valor <= 500 and valor <= float(conta["saldo"]) and int(conta["numero_de_saques"]) < 3:
                conta["saldo"] = float(conta["saldo"]) - valor
                conta["numero_de_saques"] = int(conta["numero_de_saques"]) + 1
                extrato_fum(conta_id=conta_id, acao="sacar", saldo=conta["saldo"], valor=valor, extrato_lista=extrato, cliente=cliente)
                return conta
            else:
                return "Valor ou número de saques diários excedido"
        else:
            return "Conta não encontrada"


def extrato_fum(cliente, conta_id, acao, saldo, valor, extrato_lista):
    extrato_lista.append(
        f"Cliente:{cliente} com conta de id:{conta_id}, {acao} um valor de {valor} ficando com o saldo de {saldo}")


def mostrar_contas(lista_contas):
    for conta in lista_contas:
        print(conta)
def mostrar_usuarios(lista_usuarios):
    for usuario in lista_usuarios:
        print(usuario)


def main():
    usuarios = []
    contas = []
    while True:

        print(
            """
            ===============$MENU BANCO$===============
            [NU] novo usuário
            [NC] Novo Conta
            [D]  Depositar
            [S]  Sacar
            [E]  Extrato
            [LC]  Lista de contas
            [LU]  Lista de usuarios
            [Q]  Sair
            """
        )

        opcao = input().upper()

        if opcao == "NU":
            nome = input("Digite seu nome")
            cpf = input("Digite seu CPF")
            bairro = input("Digite o seu bairro")
            cidade = input("Digite a sua cidade")
            sigla_estado = input("Digite a sigla do seu estado")

            logadouro = f"{bairro} - {cidade}/{sigla_estado}"

            print(criar_usuario(nome=nome, cpf=cpf, logadouro=logadouro, usuarios_lista=usuarios))
        elif opcao == "NC":
            nome = input("Digite seu nome")
            print(criar_conta_corrente(cliente=nome, saldo=0, contas_lista=contas, usuarios_lista=usuarios))

        elif opcao == "D":
            nome = input("Digite o nome do dono da conta")
            id_conta = input("Digite o id da conta")
            valor = float(input("Digite o valor do deposito"))

            print(deposito(cliente=nome, conta_id=id_conta, contas_lista=contas,  valor=valor))
        elif opcao == "S":
            nome = input("Digite o nome do dono da conta")
            id_conta = input("Digite o id da conta")
            valor = float(input("Digite o id da conta"))

            print(sacar(cliente=nome, conta_id=id_conta, contas_lista=contas, valor=valor))
        elif opcao == "E":
            for ex in extrato:
                print(ex)
        elif opcao == "LU":
            mostrar_usuarios(usuarios)
        elif opcao == "LC":
            mostrar_contas(contas)
        elif opcao == "Q":
            break
        else:
            print("COMANDO NÃO ENCONTRADO")


print(main())