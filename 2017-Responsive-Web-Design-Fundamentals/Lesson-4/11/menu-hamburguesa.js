var barraMenu = document.getElementById('myNav');
var divMenu = document.getElementById('menu-lateral');

function presentarMensaje() {
    alert("hola pepe!");
}

barraMenu.addEventListener("click", function () {

    presentarMensaje();

});
