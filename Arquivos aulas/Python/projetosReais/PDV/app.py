import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime # Importar para registrar data/hora da venda

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui' # Mude para uma chave segura em produção!

# --- Funções de interação com o Banco de Dados (Backend) ---

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
            codigo INTEGER UNIQUE NOT NULL,
            preco REAL NOT NULL DEFAULT 0.0
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            total REAL NOT NULL,
            usuario TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS itens_venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            venda_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            preco_unitario REAL NOT NULL,
            FOREIGN KEY (venda_id) REFERENCES vendas(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    ''')

    cursor.execute("SELECT * FROM usuarios WHERE usuario = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (usuario, senha, tipo) VALUES ('admin', 'admin', 'admin')")

    cursor.execute("SELECT * FROM usuarios WHERE usuario = 'kaiky'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (usuario, senha, tipo) VALUES ('kaiky', '0107', 'vendedor')")

    conn.commit()
    conn.close()

def buscar_usuario(user, senha):
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()
    cursor.execute("SELECT tipo FROM usuarios WHERE usuario = ? AND senha = ?", (user, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def inserir_produto(nome, codigo, preco):
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO produtos (nome, codigo, preco) VALUES (?, ?, ?)", (nome, codigo, preco))
        conn.commit()
        conn.close()
        return True, "Produto cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Erro: código de produto já cadastrado."
    except Exception as e:
        conn.close()
        return False, f"Erro ao cadastrar produto: {e}"

def obter_produtos():
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, codigo, preco FROM produtos ORDER BY nome")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def buscar_produto_por_codigo(codigo):
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco FROM produtos WHERE codigo = ?", (codigo,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado if resultado else None

def buscar_produtos_por_termo(termo):
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()
    termo_like = f"%{termo}%"

    try:
        codigo_int = int(termo)
        cursor.execute("SELECT id, nome, codigo, preco FROM produtos WHERE codigo = ? OR nome LIKE ? ORDER BY nome", (codigo_int, termo_like))
    except ValueError:
        cursor.execute("SELECT id, nome, codigo, preco FROM produtos WHERE nome LIKE ? ORDER BY nome", (termo_like,))
    
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def registrar_venda_db(total, usuario, itens_carrinho):
    conn = sqlite3.connect('pdv.db')
    cursor = conn.cursor()
    try:
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("INSERT INTO vendas (data_hora, total, usuario) VALUES (?, ?, ?)", (data_hora, total, usuario))
        venda_id = cursor.lastrowid

        for item in itens_carrinho:
            cursor.execute(
                "INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
                (venda_id, item['id'], item['quantidade'], item['preco'])
            )
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        conn.rollback()
        conn.close()
        print(f"Erro ao registrar venda: {e}")
        return False

# --- Rotas do Flask ---

@app.before_request
def before_request():
    inicializar_banco()

@app.route('/')
def index():
    if 'user_type' in session:
        if session['user_type'] == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif session['user_type'] == 'vendedor':
            return redirect(url_for('vendas'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = buscar_usuario(username, password)

        if user_type:
            session['username'] = username
            session['user_type'] = user_type
            session['carrinho'] = []
            flash(f'Login realizado com sucesso como {user_type}!', 'success')
            if user_type == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('vendas'))
        else:
            flash('Usuário ou senha inválidos!', 'danger')
            return render_template('login.html', username=username)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_type', None)
    session.pop('carrinho', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('login'))

@app.route('/admin')
def admin_dashboard():
    if 'user_type' not in session or session['user_type'] != 'admin':
        flash('Acesso negado. Faça login como administrador.', 'warning')
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html', username=session['username'])

@app.route('/admin/produtos', methods=['GET', 'POST'])
def produtos():
    if 'user_type' not in session or session['user_type'] != 'admin':
        flash('Acesso negado. Faça login como administrador.', 'warning')
        return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form['nome']
        codigo = request.form['codigo']
        preco = request.form['preco']

        if not nome or not codigo or not preco:
            flash('Todos os campos são obrigatórios!', 'danger')
        else:
            try:
                codigo = int(codigo)
                preco = float(preco)
                success, message = inserir_produto(nome, codigo, preco)
                if success:
                    flash(message, 'success')
                else:
                    flash(message, 'danger')
            except ValueError:
                flash('Código e Preço devem ser números válidos.', 'danger')
            except Exception as e:
                flash(f'Erro inesperado: {e}', 'danger')

    produtos_cadastrados = obter_produtos()
    return render_template('produtos.html', produtos=produtos_cadastrados, username=session['username'])

# A ÚNICA função 'vendas' deve ser esta, a rota do Flask
@app.route('/vendas', methods=['GET', 'POST'])
def vendas():
    if 'user_type' not in session:
        flash('Acesso negado. Faça login para acessar as vendas.', 'warning')
        return redirect(url_for('login'))

    if 'carrinho' not in session:
        session['carrinho'] = []

    produtos_encontrados = []
    
    if request.method == 'POST':
        if 'add_to_cart' in request.form:
            codigo_produto = request.form['codigo_produto_add']
            if codigo_produto:
                try:
                    codigo_int = int(codigo_produto)
                    produto_info = buscar_produto_por_codigo(codigo_int)
                    if produto_info:
                        produto_id, nome_produto, preco_produto = produto_info
                        
                        item_existente = next((item for item in session['carrinho'] if item['id'] == produto_id), None)
                        
                        if item_existente:
                            item_existente['quantidade'] += 1
                            item_existente['subtotal'] = round(item_existente['quantidade'] * item_existente['preco'], 2)
                            flash(f'Quantidade de "{nome_produto}" atualizada no carrinho.', 'info')
                        else:
                            item = {
                                'id': produto_id,
                                'nome': nome_produto,
                                'codigo': codigo_int,
                                'preco': preco_produto,
                                'quantidade': 1,
                                'subtotal': round(preco_produto, 2)
                            }
                            session['carrinho'].append(item)
                            flash(f'"{nome_produto}" adicionado ao carrinho.', 'success')
                        
                        session.modified = True
                    else:
                        flash('Produto não encontrado! Verifique o código.', 'danger')
                except ValueError:
                    flash('Por favor, digite um código numérico válido.', 'danger')
            else:
                flash('Digite o código do produto para adicionar.', 'warning')
        
        elif 'search_product' in request.form:
            termo_busca = request.form['search_term']
            if termo_busca:
                produtos_encontrados = buscar_produtos_por_termo(termo_busca)
                if not produtos_encontrados:
                    flash(f'Nenhum produto encontrado para "{termo_busca}".', 'info')
            else:
                flash('Digite um termo para buscar.', 'warning')

        elif 'clear_cart' in request.form:
            session['carrinho'] = []
            session.modified = True
            flash('Carrinho limpo!', 'info')

        elif 'finish_sale' in request.form:
            total_venda = sum(item['subtotal'] for item in session['carrinho'])
            if total_venda > 0:
                if registrar_venda_db(total_venda, session['username'], session['carrinho']):
                    session['carrinho'] = []
                    session.modified = True
                    flash(f'Venda de R$ {total_venda:.2f} registrada com sucesso!', 'success')
                else:
                    flash('Erro ao finalizar a venda. Tente novamente.', 'danger')
            else:
                flash('Carrinho vazio. Adicione produtos para finalizar a venda.', 'warning')

    total_carrinho = sum(item['subtotal'] for item in session['carrinho'])
    
    return render_template('vendas.html', 
                           carrinho=session['carrinho'], 
                           total_carrinho=total_carrinho, 
                           username=session['username'],
                           produtos_encontrados=produtos_encontrados)

if __name__ == '__main__':
    # Remover ou comentar o menu principal antigo aqui
    # while True:
    #     escolha = menu()
    #     if escolha == 1:
    #         login_menu()
    #     elif escolha == 2:
    #         print('Saindo do sistema...')
    #         break
    
    inicializar_banco() # Garante que o banco seja inicializado ao rodar o Flask
    app.run(debug=True)