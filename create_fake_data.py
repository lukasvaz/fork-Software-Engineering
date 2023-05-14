import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "igs.settings")

import django
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from faker import Faker
from model_bakery import recipe, baker

from main.models import AccountStatus, Incomes, Outcomes

from datetime import datetime
import random

income_categories = ["Pago", "Regalo", "Ahorro", "Beca"]
outcome_categories = ["Arriendo", "Comida", "Internet", "Diversion"]

# It's dummy data so there is no problem using the same password for
# all the fake users
PASSWORD = "abcde12345"

fake = Faker()

income_value = random.randint(1e5, 5e5)
outcome_value = random.randint(1e5, 5e5)

user = recipe.Recipe(User,
                username=fake.user_name(),
                password=make_password(PASSWORD))

account_status = recipe.Recipe(AccountStatus,
                        user=baker.make(user),
                        actual_balance=income_value-outcome_value)

income = recipe.Recipe(Incomes,
                account_status=baker.make(account_status),
                income=income_value,
                category=income_categories[random.randint(0, len(income_categories)-1)],
                created_at= datetime.today(),
                set_at=fake.date_between(start_date="-1y", end_date="today"),
                description="")

outcome = recipe.Recipe(Outcomes,
                    account_status=baker.make(account_status),
                    outcome=outcome_value,
                    category=outcome_categories[random.randint(0, len(outcome_categories)-1)],
                    created_at= datetime.today(),
                    set_at=fake.date_between(start_date="-1y", end_date="today"),
                    description="")

users = baker.make(user, _quantity=1)
account_statuses = baker.make(account_status, _quantity=5)
incomes = baker.make(income, _quantity=10)
outcomes = baker.make(outcome, _quantity=10)