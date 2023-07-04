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
    "Venta de chocolates, rosas y peluches aumentan un 1000% gracias a las lluvias.",
    "BREAKING NEWS: Se viene fiesta masiva el jueves 6 de julio",
    "Se inaugura un nuevo laboratorio de inteligencia artificial en la facultad de Ingeniería de la FCFM.",
    "Estudiantes de Ingeniería en Computación ganan competencia de programación a nivel nacional.",
    "Crean una nueva cátedra de criptografía avanzada en el Departamento de Ciencias de la Computación.",
    "Aumenta la demanda de pasantías en empresas de tecnología para estudiantes de ingeniería en computación.",
    "Estudiantes del DCC desarrollan una aplicación móvil para facilitar el proceso de matrícula.",
    "Se implementa un nuevo programa de mentoría entre estudiantes de ingeniería en computación de primer y último año.",
    "Investigadores del DCC obtienen fondos para desarrollar un proyecto de realidad virtual aplicada a la educación.",
    "Se abre una convocatoria para la creación de un centro de emprendimiento tecnológico en la facultad de Ingeniería.",
    "Estudiantes del DCC participan en una competencia de programación competitiva y obtienen el primer lugar.",
    "Conferencia sobre inteligencia artificial y aprendizaje automático se lleva a cabo en la FCFM, con destacados ponentes internacionales."
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