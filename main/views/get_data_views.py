from django.http import  JsonResponse, HttpRequest
from main.models import Incomes, Outcomes
from django.db.models import F, Value, CharField
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.shortcuts import render
from django.core.serializers import serialize
from django.db.models import Sum

def get_raw_transactions(request: HttpRequest):
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
    
def get_filter_sum(request: HttpRequest,type:str,groupby:str):
    """Retrieves the sum of  transactions asociated to an user filtering by type (Incomes Outcomes) and grouping by "groupby"  in json format."""
    if request.user.is_authenticated and request.method == 'GET':
        user_id = request.user.id
        if type=='outcomes':
            data = Outcomes.objects.filter(account_status__user=user_id).values(groupby).annotate(total=Sum("outcome"))

        elif type=='incomes':
            data = Incomes.objects.filter(account_status__user=user_id).values(groupby).annotate(total=Sum("income"))
        else:
            return JsonResponse({})
        
        serialized_data = list( data)
        return JsonResponse(serialized_data, safe=False)
    else:
        return JsonResponse({})
    
