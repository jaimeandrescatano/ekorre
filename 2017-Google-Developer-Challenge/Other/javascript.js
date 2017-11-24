/*
    Archivo de estudio de javascript
*/


result=10.25 + 3.99 + 7.15;
var bill=result;
var tip=bill*0.15;

var total=(bill)+(tip);

console.log("$" + total.toFixed(2));



/*
* Programming Quiz: MadLibs (2-11)
*
* 1. Declare a madLib variable
* 2. Use the adjective1, adjective2, and adjective3 variables to set the madLib variable to the message:
*
* 'The Intro to JavaScript course is amazing. James and Julia are so fun. I cannot wait to work through the rest of this entertaining content!'
*/

var madLib=null;

var adjective1 = 'amazing';
var adjective2 = 'fun';
var adjective3 = 'entertaining';

// your code goes here
var madLib = `The Intro to JavaScript course is ${adjective1}. `
+ `James and Julia are so ${adjective2}. `
+ `I cannot wait to work through the rest of this ${adjective3} content!`;

console.log(madLib);
var salida=null;
salida=madLib;

document.getElementById("salida").innerHTML = salida;




var firstName = "Rod";
var interest = "technology";
var hobby = "photograph";

var awesomeMessage = "Hi, my name is " + firstName + ". I love " + interest + ". In my spare time, I like to " + hobby + ".";
console.log(awesomeMessage)



var money = 100.50;
var price = 100.50;

if (money > price) {
console.log("You paid extra, here's your change.");
} else if (money === price) {
console.log("You paid the exact amount, have a nice day!");
} else {
console.log("That's not enough, you still owe me money.");
}



 /*
  * Programming Quiz: Even or Odd (3-2)
  *
  * Write an if...else statement that prints `even` if the
  * number is even and prints `odd` if the number is odd.
  *
  * Note - make sure to print only the string "even" or the string "odd"
  */

 // change the value of `number` to test your if...else statement
 var number = 2;

 if (number%2===0) {
     console.log('even');
 } else {
     console.log('odd');
 }


 /*
  * Programming Quiz: Musical Groups (3-3)
  */

 // change the value of `musicians` to test your conditional statements
 var musicians = 1;

 // your code goes here
 var musicians = 1;

 if (musicians <= 0)
     console.log("not a group");
 else if (musicians === 1)
     console.log("solo");
 else if (musicians === 2)
     console.log("duet");
 else if (musicians === 3)
     console.log("trio");
 else if (musicians === 4)
     console.log("quartet");
 else
     console.log("this is a large group");


     /*
      * Programming Quiz: Murder Mystery (3-4)
      */

     // change the value of `room` and `suspect` to test your code
      var room = "gallery";
      var weapon = "trophy";
      var suspect = "Ms. Van Cleve";
      var solved = false;

if (room === "dining room") {
    weapon = "knife", solved = true, suspect === "Mr. Parkes";
} else if (room === "ballroom") {
    weapon = "poison", solved = true, suspect === "Mr. Kalehoff";
} else if (room === "billiards room") {
    weapon = "pool stick", solved = true, suspect === "Mrs. Sparr";
} else {
    weapon = "trophy", solved = true, suspect === "Ms. Van Cleve";
}

if (solved) {
	console.log(suspect + " did it in the " + room + " with the " + weapon +"!");
}

/*
 * Programming Quiz - Checking Your Balance (3-5)
 */

/* Esta fue la solucion que estaba armando, funciona pero Udacity no la valida no se porque */

// change the values of `balance`, `checkBalance`, and `isActive` to test your code
var balance = 325.00;
var checkBalance = true;
var isActive = false;

// your code goes here

if (checkBalance=== false) {
  console.log("Thank you have a nice day!");
}
else {
  if (balance > 0 && isActive === true) {
    console.log("Your balance is $" + balance.toFixed(2)+".");
  }
  else if (isActive === false){
      console.log("Your account is no longer active.");
  }
  else if (balance === 0){
      console.log("Your account is empty");
  }
  else {
     console.log("Your balance is negative, please contact bank.");
  }
}


/* Esta fue la solucion que encontre y que funciono */
var balance = 325.00;
var checkBalance = true;
var isActive = false;

