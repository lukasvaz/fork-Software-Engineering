from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)

    def __str__(self):
        return self.username

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