function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('img')
    var data = new Date()
    var min = data.getMinutes()
    var hora = data.getHours()
    msg.innerText = `Agora é ${hora}:${min}`
    if (hora >= 5 && hora < 12){
        img.src = 'manha.png'
        document.body.style.background = '#c2b7a7'
    }else if (hora >= 12 && hora < 18){
        img.src = 'tarde.png'
        document.body.style.background ='#d74004'
    }else if (hora >= 18 || hora < 5){
        img.src = 'noite.png'
        document.body.style.background = '#070928'
    }

}
