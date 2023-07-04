
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

/**
 * Aplica el caracter '.' a un string compuesto de numeros para convertirlo a un valor leible
 * por humanos.
 */
function addDots(nStr) {
    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + '.' + '$2');
    }
    return x1 + x2;
}