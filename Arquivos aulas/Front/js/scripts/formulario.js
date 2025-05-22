document.getElementById('form').addEventListener('submit', function(e){
    
    e.preventDefault()

    const nome = document.getElementById('nome').value
    const email = document.getElementById('email').value

    console.log(nome)

    if(nome === '') {
        alert('kjdans')

    }

    if (email === ''){
        alert('foi')
    }

    const mensagemSucesso = document.getElementById('certo')

    mensagemSucesso.style.display = 'block'

})