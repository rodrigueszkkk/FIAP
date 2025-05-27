import sqlite3

# Criação da base e tabelas (executa só na primeira vez)
def inicializar_banco():
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            codigo INTEGER UNIQUE NOT NULL
        )
    ''')

    # Inserção de usuários fixos (admin e vendedor) se não existirem
    cursor.execute("SELECT * FROM usuarios WHERE usuario = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (usuario, senha, tipo) VALUES ('admin', 'admin', 'admin')")

    cursor.execute("SELECT * FROM usuarios WHERE usuario = 'kaiky'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (usuario, senha, tipo) VALUES ('kaiky', '0107', 'vendedor')")

    conn.commit()
    conn.close()


def menu():
    print('\n =====SISTEMA PDV=====')
    print('---CAIXA FECHADO---')
    print('1 - Fazer Login')
    print('2 - Sair do Programa')
    return int(input('\nQual opção deseja? '))


def login_menu():
    print('Digite suas credenciais')
    user = input('Usuário: ')
    password = input('Senha: ')
    login(user, password)


def login(user, senha):
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()

    cursor.execute("SELECT tipo FROM usuarios WHERE usuario = ? AND senha = ?", (user, senha))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        print('Login realizado com sucesso!')
        if resultado[0] == 'admin':
            menu_admin()
        else:
            vendas()
    else:
        print('Usuário ou senha inválidos!')
        login_menu()


def menu_admin():
    while True:
        print('\n===== MENU ADMINISTRADOR =====')
        print('1 - Cadastrar Produto')
        print('2 - Ver Produtos Cadastrados')
        print('3 - Abrir Vendas')
        print('4 - Encerrar Programa')
        opcao = int(input('\nEscolha uma opção: '))

        if opcao == 1:
            cadastro_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            vendas()
        elif opcao == 4:
            print('Encerrando o programa...')
            break


def cadastro_produto():
    nome = input('Nome do produto: ')
    codigo = int(input('Código do produto: '))

    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO produtos (nome, codigo) VALUES (?, ?)", (nome, codigo))
        conn.commit()
        print('Produto cadastrado com sucesso!')
    except sqlite3.IntegrityError:
        print('Erro: código de produto já cadastrado.')
    conn.close()


def listar_produtos():
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()

    cursor.execute("SELECT nome, codigo FROM produtos")
    produtos = cursor.fetchall()

    print('\n===== PRODUTOS CADASTRADOS =====')
    for nome, codigo in produtos:
        print(f'{nome} - Código: {codigo}')
    conn.close()


def vendas():
    print('\n===== CAIXA LIVRE =====')
    cod = int(input('Digite o código do produto: '))

    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()

    cursor.execute("SELECT nome FROM produtos WHERE codigo = ?", (cod,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        print(f'Produto encontrado: {resultado[0]}')
    else:
        print('Produto não encontrado!')


# Execução
if __name__ == '__main__':
    inicializar_banco()

    while True:
        escolha = menu()
        if escolha == 1:
            login_menu()
        elif escolha == 2:
            print('Saindo do sistema...')
            break
