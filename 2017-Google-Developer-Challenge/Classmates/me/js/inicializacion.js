function activarSecciones () {
    try {
        setTimeout(function sec_miseccion1(){
                        var mivar1 = document.getElementsByClassName("sec_miseccion1");
                        mivar1[0].style.display = "block";
                   },5);
    }
    catch(err) {
        console.log("Seccion no presente");
    }
    try {
        setTimeout(function sec_miseccion2(){
                        var mivar2 = document.getElementsByClassName("sec_miseccion2");
                        mivar2[0].style.display = "block";
                   },10);
    }
    catch(err) {
        console.log("Seccion no presente");
    }
    try {
        setTimeout(function sec_miseccion3(){
                        var mivar3 = document.getElementsByClassName("sec_miseccion3");
                        mivar3[0].style.display = "block";
                   },15);
    }
    catch(err) {
        console.log("Seccion no presente");
    }
    try {
        setTimeout(function sec_miseccion4(){
                        var mivar4 = document.getElementsByClassName("sec_miseccion4");
                        try {
                            mivar4[0].style.display = "block";
                        } catch (e) {
                            console.log("Seccion no presente");
                        }

                   },20);
    }
    catch(err) {
        console.log("Seccion no presente");
    }
    try {
        setTimeout(function sec_miseccion5(){
                        var mivar5 = document.getElementsByClassName("sec_miseccion5");
                        try {
                            mivar5[0].style.display = "block";
                        } catch (err) {
                            console.log("Seccion no presente");
                        }

                   },25);
    }
    catch(err) {
        console.log("Seccion no presente");
    }
    try {
        setTimeout(function sec_miseccion6(){
                        var mivar6 = document.getElementsByClassName("sec_miseccion6");
                        try {
                            mivar6[0].style.display = "block";
                        } catch (err) {
                            console.log("Seccion no presente");
                        }

                   },30);
    }
    catch(err) {
        console.log("Seccion no presente");
    }
    console.log("Secciones de la pagina activas!");
    return ;
}

function activarBuscadorGoogle () {
    var cx = '010659657807497246034:2sfwdj0wesi';
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);
    console.log("Google search activado!");
    return ;
}

function activarGoogleanalytics () {

    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;
        i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();
            a=s.createElement(o),  m=s.getElementsByTagName(o)[0];
            a.async=1;a.src=g;
            m.parentNode.insertBefore(a,m)
    })
    (window,document,'script','https://www.google-analytics.com/analytics.js','ga');
    ga('create', 'UA-106741690-1', 'auto');
    ga('send', 'pageview');
    console.log("Google analytics activado!");
    return ;
}

function activarCarruselDeImagenes () {
    try {
        var myIndex = 0;
        carousel();
        function carousel() {
            var i;
            var x = document.getElementsByClassName("mySlides");
            for (i = 0; i < x.length; i++) {
                x[i].style.display = "none";
            }
            myIndex++;
            if (myIndex > x.length) {myIndex = 1}
            x[myIndex-1].style.display = "block";
            setTimeout(carousel, 2000);
        }
        console.log("Carrusel de imagenes activado!");

    } catch (err) {
        console.log("Seccion no presente");
    }

    return ;
}

function activarRedessociales () {
    /* Facebook */
    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s);
        js.id = id;
        js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.10";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));

    /* Twitter */
    (document, 'script', '//platform.twitter.com/widgets.js');
    console.log("Redes sociales activasdas!");
    return ;
}

function funcionesVarias (evt) {
    /* Asign the color to the cell */
    $('.div_texto-largo').on('click', function() {

        micotiti = $(this).css('height');

        if (micotiti === "300px") {
            $(this).css('height', 'auto' );
        } else {
            $(this).css('height', '300px' );
        }

    });
}

function startProgram () {

    activarSecciones();
    activarBuscadorGoogle();
    activarGoogleanalytics();
    activarCarruselDeImagenes();
    activarRedessociales();
    funcionesVarias();

    console.log("Inicializacion de la pagina OK!");

    return;
}

$(startProgram);
