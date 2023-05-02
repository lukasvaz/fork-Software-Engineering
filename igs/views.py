from django.http import  HttpResponse
from django.template import Template,Context,loader


def directions(request):
    html = """/admin/: admin site <br>
              /home/: home site  <br>
              /base/: show base snipet  <br>
              /egreso/:show egreso code snippet <br>
              /ingreso/: show ingreso code snippet  <br>
              /fecha/: show fecha code snippet  <br>
              """
    
    return HttpResponse(html)

def base(request):    
    template=loader.get_template("base.html")
    ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)



def home(request):    
    template=loader.get_template("home.html")
    ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)


def ingreso(request):    
    template=loader.get_template("ingreso.html")
    ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)


def egreso(request):    
    template=loader.get_template("egreso.html")
    ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)



def fecha(request):    
    template=loader.get_template("fecha.html")
    ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)
