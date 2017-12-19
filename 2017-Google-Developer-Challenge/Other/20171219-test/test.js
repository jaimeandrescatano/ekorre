function startProgram() {

    var lochNess = document.querySelector(".monsters");
    console.log("It's from Scotland - " + lochNess.textContent);

    var scary = document.querySelectorAll(".monsters");
    console.log("Hide and seek champions: ");

    for (var i = 0; i < scary.length; i++) {
        console.log(scary[i].innerHTML);
    }
}

window.onload = startProgram();
