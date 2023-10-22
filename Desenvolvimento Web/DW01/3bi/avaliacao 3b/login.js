var azul = "#1E2772"
var laranja = "#FD7401"
var branco = "white"
var cinzaEscuro = "#747373"
var azulClaro = "#006eff"
var cinzaClaro = "#e2e2e2"

var registrar = document.querySelector(".buttonreg")
var login = document.querySelector(".buttonlog")
var forgot = document.querySelector(".buttonfp")
var enter = document.querySelector(".enter")
var img = document.querySelector(".img")

var txt = document.getElementsByClassName("txt")
var label = document.querySelectorAll("label")
var input = document.querySelectorAll("input")


registrar.style.color = laranja
registrar.style.backgroundColor = branco
login.style.color = azul
login.style.backgroundColor = branco
forgot.style.color = azulClaro
forgot.style.backgroundColor = branco
enter.style.backgroundColor = laranja
enter.style.color = branco
img.style.backgroundColor = cinzaClaro

for (var i = 0; i < txt.length; i++) {
    txt[i].style.color = cinzaEscuro
}
for (var i = 0; i < label.length; i++) {
    label[i].style.color = cinzaEscuro
}
for (var i = 0; i < input.length; i++) {
    input[i].style.backgroundColor = cinzaClaro
}

var botaofp = document.getElementById("fp")
botaofp.addEventListener("click", function(event) {
    event.preventDefault()
})

var botaocreate = document.getElementById("enter")
botaocreate.addEventListener("click", function(event) {
    event.preventDefault()
})


function esqueceu(){
    alert("Funcionalidade não está disponivel no momento")
}

function limpar(){
    var email = document.getElementById("email")
    var senha = document.getElementById("senha")

    email.value = ""
    senha.value = ""
}

function verificar(){
    var email = document.getElementById("email").value
    var senha = document.getElementById("senha").value
    if (email === "") {
        alert("coloque um email valido")
    } else if (senha.length < 8) {
        alert("senha tem que ter no minimo 8 caracteres")
    } else if (email != "admin@email.com.br") {
        alert("email ainda não cadastrado")
    } else if(senha != "#dw1UTFPR#") {
        alert("senha invalida")
    } else {
        alert("Usuario autenticado com sucesso")
        limpar()
    }
}
