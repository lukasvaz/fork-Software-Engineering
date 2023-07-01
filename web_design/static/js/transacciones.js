const form = document.getElementById("transaction-form");
const amount = document.getElementById("id_monto");
const date = document.getElementById("id_fecha");
const category = document.getElementById("id_categoria");

form.addEventListener('submit', function(event) {  
  checksInputs(event);
});

function checksInputs(event) {
    const amountValue = amount.value.trim();
    const dateValue = date.value;
    const categoryValue = category.value;

    if (amountValue === "") {
    setErrorFor(amount, "Ingrese un monto.", event);
    } else if (isNaN(Number(amountValue))) {
    setErrorFor(amount, "Ingrese un monto válido.", event);
    } else {
    setSuccessFor(amount);
    }

    if (dateValue === "") {
        setErrorFor(date, "Seleccione una fecha.", event);
    } else {
        setSuccessFor(date);
    }

    if (categoryValue === "") {
        setErrorFor(category, "Seleccione una categoría.", event);
    } else {
        setSuccessFor(category);
    }
};

// Obtenemos el campo de entrada utilizando su ID
// const montoInput = document.getElementById('monto');

// // Agregamos un evento al campo de entrada que se activará mientras el usuario escribe
// montoInput.addEventListener('input', function() {
//   // Obtenemos el valor actual del campo de entrada
//   let valor = montoInput.value.replace(/\./g, '');
//   // Removemos cualquier punto que ya haya sido agregado previamente
//   montoInput.value = valor.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".");
// });
