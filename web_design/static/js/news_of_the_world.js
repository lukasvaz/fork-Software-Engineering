var mensajes = [
    "El 50% de los mechones reprobó intro al álgebra. Suben las papitas y el café.",
    "La Sonia anuncia aumento del 40% en dulces durante julio.",
    "Bajan los almuerzos veganos en la mayoría de puestos afuera de 850.",
    "Se reduce el arancel en $500.000.",
    "Gasto promedio en comida en el DCC baja en un 30%, mientras que el gasto en videojuegos sube un 200%",
    "Asaltantes de Micro 507: 'Exigimos bono por perdidas durante vacaciones de invierno.'",
    "La cafeta anuncia convenio con McDonald's.",
    "Licorerías cercanas a la facultad al borde la quiebra por falta de fiestas de los viernes.",
    "DCC regala computadores gamer a sus estudiantes gracias al trabajo del grupo 18 del ramo CC4401.",
    "Venta de chocolates, rosas y peluches aumentan un 1000% gracias a las lluvias."
];


function obtenerMensajeAleatorio() {
    var indice = Math.floor(Math.random() * mensajes.length);
    return mensajes[indice];
  }
  
  function mostrarMensajes() {
    var divMensajes = document.getElementById("random-messages");
    divMensajes.innerHTML = ""; 
  
    for (var i = 0; i < 3; i++) {
      var mensaje = obtenerMensajeAleatorio();
      var p = document.createElement("p");
      p.textContent = mensaje;
      divMensajes.appendChild(p);
    }
  }
  
  window.addEventListener("load", mostrarMensajes);