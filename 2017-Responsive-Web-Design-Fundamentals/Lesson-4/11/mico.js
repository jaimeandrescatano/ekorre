/*
* Open the drawer when the menu ison is clicked.

var menu = document.querySelector('#menu');
var main = document.querySelector('main');
var drawer = document.querySelector('#drawer');

menu.addEventListener('click', function(e) {
    drawer.classList.toggle('open');
    e.stopPropagation();
});
main.addEventListener('click', function() {
    drawer.classList.remove('open');
});
*/

var d = document.getElementById('d');

function startProgram (){

    console.log(d.innerHTML);
}

// document.addEventListener('DOMContentLoaded', function () {
//
//     // Our hawaiian greeting is displayed as soon as the page loads,
//
//     startProgram();
//     // const d = document.getElementById('d');
//     // console.log(d.innerHTML);
// });

document.addEventListener('DOMContentLoaded', startProgram());
