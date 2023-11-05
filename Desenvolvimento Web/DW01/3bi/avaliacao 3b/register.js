var cor_cinzaClaro = "#e2e2e2"
var cor_branco = "white"
var cor_azul = "#1E2772"
var cor_azulClaro = "#006eff"
var cor_laranja = "#FD7401"
var cor_cinzaEscuro = "#747373"


var registrar = document.querySelector(".buttonreg")
var create = document.querySelector(".ca")
var login = document.querySelector(".buttonlog")
var img = document.querySelector(".img")
var forgot = document.querySelector(".buttonfp")

var txt = document.getElementsByClassName("txt")
var label = document.querySelectorAll("label")
var input = document.querySelectorAll("input")


registrar.style.color = cor_laranja
registrar.style.backgroundColor = cor_branco
login.style.color = cor_azul
login.style.backgroundColor = cor_branco
forgot.style.color = cor_azulClaro
forgot.style.backgroundColor = cor_branco
create.style.backgroundColor = cor_laranja
create.style.color = cor_branco
img.style.backgroundColor = cor_cinzaClaro

for (var i = 0; i < txt.length; i++) {
    txt[i].style.color = cor_cinzaEscuro
}
for (var i = 0; i < label.length; i++) {
    label[i].style.color = cor_cinzaEscuro
}
for (var i = 0; i < input.length; i++) {
    input[i].style.backgroundColor = cor_cinzaClaro
}

var botaofp = document.getElementById("fp")
botaofp.addEventListener("click", function(event) {
    event.preventDefault()
})

var botaocreate = document.getElementById("ca")
botaocreate.addEventListener("click", function(event) {
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
        limpa_elementos()
    }
    nome.value = "";
}

function esqueceu(){
    alert("Funcionalidade não está disponivel no momento")
}

function limpa_elementos(){
    var nome = document.getElementById("nome")
    var email = document.getElementById("email")
    var senha = document.getElementById("senha")

    nome.value = ""
    email.value = ""
    senha.value = ""
}