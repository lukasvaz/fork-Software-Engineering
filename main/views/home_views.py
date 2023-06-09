from django.http import HttpResponse, JsonResponse, HttpRequest
from django.template import loader
from django.shortcuts import render
from main.models import Incomes, Outcomes, AccountStatus
from django.db.models import F, Value, CharField



def get_transactions(request: HttpRequest):
    """Retrieves all transactions data asociated to the user in json format.
    """

    user_id = request.user.id
    if request.user.is_authenticated and request.method == 'GET':
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


def home(request: HttpRequest):
    """Render the home page template with the current budget and username as context parameters.
    """

    template = loader.get_template("home/table.html")
    try:
        user_id = request.user.id
        account = AccountStatus.objects.filter(user__id=user_id)
        print(account.get().actual_balance)
        print(user_id)

        ctx = {"actual_balance": account.get().actual_balance,
               "name": request.user.firstname}
    except :
        user_id = request.user.id
        account = AccountStatus.objects.filter(user__id=user_id)
        print(account.get().actual_balance)

        print("except")
        
        ctx = {}
    rendered_template = template.render(ctx)
    return HttpResponse(rendered_template)
