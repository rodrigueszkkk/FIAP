def menu() -> int:
    print('\n =====SISTEMA PDV=====')
    print('1- Cadastrar Produto')
    print('2- Ver Produtos Cadastrados')
    print('3- Encerrar Programa')
    return int(input('\n Qual opcao deseja? '))


cadastros = ()

def cadastro():

    name = str(input('Digite a descricao do produto: '))
    cod = int(input('digite o codigo do produto: ')) 

    produtos.append(name)
    produtos.append(cod)


def lista():
    print('=====LISTA DE PRODUTOS JA CADASTRADOS===== \n')


    for i in produtos:
        print (i)


produtos = []
opcao = 0

while opcao != 3:
    opcao = menu()
    if opcao == 1:
        cadastro()
    if opcao == 2:
        lista()
    if opcao == 3:
        exit

