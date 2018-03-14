// var header = document.querySelector('header');
// var main = document.querySelector('main');
var footer = document.querySelector('footer');
// var header = document.getElementById('nav_menu-hamburguesa');
// var main = document.getElementById('nav_menu-hamburguesa');
var navMenuHamburguesa = document.getElementById('nav_menu-hamburguesa');
var divMenuHamburguesa = document.getElementById('div_menu-hamburguesa');

/* Cuando el usuario da click en alguna parte sobre la barra menu se aparece el menu hamburguesa*/
function presentarMensaje() {
    console.log("proceso 1!")
    divMenuHamburguesa.classList.toggle('open');
}

/* Cuando el usuario da click en alguna parte sobre la barra menu se aparece el menu hamburguesa*/
navMenuHamburguesa.addEventListener("click", function () {
    console.log("proceso 4!")
    presentarMensaje();

});

/* Cuando el usuario da click en alguna parte fuera del menu hamburguesa sobre el header entonces se desaparece el menu*/
// header.addEventListener('click', function() {
//     console.log("proceso 2!")
//     divMenuHamburguesa.classList.remove('open');
// });

/* Cuando el usuario da click en alguna parte fuera del menu hamburguesa entonces se desaparece el menu*/
// main.addEventListener('click', function() {
//     console.log("proceso 3!")
//     divMenuHamburguesa.classList.remove('open');
// });

/* Cuando el usuario da click en alguna parte fuera del menu hamburguesa entonces se desaparece el menu*/
// footer.addEventListener('click', function() {
//     console.log("footer!")
//     divMenuHamburguesa.classList.remove('open');
// });
