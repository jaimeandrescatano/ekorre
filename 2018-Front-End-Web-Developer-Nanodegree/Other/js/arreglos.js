/* Programacion en Javascript

Manejo de arreglos

Fuentes:

1

*/

/* Adquirir datos de un arreglo metodo 1 */
const things = ['red', 'basketball', 'paperclip', 'green', 'computer', 'earth', 'udacity', 'blue', 'dogs'];

const one = things[0];
const two = things[1];
const three = things[2];

const colors = `List of Colors
1. ${one}
2. ${two}
3. ${three}`;

console.log(colors);

/* Adquirir datos de un arreglo metodo 2 */
const [one2, , , two2, , , , three2] = things;

const colors2 = `List of Colors
1. ${one2}
2. ${two2}
3. ${three2}`;

console.log(colors);
