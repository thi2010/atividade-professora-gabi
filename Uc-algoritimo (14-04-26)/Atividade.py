def soma_segura(a, b):
    try:
        return a + b
    except TypeError:
        print("Entrada inválida")
        return 0


def divisao(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Não divida por zero!"