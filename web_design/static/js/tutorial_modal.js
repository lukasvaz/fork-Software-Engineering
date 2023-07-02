$(document).ready(function() {
    $(".show-modal-tutorial").click(function() {
        $("#tutorial-modal").modal({
            fadeDuration: 200
        });
    });

    $(".show-modal-tutorial-secondary").click(function() {
        $("#firts-tutorial-modal").modal({
            fadeDuration: 200
        })
    })

    $(".show-modal-tutorial-third").click(function() {
        $("#second-tutorial-modal").modal({
            fadeDuration: 200
        })
    })

    $(".show-modal-tutorial-fourth").click(function() {
        $("#third-tutorial-modal").modal({
            fadeDuration: 200
        })
    })
});
