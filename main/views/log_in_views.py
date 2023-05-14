from django.http import  HttpResponse, Http404
from django.template import Template,Context,loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# el comportamiento actual es :iniciar sesion -> home
# 
# falta especificar distintos comportamientos (Aux de forms):
# get ->renderizar template 
# post-> validar usuario si no  ofrecer opcion de registrarse

# ***********************************************************

# AHORA MISMO ESTO NO ES NECESERIO OCUPARLO PQ SE ESTAN OCUPANDO LAS
# VIEWS POR DEFAULT DE DJANGO

# ***********************************************************

def log_in(request):
    if request.method == "GET":
        template=loader.get_template("registration/login.html")
        ctx={}
        rendered_template=template.render(ctx)
        return HttpResponse(rendered_template)
    
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            if user is not None:
                login(request, user)
                return redirect("/home")
            # else:
            #     # Must display an error to the user (TODO: Handle the error)
            #     return redirect("home")
        except:
            raise Http404("Credenciales Invalidas")