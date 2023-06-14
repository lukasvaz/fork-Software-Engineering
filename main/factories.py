import factory

from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from main.models import AccountStatus, Incomes, Outcomes

import random
import datetime

# This is dummy data so there is no problem to
# set the same password for all the dummy users
PASSWORD = "password123"
income_categories = ["Sueldo", "Cumpleanhos", "Ahorro", "Beca"]
outcome_categories = ["Arriendo", "Comida", "Internet", "Diversion"]


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = make_password(PASSWORD)


class AccountStatusFactory(DjangoModelFactory):
    class Meta:
        model = AccountStatus

    user = factory.SubFactory(UserFactory)
    actual_balance = factory.LazyAttribute(lambda x: random.randint(1e5, 5e5))


class IncomesFactory(DjangoModelFactory):
    class Meta:
        model = Incomes

    account_status = factory.SubFactory(AccountStatusFactory)
    income = factory.LazyAttribute(lambda x: random.randint(1e5, 5e5))
    category = factory.LazyAttribute(
        lambda x: random.choice(income_categories))
    created_at = factory.LazyAttribute(lambda x: datetime.datetime.now())
    set_at = factory.lazy_attribute(lambda x: datetime.date.today())
    description = ""


class OutcomesFactory(DjangoModelFactory):
    class Meta:
        model = Outcomes

    account_status = factory.SubFactory(AccountStatusFactory)
    outcome = factory.LazyAttribute(lambda x: random.randint(1e5, 5e5))
    category = factory.LazyAttribute(
        lambda x: random.choice(outcome_categories))
    created_at = factory.LazyAttribute(lambda x: datetime.datetime.now())
    set_at = factory.lazy_attribute(lambda x: datetime.date.today())
    description = ""
