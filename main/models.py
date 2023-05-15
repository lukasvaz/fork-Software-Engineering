from django.db import models
from django.contrib.auth.models import User

# We are using the default class User, fits good with our model,
# we only need the common fields: username, first_name, last_name, email and password

class AccountStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    actual_balance = models.BigIntegerField(default=0)
    
    def __str__(self):
        return f"Estado de cuenta asociado a usuario: {self.user.username}"
    
class Outcomes(models.Model):
    account_status = models.ForeignKey(AccountStatus, on_delete=models.CASCADE)
    outcome = models.PositiveBigIntegerField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    set_at = models.DateField()
    description = models.CharField(max_length=100)

    def update_balance(self):
        """Update the balance from the User's Account Status,
        substracting the new outcome.
        """

        self.account_status.actual_balance -= self.outcome
        self.save()


    def __str__(self):
        return f"Egreso asociado a usuario: {self.account_status.user.username}"

class Incomes(models.Model):
    account_status = models.ForeignKey(AccountStatus, on_delete=models.CASCADE)
    income = models.PositiveBigIntegerField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    set_at = models.DateField()
    description = models.CharField(max_length=100)

    def update_balance(self):
        """Update the balance from the User's Account Status,
        adding the new income.
        """
        
        self.account_status.actual_balance += self.outcome
        self.save()

    def __str__(self):
        return f"Ingreso asociado a usuario: {self.account_status.user.username}"