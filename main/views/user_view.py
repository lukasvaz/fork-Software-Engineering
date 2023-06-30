from django.http import  JsonResponse, HttpRequest
from django.shortcuts import render
from main.models import Incomes, Outcomes, AccountStatus
from django.db.models import F, Value, CharField
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from igs.forms import UpdateUserForm

def update_user(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, 'update_user.html', {'form': form})
        

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def change_data(request: HttpRequest):
    """Render the change user settings page template with the current configuration and ability to change them. Cache was disabled to ensure user's privacy 
    """
    ctx={}
    if request.user.is_authenticated:
        user_id = request.user.id
        try:
            account = AccountStatus.objects.filter(user__id=user_id)
            ctx = {"actual_balance": account.get().actual_balance,
                "name": request.user.first_name,}
                
        except ObjectDoesNotExist : #Account Status not associated
            ctx = {"name": request.user.first_name}
   
    return render(request,"settings.html",ctx)