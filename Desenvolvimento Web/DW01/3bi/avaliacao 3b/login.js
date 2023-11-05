var cor_cinzaClaro = "#e2e2e2"
var cor_branco = "white"
var cor_azul = "#1E2772"
var cor_azulClaro = "#006eff"
var cor_laranja = "#FD7401"
var cor_cinzaEscuro = "#747373"

var enter = document.querySelector(".enter")
var img = document.querySelector(".img")
var login = document.querySelector(".buttonlog")
var registrar = document.querySelector(".buttonreg")
var forgot = document.querySelector(".buttonfp")

var input = document.querySelectorAll("input")
var frame = document.querySelectorAll(".frame")
var txt = document.getElementsByClassName("txt")
var label = document.querySelectorAll("label")



registrar.style.color = cor_laranja
registrar.style.backgroundColor = cor_branco
login.style.color = cor_azul
login.style.backgroundColor = cor_branco
forgot.style.color = cor_azulClaro
forgot.style.backgroundColor = cor_branco
enter.style.backgroundColor = cor_laranja
enter.style.color = cor_branco
img.style.backgroundColor = cor_cinzaClaro

for (var i = 0; i < frame.length; i++) {
    frame[i].style.backgroundColor = cor_laranja
}
for (var i = 0; i < txt.length; i++) {
    txt[i].style.color = cor_cinzaEscuro
}
for (var i = 0; i < input.length; i++) {
    input[i].style.backgroundColor = cor_cinzaClaro
}
for (var i = 0; i < label.length; i++) {
    label[i].style.color = cor_cinzaEscuro
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

function limpa_elementos(){
    var email = document.getElementById("email")
    var senha = document.getElementById("senha")

    email.value = ""
    senha.value = ""
}

function verificador(){
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
        limpa_elementos()
    }
}