// your code goes here
if (checkBalance) {
    if (isActive && balance > 0) {
        console.log(`Your balance is $${balance}.`);
    } else if (!isActive) {
        console.log("Your account is no longer active.");
    } else if (balance === 0) {
        console.log("Your account is empty.");
    } else {
        console.log("Your balance is negative. Please contact bank.");
    }
} else {
    console.log("Thank you. Have a nice day!");
}




/*
 * Programming Quiz: Ice Cream (3-6)
 *
 * Write a single if statement that logs out the message:
 *
 * "I'd like two scoops of __________ ice cream in a __________ with __________."
 *
 * ...only if:
 *   - flavor is "vanilla" or "chocolate"
 *   - vessel is "cone" or "bowl"
 *   - toppings is "sprinkles" or "peanuts"
 *
 * We're only testing the if statement and your boolean operators.
 * It's okay if the output string doesn't match exactly.
 */

// change the values of `flavor`, `vessel`, and `toppings` to test your code
var flavor = "chocolate";
var vessel = "cone";
var toppings = "sprinkles";

// Add your code here
if ((flavor === "vanilla" || flavor === "chocolate") &&
		(vessel === "cone" || vessel === "bowl") &&
		(toppings === "sprinkles" || toppings === "peanuts")) {
				console.log("I'd like two scoops of " + flavor + " ice cream in a " + vessel + " with " + toppings + ".");
		}




/*
 * Programming Quiz: What do I Wear? (3-7)
 */

// change the values of `shirtWidth`, `shirtLength`, and `shirtSleeve` to test your code
var shirtWidth = 28
var shirtLength = 33;
var shirtSleeve = 10.13;

// your code goes here
if (((shirtWidth >= 18 && shirtWidth < 20) && (shirtLength >= 28 && shirtLength < 29) && (shirtSleeve >= 8.13 && shirtSleeve < 8.38))) {
  console.log("S");
}else if (((shirtWidth >= 20 && shirtWidth < 22) && (shirtLength >= 29 && shirtLength< 30) && (shirtSleeve >= 8.38 && shirtSleeve < 8.63))){
  console.log("M");
}else if (((shirtWidth >= 22 && shirtWidth < 24) && (shirtLength >= 30 && shirtLength< 31) && (shirtSleeve >= 8.63 && shirtSleeve < 8.88))){
  console.log("L");
}else if (((shirtWidth >= 24 && shirtWidth < 26) && (shirtLength >= 31 && shirtLength< 33) && (shirtSleeve >= 8.88 && shirtSleeve < 9.63))){
  console.log("XL");
}else if (((shirtWidth >= 26 && shirtWidth < 28) && (shirtLength >= 33 && shirtLength< 34) && (shirtSleeve >= 9.63 && shirtSleeve < 10.13))){
  console.log("2XL");
}else if (((shirtWidth >= 28) && (shirtLength >= 34 ) && (shirtSleeve >= 10.13 ))){
  console.log("3XL");
}else {
  console.log("N/A");
}



/*
 * Programming Quiz - Navigating the Food Chain (3-8)
 *
 * Use a series of ternary operator to set the category to one of the following:
 *   - "herbivore" if an animal eats plants
 *   - "carnivore" if an animal eats animals
 *   - "omnivore" if an animal eats plants and animals
 *   - undefined if an animal doesn't eat plants or animals
 *
 * Notes
 *   - use the variables `eatsPlants` and `eatsAnimals` in your ternary expressions
 *   - `if` statements aren't allowed ;-)
 */

// change the values of `eatsPlants` and `eatsAnimals` to test your code

// Mi codigo: funciona pero no le gusto al Udacity
var eatsPlants = false;
var eatsAnimals = true;

var category = ( eatsPlants ? (eatsAnimals ? ("omnivore") : ("herbivore") ) : (eatsAnimals ? ("carnivore") : ("undefined")))

console.log(category);

// Codigo que encontre y que funciono en el Udacity:

var category = eatsPlants && eatsAnimals ? "omnivore": eatsPlants ? "herbivore" : eatsAnimals ? "carnivore" : undefined;

console.log(category);




/*
 * Programming Quiz: Back to School (3-9)
 */

// change the value of `education` to test your code
var education = "no high school diploma";

