/* Programacion en Javascript

Manejo de objetos

Fuentes:

1 https://google.github.io/styleguide/jsguide.html  --- referencia de google

    Programming Quiz: Umbrella (7-1)

*/


/*
Un objeto es un arreglo de variables y funciones que estan agrupadas
de tal forma que se puede acceder a ellas cuando se refiere a ese
objeto,

Para el ejemplo se tiene el objeto sombrilla, que tiene dos
propiedades o variables y 2 funciones
*/

var umbrella = {
    color: "pink",
    isOpen: true,
    open: function() {
        if (umbrella.isOpen === true) {
            return "The umbrella is already opened!";
        } else {
            umbrella.isOpen = true;
            return "Julia opens the umbrella!";
        }
    },
    close: function() {
        if (umbrella.isOpen === false) {
            return "The umbrella is already closed!";
        } else {
            umbrella.isOpen = false;
            return "Julia closes the umbrella!";
        }
    },
};

console.log(umbrella.open())
console.log(umbrella.close())

/*
    Obtener datos de un objeto
*/

/* Texto */
console.log(`Hola pepe, este es el color de la sombrilla es de color ${umbrella.color}, se ve muy chula`)

/* Datos */
const { color } = umbrella;

console.log("El color de la sombrilla es:");
console.log(color);
