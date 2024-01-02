import random
from typing import Any, Optional

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import AccountStatus
from main.factories import UserFactory, AccountStatusFactory, IncomesFactory, OutcomesFactory
from django.contrib.auth.models import User

NUM_USERS = 10
NUM_ACC_STATUSES = 10
NUM_IN_OUT = 10


class Command(BaseCommand):
    help = "Generate dummy data"

    @transaction.atomic
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Deleting old data...")
        models = [User, AccountStatus]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        users = []
        account_statuses = []

        for _ in range(NUM_USERS):
            user = UserFactory()
            users.append(user)

        for _ in range(NUM_ACC_STATUSES):
            user = random.choice(users)
            account_status = AccountStatusFactory(user=user)
            users.remove(user)
            account_statuses.append(account_status)

        for _ in range(NUM_IN_OUT):
            account_status = random.choice(account_statuses)
            income = IncomesFactory(account_status=account_status)
            outcome = OutcomesFactory(account_status=account_status)
            account_status.actual_balance = income.income - outcome.outcome
            account_status.save()
            account_statuses.remove(account_status)
