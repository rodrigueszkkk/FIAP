def menu() -> int:
    print('SISTEMA ENQUETE')
    print('1) Cadastrar pergunta')
    print('2) Visuliza sua perguntas')
    print('3) Apagar pergunta')
    print('4) Sair')
    return int(input('Opcão: '))

def cadastra_pergunta(lista: list):
    num = int(input('Numero: '))
    enun = input('Enunciado: ')
    tipo = input('Tipo: ')
    alternativas = None
    if tipo != 'aberta':
        # coletar altenativas
        alternativas = []
        i = 1
        aux = input('alt ' + i + ': ')
        while aux != "":
            alternativas.append(aux)
            i =+ 1
            aux = input('alt ' + i + ": ")

    lista.append(num)
    lista.append(enun)
    lista.append(tipo)
    lista.append(alternativas)

# INICIO PROGRAMA (main)

lista = []

opcao = 0
while opcao != 4:
    opcao = menu()
    if opcao == 1:
        cadastra_pergunta(lista)
    elif opcao == 2:
        print('Visualiza a pergunta')
    elif opcao == 3:
        print('Apagar pergunta')
    elif opcao == 4:
        print('Saindo do sitema')
    else:
        print('Opcao Invalida')
