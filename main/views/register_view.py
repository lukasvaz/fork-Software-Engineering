from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.models import AccountStatus

##view for the register form , if request is GET method render the template  
#if is POST save user in database
def register_user(request):
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