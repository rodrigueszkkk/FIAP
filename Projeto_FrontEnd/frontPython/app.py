from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.get_json()
    n1 = float(data["n1"])
    n2 = float(data["n2"])
    op = data["operacao"]

    try:
        if op == "+":
            resultado = n1 + n2
        elif op == "-":
            resultado = n1 - n2
        elif op == "*":
            resultado = n1 * n2
        elif op == "/":
            resultado = n1 / n2 if n2 != 0 else "Erro: divisão por zero"
        else:
            resultado = "Operação inválida"
    except:
        resultado = "Erro no cálculo"

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)
