/*
    Este programa tiene el codigo que hice la primera vez,
    mas corto que el que se deja para presentar puesto que
    el de presentar tiene que cumplir con algunos requisitos
 */

/* Funcion generadora de la tabla */
function makeGrid (evt) {
    /* Defino las variables */
    var marranito;
    var perrito;
    var lineaTabla = "";
    var i = 1;

    /* Evito que se desaparezca la tabla generada */
    evt.preventDefault();

    /* Elimino la tabla existente si es que el usuario ya la ha definido antes */
    $("#pixel_canvas").find("tr").remove();

    /* Obtengo los valores del form */
    marranito = $("#input_height").val();
    perrito = $("#input_width").val();

    // console.log(marranito);
    // console.log(perrito);

    /* Genero la tabla */
    /* -- Genero los <td> usando ciclo "for" */
    for (var x = 1; x <= perrito; x++) {
        lineaTabla = lineaTabla+"<td>Hola!</td>";
    }

    /* -- Genero los <tr> usando ciclo "while" */
    while (i <= marranito) {
        $("#pixel_canvas").append("<tr>"+lineaTabla+"</tr>");
        i = i+1;
    }
}

/* Funcion que toma el color seleccionado */
function elegirColor (evt) {
    /* Obtengo el color */
    micoTiti = $("#colorPicker").val();

    /* Asigno el color a la celda en la que se hizo click */
    $('#pixel_canvas').on('click', 'td', function() {
        $(this).css('background-color', micoTiti );
    });
    console.log(micoTiti);
}

/* Creo mi funcion */
function miPerrito () {
    /* Obtengo los valores de la cantidad de filas y de columnas de la tabla */
    $("#sizePicker").on("submit", makeGrid);
    $("#colorPicker").on("change", elegirColor);
}

/* Paso mi funcion al objeto de jQuery */
$(miPerrito);