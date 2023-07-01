from django.http import  JsonResponse, HttpRequest
from django.shortcuts import render
from main.models import Incomes, Outcomes, AccountStatus
from django.db.models import F, Value, CharField
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from igs.forms import UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


@cache_control(private=True,no_cache=True, must_revalidate=True, no_store=True)
@login_required()
def update_user(request: HttpRequest):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        print(password_form.errors)
        if form.is_valid() and password_form.is_valid():
            print('test')
            form.save()
            password_form.save()
            return redirect('home')  # Redirect to the user's profile page
    else:
        form = UpdateUserForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'settings.html', {'form': form, 'password_form' : password_form})