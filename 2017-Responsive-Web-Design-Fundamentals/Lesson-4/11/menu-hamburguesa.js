var barraMenu = document.getElementById('myNav');
var divMenu = document.getElementById('menu-lateral');

function presentarMensaje() {
    alert("hola pepe!");
}

barraMenu.addEventListener("click", function (e) {

    // Make the coloring happen only to the clicked element by taking the target of the event.

    e.target.presentarMensaje();

});
