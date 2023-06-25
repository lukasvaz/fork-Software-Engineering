const form = document.getElementById("modify-form");
const amount = document.getElementById("id_monto");

form.addEventListener("submit", (e) => {
    checksInputs(e);
});

function checksInputs(event) {
    const amountValue = amount.value.trim();

    if (amountValue === "") {
        setErrorFor(amount, "El monto no puede estar en blanco.", event);
    } else if (isNaN(Number(amountValue))){
        setErrorFor(amount, "Ingrese un monto valido.", event);
    } else {
        setSuccessFor(amount);
    }
};

function setErrorFor(input, message, event) {
    event.preventDefault();
    const formControl = input.parentElement;
    const small = formControl.querySelector("small");

    small.innerText = message;
    formControl.className = "form-control error";
};

function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = "form-control success";
};