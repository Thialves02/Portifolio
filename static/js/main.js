let inputNome = document.querySelector('#nome')
let inputEmail = document.querySelector('#email')
let textareaMensagem = document.querySelector('#mensagem')
let btnEnviar = document.querySelector('#enviar')
let checkbox = document.querySelector('#fs')
let btn_Menu = document.querySelector('#btnMenu')

inputNome.addEventListener('keyup',() =>{
    if(inputNome.value.length < 2){
        inputNome.style.borderColor ='red'
    } else{
        inputNome.style.borderColor ='green'
    }
})

inputEmail.addEventListener('keyup',() =>{
    if(inputEmail.value.indexOf('@') == -1 || inputEmail.value.indexOf('.') == -1){
        inputEmail.style.borderColor = 'red'
    } else{
        inputEmail.style.borderColor = 'green'
    }
})

textareaMensagem.addEventListener('keyup',() =>{
    if(textareaMensagem.value.length > 100){
        textareaMensagem.style.borderColor = 'red'
    }else{
        textareaMensagem.style.borderColor = 'green'
    }
})



checkbox.addEventListener('change',()=>{
    if (checkbox.checked) {
        document.querySelector('body').style.backgroundColor = '#192734'
        document.querySelector('#habilidades').style.backgroundColor = '#192734'
        document.querySelector('body').style.color = '#ddd'
        document.querySelector('p').style.color = '#ddd'
        document.querySelector('span').style.color = '#ddd'
        
    }
    else{
        document.querySelector('body').style.backgroundColor = '#fff'
        document.querySelector('#habilidades').style.backgroundColor = '#d7e7ff'
        document.querySelector('body').style.color = 'black'
        document.querySelector('p').style.color = '#3359ec'
        document.querySelector('span').style.color = '#3359ec'
        
    }
    
})

btn_Menu.addEventListener('change',()=>{
    if(btn_Menu.checked){
        document.querySelector('#ul-id').style.display = 'block'
    }else{
        document.querySelector('#ul-id').style.display = 'none'
    }
})

btnEnviar.addEventListener('click', () => {
    /* Pega a div de carregamento */
    let carregamento = document.querySelector('#carregamento')
    /* Mostra a div de carregamento, adicionando o 'flex' ao display */
    carregamento.style.display = 'flex'
 
    /* Pega o Form */
    let form = document.querySelector('form')
    /* Esconde o Form, mudando o display pra 'none' */
    document.querySelector('#form').style.display = 'none'
 })