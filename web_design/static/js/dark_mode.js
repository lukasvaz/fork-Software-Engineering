function activarModoOscuro() {
  var body = document.body;
  var btn = document.getElementById("modo-oscuro-btn");
  body.classList.toggle("modo-oscuro");

  if (body.classList.contains("modo-oscuro")) {
    btn.textContent = "Modo Claro";
  } else {
    btn.textContent = "Modo Oscuro";
  }
}