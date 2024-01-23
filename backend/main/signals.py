from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from main.models import Incomes, Outcomes


def update_balance(instance, model):
    """Method  used  whenever an  income  is  deleted  from  the  database"""
    # updating an  instance
    if instance.pk:
        old_instance = model.objects.get(pk=instance.pk)
        instance.update_account(old_instance, instance)
    # create
    else:
        instance.add_to_account(instance)


@receiver(pre_save, sender=Incomes)
def update_income_balance(sender, instance, **kwargs):
    update_balance(instance, Incomes)


@receiver(pre_save, sender=Outcomes)
def update_outcome_balance(sender, instance, **kwargs):
    update_balance(instance, Outcomes)
