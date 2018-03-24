/* Programacion en Javascript

Manejo de strings

Fuentes:

1 -

*/


/*
Al igual que en python se puede definir un objeto con textos que pueden
usarse para conformar un texto mas grande.
*/

const persona = {
  name: 'pepe',
  telefono: '07456654'
};

const marranito = `Hello, my name is ${persona.name}`;
const marranito2 = `Hello, my name is ${persona.telefono}`;

console.log(marranito);
console.log(marranito2);


/*
 * Programming Quiz: Build an HTML Fragment (1-2)
 */

const cheetah = {
    name: 'Cheetah',
    scientificName: 'Acinonyx jubatus',
    lifespan: '10-12 years',
    speed: '68-75 mph',
    diet: 'carnivore',
    summary: 'Fastest mammal on land, the cheetah can reach speeds of 60 or perhaps even 70 miles (97 or 113 kilometers) an hour over short distances. It usually chases its prey at only about half that speed, however. After a chase, a cheetah needs half an hour to catch its breath before it can eat.',
    fact: 'Cheetahs have “tear marks” that run from the inside corners of their eyes down to the outside edges of their mouth.'
};

/*
 * Programming Quiz: Build an HTML Fragment (1-2)
 */

const cheetah = {
    name: 'Cheetah',
    scientificName: 'Acinonyx jubatus',
    lifespan: '10-12 years',
    speed: '68-75 mph',
    diet: 'carnivore',
    summary: 'Fastest mammal on land, the cheetah can reach speeds of 60 or perhaps even 70 miles (97 or 113 kilometers) an hour over short distances. It usually chases its prey at only about half that speed, however. After a chase, a cheetah needs half an hour to catch its breath before it can eat.',
    fact: 'Cheetahs have “tear marks” that run from the inside corners of their eyes down to the outside edges of their mouth.'
};

// creates an animal trading card
function createAnimalTradingCardHTML(animal) {

    const cardHTML = `
        <div class="card">
            <h3 class="name"> ${cheetah.name} </h3>
            <img src="${cheetah.name}.jpg" alt="${cheetah.name}" class="picture">
            <div class="description">'
                <p class="fact">${cheetah.fact}</p>
                <ul class="details">
                    <li><span class="bold">Scientific Name</span>: ${cheetah.scientificName}</li>
                    <li><span class="bold">Average Lifespan</span>: ${cheetah.lifespan}</li>
                    <li><span class="bold">Average Speed</span>: ${animal.speed}</li>
                    <li><span class="bold">Diet</span>: ${animal.diet}</li>
                </ul>
                <p class="brief">${cheetah.summary}</p>
            </div>
        </div>`;

    return cardHTML;
}

console.log(createAnimalTradingCardHTML(cheetah));


console.log(createAnimalTradingCardHTML(cheetah));
