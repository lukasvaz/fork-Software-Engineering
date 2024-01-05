from django.shortcuts import render, redirect
from django.http import HttpRequest
from main.models import Incomes, Outcomes

def delete_income(request: HttpRequest, id):
    """(`POST`) Modify the Income's fields by the new parameters given in the request form, uses the `id`
    parameter passed in the url to get the specific income, redirects to the homepage. (`GET`) Render the form template to modify
    the income entry.
    """
    if request.method == 'GET':
        return render(request, "delete_transaction.html")

    elif request.method == 'POST':
        income_entry = Incomes.objects.get(pk=id)
        account_status = income_entry.account_status

        # Update actual balance in AccountStatus
        account_status.actual_balance -= income_entry.incomeen  en  
        account_status.save()

        # Delete the income entry
        income_entry.delete()

        return redirect("/home/")

def delete_outcome(request: HttpRequest, id):
    """(`POST`) Modify the Outcome's fields by the new parameters given in the request form, uses
    the `id` parameter passed by the url to get the specific outcome, redirects to the homepage. (`GET`) Render the form template to modify
    the outcome entry.
    """
    if request.method == 'GET':
        return render(request, "delete_transaction.html")

    elif request.method == 'POST':
        outcome_entry = Outcomes.objects.get(pk=id)
        account_status = outcome_entry.account_status

        # Update actual balance in AccountStatus
        account_status.actual_balance += outcome_entry.outcome
        account_status.save()

        # Delete the outcome entry
        outcome_entry.delete()
        
        return redirect("/home/")
