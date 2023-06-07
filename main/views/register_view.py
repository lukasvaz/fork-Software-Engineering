from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.models import AccountStatus
from django.http import HttpRequest


def register_user(request: HttpRequest):
    """"(`POST`) Save the registration user information in the database and redirects to the login page.
    (`GET`) Render the registration form template.
    """

    if request.method == 'GET':
        return render(request, "register.html")

    elif request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username,
                                        first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        password=password)

        user_account_status = AccountStatus(user=user)
        user_account_status.save()

        return redirect("/accounts/login/")
