from django import forms

class TransactionForm(forms.Form):
    TIPO_CHOICES = [('ingreso', 'Ingreso'), ('gasto', 'Gasto')]
    CATEGORIA_CHOICES = [('comida', 'Comida'), ('transporte', 'Transporte'),
                         ('entretenimiento', 'Entretenimiento'), ('hogar', 'Hogar'),
                         ('salud', 'Salud'), ('ropa', 'Ropa'), ('otros', 'Otros')]
    tipo = forms.ChoiceField(choices=TIPO_CHOICES)
    monto = forms.IntegerField()
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES)
    custom_categoria = forms.CharField(required=False)
