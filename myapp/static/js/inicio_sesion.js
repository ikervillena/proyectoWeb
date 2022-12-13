var formulario = document.getElementById('formulario');
formulario.addEventListener("keydown", escribir);

function escribir() {
    var mensaje = document.getElementById('mensaje');
    mensaje.innerText = '¡Recuerda registrarte antes de iniciar sesión!';
    mensaje.style.color = 'red';
    document.getElementById('boton-registro').style.color = 'red';
}