from datetime import datetime

def decorador_log(func):
    def envelope(*args, **kwargs):
        result, [objeto, valor_depositado] = func(*args, **kwargs)
        try:
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(f"{func.__name__.capitalize()} de R${valor_depositado} realizado às {datetime.now().replace(microsecond=0)} pelo cliente {objeto._cliente._nome} com conta de id {objeto._id}\n")
        except FileNotFoundError as exc:
            print(f"Erro ao encontrar arquivo {exc}")
        except IOError as exc:
            print(f"Erro ao abrir arquivo {exc} ")
        return result

    return envelope
