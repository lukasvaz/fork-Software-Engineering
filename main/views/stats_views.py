from django.http import   HttpRequest
from django.shortcuts import render
from main.models import  Incomes,Outcomes,AccountStatus
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.shortcuts import render
from django.db.models import Sum,Max



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def stats(request: HttpRequest):
    """Render the statistics page template with the associated info from user.Cache was disabled to ensure user's privacy 
    """
    ctx={}
    if request.user.is_authenticated:
        user_id = request.user.id
        account = AccountStatus.objects.filter(user__id=user_id)
        max_outcomes_data = Outcomes.objects.filter(account_status__user=user_id).values('category').annotate(total=Sum("outcome")).order_by('-total').first()
        max_incomes_data = Incomes.objects.filter(account_status__user=user_id).values('category').annotate(total=Sum("income")).order_by('-total').first()
        ctx={'name':request.user.first_name,
             'max_cat_income':max_incomes_data['category'],
             "actual_balance": account.get().actual_balance,
             'max_cat_outcome':max_outcomes_data['category']}
    
    return render(request,"stats/stats.html",ctx)


