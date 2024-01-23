from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import AccountStatus, Incomes, Outcomes


class UserSerializer(serializers.HyperlinkedModelSerializer):
    actual_balance = serializers.SerializerMethodField()
    account_status = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='transactions-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_name',
                  'account_status', 'actual_balance')

    def get_actual_balance(self, obj):
        try:
            return obj.account_status.actual_balance
        except AccountStatus.DoesNotExist:
            return None


class IncomesSerializer(serializers.ModelSerializer):
    transactions_url = serializers.HyperlinkedRelatedField(view_name='transactions-detail', read_only=True, source='account_status')
    
    class Meta:
        model = Incomes
        fields = ('id','transactions_url', 'amount', 'category','description','set_at','account_status')

class SimpleIncomesSerializer(IncomesSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='incomes-detail')
    class Meta:
        model=Incomes
        fields = ('amount', 'url')

class OutcomesSerializer(serializers.ModelSerializer):
    transactions_url = serializers.HyperlinkedRelatedField(view_name='transactions-detail', read_only=True, source='account_status')
    class Meta:
        model = Outcomes
        fields = ('id','transactions_url', 'amount', 'category','description','set_at','account_status')


class SimpleOutcomesSerializer(IncomesSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='outcomes-detail')
    class Meta:
        model=Outcomes
        fields = ('amount', 'url')

class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    incomes = SimpleIncomesSerializer(many=True)
    outcomes = SimpleOutcomesSerializer(many=True)
    user = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='user-detail')

    class Meta:
        model = AccountStatus
        fields = ('id', 'user', 'actual_balance', 'incomes', 'outcomes')