// set the value of this based on a person's education
var salary;

// your code goes here
switch (education) {
  case "no high school diploma":
    salary ="$25,636";
    break;
  case "a high school diploma":
    salary ="$35,256";
    break;
  case"an Associate's degree" :
    salary ="$41,496";
    break;
  case "a Bachelor's degree":
    salary ="$59,124";
    break;
  case "a Master's degree":
    salary ="$69,732";
    break;
  case "a Professional degree":
    salary ="$89,960";
    break;
  case "a Doctoral degree":
    salary="$84,396";
    break;
}
console.log("In 2015, a person with " + education +" earned an average of "+ salary+"/year.");


/*
 * Programming Quiz: JuliaJames (4-1)
 */

var x = 1;

while (x<=20) {
    if (x%3===0 && x%5===0) {
        console.log("JuliaJames");
    }
    else if (x%3===0) {
        console.log("Julia");
    }
    else if (x%5===0) {
        console.log("James");
    }
    else {
        console.log(x);
    }

    x=x+1;
}

/*
 * Programming Quiz: 99 Bottles of Juice (4-2)
 *
 * Use the following `while` loop to write out the song "99 bottles of juice".
 * Log the your lyrics to the console.
 *
 * Note
 *   - Each line of the lyrics needs to be logged to the same line.
 *   - The pluralization of the word "bottle" changes from "2 bottles" to "1 bottle" to "0 bottles".
 */

 var num = 99;

 while (num>0) {

   if (num===2) {
     frase=num+" bottles of juice on the wall! "+num+" bottles of juice! Take one down, pass it around... "+(num-1)+" bottle of juice on the wall!";
     console.log(frase);
   }
   else if (num===1) {
     frase=num+" bottle of juice on the wall! "+num+" bottle of juice! Take one down, pass it around... "+(num-1)+" bottles of juice on the wall!";
     console.log(frase);
   }
   else {
     frase=num+" bottles of juice on the wall! "+num+" bottles of juice! Take one down, pass it around... "+(num-1)+" bottles of juice on the wall!";
     console.log(frase);
   }

   num=num-1;
 }


 /*
 * Programming Quiz: Countdown, Liftoff! (4-3)
 *
 * Using a while loop, print out the countdown output above.
 */

 var x=60;

 while (x>=0) {

   if (x===50) {
     console.log("Orbiter transfers from ground to internal power");
   }
   else if (x===31) {
     console.log("Ground launch sequencer is go for auto sequence start");
   }
   else if (x===16) {
     console.log("Activate launch pad sound suppression system");
   }
   else if (x===10) {
     console.log("Activate main engine hydrogen burnoff system");
   }
   else if (x===6) {
     console.log("Main engine start");
   }
   else if (x===0) {
     console.log("Solid rocket booster ignition and liftoff!");
   }
   else {
     console.log("T-"+x+" seconds")
   }

   x=x-1;
 }


 /*
  * Programming Quiz: Changing the Loop (4-4)
  */

 // rewrite the while loop as a for loop
 /*
 var x = 9;
 while (x >= 1) {
     console.log("hello " + x);
     x = x - 1;
 }
 */

 for (var x=9;x>=1;x=x-1) {
     console.log("hello "+x);
 }



 /*
 * Programming Quiz: Fix the Error 1 (4-5)
 */

// fix the for loop
for (var x=5;x < 10; x++) {
    console.log(x);
}


/*
 * Programming Quiz: Fix the Error 2 (4-6)
 */

// fix the for loop
for (var k = 0; k < 200; k++) {
    console.log(k);
}



/*
 * Programming Quiz: Factorials (4-7)
 */

// your code goes here

var solution=1;

for (var x=12;x>=1;x=x-1) {

    solution=solution*x;

}
console.log(solution);



/*
 * Programming Quiz: Find my Seat (4-8)
 *
 * Write a nested for loop to print out all of the different seat combinations in the theater.
 * The first row-seat combination should be 0-0
 * The last row-seat combination will be 25-99
 *
 * Things to note:
 *  - the row and seat numbers start at 0, not 1
 *  - the highest seat number is 99, not 100
 */

// Write your code here

