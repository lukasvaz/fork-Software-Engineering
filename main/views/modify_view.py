from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from main.models import AccountStatus

def modify_entry(request: HttpRequest):
    """Modify the Income/Outcome entry by the new parameters given in the request.
    """

    if request.method == 'GET':
        return render(request, "modify_entry.html")
    
    elif request.method == 'POST':
        # account_status = sacar por id
        user_id = request.user.id
        amount = request.POST['monto']
        category = request.POST['categoria']
        set_at = request.POST['fecha']
        description = request.POST['description']

        return redirect()