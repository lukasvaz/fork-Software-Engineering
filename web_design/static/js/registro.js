// Aquí va el código JavaScript para validar el formulario
const form = document.querySelector('#registration-form');
form.addEventListener('submit', (event) => {
    const username = form.elements['username'].value;
    const password = form.elements['password'].value;
    const confirm_password = form.elements['confirm-password'].value;
    const passwordRegex = /^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z0-9]{8,}$/;
    let errores = [];

    if (username.length < 5) {
        // aca se podria agregar que valide que no exista el username
        errores.push('-El nombre de usuario debe tener al menos 5 caracteres');
    } 

    if (password !== confirm_password) {
        errores.push('-Las contraseñas no coinciden.');
    }

    if (!passwordRegex.test(password)) {
        errores.push('-La contraseña debe tener al menos 8 caracteres y contener letras y números.');
    }

    if (errores.length > 0) {
        event.preventDefault();
        alert('Por favor, corrija los siguientes errores:\n\n' + errores.join('\n'))
    }
});