from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