for (var x=0;x<=25;x++) {
    for (var y=0;y<=99;y++) {
        console.log(x+"-"+y);
    }
}



/*
 * Programming Quiz: Laugh it Off 1 (5-1)
 */

// your code goes here

function laugh() {
    return("hahahahahahahahahaha!")
}

console.log(laugh());




/*
 * Programming Quiz: Laugh it Off 2 (5-2)
 *
 * Write a function called `laugh` with a parameter named `num` that represents the number of "ha"s to return.
 *
 * Note:
 *  - make sure your the final character is an exclamation mark ("!")
 */


 function laugh(num) {
     var mico = "";
     for (x=num;x>0;x--) {
         mico = mico+"ha";
     }
     mico = mico+"!";

     return(mico);
 }

 console.log(laugh(3));



 /*
 * Programming Quiz: Build A Triangle (5-3)
 */

// creates a line of * for a given length
function makeLine(length) {
    var line = "";
    for (var j = 1; j <= length; j++) {
        line += "* ";
    }
    return line + "\n";
}

// your code goes here.  Make sure you call makeLine() in your own code.

function buildTriangle (num) {
  var salida = "";
  for (x=1;x<=num;x++) {
    salida = salida + makeLine(x);

  }
  return salida;
}


// test your code by uncommenting the following line
console.log(buildTriangle(10));


/*
 * Programming Quiz: Laugh (5-4)
 Write an anonymous function expression that stores a function in a variable called "laugh" and outputs the number of "ha"s that you pass in as an argument.
 */

var laugh = function (num) {
     var mico = "";
     for (x=num;x>0;x--) {
         mico = mico+"ha";
     }
     mico = mico+"!";

     return(mico);
 }

 console.log(laugh(10));


 /*
  * Programming Quiz: Cry (5-5)
  */

 // your code goes here
 var cry=function mico() {
     return ("boohoo!");
 }

 console.log(cry())


 /*
  * Programming Quiz: Inline Functions (5-6)
  */

 // don't change this code
 function emotions(myString, myFunc) {
     console.log("I am " + myString + ", " + myFunc(2));
 }

 // your code goes here
 // call the emotions function here and pass in an
 // inline function expression


// PILAS!!! simplemente declaro la funcion como uno de los parametros de otra funcion

 emotions("happy", function laugh(num) {
      var mico = "";
      for (x=num;x>0;x--) {
          mico = mico+"ha";
      }
      mico = mico+"!";

      return(mico);
 }); // you can use your laugh function from the previous quizzes


 /*
  * Programming Quiz: UdaciFamily (6-1)
  */

 // your code goes here

 var udaciFamily = ["Julia", "James", "Jaime"];

 console.log(udaciFamily);




 /*
 * Programming Quiz: Building the Crew (6-2)
 */

var captain = "Mal";
var second = "Zoe";
var pilot = "Wash";
var companion = "Inara";
var mercenary = "Jayne";
var mechanic = "Kaylee";

// your code goes here

var crew = [captain, second, pilot, companion, mercenary, mechanic];
console.log(crew);




/*
 * Programming Quiz: The Price is Right (6-3)
 */

var prices = [1.23, 48.11, 90.11, 8.50, 9.99, 1.00, 1.10, 67.00];

// your code goes here

prices[0]=5;
prices[2]=6;
prices[7]=7;

console.log(prices);


/*
 * Programming Quiz: Colors of the Rainbow (6-4)
 Remove "Blackberry"
 Add "Yellow" and "Green"
 Add "Purple"
 */

var rainbow = ["Red", "Orange", "Blackberry", "Blue"];

rainbow.splice(2,1);
rainbow.splice(0,0, "Yellow", "Green");
rainbow.splice(0,0, "Purple");

console.log(rainbow);

// your code goes here



/*
 * Programming Quiz: Quidditch Cup (6-5)
 */

// your code goes here

var team = ["Oliver Wood", "Angelina Johnson", "Katie Bell", "Alicia Spinnet", "George Weasley", "Fred Weasley", "Harry Potter"];

function hasEnoughPlayers(num) {
  if (num.length>=7) {
    return (true);
  }
  else {
    return (false);
  }
}

console.log(hasEnoughPlayers(team));




/*
 * Programming Quiz: Joining the Crew (6-6)
 */

