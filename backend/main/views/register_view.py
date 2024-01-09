from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.models import AccountStatus
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt 

# @csrf_exempt
def register_user(request: HttpRequest):
    """"(`POST`) Save the registration user's information in the database"""
    # if request.method == 'POST':

    #     username = request.POST['username']
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     email = request.POST['email']
    #     password = request.POST['password']

    #     user = User.objects.create_user(username=username,
    #                                     first_name=first_name,
    #                                     last_name=last_name,
    #                                     email=email,
    #                                     password=password)

    #     user_account_status = AccountStatus(user=user)
    #     user_account_status.save()

    return HttpResponse({"hola":"hola"})


def logout_user(request: HttpRequest):
    """Logs out  an user and redirect to home  page"""
    logout(request)
    # messages.success(request,("Debes iniciar sesión para ver tu contenido."))
    return redirect('login')
