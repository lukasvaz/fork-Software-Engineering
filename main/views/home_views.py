from django.http import  HttpResponse , JsonResponse,HttpRequest
from django.template import Template,Context,loader
from django.shortcuts import render
from main.models import Incomes,Outcomes,AccountStatus
from django.contrib.auth.models import User
from django.db.models import F,Value,CharField


# retrieve transaction data  filtering by Income ,Outcome, All(incomes and outcomes)
# TODO: Implementing others filters and make it more extensible to other filters  
def get_transactions(request,type):
    #user_id=request.user.id
    user_id=4
    dict_data={}
    if(type=="Income"):
        incomes=Incomes.objects.filter(account_status__user=user_id).order_by(F("set_at").desc())
        incomes=incomes.annotate(type=Value('Ingreso', output_field=CharField())).annotate(amount=F('income'))[:10]        
        dict_data=list(incomes.values())

        return JsonResponse(dict_data,safe=False)
        
    if(type=="Outcome"):
        outcomes=Outcomes.objects.filter(account_status__user=user_id).order_by(F("set_at").desc())
        outcomes=outcomes.annotate(type=Value('Egreso', output_field=CharField())).annotate(amount=F('outcome'))[:10]        
        dict_data=list(outcomes.values())

        return JsonResponse(dict_data,safe=False)

    if(type=="All"):
        outcomes=Outcomes.objects.filter(account_status__user=user_id).annotate(type=Value('Egreso', output_field=CharField())).annotate(amount=F('outcome'))        
        outcomes=outcomes.values("id","amount", "category",  "set_at", "type" )        
        incomes=Incomes.objects.filter(account_status__user=user_id).annotate(type=Value('Ingreso', output_field=CharField())).annotate(amount=F('income'))        
        incomes=incomes.values("id","amount", "category", "set_at", "type" )       
        union_table=outcomes.union(incomes).order_by(F("set_at").desc())[:10]
        dict_data=list(union_table)
        return JsonResponse(dict_data,safe=False)

    return JsonResponse(dict_data)


## render the home template  passing  the current budget as context parameter and user  
def home(request):
    template=loader.get_template("home.html")
    try:
        #user_id=request.user.id
        user_id=4
        acount=AccountStatus.objects.filter(user__id=user_id)
        print(acount.get())
        ctx={"actual_balance":acount.get()}
    except:
        ctx={}
        rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)





