from rest_framework import permissions, viewsets
from django.contrib.auth.models import  User
from main.models import AccountStatus,Incomes,Outcomes
from main.views.serializer import UserSerializer,TransactionsSerializer,IncomesSerializer,OutcomesSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    queryset=User.objects.all().order_by('-date_joined')
    
    def  get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all().order_by('-date_joined')
        else:
            return User.objects.filter(id=self.request.user.id).order_by('-date_joined')


class TransactionsViewSet(viewsets.ModelViewSet):
    
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AccountStatus.objects.all()
    serializer_class = TransactionsSerializer
    # permission_classes = [permissions.IsAuthenticated]

class IncomesViewSet(viewsets.ModelViewSet):
    
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Incomes.objects.all()
    serializer_class = IncomesSerializer
    
    # permission_classes = [permissions.IsAuthenticated]

class OutcomesViewSet(viewsets.ModelViewSet):
    
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Outcomes.objects.all()
    serializer_class = OutcomesSerializer
    # permission_classes = [permissions.IsAuthenticated]


