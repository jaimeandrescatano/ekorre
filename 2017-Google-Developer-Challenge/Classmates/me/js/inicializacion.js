function miFuncion (evt) {
    /* Asign the color to the cell */
    $('.div_texto-largo').on('click', function() {

        micotiti = $(this).css('height');

        if (micotiti === "300px") {
            $(this).css('height', '1150px' );
        } else {
            $(this).css('height', '300px' );
        }

    });
}


$(miFuncion);
