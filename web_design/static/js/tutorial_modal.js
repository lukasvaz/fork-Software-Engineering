$(document).ready(function() {
    $(".show-modal-tutorial").click(function() {
        const tutorialIntroHtmlContent = `
        <div id="container-modal-tutorial-icon">
            <p style="font-size: 18px">Hola bienvenido a Financhef, acá podrás encontrar ayuda para utilizar
            la aplicacion web número uno de Beauchef:</p>
            <a class="show-modal-tutorial-secondary" style="cursor: pointer; color: #b91a1d;font-size: 20px; font-weight: 700;">Enseñame!</a>
        </div>`;
    
        $("#tutorial-modal").html(tutorialIntroHtmlContent);
        $("#tutorial-modal").modal({
            fadeDuration: 200
        });


    });
});
