from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para criar o banco de dados e a tabela
def criar_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir um novo usuário
def inserir_usuario(nome, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, senha)
        VALUES (?, ?)
    ''', (nome, senha))
    conn.commit()
    conn.close()

# Função para exibir todos os usuários cadastrados
def exibir_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Função para apagar todos os usuários
def resetar_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios')
    conn.commit()
    conn.close()

# Rota para a página principal (formulário)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para inserir um novo usuário
@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form['nome']
    senha = request.form['senha']
    inserir_usuario(nome, senha)
    return redirect(url_for('index'))  # Redireciona de volta para a página inicial

# Rota para exibir os usuários
@app.route('/usuarios')
def usuarios():
    usuarios = exibir_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

# Rota para resetar o banco de dados
@app.route('/resetar', methods=['POST'])
def resetar():
    resetar_banco()
    return redirect(url_for('index'))

if __name__ == '__main__':
    criar_banco()  # Cria o banco de dados e a tabela ao rodar o servidor
    app.run(debug=True)