# a = int(input("Informe o numero inteiro positivo: "))
# b = int(input("Informe o numero inteiro positivo: "))

def mmc (a, b):
    multiplo = a
    while multiplo % b != 0:
        multiplo = multiplo + a
    return multiplo

a = int(input("Informe o numero inteiro positivo: "))
b = int(input("Informe o numero inteiro positivo: "))

resposta = mmc(a, b)
print(resposta)