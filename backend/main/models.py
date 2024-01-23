from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
# We are using the default class User, fits good with our model,
# we only need the common fields: username, first_name, last_name, email and password


class AccountStatus(models.Model):
    user = models.OneToOneField(
        User, related_name='account_status', on_delete=models.CASCADE, unique=True, null=True)
    actual_balance = models.BigIntegerField(default=0)


    def __str__(self):
        return f"Estado de cuenta asociado a usuario: {self.user.username}"


class Outcomes(models.Model):
    account_status = models.ForeignKey(
        AccountStatus, related_name="outcomes", on_delete=models.CASCADE, blank=True)
    amount = models.PositiveBigIntegerField()
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    set_at = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True)

    def update_account(self, old_instance, new_instance):
        """Method  used  whenever an  income  is  deleted  from  the  database"""
        new_instance.account_status.actual_balance += old_instance.amount
        new_instance.account_status.actual_balance -= new_instance.amount
        self.account_status.save()

    def add_to_account(self, instance):
        """Method  used  whenever an  income  is  added  from  the  database"""
        instance.account_status.actual_balance -= instance.amount
        self.account_status.save()

    def __str__(self):
        return f"Egreso asociado a usuario: {self.account_status.user.username}"


class Incomes(models.Model):
    account_status = models.ForeignKey(
        AccountStatus, related_name="incomes", on_delete=models.CASCADE, blank=True)
    amount = models.PositiveBigIntegerField()
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    set_at = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True)

    def update_account(self, old_instance, new_instance):
        """Method  used  whenever an  income  is  deleted  from  the  database"""
        if old_instance.amount != new_instance.amount:
            new_instance.account_status.actual_balance -= old_instance.amount
            new_instance.account_status.actual_balance += new_instance.amount
            self.account_status.save()

    def add_to_account(self, instance):
        """Method  used  whenever an  income  is  added  from  the  database"""
        instance.account_status.actual_balance += instance.amount
        self.account_status.save()

    def __str__(self):
        return f"Ingrso asociado a usuario: {self.account_status.user.username}"
