from django.db import models
from django.contrib.auth.models import User

# We are using the default class User, fits good with our model,
# we only need the common fields: username, first_name, last_name, email and password

class AccountStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.PositiveBigIntegerField()
    outcome = models.PositiveBigIntegerField()
    actual_balance = models.BigIntegerField()

    def __str__(self):
        return self.actual_balance
    
class Outcomes(models.Model):
    account_status = models.ForeignKey(AccountStatus, on_delete=models.CASCADE)
    outcome = models.PositiveBigIntegerField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    set_at = models.DateTimeField()

    def __str__(self):
        return self.outcome

class Incomes(models.Model):
    account_status = models.ForeignKey(AccountStatus, on_delete=models.CASCADE)
    income = models.PositiveBigIntegerField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    set_at = models.DateTimeField()

    def __str__(self):
        return self.income