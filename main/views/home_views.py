from django.http import  HttpResponse , JsonResponse,HttpRequest
from django.template import Template,Context,loader
from django.shortcuts import render
from main.models import Incomes,Outcomes,AccountStatus
from django.contrib.auth.models import User
from django.db.models import F
## views home 

def get_transactions(request,type):
    #user_id=request.user.id
    user_id=4
    dict_data={}
    print(type)
    if(type=="Ingreso"):
        incomes=Incomes.objects.filter(account_status__user=user_id)[:10]
        dict_data=list(incomes.values())
        for values in dict_data:
            values["monto"]=values.pop("income")
            values["tipo"]="Ingreso"


        return JsonResponse(dict_data,safe=False)
        
    if(type=="Egreso"):
        outcomes=Outcomes.objects.filter(account_status__user=user_id)[:10]
        dict_data=list(outcomes.values())
        for values in dict_data:
            values["monto"]=values.pop("outcome")
            values["tipo"]="Egreso"

        return JsonResponse(dict_data,safe=False)

    return JsonResponse(dict_data)
    

def home(request):
    template=loader.get_template("home.html")
    #user_id=request.user.id
    user_id=4
    #outcomes=Outcomes.objects.filter(account_status__user=user_id)
    incomes=Incomes.objects.filter(account_status__user=user_id).order_by(F("set_at").desc())[:20]
    #union=outcomes.union(incomes).order_by(F("set_at").desc())[:20]

    #data=get_transactions(HttpRequest,"Ingreso")
    
    # Test
    #transactions=union
    
    ctx={"transactions":incomes}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)





