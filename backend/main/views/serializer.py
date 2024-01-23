from rest_framework import serializers
from django.contrib.auth.models import  User
from main.models import AccountStatus,Incomes,Outcomes

class UserSerializer(serializers.HyperlinkedModelSerializer):
    actual_balance = serializers.SerializerMethodField()
    account_status = serializers.HyperlinkedRelatedField(read_only=True, view_name='transactions-detail')
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_name','account_status', 'actual_balance')

    def get_actual_balance(self, obj):
        try:
            return obj.account_status.actual_balance
        except AccountStatus.DoesNotExist:
            return None

class IncomesSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='incomes-detail')
    class Meta:
        model = Incomes
        fields = '__all__'

    def update(self, instance, validated_data):
        print(instance)
        return super().update(instance, validated_data)


class OutcomesSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='outcomes-detail')
    
    class Meta:
        model = Outcomes
        fields = '__all__'
   
class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    incomes= IncomesSerializer(many=True)
    outcomes= OutcomesSerializer(many=True)
    user= serializers.HyperlinkedRelatedField(read_only=True,view_name='user-detail')
    class Meta:
        model = AccountStatus
        fields = ('id','user','actual_balance','incomes','outcomes')

