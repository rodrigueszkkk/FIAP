def dec_to_bin(decimal):
    pot10 = 1
    while dec != 0:
        resto = dec % 2
        binario = binario + resto * pot10
        dec = dec // 2
        pot10 = pot10 * 10

    return binario





dec = int(input("Informe o numero inteiro positivo: "))
dec = dec_to_bin()

while dec < 0:
    print('Numero invalido!')
    dec = int(input('Informe o numero inteiro positivo'))

# binario = 0
# pot10 = 1
# while dec != 0:
#     resto = dec % 2
#     binario = binario + resto * pot10
#     dec = dec // 2
#     pot10 = pot10 * 10
