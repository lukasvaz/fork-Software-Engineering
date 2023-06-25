from django.http import   HttpRequest
from django.shortcuts import render
from main.models import  Incomes,Outcomes
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.shortcuts import render
from django.db.models import Sum



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def stats(request: HttpRequest):
    """Render the statistics page template with the associated info from user.Cache was disabled to ensure user's privacy 
    """
    ctx={}
    if request.user.is_authenticated:
        user_id = request.user.id
        incomes_data = Outcomes.objects.filter(account_status__user=user_id).values('category').annotate(total=Sum("outcome"))
        outcomes_data = Incomes.objects.filter(account_status__user=user_id).values('category').annotate(total=Sum("income"))
        ctx={'name':request.user.first_name}
    
    return render(request,"stats/stats.html",ctx)


