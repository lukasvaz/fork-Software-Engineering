const formulario = document.querySelector('form');
const tipo = document.getElementById('tipo');
const monto = document.getElementById('monto');
const moneda = document.getElementById('moneda');
const fecha = document.getElementById('fecha');
const categoria = document.getElementById('categoria');

formulario.addEventListener('submit', function(event) {
  event.preventDefault(); // Evita que se envíe el formulario sin ser validado

  // Validación del campo "Tipo"
  if (tipo.value === '') {
    alert('Debe seleccionar un tipo de ingreso o gasto');
    return;
  }

  // Validación del campo "Monto"
  if (monto.value === '' || isNaN(monto.value)) {
    alert('Debe ingresar un monto válido');
    return;
  }

  // Validación del campo "Moneda"
  if (moneda.value === '') {
    alert('Debe seleccionar una moneda');
    return;
  }

  // Validación del campo "Fecha"
  if (fecha.value === '') {
    alert('Debe ingresar una fecha');
    return;
  }

  // Validación del campo "Categoría"
  if (categoria.value === '') {
    alert('Debe seleccionar una categoría');
    return;
  }

  // Si todos los campos están completos, se envía el formulario
  formulario.submit();
});

// agregar puntos al monto:

// Obtenemos el campo de entrada utilizando su ID
const montoInput = document.getElementById('monto');

// Agregamos un evento al campo de entrada que se activará mientras el usuario escribe
montoInput.addEventListener('input', function() {
  // Obtenemos el valor actual del campo de entrada
  let valor = montoInput.value.replace(/\./g, '');
  // Removemos cualquier punto que ya haya sido agregado previamente
  montoInput.value = valor.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".");
});