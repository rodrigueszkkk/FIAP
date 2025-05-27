from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de produtos em memória
produtos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    codigo = request.form['codigo']
    produtos.append({'nome': nome, 'codigo': codigo})
    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)