from django.contrib import admin
from main.models import AccountStatus,Incomes,Outcomes
from django.contrib.auth.models import User


admin.site.register(AccountStatus)
admin.site.register(Incomes)
admin.site.register(Outcomes)