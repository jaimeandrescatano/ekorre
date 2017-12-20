var header = document.querySelector('header');
var main = document.querySelector('main');
var barraMenu = document.getElementById('myNav');
var divMenu = document.getElementById('menu-lateral');

/* Cuando el usuario da click en alguna parte sobre la barra menu se aparece el menu hamburguesa*/
function presentarMensaje() {
    divMenu.classList.toggle('open');
    console.log("hola soy un mico titi!")
}

/* Cuando el usuario da click en alguna parte fuera del menu hamburguesa sobre el header entonces se desaparece el menu*/
header.addEventListener('click', function() {
    divMenu.classList.remove('open');
});

/* Cuando el usuario da click en alguna parte fuera del menu hamburguesa entonces se desaparece el menu*/
main.addEventListener('click', function() {
    divMenu.classList.remove('open');
});

/* Cuando el usuario da click en alguna parte sobre la barra menu se aparece el menu hamburguesa*/
barraMenu.addEventListener("click", function () {

    presentarMensaje();

});
