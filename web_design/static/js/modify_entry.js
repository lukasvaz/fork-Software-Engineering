const form = document.querySelector('form')
const amount = document.getElementById('id_monto')
const set_date = document.getElementById('id_fecha')
const category = document.getElementById('id_categoria')
const description = document.getElementById('id_descripcion')

form.addEventListener('submit', () => {
    if (set_date.value === '') {
        alert('Debe ingresar una fecha');
        return;
    }

    if (category.value === '') {
        alert('Debe seleccionar una categoria');
        return;
    }
});