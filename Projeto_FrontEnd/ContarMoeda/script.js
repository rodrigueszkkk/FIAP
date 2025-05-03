// document.addEventListener("DOMContentLoaded", () => {
//     const toggleDisplay = (element) => {
//         element.style.display = (element.style.display === "none" || !element.style.display) ? "block" : "none";
//     };

//     const buttons = [
//         { btnId: "#btnMoedas", targetId: "#Moedas", resetMenu: true },
//         { btnId: "#btnCedulas", targetId: "#Cedulas" },
//         { btnId: "#btnTotal", targetId: "#Total" }
//     ];

//     const menu = document.body;

//     buttons.forEach(({ btnId, targetId, resetMenu }) => {
//         const button = document.querySelector(btnId);
//         const target = document.querySelector(targetId);

//         button.addEventListener("click", () => {
//             if (resetMenu) menu.classList.remove("Active");
//             toggleDisplay(target);
//         });
//     }); 
// });

// let btnM = Abas.querySelector('#btnMoedas') // selecionando o botao
// let btnC = Abas.querySelector('#btnCedulas') // selecionando o botao
// let btnT = Abas.querySelector('#btnTotal') // selecionando o botao

// let moedas = document.querySelector('.Moedas')
// let cedulas = document.querySelector('.Cedulas')
// let total = document.querySelector('.Total')


// btnM.addEventListener('click', Moedas)
// btnC.addEventListener('click', Cedulas)
// btnT.addEventListener('click', Total)

// const menu = document.body; // selecionando o menu


// function Moedas(){
//     menu.classList.remove('Active');
//     moedas.classList.toggle('Active')
// }

// function Cedulas(){
//     menu.classList.removeAll('Active');
//     cedulas.classList.toggle('Active')
// }

// function Total(){
//     document.body.classList.remove('Active');
//     total.classList.toggle('Active')
// }


// Selecionando os botões e as seções
const botoes = document.querySelectorAll('.Abas button');
const secoes = document.querySelectorAll('.Moedas, .Cedulas, .Total');

// Função para alternar a classe Active
botoes.forEach(botao => {
    botao.addEventListener('click', () => {
        secoes.forEach(secao => secao.classList.remove('Active'));
        document.getElementById(botao.id.replace('btn', '')).classList.add('Active');
    });
});





// console.log(btnM) //mostrando no console o btn selecionado
// console.log(Abas.querySelectorAll("button"))
// let btnS = Abas.querySelectorAll("button")


// let btnM = Abas.querySelector("button"); // selecionando o botao
// let btnC = Abas.querySelector("button[1]");
// let btnT = Abas.querySelector("button[2]");
// let btnS = Abas.querySelectorAll('button');

// let btn = [
//     {
//     btnId: "#btnMoedas", 
//     targetClass: ".Moedas"
// },
//     {
//     btnId: "#btnCedulas",
//     targetClass: ".Cedulas"
// },
//     {
//     btnId: "#btnTotal",
//     targetClass: ".Total"}
// ]
// abas = Abas.querySelectorAll('button')
// displays = document.querySelectorAll('section')

// let btn = [
//     {   btnId: "#btnMoedas",
//         targetDisplay: ".Moedas"},
        
//     {   btnId: "#btnCedulas",
//         targetDisplay: ".Cedulas"},

//     {   btnId: "#btnTotal",
//         targetDisplay: ".Total"}
// ]
// let btnMoedas = 


// console.log(abas)
// console.log(btn)
// console.log(btnMoedas)

// btnM.addEventListener('click', clicou)

// function clicou() {
//     targetDisplay.classList.toggle('Active')
// }




// btn.forEach(btn => {
//     btnId = Abas.querySelectorAll('button')
//     addEventListener('click', clicou())
// })
// btn.forEach(display => {
//     targetDisplay = document.querySelectorAll("section")
// })


// console.log(btn)
// console.log(targetDisplay)

// function clicou () {
//     Moedas.classList.toggle('Active')
// }


// btnM.addEventListener("click", () => { // criando uma funcao de click no btn selecionado
//     clicou()
// });

// const Moedas = document.querySelector('#Moedas') // colocando na variavel a aba moedas



// function clicou () { // o que a funcao ira fazer
//     if (Moedas.classList.contains('Active')){
//         Moedas.classList.remove('Active')
//     } 
//     else {
//         Moedas.classList.add('Active')
//     }
// }