var captain = "Mal";
var second = "Zoe";
var pilot = "Wash";
var companion = "Inara";
var mercenary = "Jayne";
var mechanic = "Kaylee";

var crew = [captain, second, pilot, companion, mercenary, mechanic];

var doctor = "Simon";
var sister = "River";
var shepherd = "Book";

// your code goes here

crew.push(doctor);
crew.push(sister);
crew.push(shepherd);

console.log(crew);



/*
 * Programming Quiz: Another Type of Loop (6-8)
 *
 * Use the existing `test` variable and write a `forEach` loop
 * that adds 100 to each number that is divisible by 3.
 *
 * Things to note:
 *  - you must use an `if` statement to verify code is divisible by 3
 *  - you can use `console.log` to verify the `test` variable when you're finished looping
 */

var test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4,
    19, 300, 3775, 299, 36, 209, 148, 169, 299,
    6, 109, 20, 58, 139, 59, 3, 1, 139
];

// Write your code here



test.forEach(function (elemento, indice, arreglo) {
  if (elemento%3===0) {
    arreglo [indice] = elemento +100;
    //console.log(elemento);

  }
  else {
    //console.log(elemento);

  }

});

console.log(test);


/*
 * Programming Quiz: I Got Bills (6-9)
 *
 * Use the .map() method to take the bills array below and create a second array
 * of numbers called totals. The totals array should contains each amount from the
 * bills array but with a 15% tip added. Log the totals array to the console.
 *
 * For example, the first two entries in the totals array would be:
 *
 * [57.76, 21.99, ... ]
 *
 * Things to note:
 *  - each entry in the totals array must be a number
 *  - each number must have an accuracy of two decimal points
 */

 var bills = [50.23, 19.12, 34.01,
     100.11, 12.15, 9.90, 29.11, 12.99,
     10.00, 99.22, 102.20, 100.10, 6.77, 2.22
 ];

 var totals = bills.map(function(bill) {
   bill = (bill * 0.15)+bill;

   return Number(bill.toFixed(2)); //--> toFixed() need toFixed(2) to show how many decimal.
 });
 console.log(totals);


 /*
 * Programming Quiz: Nested Numbers (6-10)
 *
 *   - The `numbers` variable is an array of arrays.
 *   - Use a nested `for` loop to cycle through `numbers`.
 *   - Convert each even number to the string "even"
 *   - Convert each odd number to the string "odd"
 */

var numbers = [
    [243, 12, 23, 12, 45, 45, 78, 66, 223, 3],
    [34, 2, 1, 553, 23, 4, 66, 23, 4, 55],
    [67, 56, 45, 553, 44, 55, 5, 428, 452, 3],
    [12, 31, 55, 445, 79, 44, 674, 224, 4, 21],
    [4, 2, 3, 52, 13, 51, 44, 1, 67, 5],
    [5, 65, 4, 5, 5, 6, 5, 43, 23, 4424],
    [74, 532, 6, 7, 35, 17, 89, 43, 43, 66],
    [53, 6, 89, 10, 23, 52, 111, 44, 109, 80],
    [67, 6, 53, 537, 2, 168, 16, 2, 1, 8],
    [76, 7, 9, 6, 3, 73, 77, 100, 56, 100]
];

// your code goes here

for (var x=0;x<numbers.length;x++) {

  for (var y=0;y<numbers[x].length;y++) {

    if (numbers[x][y]%2===0) {
      numbers[x][y]="even";
    }
    else {
      numbers[x][y]="odd";
    }
  }
  console.log(numbers[x]);
}


/*
 * Programming Quiz: Umbrella (7-1)
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
    // your code goes here
    close: function() {
        if (umbrella.isOpen === false) {
            return "The umbrella is already closed!";
        } else {
            umbrella.isOpen = false;
            return "Julia closes the umbrella!";
        }
    },
};


/*
 * Programming Quiz: Menu Items (7-2)
 */

// your code goes here
var breakfast = {
    name:"The Lumberjack",
    price:9.95,
    menu:["eggs", "sausage", "toast", "hashbrowns", "pancakes"],
};


/*
 * Programming Quiz: Bank Accounts 1 (7-3)
 */

