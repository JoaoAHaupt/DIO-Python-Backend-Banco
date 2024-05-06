from datetime import datetime


def decorador_data_hora(func):
    def envelope():
        func()
        print(f"Tentativa de {func.__name__} realizada {datetime.now()}")

    return envelope
