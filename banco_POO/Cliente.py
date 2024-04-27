class Cliente:
    def __init__(self, cep):
        self._cep = cep
        self._contas = []

    @property
    def cep(self):
        return self._cep

    def realizar_transacao(self, conta, transacao):
        pass
    def adicionar_conta(self, conta):
        self._contas.append(conta)
