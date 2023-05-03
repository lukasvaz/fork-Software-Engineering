from django import forms

class TransactionForm(forms.Form):
    TIPO_CHOICES = [('ingreso', 'Ingreso'), ('gasto', 'Gasto')]
    MONEDA_CHOICES = [('CLP', 'CLP'), ('USD', 'USD'), ('EUR', 'EUR')]
    CATEGORIA_CHOICES = [('comida', 'Comida'), ('transporte', 'Transporte'),
                         ('entretenimiento', 'Entretenimiento'), ('hogar', 'Hogar'),
                         ('salud', 'Salud'), ('ropa', 'Ropa'), ('otros', 'Otros')]
    tipo = forms.ChoiceField(choices=TIPO_CHOICES)
    monto = forms.IntegerField()
    moneda = forms.ChoiceField(choices=MONEDA_CHOICES)
    fecha = forms.DateField()
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES)
    widgets = {'fecha': forms.DateInput(attrs={'type': 'date'})}