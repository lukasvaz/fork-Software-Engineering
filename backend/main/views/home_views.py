from django.http import  JsonResponse, HttpRequest
from django.shortcuts import render
from main.models import Incomes, Outcomes, AccountStatus
from django.db.models import F, Value, CharField
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.shortcuts import render

         
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request: HttpRequest):
    """Render the home page template with the current budget and username as context parameters.Cache was disabled to ensure user's privacy 
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
   
    return render(request,"home/home.html",ctx)


