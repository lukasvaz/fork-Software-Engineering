from django.http import  JsonResponse, HttpRequest
from django.shortcuts import render
from main.models import Incomes, Outcomes, AccountStatus
from django.db.models import F, Value, CharField
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.shortcuts import render


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