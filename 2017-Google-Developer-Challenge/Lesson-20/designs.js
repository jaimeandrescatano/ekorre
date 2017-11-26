/**
    @fileOverview <strong>Main javascript program </strong>
    @author <a href='mailto:jaimeandrescatano@gmail.com'>Jaime Andres Catano</a>
    @version 1.0
*/

/**
    @description Table generating function
    @param  evt
    @returns  nothing
 */

function makeGrid (evt) {
    /* Define variables */
    var tableHeight;
    var tableWidth;
    var tableRow = '';
    var i = 1;

    /* Prevent to delete the new table */
    evt.preventDefault();

    /*
        Delete the current table if the table was defined before
        - The use of the while loop is not required, but is used
          as is required by this exercise in order to delete the
          table rows.
    */
    while (true) {
        $('#pixel_canvas').find('tr').remove();
        break;
    }

    /* Getting the width and height values from the form */
    tableHeight = $('#input_height').val();
    tableWidth = $('#input_width').val();

    /* Generation of the table */
    /* -- Using 'for' loop in order to produce the <td> */
    for (var x = 1; x <= tableWidth; x++) {
        tableRow = tableRow+'<td></td>';
    }

    /* -- Using 'while' loop in order to produce the <tr> */
    while (i <= tableHeight) {
        $('#pixel_canvas').append('<tr>'+tableRow+'</tr>');
        i = i+1;
    }
    return;
}

/** @description  Getting the selected color
    @param  evt
    @returns  nothing
*/
function chooseColor (evt) {
    /* Color value from color picker */
    chosedColor = $('#colorPicker').val();

    /* Asign the color to the cell */
    $('#pixel_canvas').on('click', 'td', function() {
        $(this).css('background-color', chosedColor );
    });
    return;
}

/** @description  Starting function
    @param  nothing
    @returns  nothing
*/
function startProgram () {
    /* makeGrid function activated when the user uses the 'submit button'*/
    $('#sizePicker').on('submit', makeGrid);

    /* Color picker function */
    $('#colorPicker').on('change', chooseColor);
    return;
}

/** @description  Set the startProgram as the initial function of jQuery object
    TODO Request feedback from classmates and mentors.
*/
$(startProgram);