var savingsAccount = {
    balance: 1000,
    interestRatePercent: 1,
    deposit: function addMoney(amount) {
        if (amount > 0) {
            savingsAccount.balance += amount;
        }
    },
    withdraw: function removeMoney(amount) {
        var verifyBalance = savingsAccount.balance - amount;
        if (amount > 0 && verifyBalance >= 0) {
            savingsAccount.balance -= amount;
        }
    },
    // your code goes here
    printAccountSummary() {
        message="Welcome!\nYour balance is currently $1000 and your interest rate is 1%.";
        return (message);
    }
};

console.log(savingsAccount.printAccountSummary());




/*
 * Programming Quiz: Facebook Friends (7-5)
 */

 /*
 The object should have 3 properties:

 your name
 the number of friends you have, and
 an array of messages you've posted (as strings)
 The object should also have 4 methods:

 postMessage(message) - adds a new message string to the array
 deleteMessage(index) - removes the message corresponding to the index provided
 addFriend() - increases the friend count by 1
 removeFriend() - decreases the friend count by 1
 */

// your code goes here

var facebookProfile = {
    name: "Jaime",
    friends: 10,
    messages: ["mes1","mes2","mes3",],

    postMessage: function (message) {
      this.messages.push(message);
    },
    deleteMessage: function (indice) {
      this.messages.splice(indice, 1);
    },
    addFriend: function () {
      this.friends = this.friends + 1;
    },
    removeFriend: function () {
      this.friends = this.friends - 1;
    },
};

console.log(facebookProfile.messages);

facebookProfile.postMessage("cerdo");

console.log(facebookProfile.messages);

facebookProfile.deleteMessage(2);

console.log(facebookProfile.messages);

console.log(facebookProfile.friends);

facebookProfile.addFriend();

console.log(facebookProfile.friends);

facebookProfile.removeFriend();

console.log(facebookProfile.friends);



/*
 * Programming Quiz: Donuts Revisited (7-6)
 Directions:
Use the forEach() method to loop over the array and print out the following donut summaries using console.log.

Jelly donuts cost $1.22 each
Chocolate donuts cost $2.45 each
Cider donuts cost $1.59 each
Boston Cream donuts cost $5.99 each
 */

var donuts = [
    { type: "Jelly", cost: 1.22 },
    { type: "Chocolate", cost: 2.45 },
    { type: "Cider", cost: 1.59 },
    { type: "Boston Cream", cost: 5.99 }
];

// your code goes here

donuts.forEach(
  function (elemento) {
    frase= elemento.type + " donuts cost $" + elemento.cost + " each";
    console.log(frase);
  }
);




/* LESSON 18: jQuery */

/* Seleccionar todos los elementos del DOM */

/*
For this quiz, use a jQuery tag selector to grab all of the <li>s on the page!
*/

// Start with this variable! (don't delete it!)
var listElements;

listElements = $("li"); // your code goes here!
console.log(listElements);

// Para Seleccionar elementos del DOM de tipo class:
var listElements;

listElements = $(".myclass"); // Notar el punto igual que en css
console.log(listElements);

/* Para seleccionar elementos relacionados a un item del DOM */

