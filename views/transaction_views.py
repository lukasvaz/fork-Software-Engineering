from django.http import  HttpResponse
from django.template import Template,Context,loader
from django.shortcuts import render
from igs.forms import TransactionForm


# views transacciones
def transaction(request):
    if request.method == 'POST':
        #si post funciona debería imprimir en la terminal
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
    return render(request, 'transaccion.html', {'formulario': form})

