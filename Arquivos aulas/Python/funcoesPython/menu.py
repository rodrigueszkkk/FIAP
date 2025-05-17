def menu():
    opcao = -1
    while opcao != 5:
        print('1 - Adicao')
        print('2 - Subtracao')
        print('3 - Multiplicacao')
        print('4 - Divisao')
        print('5 - Sair')
    return opcao

opcao = menu()
opcao = int(input('Escolha uma opcao: '))
if opcao == 1:
            a = int(input('Informe o primeiro numero: '))
            b = int(input('Informe o segundo numero: '))
            print(a + b)
elif opcao == 2:
            a = int(input('Informe o primeiro numero: '))
            b = int(input('Informe o segundo numero: '))
            print(a - b)
elif opcao == 3:
            a = int(input('Informe o primeiro numero: '))
            b = int(input('Informe o segundo numero: '))
            print(a * b)
elif opcao == 4:
            a = int(input('Informe o primeiro numero: '))
            b = int(input('Informe o segundo numero: '))
            if b != 0:
                print(a / b)
            else:
                print('Divisao por zero!')

