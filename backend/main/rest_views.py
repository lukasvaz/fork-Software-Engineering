from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from main.models import AccountStatus, Incomes, Outcomes
from main.serializer import UserSerializer, TransactionsSerializer, IncomesSerializer, OutcomesSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from main.custom_permission import IndividualTransactionsPermission, UserPermission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [UserPermission]

    def get_permissions(self):
        if self.action == 'create':
            if self.request.user.is_anonymous:
                self.permission_classes = [AllowAny]
            else:
                self.permission_classes = [IsAdminUser]

        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all().order_by('-date_joined')
        else:
            return User.objects.filter(id=self.request.user.id).order_by('-date_joined')


class TransactionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Accounts Status  be  viewed.
    """
    queryset = AccountStatus.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return AccountStatus.objects.all()
        else:
            return AccountStatus.objects.filter(user=self.request.user.id)


class IncomesViewSet(
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        GenericViewSet):

    """
    API endpoint that allows Incomes to be  edited.
    """
    serializer_class = IncomesSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IndividualTransactionsPermission]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Incomes.objects.all()
        else:
            return Incomes.objects.filter(account_status=self.request.user.account_status.id)


class OutcomesViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    """
    API endpoint that allows Outcomes to be edited.
    """
    queryset = Outcomes.objects.all()
    serializer_class = OutcomesSerializer
    permission_classes = [IndividualTransactionsPermission]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Outcomes.objects.all()
        else:
            return Outcomes.objects.filter(account_status=self.request.user.account_status)
