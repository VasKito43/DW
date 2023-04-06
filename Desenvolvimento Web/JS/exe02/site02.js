function verificar(){
    var nc = document.getElementById('i')
    var data = new Date()
    var ano = data.getFullYear()
    var res = document.getElementById('res')
    if (nc.value.lenght == 0 || nc.value > ano) {
        window.alert('! ano invalido !')
    }else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(nc.value)
        var genero = ''
        /*var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        img.setAAttribute('src', 'foto.png') */
        if (fsex[0].checked) {
            genero = 'Homem'
        }else {
            genero = 'mulher'
        }
        res.style.textAlign = 'center'
        res.innerHTML = `${genero} com ${idade} anos`
    }
}