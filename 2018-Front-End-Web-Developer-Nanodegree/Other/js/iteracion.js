/* Programacion en Javascript

Iteracion

Fuentes:

1 -

*/

/* Metodo FOR clasico */

const digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (let i = 0; i < digits.length; i++) {
  console.log(digits[i]);
}

/* Metodo enredado */

const digits3 = [9990, 1, 2, 3, 456654, 5, 6, 7, 8, 13546579];
for (let index3 in digits3) {
  console.log(digits3[index3]);
}

const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
for (let index in days) {
  console.log(days[index]);
}

const days = ['car', 'pig', 'ape'];
for (let index in days) {
  console.log(days[index]);
}

/*
 * Programming Quiz: Writing a For...of Loop (1-4)
 */

 function capitalizeFirstLetter(string) {
     return string.charAt(0).toUpperCase() + string.slice(1);
 }

 const days2 = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];

 for (let i = 0; i < days2.length; i++) {
     days[i] = capitalizeFirstLetter(days[i]);
   console.log(days[i]);
 }

const books = ["Don Quixote", "The Hobbit", "Alice in Wonderland", "Tale of Two Cities"];
console.log(...books);

/*
 * Instructions: Use the spread operator to combine the `fruits` and `vegetables` arrays into the `produce` array.
 */

const fruits = ["apples", "bananas", "pears"];
const vegetables = ["corn", "potatoes", "carrots"];

const produce = [...fruits, ...vegetables];

console.log(...produce);

/*
 * Programming Quiz: Using the Rest Parameter (1-5)
 */

// your code goes here

function average(...datos) {
    let total = 0;
    for (const dato of datos) {
        total += dato;
    }
    if (average.arguments.length > 0) {
        return total / average.arguments.length;
    } else {
        return 0;
      }
}

console.log(average(2, 6));
console.log(average(2, 3, 3, 5, 7, 10));
console.log(average(7, 1432, 12, 13, 100));
console.log(average());
