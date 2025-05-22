let nome = 'Kaiky';
var sobrenome = 'Pereira'
const ultimoNome = 'Rodrigues'


const idade = 18 + 5

const idade2 = "18"

let mensagem

if (idade < 18){
    mensagem = "é menor de idade"

    let estaHabilitado = false

    console.log("esta habilitado?", estaHabilitado)

} else {
    mensagem = "é maior de idade"

    let estaHabilitado = true
    console.log("esta habilitado?", estaHabilitado)

}

console.log('type da idade',typeof idade)


console.log(nome, mensagem, idade);

function popada(){
    const info = document.getElementById("info")

    if (info.style.display === "none") {
        info.style.display = "block"
    } else {
        info.style.display = "none"
    }
}


document.getElementById('toggle').addEventListener("click", popada)


function soma (a, b){
    return a + b
}


