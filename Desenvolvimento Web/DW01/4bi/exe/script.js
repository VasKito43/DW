var menu_botao = 'desativado'

function menu(){
    
    if (menu_botao === 'desativado') {
        let menu_mobile = document.querySelector(".menu-mobile")
        let img = document.querySelector(".img_menu")
        img.src = "cruz.png"
        menu_mobile.style.left = "0%"
        
        menu_botao = 'ativado'
    }
    else {
        let menu_mobile = document.querySelector(".menu-mobile")
        let img = document.querySelector(".img_menu")
        img.src = "menu-hamburguer.png"
        menu_mobile.style.left = "-100%"
        menu_botao = 'desativado'
    }

}