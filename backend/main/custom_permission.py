from rest_framework.permissions import  BasePermission

class IndividualTransactionsPermission(BasePermission):
    """Permission class for the Incomes and Outcomes views.Handles POST, PATCH, PUT and DELETE requests"""
    def has_permission(self, request, view):
        """ Handles POST  requests """
        if request.user.is_superuser:
            return True
        elif 'account_status' in request.data:
            return int(request.data['account_status']) == request.user.account_status.id
        return True

    def has_object_permission(self, request, view, obj):
        """ Handles PATCH, PUT and DELETE requests"""
        if request.user.is_superuser:
            return True

        else:
            return obj.account_status.user.id == request.user.id

class UserPermission(BasePermission):
    """Permission class for the User view.Handles POST, PATCH, PUT and DELETE requests"""
    def has_permission(self, request, view):
        """ Handles POST  requests """
        if view.action == 'create':
            if request.user.is_anonymous:
                return True
            else:
                return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """ Handles PATCH UPDATE PUT and DELETE requests"""
        if request.user.is_superuser:
            return True

        else:
            return obj.id == request.id
