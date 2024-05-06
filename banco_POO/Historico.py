from datetime import datetime


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(),

            }
        )

    def mostrar_historico(self, tipo=None):
        if tipo == "": tipo = None
        for transacao in self._transacoes:
            if tipo is None or transacao["tipo"].lower() == tipo.lower():
                yield transacao


