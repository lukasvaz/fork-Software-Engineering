from django.http import  HttpResponse
from django.template import Template,Context,loader


def directions(request):
    html = """<h3>Urls</h3>

            <p><b>Provisionalmente</b>, cada template ubicado 
            en web_design/templates, se pude visualizar agregando "show" a url: </p>
              <p>Por ejemplo:<br>
              http://127.0.0.1:8000/show/base.html
              </p>

              """
    
    return HttpResponse(html)


def show(request,template):    
    template=loader.get_template(template)
    ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)

