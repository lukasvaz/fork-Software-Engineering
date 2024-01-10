from rest_framework import permissions, viewsets
from django.contrib.auth.models import  User
from main.models import AccountStatus,Incomes,Outcomes
from main.views.serializer import UserSerializer,TransactionsSerializer,IncomesSerializer,OutcomesSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    queryset=User.objects.all().order_by('-date_joined')

    def get_permissions(self):
        if self.action == 'create' and  self.request.user.is_anonymous:
            self.permission_classes = [AllowAny]
        else:
             self.permission_classes = [IsAuthenticated]
        return super().get_permissions()  
    
    def  get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all().order_by('-date_joined')
        else:
            return User.objects.filter(id=self.request.user.id).order_by('-date_joined')


    def update(self, request, *args, **kwargs):     
        if  self.request.user.is_superuser:
            return super().update(request, *args, **kwargs)        
        
        elif self.request.user.id!=int(self.kwargs['pk']):
            return Response("Not authorized",status=status.HTTP_401_UNAUTHORIZED)
        
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):    
        if  self.request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)        
        
        elif self.request.user.id!=int(self.kwargs['pk']):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)


class TransactionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AccountStatus.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return AccountStatus.objects.all()
        else:
            return AccountStatus.objects.filter(user=self.request.user.id)


class IncomesViewSet(viewsets.ModelViewSet):
    
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Incomes.objects.all()
    serializer_class = IncomesSerializer
    permission_classes=[permissions.IsAuthenticated]    

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Incomes.objects.all()
        else:
            return Incomes.objects.filter(user=self.request.user.id)

class OutcomesViewSet(viewsets.ModelViewSet):
    
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Outcomes.objects.all()
    serializer_class = OutcomesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Outcomes.objects.all()
        else:
            return Outcomes.objects.filter(user=self.request.user.id)
