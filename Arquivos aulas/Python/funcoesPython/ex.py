def aumento (valor, percentual):
    novoValor = (1 + percentual / 100) * valor
    return novoValor

resultado = aumento(100, 10)
print(resultado)

def divisao (a, b):
    return a * b, a // b

resultado = divisao(10, 3)
print(resultado)