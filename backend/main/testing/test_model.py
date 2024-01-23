import random
from django.contrib.auth.models import User
from django.test import TestCase
from main.models import Incomes, Outcomes, AccountStatus
from main.testing.test_api import APITestClass


class IncomesModelTest(APITestClass):
    def setUp(self):
        self.create_random_users()
        # create  random  incomes
        for user in User.objects.all():
            self.accountStatus = AccountStatus.objects.create(user=user)
            Incomes.objects.create(
                account_status=self.accountStatus,
                amount=random.randint(1, 10)*1000,
                description='test transaction',
                set_at='2021-10-10',
            )

    def test_add_income(self):
        user = User.objects.first()
        account_status = AccountStatus.objects.get(user=user)
        initial_balance = account_status.actual_balance
        income = Incomes.objects.create(
            account_status=AccountStatus.objects.get(user=user),
            amount=2000,
            description='test transaction',
            set_at='2021-10-10'
        )
        self.assertTrue(income in Incomes.objects.filter(
            account_status=AccountStatus.objects.get(user=user)))
        self.assertEqual(AccountStatus.objects.get(
            user=user).actual_balance, initial_balance+2000)

    def test_update_income(self):
        user = User.objects.first()
        initial_balance = AccountStatus.objects.get(user=user).actual_balance
        income = Incomes.objects.get(account_status__user=user)
        income.amount = income.amount+1000
        income.save()
        self.assertEqual(AccountStatus.objects.get(
            user=user).actual_balance, initial_balance+1000)


class OutcomesModelTest(APITestClass):
    def setUp(self):
        self.create_random_users()
        # create  random  outcomes
        for user in User.objects.all():
            self.accountStatus = AccountStatus.objects.create(user=user)
            Outcomes.objects.create(
                account_status=self.accountStatus,
                amount=random.randint(1, 10)*1000,
                description='test transaction',
                set_at='2021-10-10',
            )

    def test_add_outcome(self):
        user = User.objects.first()
        account_status = AccountStatus.objects.get(user=user)
        initial_balance = account_status.actual_balance
        outcome = Outcomes.objects.create(
            account_status=AccountStatus.objects.get(user=user),
            amount=2000,
            description='test transaction',
            set_at='2021-10-10'
        )
        self.assertTrue(outcome in Outcomes.objects.filter(
            account_status=AccountStatus.objects.get(user=user)))
        self.assertEqual(AccountStatus.objects.get(
            user=user).actual_balance, initial_balance-2000)

    def test_update_outcome(self):
        user = User.objects.first()
        initial_balance = AccountStatus.objects.get(user=user).actual_balance
        outcome = Outcomes.objects.get(account_status__user=user)
        outcome.amount = outcome.amount+1000
        outcome.save()
        self.assertEqual(AccountStatus.objects.get(
            user=user).actual_balance, initial_balance-1000)
