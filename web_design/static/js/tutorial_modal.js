$(".show-modal-tutorial").click(function() {
    const tutorialIntroHtmlContent = `<p>pene</p>`;

    $("#tutorial-modal").html(tutorialIntroHtmlContent);
    $("#tutorial-modal").modal({
        fadeDuration: 200
    });
});