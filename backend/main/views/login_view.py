from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirige a la página de inicio si el inicio de sesión es exitoso
        else:
            error = True  # Marca que ha ocurrido un error de inicio de sesión
            return render(request, 'registration/login.html', {'error': error})
    else:
        error = False  # Inicializa la variable de error como Falso
        return render(request, 'registration/login.html', {'error': error})

