var boton = document.getElementById('button-productos');
boton.addEventListener("click", clicked);

var ordenadores = document.getElementById('ordenadores');
var telefonos = document.getElementById('telefonos');
var audios = document.getElementById('audios');

function clicked() {
    if (boton.innerHTML == "Ver productos") {
        ordenadores.innerText = 'Ordenadores';
        telefonos.innerText = 'Telefonos';
        audios.innerText = 'Audios';
        boton.innerHTML = "Oculatar productos";
    } else {
        ordenadores.innerText = '';
        telefonos.innerText = '';
        audios.innerText = '';
        boton.innerHTML = "Ver productos"
    }
}

