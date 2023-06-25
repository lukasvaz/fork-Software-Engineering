const form = document.getElementById("modify-form");
const amount = document.getElementById("id_monto");

form.addEventListener("submit", (e) => {
    checksInputs(e);
});

function checksInputs(event) {
    const amountValue = amount.value.trim();

    if (amountValue === "") {
        setErrorFor(amount, "Ingrese un monto.", event);
    } else if (isNaN(Number(amountValue))){
        setErrorFor(amount, "Ingrese un monto válido.", event);
    } else {
        setSuccessFor(amount);
    }
};