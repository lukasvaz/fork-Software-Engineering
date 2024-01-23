from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from main.models import AccountStatus, Incomes, Outcomes
import random


class APITestClass(TestCase):
    def create_random_users(self):
        """Create 5 users, 4 normal users and 1 superuser"""
        for i in range(1, 5):
            self.user = User.objects.create_user(
                username='testuser{}'.format(i), password='12345')

        self.superuser = User.objects.create_superuser(
            'admin', 'admin@test.com', 'admin')

    def create_random_transactions(self):
        """Create 3 transactions for each user"""
        for user in User.objects.all():
            self.accountStatus = AccountStatus.objects.create(user=user)
            for _ in range(2):
                Incomes.objects.create(
                    account_status=self.accountStatus,
                    amount=100,
                    description='test transaction',
                    set_at='2021-10-10',
                )
            for _ in  range(2):
                Outcomes.objects.create(
                    account_status=self.accountStatus,
                    amount=100,
                    description='test transaction',
                    set_at='2021-10-10',
                )

# User test cases


class APIUserTestCase(APITestClass):
    """Tests for user operations"""

    def setUp(self):
        super().create_random_users()

    def test_get_login_token(self):
        """Test  for  login  token"""
        response = self.client.post(
            '/api-token-auth/', {'username': 'testuser1', 'password': '12345'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)

    def test_get_login_token_not_register(self):
        """Test  for  login  token in an unregistered user"""
        response = self.client.post(
            '/api-token-auth/', {'username': 'notregister', 'password': 'notregister'})
        self.assertTrue('token' not in response.data)
        self.assertEqual(response.status_code, 400)

    def test_create_userAPI(self):
        """Test  for  create  user"""
        response = self.client.post(
            '/api/users/', {'username': 'newuser', 'password': '12345'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 6)
        self.assertEqual(response.data["username"], 'newuser')

    def test_create_user_from_auth_user(self):
        """Test  for  create  user  from  authenticated  user, should  be  forbidden"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.post('/api/users/', {'username': 'newuser', 'password': 'newuser'}, headers={
                                    "Authorization": "token {}".format(token)})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(User.objects.count(), 5)

    def test_get_user(self):
        """Test  for  list  users should lists  all  user if  super user, otherwise just the  user authenticated"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.get(
            '/api/users/', headers={"Authorization": "token {}".format(token)})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['id'], 1)
        self.assertEqual(response.data['results'][0]['username'], 'testuser1')

    def test_get_user_not_auth(self):
        """Test  for  list  users  without  authentication, should  be  forbidden"""
        response = self.client.get('/api/users/')
        self.assertEqual(
            response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, 401)

    def test_update_user(self):
        """Test  for  update  user's  params"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.put('/api/users/1/', {'username': 'changed', 'last_name': 'changed'}, headers={
                                   "Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'changed')
        self.assertEqual(User.objects.count(), 5)
        self.assertEqual(User.objects.get(id=1).username, 'changed')
        self.assertEqual(User.objects.get(id=1).last_name, 'changed')

    def test_update_notauth(self):
        """Test  for  update  user's  params  without  authentication, should  be  forbidden"""
        user = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')
        token = Token.objects.create(user=user)
        response = self.client.put('/api/users/{}/'.format(user2.id), {'username': 'changed', 'last_name': 'changed'}, headers={
                                   "Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(user2.username, 'testuser2')

    def test_update_superuser(self):
        """Test  for  update  user's  params  as  superuser"""
        user = User.objects.get(username='admin')
        user1 = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.put('/api/users/{}/'.format(user1.id), {'username': 'changed', 'last_name': 'changed'}, headers={
                                   "Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(id=1).username, 'changed')

    def test_delete_user(self):
        """Test  for  delete  user"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.delete(
            '/api/users/{}/'.format(user.id), headers={"Authorization": "token {}".format(token)})
        self.assertEqual(response.status_code, 204)

    def test_delete_user_unatuh(self):
        """Test  for  delete  user  without  authentication, should  be  forbidden"""
        user = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')
        token = Token.objects.create(user=user)
        response = self.client.delete(
            '/api/users/{}/'.format(user2.id), headers={"Authorization": "token {}".format(token)})

        self.assertEqual(response.status_code, 404)


class APITransactionsTestCase(APITestClass):
    """Tests   for  transactions  operations"""

    def setUp(self):
        """Create 5 users, 4 normal users and 1 superuser and  3 transactions for each user"""
        super().create_random_users()
        super().create_random_transactions()

    def test_get_transactions(self):
        """Test  for  list  transactions  of  an  user"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.get('/api/transactions/', headers={
                                   "Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results'][0]['incomes']) +
                         len(response.data['results'][0]['outcomes']), 4)

    def test_get_transactions_superuser(self):
        """Test  for  list  transactions  of  an  user  as  superuser"""
        user = User.objects.get(username='admin')
        token = Token.objects.create(user=user)
        response = self.client.get('/api/transactions/', headers={
                                   "Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 5)

    def test_get_transactions_notauth(self):
        """Test  for  list  transactions  of  an  user  without  authentication, should  be  forbidden"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.get('/api/transactions/3/', headers={
                                   "Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_deleting_transactions_user(self):
        """Test  for  delete  transactions  of  an  user"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.delete(
            '/api/users/1/', headers={"Authorization": "token {}".format(token)})
        self.assertEqual(response.status_code, 204)
        response = self.client.get(
            '/api/users/1/', headers={"Authorization": "token {}".format(token)})
        response.data['detail']
        self.assertEqual(response.data['detail'].title(), 'Invalid Token.')

    
class APIIndividualTransactionsTestCase(APITestClass):
    """Test  for indiviadual  Incomes  and  Outcomes Operations"""

    def setUp(self):
        super().create_random_users()
        super().create_random_transactions()

    def test_add_income(self):
        """Test  for  add  income"""
        initial_balance = AccountStatus.objects.get(id=1).actual_balance
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.post('/api/incomes/', {"account_status": 1, "amount": 2000}, headers={
                                    "Authorization": "token {}".format(token)})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(AccountStatus.objects.get(
            id=1).actual_balance, initial_balance+2000)

    def test_add_income_unauth(self):
        """Test  for  add  income  without  authentication, should  be  forbidden"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.post('/api/incomes/', {"account_status": 2, "amount": 2000}, headers={
                                    "Authorization": "token {}".format(token)})
        self.assertEqual(response.status_code, 403)

    def test_add_outcome(self):
        """Test  for  add  outcome"""
        initial_balance = AccountStatus.objects.get(id=1).actual_balance
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.post('/api/outcomes/', {"account_status": 1, "amount": 2000}, headers={
                                    "Authorization": "token {}".format(token)})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(AccountStatus.objects.get(
            id=1).actual_balance, initial_balance-2000)

    def test_add_outcome_unauth(self):
        """Test  for  add  outcome  without  authentication, should  be  forbidden"""
        initial_balance = AccountStatus.objects.get(id=1).actual_balance
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        response = self.client.post('/api/outcomes/', {"account_status": 2, "amount": 2000}, headers={
                                    "Authorization": "token {}".format(token)})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            initial_balance, AccountStatus.objects.get(id=1).actual_balance)

    def test_patch_income(self):
        """Test  for  update  income"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)

        income = Incomes.objects.create(
            account_status=user.account_status,
            amount=100
        )
        response = self.client.patch('/api/incomes/{}/'.format(income.id), {"amount": 10000}, headers={
                                     "Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Incomes.objects.get(id=income.id).amount, 10000)

    def test_patch_income_unauth(self):
        """Test  for  update  income  without  authentication, should  be  forbidden"""
        user1 = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')
        income = Incomes.objects.create(
            account_status=user2.account_status,
            amount=100
        )
        token = Token.objects.create(user=user1)
        response = self.client.patch('/api/incomes/{}/'.format(income.pk), {"amount": 10000}, headers={
                                     "Authorization": "token {}".format(token)}, content_type='application/json')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(Incomes.objects.get(id=income.id).amount, 100)

    def test_patch_income_unauth_status(self):
        """Test  for  update  income  without  authentication, should  be  forbidden"""
        user1 = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')
        income = Incomes.objects.filter(
            account_status=user1.account_status).first()
        token = Token.objects.create(user=user1)
        response = self.client.patch('/api/incomes/{}/'.format(income.id), {"account_status": user2.account_status.id},
                                     headers={"Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Incomes.objects.get(
            id=income.id).account_status.id, income.account_status.id)

    def test_patch_outcome(self):
        """Test  for  update  outcome"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)

        income = Outcomes.objects.create(
            account_status=user.account_status,
            amount=100
        )
        response = self.client.patch('/api/outcomes/{}/'.format(income.id), {"amount": 10000}, headers={
                                     "Authorization": "token {}".format(token)}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Outcomes.objects.get(id=income.id).amount, 10000)

    def test_patch_outcome_unauth(self):
        """Test  for  update  outcome  without  authentication, should  be  forbidden"""
        user1 = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')
        income = Outcomes.objects.create(
            account_status=user2.account_status,
            amount=100
        )
        token = Token.objects.create(user=user1)
        response = self.client.patch('/api/outcomes/{}/'.format(income.id), {"amount": 10000}, headers={
                                     "Authorization": "token {}".format(token)}, content_type='application/json')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(Outcomes.objects.get(id=income.id).amount, 100)

    def test_delete_income(self):
        """Test  for  delete  income"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        income = Incomes.objects.create(
            account_status=user.account_status,
            amount=1000
        )
        self.assertTrue(income in Incomes.objects.filter(
            account_status=user.account_status))

        response = self.client.delete('/api/incomes/{}/'.format(income.id),  headers={
            "Authorization": "token {}".format(token)}, content_type='application/json')

        self.assertEqual(response.status_code, 204)
        self.assertTrue(income not in Incomes.objects.filter(
            account_status=user.account_status))

    def test_delete_outcome(self):
        """Test  for  delete  outcome"""
        user = User.objects.get(username='testuser1')
        token = Token.objects.create(user=user)
        outcome = Outcomes.objects.create(
            account_status=user.account_status,
            amount=1000
        )
        self.assertTrue(outcome in Outcomes.objects.filter(
            account_status=user.account_status))

        response = self.client.delete('/api/outcomes/{}/'.format(outcome.id),  headers={
            "Authorization": "token {}".format(token)}, content_type='application/json')

        self.assertEqual(response.status_code, 204)
        self.assertTrue(outcome not in Outcomes.objects.filter(
            account_status=user.account_status))

    def test_unauth_delete_income(self):
        """Test  for  delete  income  without  authentication, should  be  forbidden"""
        user1 = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')
        token = Token.objects.create(user=user1)
        
        income = Incomes.objects.filter(
            account_status=user2.account_status).first()

        response = self.client.delete('/api/incomes/{}/'.format(income.id),  headers={
            "Authorization": "token {}".format(token)}, content_type='application/json')

        self.assertEqual(response.status_code, 404)
        self.assertTrue(income in Incomes.objects.filter(
            account_status=user2.account_status))
