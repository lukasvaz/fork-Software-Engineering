const form = document.getElementById("register-form");
const username = document.getElementById("username");
const firstName = document.getElementById("first_name");
const lastName = document.getElementById("last_name");
const email = document.getElementById("email");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmpassword");

form.addEventListener("submit", (e) => {
    checksInputs(e);
});

function checksInputs(event) {
    const usernameValue = username.value;
    const nameValue = firstName.value;
    const lastNameValue = lastName.value;
    const emailValue = email.value;
    const passwordValue = password.value;
    const confirmPasswordValue = confirmPassword.value;
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    if (usernameValue === "") {
        setErrorFor(username, "Ingrese nombre de usuario.", event);
    } else if (usernameValue.length < 5) {
        setErrorFor(username, "El nombre de usuario debe tener al menos 5 caracteres.", event);
    }
    else {
        setSuccessFor(username);
    }

    if (nameValue === "") {
        setErrorFor(firstName, "Ingrese un nombre.", event);
    } else {
        setSuccessFor(firstName);
    }

    if (lastNameValue ==="") {
        setErrorFor(lastName, "Ingrese un apellido.", event);
    } else {
        setSuccessFor(lastName);
    }

    if (emailValue === "") {
        setErrorFor(email, "Ingrese un mail.", event)
    } else if (!emailRegex.test(emailValue)) {
        setErrorFor(email, "Ingrese un mail valido.", event);
    } else {
        setSuccessFor(email);
    }

    if (passwordValue != confirmPasswordValue) {
        setErrorFor(password, "Las contraseñas no coinciden.", event);
        setErrorFor(confirmPassword, "Las contraseñas no coinciden.", event);
    } else {
        setSuccessFor(password);
        setSuccessFor(confirmPassword);
    }

    if (!passwordRegex.test(passwordValue)) {
        setErrorFor(password, "La contraseña debe tener al menos 8 caracteres y contener letras y números.", event)
    } else {
        setSuccessFor(password);
    }

};