/* Puedo saber quienes son los parents de un item con */
$(#mielemento).parent(); // el parent inmediato
$(#mielemento).parents(); //el parent inmediato, o el parent del parent y asi hacia arriba en el DOM

/* Que items son los children? */
$(#mielemento).children(); // obtengo el listado de los children de mi elemento
$(#mielemento).find(); // obtengo los children inmediatos, o los children de los children

/* Que items son los siblings? */
$(#mielemento).siblings(); // obtengo los siblings de mi elemento


/*
For this quiz, remove the class 'featured' from Article #2 and add it to Article #3!

You must use jQuery's toggleClass method!
*/

// don't change these variable!
var article2, article3;

// your code goes here!

article3 = $(".featured").next().toggleClass("featured");

article2 = $(".featured").toggleClass();

/*
For this quiz, set the href of the <a> in the first nav item to "#1".

You must use jQuery's attr() method!
*/

// Start with this variable!
/* Esta fue mi solucion y funciona pero el sistema de audacity no lo valida */
var navList;

firstItem = $(".nav-list");// your code goes here!

firstItem = firstItem.children();

firstItem = firstItem.first();

firstItem = firstItem.find("a");

firstItem = firstItem.attr("href", "#1");

console.log(firstItem);

/* Esta fue la solucion que encontre en el foro y que funciono */
var navList;
navList = $('.nav-list li a').first();
navList.attr('href', '#1');


/*
For this quiz, change the font-size of all the article-items to 20px!

You must use jQuery's css() method!
*/

// Start with this variable!
var articleItems;

articleItems = $(".article-item").css("font-size", "20px");// your code goes here!


/* Como procedimiento de trabajo con jQuery puedo crear un h1 temporal para ver la salida y para no tener que usar la consola de javascript */
var articleItems;
var misalida;
articleItems = $(".articles").find("ul").html(); //notar que tomo el html

misalida = $("#misalida"); // aqui tomo mi p temporal dentro de h1
misalida = misalida.text(articleItems);




/*
For this quiz, use jQuery's val method to make live changes to the 'Cool Articles' <h1>!

The starter code below creates an event listener that will run any time the input changes.
For more on events, check the instructor notes.
*/


$('#input').on('change', function() {
    var val;
    var texto;


    texto = $("#input").val();

    val = $(".articles").find("h1");
    val = val.text(texto);
});


/*
For this quiz, remove the <ul> from the first article item!

You must use jQuery's remove() method.
*/

// Start with this variable!
var articleItems;
articleItems = $(".articles").find("ul").find("ul").remove();



/* Insertar componentes dentro del tag despues y antes de lo que hay actualmente dentro del tag */
elemento.append()
elemento.prepend()

/* Insertar siblings de un elemento */
elemento.insertAfter()
elemento.insertBefore()



/*
For this quiz, you'll need to add to the DOM tree that already exists.

'#family2' should be a sibling of and come after '#family1'. '#bruce' should be the only immediate child
of '#family2'. '#bruce' should have two <div>s as children, '#madison' and '#hunter'.
*/

/* Creo el div con el id de familia 2 */

sapo = $("#family1").html();

$("<div id=\"family2\">"+sapo+"</div>").insertAfter("#family1");

/* Cambio el nombre del h1 */

$("#family2").children("h1").text("Family2");

/* En family2 Paso a bob a ser hijo de alex y de una vez le cambio el id a hunter*/

micotiti = $("#family2").children("#alex").children("#jane");

gato = $("#family2").children("#taylor").children("#bob").html();

$("<div id=\"hunter\">"+gato+"</div>").insertAfter(micotiti);

/* Elimino  el div de taylor */

$("#family2").children("#taylor").remove();

/* Cambio el nombre de Alex a Bruce */

$("#family2").children("#alex").attr("id","bruce");

/* Cambio el nombre de h2 de Alex a Bruce */

$("#family2").children("#bruce").children("h2").text("Bruce");

/* Cambio el id de jane a madison */

$("#family2").children("#bruce").children("#jane").attr("id", "madison");

/* Cambio el nombre de h3 de jane a Madison */

$("#family2").children("#bruce").children("#madison").children("h3").text("Madison");

/* Cambio el nombre de h3 de bob a Hunter */

$("#family2").children("#bruce").children("#hunter").children("h3").text("Hunter");




/*
For this quiz, use jQuery's each() method to iterate through the <p>s,
calculate the length of each one, and add each length to the end of each <p>.

Also, make sure you don't change the text inside each <p> except to add the length, otherwise your
length numbers won't be correct!
*/

/* Defino un arreglo */
var miarreglo=[];
var perrito;

/* Obtengo el dom de la class article-list y busco todos los "p" y a cada uno le hago un cambio*/
$(".article-list").find("p").each(

    function ( index ) {
        /* Guardo la informacion de cada parrafo en mi arreglo */
        miarreglo[index] = $( this ).text();

        /* Calculo length para cada parrafo */
        gato = miarreglo[index].length;

        /* Inserto la length dentro de cada parrafo al final segun indicacion */
        perrito = $( this ).text();
        perrito = perrito + gato;
        $( this ).text(perrito);

        //console.log(miarreglo[index].length);
        //console.log( index + ": " + $( this ).text() );
    }

    );
