from django.http import HttpResponse, JsonResponse, HttpRequest
from django.template import loader
from django.shortcuts import render, redirect
from main.models import Incomes, Outcomes, AccountStatus
from django.db.models import F, Value, CharField
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control


def get_transactions(request: HttpRequest):
    """Retrieves all transactions data asociated to the user in json format.
    """
    if request.user.is_authenticated and request.method == 'GET':
        user_id = request.user.id
        dict_data = {}
        outcomes = Outcomes.objects.filter(account_status__user=user_id).annotate(
            type=Value('Egreso', output_field=CharField())).annotate(amount=F('outcome'))
        outcomes = outcomes.values(
            "id", "amount", "category",  "set_at", "type", "description")
        incomes = Incomes.objects.filter(account_status__user=user_id).annotate(
            type=Value('Ingreso', output_field=CharField())).annotate(amount=F('income'))
        incomes = incomes.values(
            "id", "amount", "category", "set_at", "type", "description")
        union_table = outcomes.union(incomes).order_by(F("set_at").desc())
        dict_data = list(union_table)
        return JsonResponse(dict_data, safe=False)
    else:
        return JsonResponse({})
         
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request: HttpRequest):
    """Render the home page template with the current budget and username as context parameters.Cache was disabled to ensure user's privacy 
    """
    template = loader.get_template("home/home.html")
    ctx={}
    if request.user.is_authenticated:
        user_id = request.user.id
        try:
            account = AccountStatus.objects.filter(user__id=user_id)
            ctx = {"actual_balance": account.get().actual_balance,
                "name": request.user.first_name,
                "log":"Log out"}
                
        except ObjectDoesNotExist : #Account Status not associated
            ctx = {"name": request.user.first_name}
    else:
        ctx={"log":"Log-in"}
    rendered_template = template.render(ctx)
    return HttpResponse(rendered_template)


def logout_view(request):
        logout(request)
        return redirect("home")