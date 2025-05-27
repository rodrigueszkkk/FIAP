def menu() -> int:
    print('\n =====SISTEMA PDV=====')
    print('---CAIXA FECHADO---')
    print('1- Fazer Login')
    print('2- Sair do Programa')
    return int(input('\n Qual opcao deseja? \n'))


def login_menu():
    print('Digite Suas Credenciais')
    user = input('Usuario: ')
    password = input('Senha: ')
    login(user, password)


def login(user: str, password: str):
    if user == 'admin' and password == 'admin':
        print('Login realizado com sucesso!')
        menu_admin()
    elif user == 'kaiky' and password == '0107':
        print('Login realizado com sucesso!')
        vendas()
    else:
        print('Usuario ou senha invalidos!')
        login_menu()
        return

def vendas():
    print('CAIXA LIVRE')
    cod = int(input('Digite o codigo do produto: '))
    if cod in produtos:
        print(f'Produto encontrado: {produtos[cod]}')
    else:
        print('Produto nao encontrado!')


def menu_admin():
    print('\n =====SISTEMA PDV=====')
    print('1- Cadastrar Produto')
    print('2- Ver Produtos Cadastrados')
    print('3- Encerrar Programa')
    print('4- Abrir Vendar')
    opcao = int(input('\n Qual opcao deseja? \n'))
    
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        lista()
    elif opcao == 3:
        print('Encerrando o programa...')
        exit()
    elif opcao == 4:
        vendas()


def cadastro():

    name = str(input('Digite a descricao do produto: '))
    cod = int(input('digite o codigo do produto: ')) 

    produtos.append(f'Produto: {name} \n Codigo: {cod} \n')



def lista():
    print('=====LISTA DE PRODUTOS JA CADASTRADOS===== \n')

    for i in produtos:
        print (i)
    

    
cadastros = ()
produtos = []
opcao = 0
  

if __name__ == '__main__':
    while opcao != 3:
        opcao = menu()
        if opcao == 1:
            login_menu()
        elif opcao == 2:
            print('Saindo do sistema')
            
        
