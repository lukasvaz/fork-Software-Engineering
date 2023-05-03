from django.http import  HttpResponse
from django.template import Template,Context,loader
from django.shortcuts import render
from .forms import TransactionForm

def directions(request):
    html = """<h3>Urls</h3>

            <p><b>Provisionalmente</b>, cada template ubicado 
            en web_design/templates, se pude visualizar agregando "show" a url: </p>
              <p>Por ejemplo:<br>
              http://127.0.0.1:8000/show/base.html
              </p>

              """
    
    return HttpResponse(html)


def transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Procesar el formulario aquí
            tipo = form.cleaned_data['tipo']
            monto = form.cleaned_data['monto']
            moneda = form.cleaned_data['moneda']
            fecha = form.cleaned_data['fecha']
            categoria = form.cleaned_data['categoria']
            # hacer algo con los datos (almacenar en base de datos)
            # aca se puede renderizar un html que te diga que se envio bien el formulario
            #return render(request, 'success.html')
    else:
        form = TransactionForm()
    return render(request, 'transaccion.html', {'form': form})

def show(request,template):    
    template=loader.get_template(template)
    ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)

def vista_form(request):
    form = TransactionForm()
    return render(request, 'transaccion.html', {'formulario': form})
