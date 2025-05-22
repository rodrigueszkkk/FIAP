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
        aux = input(f'alt {i} :')
        while aux != "":
            alternativas.append(aux)
            i = i + 1
            aux = input(f'alt {i} :')

    lista.append(num)
    lista.append(enun)
    lista.append(tipo)
    lista.append(alternativas)

def monta_alternativas(opcoes: list) -> str:
    resp = ''
    letras = 'abcdefghijk'
    i = 0
    while i < len(opcoes):
        resp = resp + f'\t{letras[i]}) {opcoes[i]}\n'
        i = i + 1
    return resp



def aplica_enquete(perguntas: list, respostas: list):
    i = 0
    while i < len(perguntas):
        print(f'{perguntas[i]}) {perguntas[i+1]}')
        if perguntas[i+2] != 'aberta':
            info = monta_alternativas(perguntas[i+3])
            print(info)

        resp = input('Respo: ')
        respostas.append(resp)
        i =+ 4    

    print(f'')




# INICIO PROGRAMA (main)

lista = []
respostas = []
opcao = 0
while opcao != 4:
    opcao = menu()
    if opcao == 1:
        cadastra_pergunta(lista)
    elif opcao == 2:
        print(lista)
    elif opcao == 3:
        print('Apagar pergunta')
    elif opcao == 4:
        aplica_enquete(lista, respostas)
    else:
        print('Opcao Invalida')
