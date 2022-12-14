let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}


//Efectos carrito y favoritos
const mover = {
  transform: 'translateY(-100em)'
}

const timing = {
  duration: 2000,
  iteration: 1,
}

//Carrito
var a = document.getElementById('carrito');
a.addEventListener("click", carrito)

function carrito(){
  document.getElementById('imgcarrito').style.width= '2.5%';
  document.getElementById('imgcarrito').style.height= '4%';
  document.getElementById('imgcarrito').animate(mover,timing);
}

//Favorito
var b = document.getElementById('favorito');
b.addEventListener("click", fav)

function fav(){
  document.getElementById('imgfav').style.width= '2.5%';
  document.getElementById('imgfav').style.height= '4%';
  document.getElementById('imgfav').animate(mover,timing);
}