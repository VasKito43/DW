let diagonal = document.querySelectorAll(".diagonal")
let coluna_central = document.querySelectorAll(".coluna_central")
let linha_central = document.querySelectorAll(".linha_central")
let preenchimento = document.querySelectorAll(".preenchimento")



let ativador = 'ativado'

function cor() {

    if (ativador === 'ativado'){
        for (var i = 0; i < diagonal.length; i++) {
            diagonal[i].style.background = "white"
        }
        for (var i = 0; i < coluna_central.length; i++) {
            coluna_central[i].style.background = "white"
        }
        for (var i = 0; i < linha_central.length; i++) {
            linha_central[i].style.background = "white"
        }
        for (var i = 0; i < preenchimento.length; i++) {
            preenchimento[i].style.background = "white"
        }
        ativador = 'desativado'
    } else{
        for (var i = 0; i < diagonal.length; i++) {
            diagonal[i].style.background = "#247BA0"
        }
        for (var i = 0; i < coluna_central.length; i++) {
            coluna_central[i].style.background = "#70C1B3"
        }
        for (var i = 0; i < linha_central.length; i++) {
            linha_central[i].style.background = "#F25F5C"
        }
        for (var i = 0; i < preenchimento.length; i++) {
            preenchimento[i].style.background = "#FFE066"
        }
        ativador = 'ativado'
    }
}