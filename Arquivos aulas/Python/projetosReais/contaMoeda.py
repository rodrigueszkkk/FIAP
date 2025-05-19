def multi():
    res = qt * valor
    return res

qt = 0
valor = 0

def menu():
    print('''Escolha uma opção:
    [1] - Calcular o valor total
    [2] - Sair''')
    opcao = int(input('Qual opção você deseja? '))
    return opcao

opcao = 0 
while opcao != 2:
    opcao = menu()
    if opcao == 1:
        print(f'O valor total é: {multi()}')
    elif opcao == 2:
        print('Saindo do sistema')
        exit
    else:
        print('Opção inválida, tente novamente.')

