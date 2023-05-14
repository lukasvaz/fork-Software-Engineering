from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'GET':
        return render(request, "registro.html")
    
    elif request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password).save()
        
        return redirect("/")