from django.shortcuts import render, redirect
from django.http import HttpRequest
from main.models import Incomes, Outcomes
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required


@cache_control(private=True,no_cache=True, must_revalidate=True, no_store=True)
@login_required()
def modify_income(request: HttpRequest, id):
    """(`POST`) Modify the Income's fields by the new parameters given in the request form, uses the `id`
    parameter passed in the url to get the specific income, redirects to the homepage. (`GET`) Render the form template to modify
    the income entry.
    """

    if request.method == 'GET':
        return render(request, "modify_entry.html")

    elif request.method == 'POST':
        income_entry = Incomes.objects.get(pk=id)
        account_status = income_entry.account_status
        new_income = int(request.POST['monto'])

        # Update actual balance in AccountStatus
        account_status.actual_balance -= income_entry.income
        account_status.actual_balance += new_income
        account_status.save()

        income_entry.income = new_income
        income_entry.category = request.POST['categoria']
        income_entry.set_at = request.POST['fecha']
        income_entry.description = request.POST['descripcion']

        income_entry.save()

        return redirect("/home/")


@cache_control(private=True,no_cache=True, must_revalidate=True, no_store=True)
@login_required()
def modify_outcome(request: HttpRequest, id):
    """(`POST`) Modify the Outcome's fields by the new parameters given in the request form, uses
    the `id` parameter passed by the url to get the specific outcome, redirects to the homepage. (`GET`) Render the form template to modify
    the outcome entry.
    """

    if request.method == 'GET':
        return render(request, "modify_entry.html")

    elif request.method == 'POST':
        outcome_entry = Outcomes.objects.get(pk=id)
        account_status = outcome_entry.account_status
        new_outcome = int(request.POST['monto'])

        # Update actual balance in AccountStatus
        account_status.actual_balance += outcome_entry.outcome
        account_status.actual_balance -= new_outcome
        account_status.save()

        outcome_entry.outcome = new_outcome
        outcome_entry.category = request.POST['categoria']
        outcome_entry.set_at = request.POST['fecha']
        outcome_entry.description = request.POST['descripcion']

        outcome_entry.save()

        return redirect("/home")
