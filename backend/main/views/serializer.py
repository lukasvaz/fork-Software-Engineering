from rest_framework import serializers
from django.contrib.auth.models import  User
from main.models import AccountStatus,Incomes,Outcomes

class UserSerializer(serializers.HyperlinkedModelSerializer):
    actual_balance = serializers.SerializerMethodField()
    account_status = serializers.HyperlinkedRelatedField(read_only=True, view_name='transactions-detail')
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'account_status', 'actual_balance')

    def get_actual_balance(self, obj):
        try:
            return obj.account_status.actual_balance
        except AccountStatus.DoesNotExist:
            return None

class IncomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incomes
        fields = ('id','amount','category','created_at','set_at','description')

class OutcomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcomes
        fields = ('id','amount','category','created_at','set_at','description')
   
class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    incomes= IncomesSerializer(many=True)
    outcomes= OutcomesSerializer(many=True)
    user= serializers.HyperlinkedRelatedField(read_only=True,view_name='user-detail')
    class Meta:
        model = AccountStatus
        fields = ('id','user','actual_balance','incomes','outcomes')

