"""
URL configuration for igs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from main.views import home_views, stats_views, transaction_views, register_view, modify_view, delete_view,stats_views,get_data_views, login_view, user_view

urlpatterns = [
    path('', lambda req:redirect('accounts/login'), name='root'),
    path("home/", home_views.home, name="home"),
    path("get-raw-transactions", get_data_views.get_raw_transactions),
    path("get-filter-aggregate", get_data_views.get_filter_sum),
    path("get-filter-aggregate/<str:type>", get_data_views.get_filter_sum),
    path("get-filter-aggregate/<str:type>/<str:groupby>", get_data_views.get_filter_sum),
    path("log-out", register_view.logout_user, name="log-out"),
    path("admin/", admin.site.urls),
    path("transaction/", transaction_views.transaction, name="transaction"),
    path("registro/", register_view.register_user, name="registro"),
    path("accounts/", include("django.contrib.auth.urls"), name="accounts"),
    path("modify/income/<int:id>",
         modify_view.modify_income, name='modify'),
    path("modify/outcome/<int:id>", modify_view.modify_outcome),
    path("delete/income/<int:id>",
         delete_view.delete_income, name='delete'),
    path("delete/outcome/<int:id>", delete_view.delete_outcome),
    path("user-data", user_view.update_user, name='user-data'),
    path("stats/", stats_views.stats,name="stats"),
    path('login/', login_view.login_view, name='login'),
]
