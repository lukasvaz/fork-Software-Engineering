from django.http import  HttpResponse , JsonResponse,HttpRequest
from django.template import Template,Context,loader
from django.shortcuts import render
from main.models import Incomes,Outcomes,AccountStatus
from django.contrib.auth.models import User
from django.db.models import F,Value,CharField


#retrieve transaction data  filtering by Income ,Outcome, All(incomes and outcomes)
#is it suposed to be called  by an ajax request  in home

# TODO: Implementing others filters and make it more extensible to other filters  

def get_transactions(request):
    user_id=request.user.id
    if request.user.is_authenticated and request.method=='GET':
        dict_data={}
        outcomes=Outcomes.objects.filter(account_status__user=user_id).annotate(type=Value('Egreso', output_field=CharField())).annotate(amount=F('outcome'))        
        outcomes=outcomes.values("id","amount", "category",  "set_at", "type" ,"description")        
        incomes=Incomes.objects.filter(account_status__user=user_id).annotate(type=Value('Ingreso', output_field=CharField())).annotate(amount=F('income'))        
        incomes=incomes.values("id","amount", "category", "set_at", "type" ,"description")       
        union_table=outcomes.union(incomes).order_by(F("set_at").desc())[:10]
        dict_data=list(union_table)
        return JsonResponse(dict_data,safe=False)



## render the home template  passing  the current budget and username as context parameter   
def home(request):
    template=loader.get_template("home.html")
    try:
        user_id=request.user.id
        acount=AccountStatus.objects.filter(user__id=user_id)
        print(acount.get().actual_balance)

        ctx={"actual_balance":acount.get().actual_balance,"name":request.user.username}
    except:
        ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)





