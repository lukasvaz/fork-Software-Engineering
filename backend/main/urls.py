from django.urls import path, include
from rest_framework import routers
import main.views.rest_views as rest_views
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'api/users', rest_views.UserViewSet) 

urlpatterns = [
path('',include(router.urls)),
path('api-token-auth/', views.obtain_auth_token),
path('api/transactions/',rest_views.TransactionsViewSet.as_view({'get':'list'})),
path('api/transactions/<int:pk>/',rest_views.TransactionsViewSet.as_view({'get':'retrieve'}) ,name ="transactions-detail"),
path('api/incomes/<int:pk>/',rest_views.IncomesViewSet.as_view({'patch':'partial_update','put':'update','delete':'destroy','get':'retrieve'}),name ="incomes-detail"),
path('api/incomes/',rest_views.IncomesViewSet.as_view({'post':'create'})),
path('api/outcomes/<int:pk>/',rest_views.OutcomesViewSet.as_view({'patch':'partial_update','put':'update','delete':'destroy','get':'retrieve'}),name ="outcomes-detail"),
path('api/outcomes/',rest_views.OutcomesViewSet.as_view({'post':'create'})),
]
