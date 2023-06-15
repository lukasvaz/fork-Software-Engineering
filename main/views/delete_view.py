from django.shortcuts import render, redirect
from django.http import HttpRequest
from main.models import Incomes, Outcomes


def delete_income(request: HttpRequest, id):
    """(`POST`) Modify the Income's fields by the new parameters given in the request form, uses the `id`
    parameter passed in the url to get the specific income, redirects to the homepage. (`GET`) Render the form template to modify
    the income entry.
    """
    print("prueba")
    return redirect("/home/")


def delete_outcome(request: HttpRequest, id):
    """(`POST`) Modify the Outcome's fields by the new parameters given in the request form, uses
    the `id` parameter passed by the url to get the specific outcome, redirects to the homepage. (`GET`) Render the form template to modify
    the outcome entry.
    """
    print("prueba")
    return redirect("/home")
