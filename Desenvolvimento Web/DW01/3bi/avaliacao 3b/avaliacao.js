var azul = "#1E2772"
var laranja = "#FD7401"
var branco = "white"
var cinzaEscuro = "#747373"
var azulClaro = "#006eff"
var cinzaClaro = "#e2e2e2"


var registrar = document.querySelector(".buttonreg")
var login = document.querySelector(".buttonlog")
var forgot = document.querySelector(".buttonfp")
var create = document.querySelector(".ca")
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
create.style.backgroundColor = laranja
create.style.color = branco
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

var botaocreate = document.getElementById("ca")
botaocreate.addEventListener("click", function(event) {
    event.preventDefault()
})

var botaoregistra = document.getElementById("register")
botaoregistra.addEventListener("click", function(event) {
    event.preventDefault()
})

var botaologin = document.getElementById("login")
botaologin.addEventListener("click", function(event) {
    event.preventDefault()
})


function verificador(){
    var nome = document.getElementById("nome").value
    var email = document.getElementById("email").value
    var senha = document.getElementById("senha").value
    if (nome === "") {
        alert("Coloque um nome valido")
    } else if (email === "") {
        alert("coloque um email valido")
    } else if (senha.length < 8) {
        alert("senha tem que ter no minimo 8 caracteres")
    } else {
        alert("cadastro realizado com sucesso")
        limpar()
    }
    nome.value = "";
}

function esqueceu(){
    alert("Funcionalidade não está disponivel no momento")
}

function limpar(){
    var nome = document.getElementById("nome")
    var email = document.getElementById("email")
    var senha = document.getElementById("senha")

    nome.value = ""
    email.value = ""
    senha.value = ""
}