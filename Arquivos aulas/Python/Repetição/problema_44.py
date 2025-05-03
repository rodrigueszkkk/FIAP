nota = float(input('Digite a nota: '))

while nota < 0 or nota > 10:
    print('Nota invalida')
    nota = float(input('Nota: '))

outra_nota = float(input('Digite outra nota: '))
while outra_nota < 0 or nota > 10:
    print('Nota invalida')
    nota = float(input('Nota: '))

media = (nota + outra_nota) / 2
print('Media final: ', media)
