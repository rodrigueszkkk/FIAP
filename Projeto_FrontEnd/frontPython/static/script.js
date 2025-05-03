function calcular() {
    const n1 = document.getElementById("n1").value;
    const n2 = document.getElementById("n2").value;
    const operacao = document.getElementById("operacao").value;

    fetch("/calcular", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ n1, n2, operacao })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("resultado").innerText = "Resultado: " + data.resultado;
    });
}
