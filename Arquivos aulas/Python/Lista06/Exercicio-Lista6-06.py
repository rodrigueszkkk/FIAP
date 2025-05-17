
import math

def desvio_padrao(tupla):
    media = sum(tupla) / len(tupla)
    soma_diferencas = sum((x - media) ** 2 for x in tupla)
    return math.sqrt(soma_diferencas / (len(tupla) - 1))

print(desvio_padrao((10.5, 7.2, 9.8, 5.5, 6.6)))
