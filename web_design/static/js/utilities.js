
/**
 * Setea el mensaje de error a mostrar si el elemento HTML no satisface
 * los requisitos de validacion desde el lado del cliente, se pasa el evento para llamar 
 * `preventDefault` y no realizar el envio del form.
 */
function setErrorFor(input, message, event) {
    event.preventDefault();
    const formControl = input.parentElement;
    const small = formControl.querySelector("small");

    small.innerText = message;
    formControl.className = "form-control error";
};

/**
 * Setea el elemento HTML como correcto luego de satisfacer los requisitos de validacion desde el lado
 * del cliente.
 */
function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = "form-control success";
};