from django.http import  HttpResponse
from django.template import Template,Context,loader
from django.shortcuts import render




## views home 

def home(request):

    template=loader.get_template("home.html")
    # obtener desde  base de datos
    #importar modelo-> from models.py import Ingresos Egresos Estado_Cuenta
    
    #obtener_saldo actual
    #    user_id=request.user.id
    #    Estados_cuenta_usuario= Estado_cuenta.objects.filter(user_id=user_id)
    #   saldo_actual=   
    #    Ingresos_sesion=Ingresos.objects.filter()
    #    Egresos_sesion=Egresos.objects.filter()
   
    # Test
    transactions=[]
    # transaction1={"date":"15/09/2023","name":"compra semanal","value":13000,"category":"Compra","type":"Egreso"}
    # transaction2={"date":"12/10/2023","name":"compra regalo","value":25000,"category":"Otros","type":"Egreso"}
    # transaction3={"date":"5/12/2023","name":"cena familiar","value":43000,"category":"Cena","type":"Egreso"}
    # transactions.append(transaction1)
    # transactions.append(transaction2)
    # transactions.append(transaction3)
    
    
    ctx={"transactions":transactions}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)





