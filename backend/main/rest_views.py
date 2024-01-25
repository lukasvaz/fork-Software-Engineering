from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from main.models import AccountStatus, Incomes, Outcomes
from main.serializer import UserSerializer, TransactionsSerializer, IncomesSerializer, OutcomesSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from main.custom_permission import IndividualTransactionsPermission, UserPermission
from main.mixins  import FilterQuerySetMixin

class UserViewSet( FilterQuerySetMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
    queryset_params ={
        'filter':'pk',
        'request_user':'pk'
                      }
class TransactionsViewSet(FilterQuerySetMixin,viewsets.ModelViewSet):
    """
    API endpoint that allows Accounts Status  be  viewed.
    """
    serializer_class = TransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    queryset_params ={
        'filter':'user',
        'request_user':'pk'
                      }
    
class IncomesViewSet(
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        FilterQuerySetMixin,
        GenericViewSet):

    """
    API endpoint that allows Incomes to be  edited.
    """
    serializer_class = IncomesSerializer
    permission_classes = [IndividualTransactionsPermission]

    queryset_params ={
        'filter':'account_status',
        'request_user':'account_status'
                      }
    

class OutcomesViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      FilterQuerySetMixin,
                      GenericViewSet):
    """
    API endpoint that allows Outcomes to be edited.
    """
    serializer_class = OutcomesSerializer
    permission_classes = [IndividualTransactionsPermission]
    queryset_params ={
        'filter':'account_status',
        'request_user':'account_status'
                      }
    