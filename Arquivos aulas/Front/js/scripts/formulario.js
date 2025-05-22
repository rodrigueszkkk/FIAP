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

    if (nome && email){
    const mensagemSucesso = document.getElementById('certo')
}
    

})