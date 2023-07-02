function activarModoOscuro() {
    var body = document.body;
    body.classList.toggle("modo-oscuro");
  
    // Almacenar la preferencia del modo oscuro en el almacenamiento local
    var modoOscuroActivado = body.classList.contains("modo-oscuro");
    localStorage.setItem("modoOscuro", modoOscuroActivado);
  }
  
  // Función para aplicar el modo oscuro cuando se carga la página
  function aplicarModoOscuro() {
    var modoOscuroActivado = localStorage.getItem("modoOscuro");
    var body = document.body;
  
    // Verificar si el modo oscuro está activado en el almacenamiento local
    if (modoOscuroActivado === "true") {
      body.classList.add("modo-oscuro");
    } else {
      body.classList.remove("modo-oscuro");
    }
  }
  
  // Ejecutar la función al cargar la página
  window.addEventListener("DOMContentLoaded", aplicarModoOscuro);